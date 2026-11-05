import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

# Load the pure original
photo = Image.open("scratch/pure_portrait_original.jpg").convert("RGB")
w, h = photo.size
arr = np.array(photo, dtype=float)
print(f"Loaded pure photo: {w}x{h}")

bg = np.array([8.0, 8.0, 8.0]) # Target #080808

# Create an alpha / blend weight for the background
# 1.0 = keep original photo pixel
# 0.0 = pure #080808 background
blend = np.ones((h, w), dtype=float)

# 1. Top background fade (above hair, Y < 40)
for y in range(45):
    blend[y, :] *= max(0.0, (y - 5) / 40.0)

# 2. Left window gobo fade (X < 275, Y < 460)
for y in range(460):
    for x in range(275):
        # Distance from subject edge at (y, 275)
        dist_x = (275 - x) / 275.0
        # Smooth cosine drop to 0
        factor = 0.5 * (1.0 + np.cos(np.clip(dist_x * np.pi, 0, np.pi)))
        blend[y, x] = min(blend[y, x], factor)

# 3. Right background fade (X > 560, Y < 460)
for y in range(460):
    for x in range(560, w):
        dist_x = (x - 560) / (w - 560.0)
        factor = 0.5 * (1.0 + np.cos(np.clip(dist_x * np.pi, 0, np.pi)))
        blend[y, x] = min(blend[y, x], factor)

# 4. Far left and far right coat edges fade
for x in range(35):
    blend[:, x] *= max(0.0, x / 35.0)
for x in range(w - 35, w):
    blend[:, x] *= max(0.0, (w - 1 - x) / 35.0)

# 5. Bottom coat dissolve (Y from h-100 to h)
for y in range(h - 100, h):
    prog = (h - 1 - y) / 100.0
    blend[y, :] *= max(0.0, prog)

# Apply the background blend to pure #080808
result = np.zeros_like(arr)
for c in range(3):
    result[:, :, c] = arr[:, :, c] * blend + bg[c] * (1.0 - blend)

# 6. ADD THE PHOTOGRAPHIC RED RIM LIGHT (Like Daniel Smith reference)
# In Daniel Smith:
# Red kicker light hits the right edge (viewer's right) of hair, ear, jaw, neck, shoulder, and coat.
# Let's define the rim light zone:
# Face / hair right edge: Y from 50 to 450, X from 510 to 575
# Shoulder right edge: Y from 450 to 650, X from 640 to 800
# Coat right edge: Y from 650 to 880, X from 720 to 814

rim_mask = np.zeros((h, w), dtype=float)

# Hair & ear rim light (subtle, beautiful crimson highlight on edge)
for y in range(50, 440):
    if y < 240:
        # Hair right edge
        edge_x = 555
        sigma_x = 18
    elif y < 330:
        # Ear rim (catches bright red rim light!)
        edge_x = 566
        sigma_x = 14
    else:
        # Jaw & neck edge
        edge_x = 520
        sigma_x = 16
    
    for x in range(w):
        # Light falls on the edge of the subject
        dist = abs(x - edge_x)
        if dist < sigma_x * 2.2:
            intensity = np.exp(-0.5 * (dist / sigma_x)**2)
            # Modulate by subject presence (blend > 0.4)
            rim_mask[y, x] = intensity * blend[y, x]

# Shoulder & coat rim light
for y in range(440, 880):
    if y < 580:
        # Shoulder curve
        prog = (y - 440) / 140.0
        edge_x = 530 + prog * 230
        sigma_x = 24
    else:
        # Outer coat arm
        edge_x = 765
        sigma_x = 28
    
    for x in range(w):
        dist = abs(x - edge_x)
        if dist < sigma_x * 2.0:
            intensity = np.exp(-0.5 * (dist / sigma_x)**2)
            rim_mask[y, x] = intensity * blend[y, x]

# Smooth the rim light for natural falloff
rim_mask = gaussian_filter(rim_mask, sigma=2.0)

# Red rim light colors:
# Primary red: #E5092B (229, 9, 43)
# Hot specular core: (255, 75, 95)
rim_color = np.array([229.0, 12.0, 43.0])
specular_color = np.array([255.0, 90.0, 110.0])

# Add the red rim light onto the subject pixels
# Screen blend formula: 1 - (1 - A)*(1 - B)
for c in range(3):
    # Base red rim
    rim_val = rim_mask * (rim_color[c] / 255.0) * 0.85
    # Add specular core where rim is strongest (> 0.6)
    spec_val = np.maximum(0.0, (rim_mask - 0.5) / 0.5)**1.5 * (specular_color[c] / 255.0) * 0.45
    
    # Apply onto result
    curr = result[:, :, c] / 255.0
    screened = 1.0 - (1.0 - curr) * (1.0 - (rim_val + spec_val))
    result[:, :, c] = screened * 255.0

# 7. Subtle atmospheric red backlight glow
# Soft, low-intensity glow radiating behind the subject
xx, yy = np.meshgrid(np.arange(w), np.arange(h))
dist_center = np.sqrt(((xx - 450) / 1.4)**2 + ((yy - 320) / 1.0)**2)
ambient_glow = np.exp(-0.5 * (dist_center / 220.0)**2) * 0.22 # gentle
for c in range(3):
    glow_val = ambient_glow * (1.0 - blend) * rim_color[c]
    result[:, :, c] += glow_val

# Ensure all 4 outer borders are 100% pure #080808
result[0:4, :, :] = bg
result[-4:, :, :] = bg
result[:, 0:4, :] = bg
result[:, -4:, :] = bg

# Save final image!
final = Image.fromarray(np.clip(result, 0, 255).astype(np.uint8))
final.save("scratch/test_daniel_style.png")
print("Saved scratch/test_daniel_style.png")

