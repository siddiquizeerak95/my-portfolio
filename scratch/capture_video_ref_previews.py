import subprocess
import os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ARTIFACT_DIR = r"C:\Users\siddi\.gemini\antigravity\brain\4dd10c7b-bb97-46d2-a619-344ea8415c35"

def cap(url, name, size):
    dest = os.path.join(ARTIFACT_DIR, name)
    cmd = [CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--window-size={size}', f'--screenshot={dest}', '--virtual-time-budget=600', url]
    subprocess.run(cmd, timeout=10)
    print(name, os.path.exists(dest), os.path.getsize(dest) if os.path.exists(dest) else 0)

cap('http://127.0.0.1:5500/index.html?skip_preloader=1', 'preview_video_reference_hero_dark.png', '1440,950')
cap('http://127.0.0.1:5500/index.html?skip_preloader=1&theme=light', 'preview_video_reference_hero_light.png', '1440,950')
cap('http://127.0.0.1:5500/index.html?skip_preloader=1', 'preview_video_reference_hero_tablet.png', '900,1050')
cap('http://127.0.0.1:5500/index.html?skip_preloader=1', 'preview_video_reference_hero_mobile.png', '390,844')

print("All video reference previews captured!")

