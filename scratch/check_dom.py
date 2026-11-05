import subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    CHROME,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1440,900",
    "--virtual-time-budget=2000",
    "--dump-dom",
    "http://127.0.0.1:5500/blog.html"
]
res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
for i in range(3):
    print(f"b3d-card-{i} in DOM:", f'id="b3d-card-{i}"' in res.stdout)

