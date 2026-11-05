import subprocess
import os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_img = r"C:\Users\siddi\Desktop\New folder\test_file_uri.png"
file_url = "file:///c:/Users/siddi/Desktop/New folder/index.html?skip_preloader=1"

cmd = [
    CHROME,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1440,900",
    "--enable-logging=stderr",
    "--v=1",
    "--virtual-time-budget=1000",
    f"--screenshot={out_img}",
    file_url
]

res = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
print("File URI Chrome stderr:")
for line in res.stderr.splitlines():
    if any(k in line.lower() for k in ['error', 'warn', '404', 'net::', 'failed']):
        print("  ", line)
print("Screenshot size:", os.path.getsize(out_img) if os.path.exists(out_img) else 0)

