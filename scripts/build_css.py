import os
import hashlib
import sys

MODULE_FILES = [
    "css/01-tokens.css",
    "css/02-base-reset.css",
    "css/03-preloader.css",
    "css/04-header-nav.css",
    "css/05-buttons-layout.css",
    "css/06-hero-orbit.css",
    "css/07-sections.css",
    "css/08-responsive-blog.css",
    "css/09-3d-redesign.css",
    "css/10-motion-restored-hero.css"
]

TARGET_FILE = "style.css"

def compute_sha256(data_bytes):
    return hashlib.sha256(data_bytes).hexdigest()

def compile_modules_in_memory():
    """Reads all 10 modules in binary mode and concatenates them in memory."""
    for m in MODULE_FILES:
        if not os.path.exists(m):
            print(f"[FATAL ERROR] Required CSS module file missing: {m}")
            sys.exit(1)

    in_memory_chunks = []
    for m in MODULE_FILES:
        with open(m, "rb") as fl:
            chunk = fl.read()
            in_memory_chunks.append(chunk)

    compiled_bytes = b"".join(in_memory_chunks)
    return compiled_bytes

def verify_mode():
    """Strictly read-only verification comparing in-memory modules against root style.css."""
    print("=" * 80)
    print("ZS STUDIO — CSS BUILD VERIFICATION (--verify, STRICTLY READ-ONLY)")
    print("=" * 80)

    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] Target file does not exist on disk: {TARGET_FILE}")
        sys.exit(1)

    compiled_bytes = compile_modules_in_memory()
    compiled_hash = compute_sha256(compiled_bytes)

    with open(TARGET_FILE, "rb") as fl:
        target_bytes = fl.read()
    target_hash = compute_sha256(target_bytes)

    print(f"Compiled Memory Size : {len(compiled_bytes):>8} bytes | SHA-256: {compiled_hash}")
    print(f"On-Disk Target Size  : {len(target_bytes):>8} bytes | SHA-256: {target_hash}")

    byte_match = (compiled_bytes == target_bytes)
    hash_match = (compiled_hash == target_hash)

    print("-" * 80)
    print(f"Exact Byte-for-Byte Match : {byte_match}")
    print(f"SHA-256 Hash Match        : {hash_match}")

    if byte_match and hash_match:
        print("[PASS] SUCCESS: In-memory CSS modules match root style.css 100%. (0 disk writes)")
        print("=" * 80)
        sys.exit(0)
    else:
        print("[FAIL] MISMATCH: Compiled CSS differs from root style.css!")
        print("=" * 80)
        sys.exit(1)

def build_mode():
    """Builds style.css from modules using atomic write replacement."""
    print("=" * 80)
    print("ZS STUDIO — ATOMIC CSS COMPILER")
    print("=" * 80)

    compiled_bytes = compile_modules_in_memory()
    compiled_hash = compute_sha256(compiled_bytes)

    # Check if target already exists and matches exactly
    if os.path.exists(TARGET_FILE):
        with open(TARGET_FILE, "rb") as fl:
            existing_bytes = fl.read()
        existing_hash = compute_sha256(existing_bytes)

        if compiled_bytes == existing_bytes and compiled_hash == existing_hash:
            print(f"[INFO] '{TARGET_FILE}' is already byte-identical and up to date.")
            print(f"  Size   : {len(compiled_bytes)} bytes")
            print(f"  SHA-256: {compiled_hash}")
            print("=" * 80)
            sys.exit(0)

    # Atomic write replacement
    temp_target = TARGET_FILE + ".tmp"
    with open(temp_target, "wb") as f_out:
        f_out.write(compiled_bytes)
        f_out.flush()
        os.fsync(f_out.fileno())

    os.replace(temp_target, TARGET_FILE)
    print(f"[SUCCESS] Atomically updated '{TARGET_FILE}'.")
    print(f"  Size   : {len(compiled_bytes)} bytes")
    print(f"  SHA-256: {compiled_hash}")
    print("=" * 80)
    sys.exit(0)

def main():
    if "--verify" in sys.argv:
        verify_mode()
    else:
        build_mode()

if __name__ == "__main__":
    main()

