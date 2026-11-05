import subprocess
import os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\siddi\Desktop\New folder"
out_img = os.path.join(artifact_dir, "test_hero_debug.png")

cmd = [
    CHROME,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1440,900",
    "--enable-logging=stderr",
    "--v=1",
    "--virtual-time-budget=1000",
    f"--screenshot={out_img}",
    "http://127.0.0.1:5500/index.html?skip_preloader=1"
]

res = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
print("Chrome stderr:")
for line in res.stderr.splitlines():
    if any(k in line.lower() for k in ['error', 'warn', 'image', '404', 'net::', 'failed']):
        print("  ", line)

print("Screenshot generated:", os.path.exists(out_img), os.path.getsize(out_img) if os.path.exists(out_img) else 0)

