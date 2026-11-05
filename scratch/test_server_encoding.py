import urllib.request

url1 = "http://127.0.0.1:5500/NEW%20IMAGE%20FOR%20WEBSITE.jpeg"
try:
    with urllib.request.urlopen(url1) as resp:
        print("URL1 (with %20) status:", resp.status, "length:", len(resp.read()))
except Exception as e:
    print("URL1 error:", e)

url2 = "http://127.0.0.1:5500/NEW IMAGE FOR WEBSITE.jpeg"
try:
    with urllib.request.urlopen(url2) as resp:
        print("URL2 (with spaces) status:", resp.status, "length:", len(resp.read()))
except Exception as e:
    print("URL2 error:", e)

