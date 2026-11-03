import subprocess
import os
import sys

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE_DIR = r"c:\Users\siddi\Desktop\New folder"

def capture_screenshot(url, filename, window_size="1440,900", virtual_time=2500):
    output_path = os.path.join(BASE_DIR, filename)
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={window_size}",
        f"--screenshot={output_path}",
        f"--virtual-time-budget={virtual_time}",
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    exists = os.path.exists(output_path)
    size = os.path.getsize(output_path) if exists else 0
    print(f"Captured {filename}: {exists} ({size} bytes)")
    return exists

if __name__ == "__main__":
    if len(sys.argv) > 2:
        capture_screenshot(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "1440,900")
    else:
        capture_screenshot("http://127.0.0.1:5500/about.html", "preview_redesigned_about.png")
