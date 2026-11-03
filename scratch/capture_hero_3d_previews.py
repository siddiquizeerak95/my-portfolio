import subprocess
import os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ARTIFACT_DIR = r"C:\Users\siddi\.gemini\antigravity\brain\4dd10c7b-bb97-46d2-a619-344ea8415c35"

def capture(url, out_name, size="1440,950", vtime=8500):
    dest = os.path.join(ARTIFACT_DIR, out_name)
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={size}",
        f"--screenshot={dest}",
        f"--virtual-time-budget={vtime}",
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    print(f"Captured {out_name}: {os.path.exists(dest)} ({os.path.getsize(dest) if os.path.exists(dest) else 0} bytes)")

# 1. Desktop Dark Mode
capture("http://127.0.0.1:5500/index.html", "preview_hero_3d_perspective_dark.png", "1440,950")

# 2. Desktop Light Mode
capture("http://127.0.0.1:5500/index.html?theme=light", "preview_hero_3d_perspective_light.png", "1440,950")

# 3. Tablet Dark Mode
capture("http://127.0.0.1:5500/index.html", "preview_hero_3d_perspective_tablet.png", "900,1050")

# 4. Mobile Dark Mode
capture("http://127.0.0.1:5500/index.html", "preview_hero_3d_perspective_mobile.png", "390,844")

print("All 3D Perspective hero previews captured!")

