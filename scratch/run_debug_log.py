import subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    CHROME,
    "--headless=new",
    "--disable-gpu",
    "--enable-logging=stderr",
    "--v=1",
    "--window-size=1440,900",
    "--virtual-time-budget=2000",
    "http://127.0.0.1:5500/blog.html?scroll=1200"
]
res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
for line in res.stderr.splitlines():
    if "CONSOLE" in line or "DEBUG" in line or "Error" in line:
        print(line)

