import subprocess
import sys
import time
import os
import urllib.request

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

PAGES = [
    "index.html",
    "about.html",
    "projects.html",
    "skills.html",
    "blog.html",
    "contact.html",
    "blog-how-i-built-my-portfolio.html",
    "blog-my-journey-as-a-developer.html",
    "blog-why-i-prefer-minimalist-web-design.html",
    "case-study.html",
    "case-study-ecommerce.html",
    "case-study-finance.html",
    "case-study-banking.html",
    "case-study-portfolio.html"
]

def is_console_error(line):
    """Categorizes whether a Chrome log line represents an actionable runtime console error."""
    # 1. Chrome ERROR level console log
    if "ERROR:CONSOLE" in line:
        return True

    # 2. Chrome :CONSOLE: entries
    if ":CONSOLE:" in line:
        # Ignore benign browser notices
        if "<link rel=preload> uses an unsupported `as` value" in line:
            return False

        # Actionable error patterns
        error_indicators = [
            "Uncaught ",
            "Error:",
            "TypeError",
            "ReferenceError",
            "SyntaxError",
            "RangeError",
            "Failed to load resource",
            "net::ERR_",
            "404 (Not Found)",
            "Refused to apply style",
            "Refused to execute script",
            "Deliberate test error",
            "❌"
        ]
        for ind in error_indicators:
            if ind.lower() in line.lower():
                return True

    return False

def detect_base_url():
    """Detects active server port or parses CLI override."""
    for i, arg in enumerate(sys.argv):
        if arg == "--url" and i + 1 < len(sys.argv):
            return sys.argv[i + 1].rstrip("/")
        if arg.startswith("--url="):
            return arg.split("=", 1)[1].rstrip("/")
        if arg == "--port" and i + 1 < len(sys.argv):
            return f"http://127.0.0.1:{sys.argv[i + 1]}"
        if arg.startswith("--port="):
            return f"http://127.0.0.1:{arg.split('=', 1)[1]}"

    for port in [8080, 5500]:
        test_url = f"http://127.0.0.1:{port}/index.html"
        try:
            req = urllib.request.urlopen(test_url, timeout=1.0)
            if req.status == 200:
                print(f"[INFO] Auto-detected active server on port {port}")
                return f"http://127.0.0.1:{port}"
        except Exception:
            continue

    print("[WARN] No active server detected on port 8080 or 5500. Defaulting to http://127.0.0.1:8080")
    return "http://127.0.0.1:8080"

def audit_url(url, timeout=15):
    """Executes headless Chrome against the URL and extracts console errors."""
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--enable-logging=stderr",
        "--v=1",
        "--dump-dom",
        "--virtual-time-budget=2000",
        url
    ]
    t0 = time.time()
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        elapsed = time.time() - t0
        errors = [line.strip() for line in res.stderr.splitlines() if is_console_error(line)]
        return errors, elapsed
    except subprocess.TimeoutExpired:
        elapsed = time.time() - t0
        return [f"TIMEOUT: Page execution timed out after {timeout}s"], elapsed

def main():
    positional_args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if positional_args:
        target = positional_args[0]
        if not target.startswith("http://") and not target.startswith("https://"):
            base = detect_base_url()
            target = f"{base}/{target.lstrip('/')}"

        print(f"Auditing single target: {target}")
        errors, elapsed = audit_url(target)
        if errors:
            print(f"[FAIL] ({elapsed:.2f}s) {target}: {len(errors)} error(s) detected")
            for e in errors:
                print("   ❌", e)
            sys.exit(1)
        else:
            print(f"[PASS] ({elapsed:.2f}s) {target}: 0 console errors")
            sys.exit(0)

    base_url = detect_base_url()
    print("=" * 80)
    print(f"ZS STUDIO — HEADLESS CHROME CONSOLE ERROR AUDIT ({len(PAGES)} Pages)")
    print(f"Base URL: {base_url}")
    print("=" * 80)

    all_passed = True
    total_time = 0.0

    for page in PAGES:
        url = f"{base_url}/{page}"
        errors, elapsed = audit_url(url)
        total_time += elapsed

        if errors:
            all_passed = False
            print(f"[FAIL] ({elapsed:.2f}s) {url}:")
            for e in errors:
                print("   ❌", e)
        else:
            print(f"[PASS] ({elapsed:.2f}s) {url}: 0 console errors")

    print("=" * 80)
    print(f"Audit completed in {total_time:.2f}s across {len(PAGES)} pages.")

    if all_passed:
        print(f"RESULT: ALL {len(PAGES)} PAGES PASSED WITH 0 CONSOLE ERRORS!")
        print("=" * 80)
        sys.exit(0)
    else:
        print("RESULT: CONSOLE ERRORS DETECTED ON ONE OR MORE PAGES.")
        print("=" * 80)
        sys.exit(1)

if __name__ == "__main__":
    main()
