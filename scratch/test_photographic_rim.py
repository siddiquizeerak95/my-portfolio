import numpy as np
from PIL import Image

# Start from the unedited original image
# Let's inspect NEW IMAGE FOR WEBSITE.jpeg.orig
im_orig = Image.open("NEW IMAGE FOR WEBSITE.jpeg.orig").convert("RGB")
w_orig, h_orig = im_orig.size
print(f"Orig size: {w_orig}x{h_orig}")

# Let's crop the white borders from NEW IMAGE FOR WEBSITE.jpeg.orig
# In orig: white borders at top and bottom
arr_orig = np.array(im_orig)
# Find rows that are not white (mean < 250)
non_white_y = np.where(arr_orig.mean(axis=(1,2)) < 245)[0]
y_min, y_max = non_white_y.min(), non_white_y.max()
print(f"Non-white Y range: {y_min} to {y_max}")

# Crop to actual photo area
photo = arr_orig[y_min:y_max+1, :, :]
h, w, _ = photo.shape
print(f"Photo size: {w}x{h}")

# Save cropped clean original
Image.fromarray(photo).save("scratch/photo_clean_cropped.jpg", quality=98)

