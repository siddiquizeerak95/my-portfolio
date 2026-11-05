import urllib.request
import subprocess
import time
import os

# Start a temporary python -m http.server on port 8081
p = subprocess.Popen(['python', '-m', 'http.server', '8081'])
time.sleep(1)

test_urls = [
    "http://127.0.0.1:8081/NEW%20IMAGE%20FOR%20WEBSITE.jpeg",
    "http://127.0.0.1:8081/NEW%2520IMAGE%2520FOR%2520WEBSITE.jpeg",
    "http://127.0.0.1:8081/new%20image.jpeg",
    "http://127.0.0.1:8081/Profile%20Pic.jpg",
]

for u in test_urls:
    try:
        with urllib.request.urlopen(u) as resp:
            print(f"[200 OK] {u} -> length {len(resp.read())}")
    except Exception as e:
        print(f"[FAIL] {u} -> {e}")

p.terminate()
p.wait()

