import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

# 1. Load pure original photo and watershed mask
photo = Image.open("scratch/pure_portrait_original.jpg").convert("RGB")
w, h = photo.size
arr = np.array(photo, dtype=float)

mask_img = Image.open("scratch/watershed_full_mask.png").convert("L")
mask = (np.array(mask_img) > 128).astype(float)

xx, yy = np.meshgrid(np.arange(w), np.arange(h))

# 2. Perfect the hair region:
# Ensure top-right of hair (Y: 30 to 180, X: 450 to 570) is full and naturally rounded
# Hair dome curve:
hair_dome = np.zeros((h, w), dtype=bool)
for y in range(32, 240):
    if y < 140:
        prog = (y - 32) / 108.0
        rad = np.sqrt(max(0.01, 1.0 - (1.0 - prog)**2)) * 145
        hair_dome[y, int(421 - rad*0.95):int(421 + rad*1.05)] = True
    else:
        hair_dome[y, 275:570] = True

mask[hair_dome] = 1.0

# 3. Soft photographic edge feathering (sigma = 2.5)
feathered_mask = gaussian_filter(mask, sigma=2.2)

# Bottom fade (last 85 pixels) so coat dissolves into #080808
bottom_fade = np.ones(h)
for y in range(h - 85, h):
    bottom_fade[y] = max(0.0, (h - 1 - y) / 85.0)
feathered_mask *= bottom_fade[:, None]

# Target background color: #080808
bg = np.array([8.0, 8.0, 8.0])

# 4. Composite subject onto #080808
composite = np.zeros_like(arr)
for c in range(3):
    composite[:, :, c] = arr[:, :, c] * feathered_mask + bg[c] * (1.0 - feathered_mask)

# 5. DANIEL SMITH RED RIM LIGHT:
# Calculate right-facing perimeter gradient
grad_y, grad_x = np.gradient(feathered_mask)
right_edge = np.maximum(0.0, -grad_x)
if right_edge.max() > 0:
    right_edge /= right_edge.max()

# Spread the rim light inward by 12px for a soft kicker light
rim_kicker = gaussian_filter(right_edge, sigma=4.0) * 1.6
# Also catch the outer surface of the right shoulder and ear:
right_zone = np.clip((xx - 500) / (w - 500.0), 0.0, 1.0)**2.0
rim_soft_fill = right_zone * feathered_mask * 0.45

total_rim = np.clip(rim_kicker + rim_soft_fill, 0.0, 1.0) * feathered_mask

# Rim colors:
# Primary red: #E5092B (229, 9, 43)
# Highlight: (255, 65, 85)
rim_color = np.array([229.0, 9.0, 43.0])
rim_highlight = np.array([255.0, 70.0, 95.0])

for c in range(3):
    curr = composite[:, :, c] / 255.0
    kicker = total_rim * (rim_color[c] / 255.0) * 0.95
    specular = (right_edge**1.5) * (rim_highlight[c] / 255.0) * 0.5
    screened = 1.0 - (1.0 - curr) * (1.0 - np.clip(kicker + specular, 0.0, 0.95))
    composite[:, :, c] = screened * 255.0

# 6. Soft atmospheric red glow concentrated BEHIND the subject
dist_behind = np.sqrt(((xx - 460) / 1.5)**2 + ((yy - 340) / 1.1)**2)
ambient_glow = np.exp(-0.5 * (dist_behind / 220.0)**2) * (1.0 - feathered_mask) * 0.22
for c in range(3):
    composite[:, :, c] += ambient_glow * rim_color[c]

# Outer 4px borders are 100% pure #080808
composite[0:4, :, :] = bg
composite[-4:, :, :] = bg
composite[:, 0:4, :] = bg
composite[:, -4:, :] = bg

# Save final images
final_arr = np.clip(composite, 0, 255).astype(np.uint8)
final_img = Image.fromarray(final_arr)

final_img.save("scratch/perfect_cinematic_final.png")
final_img.save("NEW IMAGE FOR WEBSITE.jpeg", quality=98)
final_img.save("new image.jpeg", quality=98)
final_img.save("Profile Pic.jpg", quality=98)

# Transparent PNG version:
rgba = np.zeros((h, w, 4), dtype=np.uint8)
rgba[:, :, 0:3] = np.clip(composite, 0, 255).astype(np.uint8)
rgba[:, :, 3] = np.clip(feathered_mask * 255, 0, 255).astype(np.uint8)
Image.fromarray(rgba).save("scratch/zeerak_daniel_transparent.png")
Image.fromarray(rgba).save("zeerak_daniel_transparent.png")

print("Generated perfect cinematic portrait successfully!")

