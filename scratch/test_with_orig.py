import shutil
import subprocess
import os

# Backup current padded image
shutil.copy('NEW IMAGE FOR WEBSITE.jpeg', 'scratch/NEW_IMAGE_letterboxed.jpeg')

# Copy orig to NEW IMAGE FOR WEBSITE.jpeg
shutil.copy('NEW IMAGE FOR WEBSITE.jpeg.orig', 'NEW IMAGE FOR WEBSITE.jpeg')

# Also create profile-pic.jpg and Profile Pic.jpg and new image.jpeg so all paths work everywhere
shutil.copy('NEW IMAGE FOR WEBSITE.jpeg.orig', 'Profile Pic.jpg')
shutil.copy('NEW IMAGE FOR WEBSITE.jpeg.orig', 'new image.jpeg')

print("Copied orig (1203x1600) to NEW IMAGE FOR WEBSITE.jpeg, Profile Pic.jpg, and new image.jpeg")

# Now let's take a screenshot of index.html hero section
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_img = r"C:\Users\siddi\Desktop\New folder\test_hero_with_orig.png"

cmd = [
    CHROME,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1440,900",
    "--virtual-time-budget=800",
    f"--screenshot={out_img}",
    "http://127.0.0.1:5500/index.html?skip_preloader=1"
]

res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
print("Screenshot captured, size:", os.path.getsize(out_img) if os.path.exists(out_img) else 0)

