import numpy as np
from PIL import Image

m1 = np.array(Image.open("scratch/watershed_mask.png").convert("L")) > 128
m2 = np.array(Image.open("scratch/watershed_full_mask.png").convert("L")) > 128

# m1 has the head & hair (Y < 450)
# m2 has the coat (Y >= 450)
combined = np.zeros_like(m1)
combined[:440, :] = m1[:440, :]
combined[440:, :] = m2[440:, :]

Image.fromarray((combined * 255).astype(np.uint8)).save("scratch/perfect_mask.png")
print("Saved scratch/perfect_mask.png")

