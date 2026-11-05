import numpy as np
from PIL import Image
import skimage.filters
import skimage.segmentation
import skimage.morphology

photo = Image.open("scratch/pure_portrait_original.jpg").convert("RGB")
w, h = photo.size
arr = np.array(photo)
gray = skimage.color.rgb2gray(arr)

# 1. Markers: 1 = Background, 2 = Foreground, 0 = Unknown
markers = np.zeros_like(gray, dtype=int)

# Background seeds:
markers[0:30, :] = 1 # top
markers[0:350, 0:180] = 1 # upper left window gobo
markers[0:350, 640:] = 1  # upper right dark charcoal
markers[350:, 0:25] = 1   # far left edge
markers[350:, 790:] = 1   # far right edge

# Foreground seeds:
markers[240:420, 360:460] = 2 # face
markers[60:180, 360:460] = 2  # hair center
markers[440:560, 380:450] = 2 # turtleneck
markers[580:850, 180:350] = 2 # left lapel & chest
markers[580:850, 470:640] = 2 # right lapel & chest
markers[620:850, 70:180] = 2  # left arm
markers[620:850, 640:760] = 2 # right arm

# Elevation map: Sobel filter
elevation = skimage.filters.sobel(gray)

# Watershed segmentation
seg = skimage.segmentation.watershed(elevation, markers)
mask = (seg == 2)

# Fill holes
mask = skimage.morphology.remove_small_holes(mask, max_size=10000)
mask = skimage.morphology.remove_small_objects(mask, max_size=10000)

print(f"Mask computed! Foreground pixels: {np.sum(mask)}")
Image.fromarray((mask * 255).astype(np.uint8)).save("scratch/test_segmented_mask.png")

