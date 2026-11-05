import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

# Load original pure photo
photo = Image.open("scratch/pure_portrait_original.jpg").convert("RGB")
w, h = photo.size
arr = np.array(photo, dtype=float)

# Background target: #080808
bg = np.array([8.0, 8.0, 8.0])

# Subject skin detection:
r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
max_rgb = np.maximum(np.maximum(r, g), b)
min_rgb = np.minimum(np.minimum(r, g), b)
chroma = max_rgb - min_rgb
saturation = np.where(max_rgb > 0, chroma / (max_rgb + 1e-5), 0)

# Skin pixels have high chroma and warm hue
skin = (r > 90) & (g > 40) & (b > 20) & ((r - g) > 12) & (r > b) & (saturation > 0.2)

# Create an organic, continuous subject confidence field:
# Hair & head: Y from 30 to 450, X from 270 to 570
# Torso & coat: Y from 420 to 924, X from 40 to 780
xx, yy = np.meshgrid(np.arange(w), np.arange(h))

# Subject presence probability
subject_weight = np.zeros((h, w), dtype=float)

# Hair region
hair = (yy >= 32) & (yy <= 240) & (xx >= 270) & (xx <= 570)
subject_weight[hair] = 0.95
subject_weight[skin] = 1.0

# Turtleneck & coat region
for y in range(400, h):
    # Sloping coat width
    prog = (y - 400) / (h - 400)
    left_x = 360 - prog * 315 # 360 to 45
    right_x = 510 + prog * 275 # 510 to 785
    inside = (xx[y, :] >= left_x) & (xx[y, :] <= right_x)
    subject_weight[y, inside] = 1.0

# Feather the subject weight softly (12px gaussian blur)
feathered_subject = gaussian_filter(subject_weight, sigma=8.0)

# Bottom fade (last 100px fades to 0)
bottom_fade = np.ones(h)
for y in range(h - 100, h):
    bottom_fade[y] = max(0.0, (h - 1 - y) / 100.0)
feathered_subject *= bottom_fade[:, None]

# Blend background smoothly to pure #080808
result = np.zeros_like(arr)
for c in range(3):
    result[:, :, c] = arr[:, :, c] * feathered_subject + bg[c] * (1.0 - feathered_subject)

# NOW: Add authentic studio directional RED RIM LIGHT from the right!
# In real photography (Daniel Smith):
# A red strobe on the right casts light that falls off with distance from the right edge.
# Light intensity is highest on the right edge (X: 520 to 780) and decays across the face and coat.
decay_x = np.clip((xx - 420) / (w - 420.0), 0.0, 1.0)**1.4

# Light falls only on the subject and immediate rim
rim_intensity = decay_x * feathered_subject * 0.75

# Red color: #E5092B (229, 9, 43)
rim_color = np.array([229.0, 15.0, 45.0])

for c in range(3):
    curr = result[:, :, c] / 255.0
    rim_add = rim_intensity * (rim_color[c] / 255.0)
    # Screen blend
    screened = 1.0 - (1.0 - curr) * (1.0 - rim_add)
    result[:, :, c] = screened * 255.0

# Add a hot rim highlight right on the right ear and cheek edge
ear_cheek = (yy >= 220) & (yy <= 360) & (xx >= 530) & (xx <= 575)
ear_cheek_glow = gaussian_filter(ear_cheek.astype(float), sigma=4.0) * 0.65
for c in range(3):
    curr = result[:, :, c] / 255.0
    kicker = ear_cheek_glow * (rim_color[c] / 255.0)
    result[:, :, c] = (1.0 - (1.0 - curr) * (1.0 - kicker)) * 255.0

# Soft ambient glow behind subject
dist_behind = np.sqrt(((xx - 450) / 1.5)**2 + ((yy - 350) / 1.1)**2)
ambient_glow = np.exp(-0.5 * (dist_behind / 240.0)**2) * (1.0 - feathered_subject) * 0.25
for c in range(3):
    result[:, :, c] += ambient_glow * rim_color[c]

# Outer 4px borders are pure #080808
result[0:4, :, :] = bg
result[-4:, :, :] = bg
result[:, 0:4, :] = bg
result[:, -4:, :] = bg

final = Image.fromarray(np.clip(result, 0, 255).astype(np.uint8))
final.save("scratch/test_studio_lighting.png")
print("Saved scratch/test_studio_lighting.png")

