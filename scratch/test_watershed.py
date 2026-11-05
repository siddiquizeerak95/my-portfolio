import numpy as np
from PIL import Image
import skimage.filters
import skimage.segmentation
import skimage.morphology
from scipy.ndimage import gaussian_filter

photo = Image.open("scratch/pure_portrait_original.jpg").convert("RGB")
w, h = photo.size
arr = np.array(photo)
gray = skimage.color.rgb2gray(arr)

# Background seeds: top, left, right edges where we know it is background
markers = np.zeros_like(gray, dtype=int)
markers[0:20, :] = 1 # bg
markers[:, 0:15] = 1 # bg
markers[:, -15:] = 1 # bg
markers[0:250, 0:120] = 1 # bg upper left
markers[0:250, -120:] = 1 # bg upper right

# Foreground seeds
markers[180:350, 360:460] = 2 # face
markers[50:180, 340:480] = 2  # hair center
markers[440:600, 370:450] = 2 # turtleneck
markers[550:850, 100:300] = 2 # left coat & shoulder
markers[550:850, 520:720] = 2 # right coat & shoulder
markers[650:900, 300:520] = 2 # coat center

# Elevation map using Sobel
elevation_map = skimage.filters.sobel(gray)

# Watershed segmentation
seg = skimage.segmentation.watershed(elevation_map, markers)
mask = (seg == 2)

# Fill holes
mask = skimage.morphology.remove_small_holes(mask, max_size=5000)
mask = skimage.morphology.remove_small_objects(mask, max_size=5000)

print("Watershed complete, mask true count:", np.sum(mask))
Image.fromarray((mask * 255).astype(np.uint8)).save("scratch/watershed_full_mask.png")
