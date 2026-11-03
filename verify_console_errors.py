import subprocess
import json

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
URLS = [
    "http://127.0.0.1:5500/index.html",
    "http://127.0.0.1:5500/about.html",
    "http://127.0.0.1:5500/projects.html",
    "http://127.0.0.1:5500/skills.html",
    "http://127.0.0.1:5500/blog.html",
    "http://127.0.0.1:5500/contact.html",
    "http://127.0.0.1:5500/blog-how-i-built-my-portfolio.html",
    "http://127.0.0.1:5500/blog-my-journey-as-a-developer.html",
    "http://127.0.0.1:5500/blog-why-i-prefer-minimalist-web-design.html",
    "http://127.0.0.1:5500/case-study.html",
    "http://127.0.0.1:5500/case-study-ecommerce.html",
    "http://127.0.0.1:5500/case-study-finance.html",
    "http://127.0.0.1:5500/case-study-banking.html",
    "http://127.0.0.1:5500/case-study-portfolio.html"
]

all_passed = True
for url in URLS:
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--enable-logging=stderr",
        "--v=1",
        "--virtual-time-budget=2000",
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    errors = [line for line in res.stderr.splitlines() if "ERROR:CONSOLE" in line]
    if errors:
        all_passed = False
        print(f"[FAIL] {url}:")
        for e in errors:
            print("  ", e)
    else:
        print(f"[PASS] {url}: 0 console errors")

if all_passed:
    print(f"\nALL {len(URLS)} PAGES PASSED WITH 0 CONSOLE ERRORS!")
