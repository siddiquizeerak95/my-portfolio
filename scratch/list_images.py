import os

files = os.listdir('.')
for f in sorted(files):
    ext = os.path.splitext(f)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png', '.webp', '.svg']:
        size = os.path.getsize(f)
        print(f"{f}: {size} bytes")

