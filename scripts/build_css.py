import os
import hashlib
import sys
import re

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

STANDALONE_FILES = [
    "sculpture-intro.css",
    "blog-3d.css"
]

def compute_sha256(data_bytes):
    return hashlib.sha256(data_bytes).hexdigest()

def minify_css(css_text: str) -> str:
    """
    Lossless, deterministic CSS minifier.
    Preserves string literals, calc() operator spacing, @media queries, and CSS custom properties.
    """
    output = []
    i = 0
    n = len(css_text)

    in_string = None  # '"' or "'"
    in_comment = False
    current_token = []

    # Pass 1: Strip comments while strictly preserving string literals
    while i < n:
        char = css_text[i]
        next_char = css_text[i+1] if i + 1 < n else ''

        # Comments
        if not in_string and not in_comment and char == '/' and next_char == '*':
            in_comment = True
            i += 2
            continue

        if in_comment:
            if char == '*' and next_char == '/':
                in_comment = False
                i += 2
            else:
                i += 1
            continue

        # Strings
        if not in_string and (char == '"' or char == "'"):
            in_string = char
            current_token.append(char)
            i += 1
            continue

        if in_string:
            current_token.append(char)
            if char == '\\':
                if i + 1 < n:
                    i += 1
                    current_token.append(css_text[i])
            elif char == in_string:
                in_string = None
            i += 1
            continue

        current_token.append(char)
        i += 1

    cleaned = "".join(current_token)

    # Pass 2: Token-aware whitespace normalization protecting strings
    string_pattern = re.compile(r'("(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')')
    parts = string_pattern.split(cleaned)

    minified_parts = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            # String literal: preserve byte-exact
            minified_parts.append(part)
        else:
            p = part
            # Collapse whitespace sequences
            p = re.sub(r'\s+', ' ', p)

            # Remove spaces around structural delimiters
            p = re.sub(r'\s*\{\s*', '{', p)
            p = re.sub(r'\s*\}\s*', '}', p)
            p = re.sub(r'\s*;\s*', ';', p)
            p = re.sub(r'\s*,\s*', ',', p)

            # Remove trailing semicolons before closing brace
            p = re.sub(r';\}', '}', p)

            # Remove whitespace around colons in declarations
            p = re.sub(r'\s*:\s*', ':', p)

            # Restore required space after @media, @keyframes, @supports, @import
            p = re.sub(r'(@media|@keyframes|@supports|@import)\(', r'\1 (', p)
            p = re.sub(r'(@media|@keyframes|@supports|@import):', r'\1 :', p)

            # Ensure "and (" in media queries has space
            p = re.sub(r'\band\(', 'and (', p)

            # Preserve calc() + and - operators required by CSS spec
            def fix_calc_spaces(match):
                inner = match.group(0)
                inner = re.sub(r'(\d|\%|[a-z])\+([0-9a-z\.])', r'\1 + \2', inner)
                inner = re.sub(r'(\d|\%|[a-z])\-([0-9a-z\.])', r'\1 - \2', inner)
                return inner

            p = re.sub(r'calc\([^)]+\)', fix_calc_spaces, p)

            # Remove empty rulesets
            p = re.sub(r'[^{};]+?\{\}', '', p)

            minified_parts.append(p.strip())

    res = "".join(minified_parts)
    res = re.sub(r';+', ';', res)
    res = re.sub(r';\}', '}', res)
    return res.strip()

def compile_modules_in_memory():
    """Reads all 10 modules in UTF-8 text mode, minifies them losslessly, and returns compiled UTF-8 bytes."""
    for m in MODULE_FILES:
        if not os.path.exists(m):
            print(f"[FATAL ERROR] Required CSS module file missing: {m}")
            sys.exit(1)

    raw_chunks = []
    for m in MODULE_FILES:
        with open(m, "r", encoding="utf-8") as fl:
            raw_chunks.append(fl.read())

    full_css = "\n".join(raw_chunks)
    minified_css = minify_css(full_css)
    return minified_css.encode("utf-8")

def verify_mode():
    """Strictly read-only verification comparing in-memory compiled modules against root style.css."""
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
