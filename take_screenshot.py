import subprocess
import os
import sys
import urllib.request
import re

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SCREENSHOT_DIR = os.path.join(PROJECT_ROOT, "scratch", "screenshots")

def detect_base_url():
    """Detects active server port (8080 or 5500)."""
    for port in [8080, 5500]:
        test_url = f"http://127.0.0.1:{port}/index.html"
        try:
            req = urllib.request.urlopen(test_url, timeout=1.0)
            if req.status == 200:
                return f"http://127.0.0.1:{port}"
        except Exception:
            continue
    return "http://127.0.0.1:8080"

def resolve_output_path(target_path, allow_overwrite=False):
    """
    Resolves the destination path ensuring it is safely inside scratch/screenshots/
    by default, auto-creates parent folders, and handles overwrite safety.
    """
    if not target_path:
        target_path = "screenshot.png"

    # If user provided a bare filename or relative path without directory, place in DEFAULT_SCREENSHOT_DIR
    if not os.path.isabs(target_path):
        # If target starts with scratch/ or scratch\, resolve from PROJECT_ROOT
        if target_path.startswith("scratch"):
            target_path = os.path.join(PROJECT_ROOT, target_path)
        else:
            # Place in DEFAULT_SCREENSHOT_DIR
            target_path = os.path.join(DEFAULT_SCREENSHOT_DIR, target_path)

    # If target is an existing directory, generate default filename inside it
    if os.path.isdir(target_path):
        target_path = os.path.join(target_path, "screenshot.png")

    parent_dir = os.path.dirname(target_path)
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)

    # Overwrite protection: if file exists and allow_overwrite is False, increment filename
    if os.path.exists(target_path) and not allow_overwrite:
        base, ext = os.path.splitext(target_path)
        counter = 1
        while os.path.exists(f"{base}_{counter}{ext}"):
            counter += 1
        target_path = f"{base}_{counter}{ext}"

    return os.path.abspath(target_path)

def capture_screenshot(url, output_target="screenshot.png", window_size="1440,900", virtual_time=2500, overwrite=False):
    # Ensure URL is fully qualified
    if not url.startswith("http://") and not url.startswith("https://"):
        base = detect_base_url()
        url = f"{base}/{url.lstrip('/')}"

    resolved_path = resolve_output_path(output_target, allow_overwrite=overwrite)

    # Chrome screenshot arguments
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={window_size}",
        f"--screenshot={resolved_path}",
        f"--virtual-time-budget={virtual_time}",
        url
    ]

    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        exists = os.path.exists(resolved_path)
        size = os.path.getsize(resolved_path) if exists else 0

        # Safety verification: ensure screenshot was NOT created in project root
        root_dir = os.path.abspath(PROJECT_ROOT)
        resolved_dir = os.path.dirname(resolved_path)
        if resolved_dir == root_dir:
            print(f"[ERROR] Screenshot was directed to project root: {resolved_path}")
            return False, resolved_path, 0

        if exists and size > 0:
            print(f"[PASS] Screenshot saved: {resolved_path} ({size} bytes)")
            return True, resolved_path, size
        else:
            print(f"[FAIL] Screenshot capture failed or resulted in 0 bytes for: {url}")
            return False, resolved_path, 0
    except subprocess.TimeoutExpired:
        print(f"[FAIL] Screenshot timed out for: {url}")
        return False, resolved_path, 0

def main():
    args = sys.argv[1:]
    allow_overwrite = "--overwrite" in args
    clean_args = [a for a in args if a != "--overwrite"]

    url = clean_args[0] if len(clean_args) > 0 else "about.html"
    filename = clean_args[1] if len(clean_args) > 1 else "preview_about.png"
    size = clean_args[2] if len(clean_args) > 2 else "1440,900"

    success, path, byte_size = capture_screenshot(
        url,
        output_target=filename,
        window_size=size,
        overwrite=allow_overwrite
    )

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
