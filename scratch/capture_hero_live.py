import subprocess
import os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\siddi\.gemini\antigravity\brain\4dd10c7b-bb97-46d2-a619-344ea8415c35"
out_img = os.path.join(artifact_dir, "hero_portrait_live.png")

cmd = [
    CHROME,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1440,900",
    "--enable-logging=stderr",
    "--v=1",
    "--virtual-time-budget=2000",
    f"--screenshot={out_img}",
    "http://127.0.0.1:5500/index.html?skip_preloader=1"
]

res = subprocess.run(cmd, capture_output=True, text=True, timeout=25)
print("Chrome stderr errors/warnings:")
for line in res.stderr.splitlines():
    if any(k in line.lower() for k in ['error', 'warn', 'image', '404', 'net::', 'failed']):
        print("  ", line)

print("Screenshot generated:", os.path.exists(out_img), os.path.getsize(out_img) if os.path.exists(out_img) else 0)

