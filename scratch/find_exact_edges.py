import numpy as np
from PIL import Image

im = Image.open("NEW IMAGE FOR WEBSITE.jpeg")
arr = np.array(im)
h, w, _ = arr.shape
r = arr[:, :, 0].astype(float)
g = arr[:, :, 1].astype(float)
b = arr[:, :, 2].astype(float)

skin = (r > 95) & (g > 40) & (b > 20) & ((r - g) > 12) & (r > b)

# For each Y in face region (240 to 450), find min and max X of skin:
print("Skin boundaries:")
for y in range(240, 460, 20):
    xs = np.where(skin[y, :])[0]
    if len(xs) > 0:
        print(f"Y={y}: skin left={xs.min()}, right={xs.max()}")

# For coat region (460 to 920):
# Coat is dark wool, but has luminance > 12 (background near border is 6-8)
# Let's inspect where coat edge is:
print("\nCoat boundaries:")
for y in range(460, 920, 50):
    # Coat center is around 420. Look outward from 420 to left and right:
    # Coat has distinct texture/values
    # In each row, let's see where the edge drops to background (< 15)
    row = arr[y, :, :].mean(axis=-1)
    # find where row > 15
    above_bg = np.where(row > 15)[0]
    if len(above_bg) > 0:
        print(f"Y={y}: row > 15 range: {above_bg.min()} to {above_bg.max()}")

