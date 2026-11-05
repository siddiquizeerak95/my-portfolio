import subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

files = ["v1_encoded.html", "v2_spaces.html", "v3_clean.html", "v4_clean_spaces.html"]

print("--- Testing via HTTP Server (http://127.0.0.1:5500/) ---")
for f in files:
    url = f"http://127.0.0.1:5500/{f}"
    cmd = [
        CHROME,
        "--headless=new",
        "--dump-dom",
        "--virtual-time-budget=600",
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    # Check result div
    res_text = ""
    if '<div id="result">' in res.stdout:
        res_text = res.stdout.split('<div id="result">')[1].split('</div>')[0]
    print(f"HTTP {f}: result = '{res_text}'")

print("\n--- Testing via FILE:/// URI ---")
for f in files:
    import os
    abs_path = os.path.abspath(f).replace('\\', '/')
    url = f"file:///{abs_path}"
    cmd = [
        CHROME,
        "--headless=new",
        "--dump-dom",
        "--virtual-time-budget=600",
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    res_text = ""
    if '<div id="result">' in res.stdout:
        res_text = res.stdout.split('<div id="result">')[1].split('</div>')[0]
    print(f"FILE {f}: result = '{res_text}'")

