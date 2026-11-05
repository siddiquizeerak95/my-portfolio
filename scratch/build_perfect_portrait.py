import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import gaussian_filter, distance_transform_edt

im = Image.open("NEW IMAGE FOR WEBSITE.jpeg").convert("RGB")
w, h = im.size
arr = np.array(im, dtype=float)

# Background color of the website
bg_target = np.array([8.0, 8.0, 8.0])

# Subject region:
# Face / skin coordinates:
# X: 275 to 570, Y: 90 to 465
# Hair: X: 280 to 565, Y: 30 to 220
# Coat: Y: 420 to 922, expanding out to X: 35 to 805

# Notice: What needs to fade to #080808?
# Only the background areas!
# Area 1: Top background (Y: 0 to 45)
# Area 2: Top-left window shadow (X: 0 to 270, Y: 0 to 440)
# Area 3: Top-right studio background (X: 570 to 842, Y: 0 to 440)
# Area 4: Left edge outside coat (X: 0 to 40, Y: 440 to 922)
# Area 5: Right edge outside coat (X: 800 to 842, Y: 440 to 922)
# Area 6: Bottom edge of coat (Y: 820 to 922) so it melts into the black floor

# Let's create an exact subject mask M:
# In the subject area: M = 1.0 (preserve 100% authentic photograph)
# In the outer background: M = 0.0 (smoothly becomes pure #080808)
# In the transition: smooth cosine / hermite blend

# Let's define the boundary curve of Zeerak:
# For each Y from 0 to h-1, define left_bound and right_bound
left_bound = np.zeros(h)
right_bound = np.zeros(h)

for y in range(h):
    if y < 35:
        # Above hair: all background
        left_bound[y] = 421
        right_bound[y] = 421
    elif y < 140:
        # Top of hair: dome shape
        prog = (y - 35) / 105.0
        # semicircle radius ~ 135
        rad = np.sqrt(max(0.01, 1.0 - (1.0 - prog)**2)) * 135
        left_bound[y] = 421 - rad
        right_bound[y] = 421 + rad
    elif y < 240:
        # Hair sides & temples
        left_bound[y] = 278
        right_bound[y] = 564
    elif y < 360:
        # Ears and cheeks (ears poke out to 270 and 572)
        left_bound[y] = 265
        right_bound[y] = 575
    elif y < 450:
        # Jaw and neck
        left_bound[y] = 285
        right_bound[y] = 555
    elif y < 550:
        # Shoulders (sloping down)
        prog = (y - 450) / 100.0
        left_bound[y] = 285 - prog * 175  # expands from 285 to 110
        right_bound[y] = 555 + prog * 165 # expands from 555 to 720
    elif y < 750:
        # Upper coat & arms
        prog = (y - 550) / 200.0
        left_bound[y] = 110 - prog * 65   # expands from 110 to 45
        right_bound[y] = 720 + prog * 65  # expands from 720 to 785
    else:
        # Lower coat
        prog = (y - 750) / 172.0
        left_bound[y] = 45 - prog * 25    # expands from 45 to 20
        right_bound[y] = 785 + prog * 30  # expands from 785 to 815

# Now generate a distance field from the boundary
mask = np.zeros((h, w), dtype=float)
xx, yy = np.meshgrid(np.arange(w), np.arange(h))

for y in range(h):
    lb = left_bound[y]
    rb = right_bound[y]
    if lb >= rb:
        continue
    # Inside subject
    row_x = np.arange(w)
    inside = (row_x >= lb) & (row_x <= rb)
    mask[y, inside] = 1.0

# Smooth the mask with gaussian filter for organic edge feathering
# Hair and shoulders get a smooth 8-pixel feathered edge
smoothed_mask = gaussian_filter(mask, sigma=5.0)

# Also fade the bottom 100 pixels to #080808 so the coat bottom melts into the viewport
bottom_fade = np.ones(h)
for y in range(h - 110, h):
    bottom_fade[y] = max(0.0, (h - 1 - y) / 110.0)
smoothed_mask = smoothed_mask * bottom_fade[:, None]

# Now, let's create the composite:
# composite = arr * smoothed_mask + bg_target * (1.0 - smoothed_mask)
composite = np.zeros_like(arr)
for c in range(3):
    composite[:, :, c] = arr[:, :, c] * smoothed_mask + bg_target[c] * (1.0 - smoothed_mask)

# Save intermediate preview
Image.fromarray(np.clip(composite, 0, 255).astype(np.uint8)).save("scratch/feathered_blend.png")
print("Saved scratch/feathered_blend.png")

