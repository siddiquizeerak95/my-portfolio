import os

files = os.listdir('.')
matches = [f for f in files if 'image' in f.lower() or 'pic' in f.lower() or 'profile' in f.lower()]
print("Matching files:", matches)

for m in matches:
    print(f"File: '{m}', size: {os.path.getsize(m)}, exists: {os.path.exists(m)}")

