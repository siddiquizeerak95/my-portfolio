# Phase 3 Context: Security Boundary Hardening & Developer Tooling Polish

Authoritative implementation decisions, security boundaries, developer tooling specifications, and verification safeguards locked for Phase 3.

---

## 1. Core Principles & Non-Negotiable Invariants

1. **Zero Production Visual or Functional Regressions:**
   - Website design, layouts, typography, animations, Three.js 3D cosmos stage, and HTML files remain 100% unchanged.
   - CSS module contents in `css/` remain completely untouched.
   - `sculpture-intro.css`, `sculpture-intro.js`, `blog-3d.css`, and `blog-3d.js` remain completely untouched.
2. **Confidentiality & Cryptographic Hygiene:**
   - Private key contents (`keys/zeerak_private_KEY_KEEP_SAFE.asc`), `.env` variables, and SMTP secrets must **never** be logged, printed to console, or staged in Git.
   - Real personal transmissions in `inbox/` are never used as test fixtures. Decryption testing uses isolated synthetic test keypairs and synthetic ciphertexts generated in `scratch/test_e2ee/`.
   - The public key distributed to website visitors remains tracked and accessible at `assets/keys/zeerak_public.asc` (and embedded in `contact-e2ee.js`).
   - The root `keys/` directory is reserved solely for private offline keys and is completely excluded from version control.
3. **Deterministic Tooling & Verification Integrity:**
   - Console error detection must be explicitly tested with a deliberately failing test page to verify that real errors are caught and return non-zero exit codes.
   - Decryption CLI `--help` must exit cleanly with code 0 without blocking on stdin.
   - Screenshot generation must target `scratch/screenshots/` without polluting root, and guard existing files against unexpected overwrites.
4. **No Unapproved Execution:**
   - All implementation steps are strictly gated by explicit user review and approval of `03-PLAN.md`.
   - Backup checkpoints and recovery rollback mechanisms must be established before modifying any project files.

---

## 2. Technical Decisions & Architectural Specifications

### Decision 1: `.gitignore` Hardening & Two-Way Public Key Verification
- **Pre-Modification Audit:** Run `git ls-files keys/` to confirm zero files inside `keys/` are currently tracked in Git index.
- **Explicit Public Key Tracking Verification:**
  - `git ls-files --error-unmatch assets/keys/zeerak_public.asc` (must exit 0, confirming it is actively tracked).
  - `git check-ignore assets/keys/zeerak_public.asc` (must exit non-zero / return empty, confirming it is NOT ignored).
  - Do not rely on `git status` alone.
- **Rule Hardening:** Replace selective glob rules (`keys/*private*`, `keys/*secret*`) with a blanket exclusion for the entire directory:
  ```gitignore
  # Private Encryption Keys (Keep strictly private — held offline)
  keys/
  *.private.asc
  *.sec.asc
  *.key
  *.pem
  ```

### Decision 2: Decryption CLI Ergonomics & Safe Synthetic Testing (`decrypt_message.js`)
- **Key Resolution Hierarchy:**
  1. CLI argument: `--key <path>` or `-k <path>` (supports quotes and paths containing whitespace).
  2. Environment variable: `process.env.PRIVATE_KEY_PATH` (loaded with `dotenv.config()`).
  3. Default fallback: `'keys/zeerak_private_KEY_KEEP_SAFE.asc'`.
- **Command-Line Interface:**
  - `--help` / `-h` flag: Prints clean usage instructions and exits immediately with code 0 without launching interactive stdin mode.
  - File input mode: `node decrypt_message.js <message_path>`
  - Flag-and-file combinations in any order: `node decrypt_message.js -k <key_path> <message_path>` or `node decrypt_message.js <message_path> --key <key_path>`
  - Interactive paste mode: `node decrypt_message.js` (or `node decrypt_message.js -k <key_path>`) launches interactive readline stdin paste mode.
- **Safe Diagnostics & Testing:**
  - If a key file is missing, outputs helpful troubleshooting guidance to stderr without logging private key data or environment secrets.
  - Testing uses a synthetic test keypair and dummy message generated in `scratch/test_e2ee/`. Personal transmissions in `inbox/` are never touched.

### Decision 3: Headless Chrome Console Verification & Positive/Negative Error Detection (`verify_console_errors.py`)
- **Dynamic Port Detection:**
  - Auto-probes active ports in order: `http://127.0.0.1:8080` (Node server.js default), then `http://127.0.0.1:5500` (VS Code Live Server).
  - Supports `--port <int>` and `--url <base-url>` command-line flags.
- **Explicit Console Error Detection & Chrome Loop Termination:**
  - Uses `--enable-logging=stderr --v=1` and `--dump-dom` to capture all `ERROR:CONSOLE` log lines.
  - Deliberate Failure Verification: Tested against a temporary page `scratch/test_console_error.html` with intentional script errors to prove that `verify_console_errors.py` detects errors and exits with a non-zero exit code (`1`).
  - Loop Termination Verification: Measures execution timing on `index.html` to confirm that Three.js `requestAnimationFrame` loops do not hang Chrome and that each page exits deterministically in under 3 seconds.
- **Full Coverage:** Audits all 14 production HTML pages and returns exit code 0 on complete pass.

### Decision 4: Screenshot Utility Standardization & Overwrite Protection (`take_screenshot.py`)
- **Default Storage Location:** Output defaults to `scratch/screenshots/` instead of polluting the project root.
- **Safe Path Resolution:** Supports both directory targets (`scratch/screenshots/`) and explicit file targets (`scratch/screenshots/custom_name.png`), ensuring parent directories are created automatically.
- **Overwrite Protection:** Checks if target screenshot already exists; if so, appends a numeric counter (or respects an explicit `--overwrite` flag) to prevent accidental loss of previous captures.
- **Root Cleanliness Check:** Verifies that no `.png` files are created in the repository root directory.
- **Absolute Paths for Windows:** Converts target paths via `os.path.abspath()` so Chrome headless writes screenshots reliably without silent failures.

### Decision 5: Production Tracked CSS Build Pipeline (`scripts/build_css.py`)
- **Tracked Location:** Placed in `scripts/build_css.py` so fresh repository checkouts possess the build tooling.
- **Read-Only `--verify` Mode:**
  - Concatenates the 10 modules (`css/01-tokens.css` through `css/10-motion-restored-hero.css`) in memory.
  - Performs a byte-level comparison against root `style.css`.
  - Exits with `0` if identical or `1` if mismatched, without performing any disk writes or touching files.
- **Atomic Build Mode:**
  - Reads all 10 modules in binary mode (`read_bytes()`) to preserve exact original line endings (CRLF/LF).
  - Compares compiled bytes against `style.css`; if identical, reports up-to-date.
  - If different, writes to `style.css.tmp`, flushes and syncs to disk, then performs an atomic `os.replace` to `style.css`.
- **Package.json Scripts:**
  - `"build:css": "python scripts/build_css.py"`
  - `"verify:css": "python scripts/build_css.py --verify"`

---

## 3. Verification & Safety Matrix

| Test Case | Method | Expected Outcome |
| :--- | :--- | :--- |
| **Git Key Exclusion** | Create temporary `keys/test_fake.asc` and run `git check-ignore keys/test_fake.asc` | Rule matches; file is completely ignored by Git |
| **Public Key Tracking** | `git ls-files --error-unmatch assets/keys/zeerak_public.asc` & `git check-ignore assets/keys/zeerak_public.asc` | Exit 0 on ls-files (tracked); Exit 1 on check-ignore (NOT ignored) |
| **CLI Decryption Help** | `node decrypt_message.js --help` | Prints usage and exits 0 cleanly without blocking on stdin |
| **Synthetic Decryption (`--key`)** | `node decrypt_message.js -k "scratch/test_e2ee/path with spaces/test_private.asc" scratch/test_e2ee/synthetic.txt` | Successfully decrypts synthetic payload; zero secrets leaked |
| **Synthetic Decryption (Env Var)** | Run with `PRIVATE_KEY_PATH` set to synthetic test key | Successfully decrypts synthetic payload via environment variable |
| **Console Error Detection Test** | Run `verify_console_errors.py` against deliberate error page | Detects `ERROR:CONSOLE` and exits with non-zero exit code (1) |
| **14-Page Console Audit** | `python verify_console_errors.py` on active port | 14/14 production pages pass with 0 errors in < 30 seconds total |
| **Screenshot Output Safety** | Run `python take_screenshot.py` | Saved in `scratch/screenshots/`, valid PNG (>10KB), existing files safe, root clean |
| **CSS Build Equality** | `npm run verify:css` | 100% byte-for-byte and SHA-256 match confirmed without file modification |
