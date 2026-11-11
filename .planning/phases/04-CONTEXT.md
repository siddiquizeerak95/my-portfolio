# Phase 4 Context: Full Multi-Page Verification & Sign-Off

Authoritative verification specifications, security constraints, multi-device visual matrix, responsive audit protocols, and milestone sign-off criteria locked for Phase 4.

---

## 1. Core Principles & Non-Negotiable Invariants

1. **Zero Code or Visual Modifications:**
   - Production HTML files, CSS modules (`css/01` through `10`), root `style.css`, JavaScript engines, Three.js 3D cosmos stage, and animations remain 100% untouched.
   - If visual discrepancies or overflow conditions are identified, they must be recorded and reported with exact measurements without automatically changing website code.
2. **Explicit Active Server Verification & Cryptographic Isolation (`REQ-VER-03`):**
   - Active Node Process Audit: Identify the process listening on port 8080, confirm its PID, and verify its actual runtime environment contains `TEST_MODE=true`.
   - Strict Loopback Binding: Confirm the server listening address is exactly `127.0.0.1`, not `0.0.0.0`, `::`, or an external interface. If currently bound to a wildcard, enforce `127.0.0.1` loopback binding.
   - Code-Path Immunity: Inspect `/api/contact` in `server.js` to conclusively verify that the `TEST_MODE` branch writes locally to `inbox/` and returns before any SMTP, Gmail, Resend API, or external webhook dispatch can occur.
   - Conclusive Verification Gate: If any pre-flight check cannot be conclusively verified, abort immediately before sending any payload.
   - API Assertion: Confirm the API response explicitly reports `method: "test_mode"`.
   - Key Immutability: Use existing authoritative keys (`assets/keys/zeerak_public.asc` and `keys/zeerak_private_KEY_KEEP_SAFE.asc`) in-place without copying, exposing, or modifying them.
   - Confidentiality: Private key bytes and `.env` credentials must never be printed to stdout/stderr.
   - Guaranteed Surgical Cleanup:
     - Take a snapshot of `inbox/` before transmission.
     - Identify newly created `transmission_*.txt` files by comparing the directory against the snapshot.
     - Conclusive Ciphertext Verification: Verify the new file corresponds to this test using a ciphertext-based check, confirming that the stored encrypted payload matches the exact armored PGP ciphertext sent.
     - Timeout Recovery: If the HTTP request times out, repeat directory comparison and ciphertext verification.
     - Single-File Path Resolution: Assign the full absolute path only when exactly one file can be conclusively identified as belonging to this test.
     - Ambiguity Protection: If identification is ambiguous (0 or >1 matches), do NOT delete anything and report the cleanup limitation.
     - Use `try/finally` in `scratch/test_e2ee_pipeline.js` so cleanup is guaranteed to run even if decryption or plaintext comparison throws an error.
     - Delete ONLY the verified exact file using its full path. Never delete files using wildcard patterns or timestamps alone.
     - Preserve all historical inbox files.
     - Report cleanup errors separately without masking the underlying test failure.
3. **Comprehensive Visual & Responsive Verification (`REQ-VER-02`):**
   - Exact 36 visual combinations: 6 pages × 3 viewports × 2 themes.
   - Stored in a run-specific directory inside `scratch/screenshots/phase4_verification/run_<timestamp>/` with a manifest tracking all captures.
   - Collision-safe filenames; existing previous captures are never overwritten.
   - Validated via dedicated script: asserts all 36 files exist, each has a valid PNG binary signature (`\x89PNG\r\n\x1a\n`), and each exceeds 10 KB (`> 10240` bytes).
   - Zero `.png` captures created in the repository root directory.
4. **Mathematical Mobile Overflow Audit:**
   - All 14 HTML pages evaluated at `390px` mobile viewport width.
   - `scrollWidth` and `clientWidth` must be recorded and logged for every page.
   - Any overflow must be reported with exact pixel values without auto-fixing.
5. **Final Milestone Sign-Off:**
   - Requirements marked `COMPLETED & VERIFIED` only when all acceptance tests pass genuinely.
   - Verify that all four local backup branches exist (`backup/pre-phase1-checkpoint`, `backup/pre-phase2-css`, `backup/pre-phase3-tooling`, `backup/pre-phase4-verification`).
   - Confirm that NO backup branch was pushed to GitHub remote (`git branch -r`).
   - All recovery manifests and historical files preserved.

---

## 2. Technical Specifications & Methodology

### Gate 1: 14-Page Headless Chrome Console Audit (`REQ-VER-01`)
- **Runner:** `python verify_console_errors.py`
- **Target:** All 14 production HTML pages on `http://127.0.0.1:8080`:
  1. `index.html`
  2. `about.html`
  3. `projects.html`
  4. `skills.html`
  5. `blog.html`
  6. `contact.html`
  7. `blog-how-i-built-my-portfolio.html`
  8. `blog-my-journey-as-a-developer.html`
  9. `blog-why-i-prefer-minimalist-web-design.html`
  10. `case-study.html`
  11. `case-study-ecommerce.html`
  12. `case-study-finance.html`
  13. `case-study-banking.html`
  14. `case-study-portfolio.html`
- **Acceptance Criteria:**
  - 14 / 14 pages report `0 console errors`.
  - `index.html` terminates in under 3.0s without hanging.
  - Process exits with code `0`.

---

### Gate 2: 36-Combination Visual & Theme Verification Matrix (`REQ-VER-02`)
- **Matrix Dimensions:**
  - **6 Representative Pages:** `index.html`, `about.html`, `projects.html`, `skills.html`, `contact.html`, `blog.html`
  - **3 Viewport Breakpoints:**
    - Desktop: `1440 × 900`
    - Tablet: `768 × 1024`
    - Mobile: `390 × 844`
  - **2 Themes:**
    - Dark Mode: default theme
    - Light Mode: `[data-theme="light"]`
- **Output Storage & Verification:**
  - Stored inside `scratch/screenshots/phase4_verification/run_<timestamp>/` with `manifest.json`.
  - Validated by `scratch/verify_screenshots.py`:
    - All 36 expected combinations exist.
    - Every file starts with the 8-byte PNG signature `\x89PNG\r\n\x1a\n`.
    - Every file size exceeds 10,240 bytes.
    - Zero `.png` files in the repository root.

---

### Gate 3: Mathematical Mobile Horizontal Overflow Audit
- **Measurement Method:** Headless Chrome evaluates each page at `390px` width:
  ```javascript
  const scrollWidth = document.documentElement.scrollWidth;
  const clientWidth = document.documentElement.clientWidth;
  const overflow = scrollWidth - clientWidth;
  return { scrollWidth, clientWidth, overflow, hasOverflow: overflow > 0 };
  ```
- **Coverage:** All 14 HTML pages.
- **Acceptance Criteria:**
  - Complete measurement log recorded for all 14 pages.
  - Every page confirms `scrollWidth <= clientWidth` (zero horizontal overflow).

---

### Gate 4: Real E2EE Contact Encryption, Offline Decryption & Guaranteed Cleanup (`REQ-VER-03`)
- **Safety Pre-Flight:**
  1. Identify Node process listening on port 8080 (via `Get-NetTCPConnection`).
  2. Verify listening address is strictly `127.0.0.1` (loopback only).
  3. Verify process environment has `TEST_MODE=true`.
  4. Verify `/api/contact` code path in `server.js` returns locally before any external SMTP/Resend/webhook dispatch.
  5. Abort immediately if any check cannot be conclusively confirmed.
- **Pipeline Execution (`scratch/test_e2ee_pipeline.js`):**
  1. Pre-transmission snapshot: read all existing files in `inbox/`.
  2. Synthetic test payload:
     - Name: `Phase 4 Verification Agent`
     - Email: `verify-agent@zs-studio.local`
     - Subject: `Phase 4 E2EE Full Pipeline Validation`
     - Message: `VERIFICATION PAYLOAD: Client-side OpenPGP encryption and offline decryption verified successfully!`
  3. Encrypt payload client-side with `assets/keys/zeerak_public.asc` (via OpenPGP) into `armoredCiphertext`.
  4. POST encrypted payload `{ name, email, subject, encrypted_message: armoredCiphertext }` to `http://127.0.0.1:8080/api/contact`.
  5. Assert response status is 200 and body is `{ success: true, method: 'test_mode' }`.
  6. Conclusive File Identification:
     - Diff `inbox/` against pre-transmission snapshot.
     - Conclusively verify that candidate file contains the exact `armoredCiphertext` sent.
     - If the HTTP request times out, repeat directory comparison and ciphertext check.
     - Assign full path to `createdTransmissionFile` ONLY if exactly one file matches.
     - If identification is ambiguous, do not delete anything; report the cleanup limitation.
  7. Decrypt offline with `keys/zeerak_private_KEY_KEEP_SAFE.asc`.
  8. Assert decrypted plaintext matches original synthetic message byte-for-byte.
  9. `try/finally` Guaranteed Cleanup: Delete ONLY that verified exact file `inbox/transmission_<timestamp>.txt`. Report cleanup failures separately without hiding any assertion failure.
  10. Exits with non-zero code if any step fails.

---

### Gate 5: Production CSS & Storage Metrics Final Sign-Off
- **CSS Verification:** `npm run verify:css` re-run in strictly read-only mode (100% byte & SHA-256 match).
- **Storage Metrics Verification:**
  - `assets/` size confirmed under 17 MB (currently 3.08 MB).
  - Root directory confirmed clean of all loose screenshots and `.bak` files.
- **Git Safety Verification:**
  - Verify all 4 local backup branches exist: `backup/pre-phase1-checkpoint`, `backup/pre-phase2-css`, `backup/pre-phase3-tooling`, `backup/pre-phase4-verification`.
  - Confirm `git branch -r` contains zero backup branches on remote.
- **Milestone Documentation Updates:**
  - `STATE.md`: Update to 100% milestone completion.
  - `REQUIREMENTS.md`: Mark all 9 requirements `COMPLETED & VERIFIED`.
  - `ROADMAP.md`: Mark all 4 phases `COMPLETED & VERIFIED`.
