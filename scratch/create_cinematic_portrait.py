import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import distance_transform_edt, gaussian_filter

# 1. Load the original portrait
img = Image.open("NEW IMAGE FOR WEBSITE.jpeg").convert("RGB")
w, h = img.size
arr = np.array(img, dtype=np.float64)

print(f"Loaded image {w}x{h}")

# Target website background: #080808
bg_color = np.array([8.0, 8.0, 8.0])

# 2. Segment the subject
# Zeerak is composed of:
# - Skin (face, ears, neck): R > 90, typical skin tone ratios
# - Hair: top center, dark with some texture (R: 15-45, G: 15-45, B: 15-45)
# - Turtleneck: center below chin, black/dark knit
# - Overcoat: shoulders and chest, black wool with lapels
# The background:
# - Left window shadow: diffuse lighter grey-black stripes
# - Right wall: dark grey-black
# Top background: Y < 40
# Outer left: X < 60
# Outer right: X > 780

# Let's create an accurate subject mask using spatial + color analysis
# Subject is roughly inside an ellipse / convex hull centered horizontally
x_coords = np.arange(w)
y_coords = np.arange(h)
xx, yy = np.meshgrid(x_coords, y_coords)

# Face & hair region (Y from 30 to 450, X from 260 to 580)
# Torso & shoulders region (Y from 400 to 922, X from 50 to 800)
# Subject boundary prior
subject_prior = np.zeros((h, w), dtype=bool)

# Upper body trapezoid / ellipse
for y in range(h):
    if y < 35:
        # Above hair: background
        continue
    elif y < 220:
        # Hair region: X between 270 and 570
        hw = 160 + (y - 35) * 0.2
        subject_prior[y, int(423 - hw):int(423 + hw)] = True
    elif y < 450:
        # Face, ears, neck
        # Ears extend to ~270 on left, 575 on right
        ew = 165
        subject_prior[y, int(423 - ew):int(423 + ew)] = True
    else:
        # Shoulders and coat: widens as Y goes down
        # At y=500: width ~ 240 each side
        # At y=922: width ~ 390 each side (almost full width at bottom)
        prog = (y - 450) / (922 - 450)
        sw = 175 + prog * 215
        subject_prior[y, max(0, int(423 - sw)):min(w, int(423 + sw))] = True

# Now refine using image features:
# Background is dark grey/black; subject face/skin is bright; hair/coat has texture
# Let's inspect differences between subject and background
mask = np.zeros((h, w), dtype=float)

# In the subject prior, distinguish subject from the studio background
# Skin pixels are 100% subject
r = arr[:, :, 0]
g = arr[:, :, 1]
b = arr[:, :, 2]
skin_mask = (r > 95) & (g > 40) & (b > 20) & ((r - g) > 12) & (r > b) & (xx > 260) & (xx < 580) & (yy > 80) & (yy < 480)

# Hair region
hair_mask = (yy >= 35) & (yy <= 240) & (xx >= 290) & (xx <= 560)

# Turtleneck & coat region
coat_mask = (yy >= 420) & subject_prior

# Combine initial subject core
subject_core = skin_mask | hair_mask | coat_mask

# Now smooth and expand to natural silhouette
# Use distance transform from core and distance from background
bg_seeds = np.zeros((h, w), dtype=bool)
bg_seeds[0:30, :] = True
bg_seeds[:, 0:40] = True
bg_seeds[:, -40:] = True
# Upper left corner where window shadow was
bg_seeds[0:350, 0:240] = True
# Upper right corner
bg_seeds[0:350, 600:] = True

# Ensure skin and hair are NOT in bg_seeds
bg_seeds = bg_seeds & (~skin_mask) & (~hair_mask)

print("Computing smooth alpha matte...")
# Trimap: 1.0 = subject, 0.0 = background, 0.5 = boundary
trimap = np.full((h, w), 0.5)
trimap[bg_seeds] = 0.0

# Solid foreground: core inside subject
fg_seeds = np.zeros((h, w), dtype=bool)
fg_seeds[skin_mask] = True
fg_seeds[(yy >= 60) & (yy <= 200) & (xx >= 330) & (xx <= 520)] = True # hair center
fg_seeds[(yy >= 480) & (yy <= 880) & (xx >= 200) & (xx <= 650)] = True # coat center
trimap[fg_seeds] = 1.0

# Solve alpha matte using pymatting
import pymatting
alpha = pymatting.estimate_alpha_lkm(arr / 255.0, trimap)
alpha = np.clip(alpha, 0.0, 1.0)

# Let's also ensure bottom of coat dissolves smoothly into #080808
bottom_fade = np.ones((h, w))
for y in range(h - 120, h):
    bottom_fade[y, :] = (h - 1 - y) / 120.0
alpha = alpha * bottom_fade

# 3. Create composite with pure #080808 background
composite = np.zeros((h, w, 3), dtype=np.float64)
for c in range(3):
    composite[:, :, c] = arr[:, :, c] * alpha + bg_color[c] * (1.0 - alpha)

# 4. Save test cutout and composite
Image.fromarray((alpha * 255).astype(np.uint8)).save("scratch/test_alpha.png")
Image.fromarray(np.clip(composite, 0, 255).astype(np.uint8)).save("scratch/test_composite.png")
print("Saved scratch/test_alpha.png and scratch/test_composite.png")
