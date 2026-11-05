import subprocess
import os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\siddi\.gemini\antigravity\brain\4dd10c7b-bb97-46d2-a619-344ea8415c35"

tests = [
    {
        "name": "hero_tablet.png",
        "size": "768,1024",
        "url": "http://127.0.0.1:5500/index.html?skip_preloader=1"
    },
    {
        "name": "hero_mobile.png",
        "size": "390,844",
        "url": "http://127.0.0.1:5500/index.html?skip_preloader=1"
    },
    {
        "name": "hero_light_mode.png",
        "size": "1440,900",
        "url": "http://127.0.0.1:5500/index.html?theme=light&skip_preloader=1"
    },
    {
        "name": "about_page_portrait.png",
        "size": "1440,900",
        "url": "http://127.0.0.1:5500/about.html?skip_preloader=1"
    }
]

for t in tests:
    out_path = os.path.join(artifact_dir, t["name"])
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        f"--window-size={t['size']}",
        "--virtual-time-budget=2000",
        f"--screenshot={out_path}",
        t["url"]
    ]
    subprocess.run(cmd, capture_output=True, timeout=20)
    print(f"Captured {t['name']}: exists={os.path.exists(out_path)}, size={os.path.getsize(out_path) if os.path.exists(out_path) else 0}")

