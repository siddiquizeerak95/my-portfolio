import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

# Load NEW IMAGE FOR WEBSITE.jpeg
im = Image.open("NEW IMAGE FOR WEBSITE.jpeg").convert("RGB")
w, h = im.size
arr = np.array(im, dtype=float)
print(f"Canvas size: {w}x{h}")

# Target website background: #080808 (RGB: 8, 8, 8)
bg = np.array([8.0, 8.0, 8.0])

# Zeerak's location in this canvas:
# Hair top: Y ~ 205
# Face & skin: Y from 260 to 520, X from 280 to 580
# Neck & collar: Y from 520 to 620, X from 340 to 520
# Coat & shoulders: Y from 600 to 1095, X from 20 to 830

# Let's detect skin:
r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
skin = (r > 90) & (g > 40) & (b > 20) & ((r - g) > 12) & (r > b) & (arr.mean(axis=-1) > 40)

# Build a precise subject mask:
subject_mask = np.zeros((h, w), dtype=float)

# Face and skin are 100% subject
subject_mask[skin] = 1.0

# Hair region: Y from 205 to 370, X from 275 to 575
# In the hair region, hair has distinct texture and pixels > 18
hair_zone = (arr.mean(axis=-1) > 16)
for y in range(205, 370):
    for x in range(275, 575):
        if hair_zone[y, x]:
            subject_mask[y, x] = 1.0

# Turtleneck & collar: Y from 500 to 620, X from 335 to 525
subject_mask[500:620, 335:525] = 1.0

# Coat: Y from 600 to 1095
# In each row, coat starts where pixels are non-zero:
for y in range(600, 1095):
    # sloped shoulder boundary:
    prog = (y - 600) / (1095 - 600)
    left_x = int(340 - prog * 315) # 340 down to 25
    right_x = int(520 + prog * 300) # 520 up to 820
    subject_mask[y, max(0, left_x):min(w, right_x)] = 1.0

# Feather the subject mask softly (2.5px gaussian blur)
feathered_mask = gaussian_filter(subject_mask, sigma=2.5)

# Coat bottom dissolve: Y from 1000 to 1095 smoothly fades to 0
for y in range(1000, 1095):
    prog = (1095 - 1 - y) / 95.0
    feathered_mask[y, :] *= max(0.0, prog)
feathered_mask[1095:, :] = 0.0

# Now, blend the entire image to pure #080808 background:
composite = np.zeros_like(arr)
for c in range(3):
    composite[:, :, c] = arr[:, :, c] * feathered_mask + bg[c] * (1.0 - feathered_mask)

# ADD THE CINEMATIC RED RIM LIGHT (Daniel Smith Reference):
# Kicker light hits right edge of hair, ear, cheek, neck, and shoulder
grad_y, grad_x = np.gradient(feathered_mask)
right_edge = np.maximum(0.0, -grad_x)
if right_edge.max() > 0:
    right_edge /= right_edge.max()

# Spread rim light softly (sigma = 4.0)
rim_spread = gaussian_filter(right_edge, sigma=4.0) * 1.5

rim_color = np.array([229.0, 9.0, 43.0]) # #E5092B
rim_highlight = np.array([255.0, 75.0, 95.0])

for c in range(3):
    curr = composite[:, :, c] / 255.0
    kicker = rim_spread * feathered_mask * (rim_color[c] / 255.0) * 0.95
    specular = (right_edge**1.4) * (rim_highlight[c] / 255.0) * 0.45
    screened = 1.0 - (1.0 - curr) * (1.0 - np.clip(kicker + specular, 0.0, 0.95))
    composite[:, :, c] = screened * 255.0

# Soft atmospheric red glow concentrated BEHIND the subject
xx, yy = np.meshgrid(np.arange(w), np.arange(h))
dist_behind = np.sqrt(((xx - 450) / 1.5)**2 + ((yy - 480) / 1.1)**2)
ambient_glow = np.exp(-0.5 * (dist_behind / 250.0)**2) * (1.0 - feathered_mask) * 0.22
for c in range(3):
    composite[:, :, c] += ambient_glow * rim_color[c]

# Ensure outer borders are 100% pure #080808
composite[0:15, :, :] = bg
composite[-15:, :, :] = bg
composite[:, 0:15, :] = bg
composite[:, -15:, :] = bg

# Save output
final_arr = np.clip(composite, 0, 255).astype(np.uint8)
final_img = Image.fromarray(final_arr)

final_img.save("scratch/test_canvas_seamless.png")
print("Saved scratch/test_canvas_seamless.png")

