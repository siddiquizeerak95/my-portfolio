import numpy as np
from PIL import Image
import pymatting
from scipy.ndimage import binary_erosion, binary_dilation

print("Loading image...")
img = Image.open("NEW IMAGE FOR WEBSITE.jpeg").convert("RGB")
w, h = img.size
img_arr = np.array(img, dtype=np.float64) / 255.0

print(f"Image shape: {img_arr.shape}")

