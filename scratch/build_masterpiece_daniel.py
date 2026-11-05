import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

# 1. Load photo and mask
photo = Image.open("scratch/pure_portrait_original.jpg").convert("RGB")
w, h = photo.size
arr = np.array(photo, dtype=float)

mask = (np.array(Image.open("scratch/test_segmented_mask.png").convert("L")) > 128).astype(float)

# 2. Feather mask naturally (sigma = 2.0)
feathered_mask = gaussian_filter(mask, sigma=2.0)

# Bottom fade (last 90 pixels)
bottom_fade = np.ones(h)
for y in range(h - 90, h):
    bottom_fade[y] = max(0.0, (h - 1 - y) / 90.0)
feathered_mask *= bottom_fade[:, None]

# 3. Base composite on pure #080808
bg = np.array([8.0, 8.0, 8.0])
composite = np.zeros_like(arr)
for c in range(3):
    composite[:, :, c] = arr[:, :, c] * feathered_mask + bg[c] * (1.0 - feathered_mask)

# 4. Cinematic photographic red rim light (Daniel Smith reference)
# Right perimeter gradient of the subject:
grad_y, grad_x = np.gradient(feathered_mask)
right_edge = np.maximum(0.0, -grad_x)
if right_edge.max() > 0:
    right_edge /= right_edge.max()

# Spread rim light softly (sigma = 4.0)
rim_right = gaussian_filter(right_edge, sigma=4.0) * 1.5

# Rim color: #E5092B (229, 9, 43)
# Hot specular edge highlight: (255, 75, 95)
rim_color = np.array([229.0, 9.0, 43.0])
rim_highlight = np.array([255.0, 75.0, 95.0])

for c in range(3):
    curr = composite[:, :, c] / 255.0
    kicker = rim_right * feathered_mask * (rim_color[c] / 255.0) * 0.95
    specular = (right_edge**1.4) * (rim_highlight[c] / 255.0) * 0.45
    screened = 1.0 - (1.0 - curr) * (1.0 - np.clip(kicker + specular, 0.0, 0.95))
    composite[:, :, c] = screened * 255.0

# 5. Soft atmospheric red glow concentrated BEHIND the subject
xx, yy = np.meshgrid(np.arange(w), np.arange(h))
dist_behind = np.sqrt(((xx - 440) / 1.5)**2 + ((yy - 340) / 1.1)**2)
ambient_glow = np.exp(-0.5 * (dist_behind / 230.0)**2) * (1.0 - feathered_mask) * 0.20
for c in range(3):
    composite[:, :, c] += ambient_glow * rim_color[c]

# 6. Ensure outer 4px borders are pure #080808
composite[0:4, :, :] = bg
composite[-4:, :, :] = bg
composite[:, 0:4, :] = bg
composite[:, -4:, :] = bg

# 7. Save outputs
final_arr = np.clip(composite, 0, 255).astype(np.uint8)
final_img = Image.fromarray(final_arr)

final_img.save("scratch/masterpiece_daniel.png")
final_img.save("NEW IMAGE FOR WEBSITE.jpeg", quality=98)
final_img.save("new image.jpeg", quality=98)
final_img.save("Profile Pic.jpg", quality=98)

# Transparent PNG version:
rgba = np.zeros((h, w, 4), dtype=np.uint8)
rgba[:, :, 0:3] = np.clip(composite, 0, 255).astype(np.uint8)
rgba[:, :, 3] = np.clip(feathered_mask * 255, 0, 255).astype(np.uint8)
Image.fromarray(rgba).save("zeerak_daniel_transparent.png")
Image.fromarray(rgba).save("scratch/zeerak_daniel_transparent.png")

print("Masterpiece portrait saved successfully!")

