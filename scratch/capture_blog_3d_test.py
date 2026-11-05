import subprocess
import os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\siddi\.gemini\antigravity\brain\4dd10c7b-bb97-46d2-a619-344ea8415c35"

# Let's test test_blog_3d.html
out_top = os.path.join(artifact_dir, "test_b3d_stage1.png")
cmd = [
    CHROME,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1440,900",
    "--virtual-time-budget=2000",
    f"--screenshot={out_top}",
    "http://127.0.0.1:5500/scratch/test_blog_3d.html"
]
subprocess.run(cmd, capture_output=True)
print("Captured stage 1:", os.path.exists(out_top), os.path.getsize(out_top) if os.path.exists(out_top) else 0)

