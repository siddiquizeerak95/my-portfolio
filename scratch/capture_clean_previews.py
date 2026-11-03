import subprocess
import os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ARTIFACT_DIR = r"C:\Users\siddi\.gemini\antigravity\brain\4dd10c7b-bb97-46d2-a619-344ea8415c35"

def capture(url, out_name, size="1440,950"):
    dest = os.path.join(ARTIFACT_DIR, out_name)
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={size}",
        f"--screenshot={dest}",
        "--virtual-time-budget=2000",
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    exists = os.path.exists(dest)
    size_bytes = os.path.getsize(dest) if exists else 0
    print(f"Captured {out_name}: {exists} ({size_bytes} bytes)")

# 1. Desktop Light Mode
capture("http://127.0.0.1:5500/index.html?theme=light", "preview_hero_3d_perspective_light.png", "1440,950")

# 2. Tablet Dark Mode
capture("http://127.0.0.1:5500/index.html", "preview_hero_3d_perspective_tablet.png", "900,1050")

# 3. Mobile Dark Mode
capture("http://127.0.0.1:5500/index.html", "preview_hero_3d_perspective_mobile.png", "390,844")

print("Clean captures completed!")

