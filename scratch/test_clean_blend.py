import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

photo = Image.open("scratch/pure_portrait_original.jpg").convert("RGB")
w, h = photo.size
arr = np.array(photo, dtype=float)

# Load the watershed mask
mask_img = Image.open("scratch/watershed_full_mask.png").convert("L")
mask = (np.array(mask_img) > 128).astype(float)

# Smooth the mask edge by 3 pixels for a soft photographic feather
smooth_mask = gaussian_filter(mask, sigma=2.5)

# Bottom fade (last 80px)
for y in range(h - 80, h):
    smooth_mask[y, :] *= max(0.0, (h - 1 - y) / 80.0)

bg = np.array([8.0, 8.0, 8.0])

# Base cutout on #080808
result = np.zeros_like(arr)
for c in range(3):
    result[:, :, c] = arr[:, :, c] * smooth_mask + bg[c] * (1.0 - smooth_mask)

# Now, add red directional light ONLY where smooth_mask > 0.1 (ON THE SUBJECT)!
# Light comes from the right (X > 450)
xx, yy = np.meshgrid(np.arange(w), np.arange(h))
right_grad = np.clip((xx - 440) / (w - 440.0), 0.0, 1.0)**1.5

# Rim falls on subject's right side:
rim_light = right_grad * smooth_mask * 0.85

rim_color = np.array([229.0, 15.0, 45.0]) # #E5092B

for c in range(3):
    curr = result[:, :, c] / 255.0
    kicker = rim_light * (rim_color[c] / 255.0)
    screened = 1.0 - (1.0 - curr) * (1.0 - kicker)
    result[:, :, c] = screened * 255.0

# Soft ambient glow BEHIND subject (only where smooth_mask < 0.5)
dist_behind = np.sqrt(((xx - 450) / 1.5)**2 + ((yy - 350) / 1.1)**2)
ambient_glow = np.exp(-0.5 * (dist_behind / 240.0)**2) * (1.0 - smooth_mask) * 0.22
for c in range(3):
    result[:, :, c] += ambient_glow * rim_color[c]

# Pure borders
result[0:4, :, :] = bg
result[-4:, :, :] = bg
result[:, 0:4, :] = bg
result[:, -4:, :] = bg

final = Image.fromarray(np.clip(result, 0, 255).astype(np.uint8))
final.save("scratch/test_clean_watershed_blend.png")
print("Saved scratch/test_clean_watershed_blend.png")

