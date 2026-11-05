import os

for root, dirs, files in os.walk('.'):
    # Skip .git and brain
    if '.git' in root or '.system_generated' in root:
        continue
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        if ext in ['.jpg', '.jpeg', '.png', '.webp', '.svg']:
            p = os.path.join(root, f)
            print(f"{p}: {os.path.getsize(p)} bytes")

