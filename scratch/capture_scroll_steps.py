import subprocess
import os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\siddi\.gemini\antigravity\brain\4dd10c7b-bb97-46d2-a619-344ea8415c35"

# We can test scroll positions using JavaScript evaluation in Chrome or by navigating with hash / scroll script
# Let's create an evaluation script that scrolls and captures
steps = [
    ("test_b3d_scroll_top.png", 0),
    ("test_b3d_scroll_mid1.png", 650),
    ("test_b3d_scroll_mid2.png", 1300),
    ("test_b3d_scroll_end.png", 1950)
]

for name, scroll_y in steps:
    out_path = os.path.join(artifact_dir, name)
    # We can inject a tiny script into test_blog_3d.html to scroll to scroll_y
    test_url = f"http://127.0.0.1:5500/scratch/test_blog_3d.html?scrolly={scroll_y}"
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--window-size=1440,900",
        "--virtual-time-budget=3000",
        f"--screenshot={out_path}",
        test_url
    ]
    subprocess.run(cmd, capture_output=True)
    print(f"Captured {name}: exists={os.path.exists(out_path)}, size={os.path.getsize(out_path) if os.path.exists(out_path) else 0}")
