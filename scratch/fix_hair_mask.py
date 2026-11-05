import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter, binary_fill_holes

mask = np.array(Image.open("scratch/test_segmented_mask.png").convert("L")) > 128
photo = np.array(Image.open("scratch/pure_portrait_original.jpg"))
mean_val = photo.mean(axis=-1)

# In the hair area (Y: 30 to 200, X: 500 to 580):
# Hair edge: where mean_val > 19
hair_patch = (mean_val > 18)
mask[30:200, 500:580] |= hair_patch[30:200, 500:580]

# Also ensure smooth hair boundary at the top
mask = binary_fill_holes(mask)

Image.fromarray((mask * 255).astype(np.uint8)).save("scratch/perfect_segmented_mask.png")
print("Saved scratch/perfect_segmented_mask.png, count:", np.sum(mask))

