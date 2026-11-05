import numpy as np
from PIL import Image

img = Image.open("NEW IMAGE FOR WEBSITE.jpeg")
arr = np.array(img)
h, w, _ = arr.shape

# Let's find skin tone pixels (Cb, Cr or R > G > B with typical skin ratio)
r = arr[:, :, 0].astype(float)
g = arr[:, :, 1].astype(float)
b = arr[:, :, 2].astype(float)

# Skin condition
skin_mask = (r > 95) & (g > 40) & (b > 20) & ((r - g) > 15) & (r > b) & ((r - b) > 15)
skin_y, skin_x = np.where(skin_mask)

print(f"Skin pixels count: {len(skin_y)}")
print(f"Skin X range: {skin_x.min()} to {skin_x.max()} (center: {(skin_x.min() + skin_x.max())/2})")
print(f"Skin Y range: {skin_y.min()} to {skin_y.max()} (center: {(skin_y.min() + skin_y.max())/2})")

