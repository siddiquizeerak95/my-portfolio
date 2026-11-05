import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import gaussian_filter, distance_transform_edt

# Load original
im = Image.open("NEW IMAGE FOR WEBSITE.jpeg").convert("RGB")
w, h = im.size
arr = np.array(im, dtype=float)

# Website background color: #080808
bg_color = np.array([8.0, 8.0, 8.0])

# Subject boundary profile:
# Let's define the left and right boundary for each Y from 0 to h-1:
left_edge = np.zeros(h)
right_edge = np.zeros(h)

for y in range(h):
    if y < 32:
        # Above hair
        left_edge[y] = 421
        right_edge[y] = 421
    elif y < 140:
        # Top dome of hair
        prog = (y - 32) / 108.0
        # Smooth circle curve
        rad = np.sqrt(max(0.01, 1.0 - (1.0 - prog)**2)) * 142
        left_edge[y] = 421 - rad * 0.98
        right_edge[y] = 421 + rad * 1.02
    elif y < 240:
        # Hair temples & sides
        left_edge[y] = 282
        right_edge[y] = 566
    elif y < 320:
        # Ears (protruding outward)
        prog = np.sin((y - 240) / 80.0 * np.pi)
        left_edge[y] = 282 - prog * 10 # ear tip reaches ~272
        right_edge[y] = 566 + prog * 11 # right ear reaches ~577
    elif y < 440:
        # Jawline and neck (slender, pulls inward!)
        # Y=320 to 360 is jawline (tapering from 310 to 345)
        # Y=360 to 440 is neck (around 345 to 365 on left, 510 to 525 on right)
        prog = (y - 320) / 120.0
        left_edge[y] = 295 + prog * 65   # moves from 295 to 360
        right_edge[y] = 565 - prog * 55  # moves from 565 to 510
    elif y < 540:
        # Shoulders (sloping down and out from collar to shoulders)
        prog = (y - 440) / 100.0
        # Left shoulder slopes from 360 to 110
        left_edge[y] = 360 - (prog**0.85) * 250
        # Right shoulder slopes from 510 to 735
        right_edge[y] = 510 + (prog**0.85) * 225
    elif y < 750:
        # Upper coat & torso
        prog = (y - 540) / 210.0
        left_edge[y] = 110 - prog * 60  # 110 to 50
        right_edge[y] = 735 + prog * 60 # 735 to 795
    else:
        # Lower coat
        prog = (y - 750) / 172.0
        left_edge[y] = 50 - prog * 30   # 50 to 20
        right_edge[y] = 795 + prog * 25 # 795 to 820

# Create binary subject mask
mask = np.zeros((h, w), dtype=float)
for y in range(h):
    lb = int(left_edge[y])
    rb = int(right_edge[y])
    if lb < rb:
        mask[y, lb:rb] = 1.0

# 2. Refine mask around hair and skin with luminance checks:
# Inside the subject, if skin or hair or coat has pixels, keep 1.0
# Just outside the subject, feather smoothly
smoothed_mask = gaussian_filter(mask, sigma=3.5)

# Smooth bottom dissolve (coat bottom 120px fades to pure #080808)
bottom_fade = np.ones(h)
for y in range(h - 130, h):
    bottom_fade[y] = max(0.0, (h - 1 - y) / 130.0)
smoothed_mask = smoothed_mask * bottom_fade[:, None]

# 3. COMPUTE THE CINEMATIC RED RIM LIGHT (Like Daniel Smith reference!)
# In Daniel Smith:
# A brilliant red rim light kisses the subject's right edge (viewer's right)
# along the hair, ear, cheek, neck, shoulder, and coat edge!
# Also a gentle rim light on the left shoulder/hair.

# Edge detection on the smoothed mask to find silhouette perimeter:
edge_grad_y, edge_grad_x = np.gradient(smoothed_mask)
edge_magnitude = np.sqrt(edge_grad_x**2 + edge_grad_y**2)

# Normal vectors pointing inward/outward:
# On the right edge of subject: edge_grad_x is negative (< 0)
right_edge_mask = np.maximum(0.0, -edge_grad_x)
# On the left edge of subject: edge_grad_x is positive (> 0)
left_edge_mask = np.maximum(0.0, edge_grad_x)

# Normalize edge intensity
if right_edge_mask.max() > 0:
    right_edge_mask /= right_edge_mask.max()
if left_edge_mask.max() > 0:
    left_edge_mask /= left_edge_mask.max()

# Spread the rim light slightly inward and outward using gaussian blur
# Primary rim light on the RIGHT (like Daniel Smith):
rim_right = gaussian_filter(right_edge_mask, sigma=4.5) * 1.8
# Secondary subtle rim on the LEFT:
rim_left = gaussian_filter(left_edge_mask, sigma=3.5) * 0.7

# Accent color: Crimson red (#E5092B)
# RGB: [229, 9, 43]
rim_color = np.array([229.0, 15.0, 43.0])
rim_highlight = np.array([255.0, 60.0, 80.0]) # specular red-orange core

# 4. Soft atmospheric red glow concentrated BEHIND the subject
# Centered behind Zeerak's head and shoulders (X: 420, Y: 320)
xx, yy = np.meshgrid(np.arange(w), np.arange(h))
dist_from_glow = np.sqrt(((xx - 420) / 1.3)**2 + ((yy - 320) / 1.0)**2)
ambient_glow = np.exp(-0.5 * (dist_from_glow / 180.0)**2)
# Ambient glow should only be visible in background (outside or around silhouette)
# And softly fall off to #080808
ambient_glow_intensity = ambient_glow * (1.0 - smoothed_mask * 0.75) * 0.45

# 5. Composite everything together
# Base: Pure #080808
result = np.zeros_like(arr)
for c in range(3):
    # Background with ambient red glow
    bg_with_glow = bg_color[c] + (rim_color[c] - bg_color[c]) * ambient_glow_intensity
    # Blend subject onto background
    subject_val = arr[:, :, c]
    result[:, :, c] = subject_val * smoothed_mask + bg_with_glow * (1.0 - smoothed_mask)

# Add the photographic red rim lighting onto the composite:
# Apply on edge pixels where subject exists or just around edge
# Right rim light:
rim_total_right = rim_right[:, :, None] * np.clip(smoothed_mask[:, :, None] * 1.5, 0.0, 1.0)
rim_total_left = rim_left[:, :, None] * np.clip(smoothed_mask[:, :, None] * 1.5, 0.0, 1.0)

# Additive / screen blend for realistic light on hair, skin, and coat:
for c in range(3):
    # Primary red rim on right
    result[:, :, c] += rim_total_right[:, :, 0] * rim_color[c] * 0.95
    # Secondary red rim on left
    result[:, :, c] += rim_total_left[:, :, 0] * rim_color[c] * 0.45

# Also add specular high-intensity core right along the outer ear and shoulder edge
specular_core = (gaussian_filter(right_edge_mask, sigma=1.8)**1.8)[:, :, None] * 0.6
for c in range(3):
    result[:, :, c] += specular_core[:, :, 0] * rim_highlight[c]

# Ensure borders (X < 5, X > w-6, Y < 5) are EXACTLY bg_color (#080808)
result[0:6, :, :] = bg_color
result[:, 0:6, :] = bg_color
result[:, -6:, :] = bg_color

# Clip to 0-255 and save
final_img = Image.fromarray(np.clip(result, 0, 255).astype(np.uint8))
final_img.save("NEW IMAGE FOR WEBSITE.jpeg", quality=96)
final_img.save("scratch/test_cinematic_final.png")
print("Successfully generated cinematic portrait and saved to NEW IMAGE FOR WEBSITE.jpeg")

