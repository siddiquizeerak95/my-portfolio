import subprocess
import os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\siddi\.gemini\antigravity\brain\4dd10c7b-bb97-46d2-a619-344ea8415c35"
out_img = os.path.join(artifact_dir, "test_cinematic_comparison.png")

cmd = [
    CHROME,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1200,800",
    "--virtual-time-budget=1000",
    f"--screenshot={out_img}",
    "http://127.0.0.1:5500/scratch/test_cinematic_hero.html"
]

res = subprocess.run(cmd, capture_output=True, timeout=20)
print("Captured comparison:", os.path.exists(out_img), os.path.getsize(out_img) if os.path.exists(out_img) else 0)

