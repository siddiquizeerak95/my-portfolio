import subprocess, os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\siddi\.gemini\antigravity\brain\4dd10c7b-bb97-46d2-a619-344ea8415c35"

scroll_points = [0, 400, 800, 1200, 1600, 2000]

for s in scroll_points:
    out = os.path.join(artifact_dir, f"blog_test_scroll_{s}.png")
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--window-size=1440,900",
        "--virtual-time-budget=2000",
        f"--screenshot={out}",
        f"http://127.0.0.1:5500/blog.html?scroll={s}"
    ]
    subprocess.run(cmd, capture_output=True, timeout=25)
    print(f"Scroll {s} captured:", os.path.exists(out), os.path.getsize(out) if os.path.exists(out) else 0)

