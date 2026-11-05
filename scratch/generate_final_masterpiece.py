import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

# 1. Load the original photo and the watershed mask
photo = Image.open("scratch/pure_portrait_original.jpg").convert("RGB")
w, h = photo.size
arr = np.array(photo, dtype=float)

mask_img = Image.open("scratch/watershed_full_mask.png").convert("L")
raw_mask = (np.array(mask_img) > 128).astype(float)

# 2. Feather the mask naturally for photographic edge quality
feathered_mask = gaussian_filter(raw_mask, sigma=2.0)

# Bottom fade (last 90 pixels) so the coat dissolves seamlessly into the page background
bottom_fade = np.ones(h)
for y in range(h - 90, h):
    bottom_fade[y] = max(0.0, (h - 1 - y) / 90.0)
feathered_mask *= bottom_fade[:, None]

# Target website background: #080808 (RGB: 8, 8, 8)
bg_target = np.array([8.0, 8.0, 8.0])

# 3. Create the base composite on #080808
composite = np.zeros_like(arr)
for c in range(3):
    composite[:, :, c] = arr[:, :, c] * feathered_mask + bg_target[c] * (1.0 - feathered_mask)

# 4. COMPUTE THE CINEMATIC RED RIM LIGHT (Exact match to Daniel Smith reference)
# Find the right edge of the silhouette:
grad_y, grad_x = np.gradient(feathered_mask)
# Right edge: where mask decreases as X increases (grad_x is negative)
right_edge = np.maximum(0.0, -grad_x)
# Left edge: subtle fill rim light
left_edge = np.maximum(0.0, grad_x)

# Normalize edge gradients
if right_edge.max() > 0:
    right_edge /= right_edge.max()
if left_edge.max() > 0:
    left_edge /= left_edge.max()

# Spread the rim light softly across the edge (falloff ~ 5px inward/outward)
rim_right = gaussian_filter(right_edge, sigma=3.5)
rim_left = gaussian_filter(left_edge, sigma=3.0)

# Rim colors:
# Primary red: #E5092B (229, 9, 43)
# Hot specular edge highlight: (255, 80, 95)
rim_color = np.array([229.0, 9.0, 43.0])
specular_color = np.array([255.0, 80.0, 95.0])

# Apply red rim light onto the composite:
# The rim light illuminates the edge pixels of the subject
for c in range(3):
    # Right rim: strong photographic kicker
    rim_val_r = rim_right * (rim_color[c] / 255.0) * 0.95
    # Specular core right on the sharp edge
    spec_val_r = (right_edge**1.4) * (specular_color[c] / 255.0) * 0.45
    
    # Left rim: subtle atmospheric kicker
    rim_val_l = rim_left * (rim_color[c] / 255.0) * 0.35
    
    # Screen blend onto composite: 1 - (1 - composite)*(1 - rim)
    curr = composite[:, :, c] / 255.0
    kicker = np.clip(rim_val_r + spec_val_r + rim_val_l, 0.0, 0.95)
    screened = 1.0 - (1.0 - curr) * (1.0 - kicker)
    composite[:, :, c] = screened * 255.0

# 5. Soft atmospheric red glow concentrated BEHIND the subject
# Gentle ambient crimson radial glow
xx, yy = np.meshgrid(np.arange(w), np.arange(h))
# Center behind his neck/shoulder: X=450, Y=350
dist_sq = ((xx - 450) / 1.5)**2 + ((yy - 350) / 1.1)**2
ambient = np.exp(-0.5 * (dist_sq / (200.0**2))) * 0.18 # restrained, elegant
for c in range(3):
    glow = ambient * (1.0 - feathered_mask) * rim_color[c]
    composite[:, :, c] += glow

# 6. Ensure the outer borders (top, bottom, left, right) are 100% pure #080808
composite[0:4, :, :] = bg_target
composite[-4:, :, :] = bg_target
composite[:, 0:4, :] = bg_target
composite[:, -4:, :] = bg_target

# Save both PNG (for highest quality) and JPEG
final_arr = np.clip(composite, 0, 255).astype(np.uint8)
final_img = Image.fromarray(final_arr)

final_img.save("scratch/daniel_masterpiece.png")
final_img.save("NEW IMAGE FOR WEBSITE.jpeg", quality=98)
final_img.save("new image.jpeg", quality=98)
final_img.save("Profile Pic.jpg", quality=98)

# Also create a transparent PNG with alpha channel:
rgba = np.zeros((h, w, 4), dtype=np.uint8)
rgba[:, :, 0:3] = np.clip(composite, 0, 255).astype(np.uint8)
rgba[:, :, 3] = np.clip(feathered_mask * 255, 0, 255).astype(np.uint8)
Image.fromarray(rgba).save("scratch/zeerak_transparent_cutout.png")

print("Generated and saved all images successfully!")

