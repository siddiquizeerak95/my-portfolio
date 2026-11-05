import urllib.request
import urllib.parse

urls = [
    "http://127.0.0.1:5500/NEW%20IMAGE%20FOR%20WEBSITE.jpeg",
    "http://127.0.0.1:5500/NEW IMAGE FOR WEBSITE.jpeg",
    "http://127.0.0.1:5500/new%20image.jpeg",
    "http://127.0.0.1:5500/Profile%20Pic.jpg"
]

for u in urls:
    try:
        req = urllib.request.Request(urllib.parse.quote(u, safe=':/?=&'))
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            print(f"[SUCCESS] {u} -> Status: {resp.status}, Length: {len(data)} bytes, Content-Type: {resp.headers.get('Content-Type')}")
    except Exception as e:
        print(f"[ERROR] {u} -> {e}")

