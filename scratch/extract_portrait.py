from PIL import Image
from rembg import remove
import os

input_path = "NEW IMAGE FOR WEBSITE.jpeg"
output_path = "zeerak_portrait_transparent.png"

print(f"Reading {input_path}...")
inp = Image.open(input_path)
print(f"Input size: {inp.size}, format: {inp.format}")

print("Removing background with rembg...")
out = remove(inp)

print(f"Saving transparent cutout to {output_path}...")
out.save(output_path, "PNG")
print(f"Done! File size: {os.path.getsize(output_path)} bytes")

