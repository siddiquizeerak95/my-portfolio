---
phase: 3
wave: 1
requirements:
  - REQ-SEC-01
must_haves:
  phase_3_truths:
    - "The entire root keys/ directory is excluded in .gitignore while assets/keys/zeerak_public.asc remains actively tracked in Git"
    - "Public key tracking is verified using git ls-files --error-unmatch and git check-ignore, not git status alone"
    - "No private key contents, encryption keys, personal transmissions from inbox/, or sensitive environment values are printed or committed"
    - "Safe decryption testing uses isolated synthetic test keypairs and synthetic messages generated in scratch/test_e2ee/"
    - "decrypt_message.js --help prints usage instructions and exits 0 cleanly without launching interactive stdin mode"
    - "decrypt_message.js supports --key / -k flags (including paths with spaces), PRIVATE_KEY_PATH environment variable, and default fallback path"
    - "decrypt_message.js preserves existing file-input argument and interactive stdin paste modes"
    - "verify_console_errors.py explicit console-error detection is proven with a deliberate failing test page before auditing production pages"
    - "verify_console_errors.py auto-detects active server port, uses --dump-dom, and confirms Three.js pages terminate within expected time"
    - "take_screenshot.py directs screenshots to scratch/screenshots/ by default, handles directory/file targets, protects existing files from unexpected overwrites, and produces zero screenshots in root"
    - "scripts/build_css.py provides a strictly read-only --verify mode and atomic byte-preserving build replacement"
    - "package.json registers build:css and verify:css scripts"
    - "All website visuals, HTML, CSS module contents, Three.js 3D cosmos, and animations remain 100% untouched"
  phase_3_artifacts:
    - path: ".gitignore"
      description: "Hardened gitignore excluding the root keys/ directory and private key patterns while preserving public keys"
    - path: "decrypt_message.js"
      description: "Enhanced offline decryption utility supporting --help, --key/-k, PRIVATE_KEY_PATH, spaces in paths, and stdin/file input"
    - path: "verify_console_errors.py"
      description: "Upgraded headless Chrome console audit runner with auto port detection, --dump-dom, and verified error detection"
    - path: "take_screenshot.py"
      description: "Standardized screenshot capture utility targeting scratch/screenshots/ with overwrite safety"
    - path: "scripts/build_css.py"
      description: "Tracked CSS build and verification script with atomic write and strictly read-only --verify flag"
    - path: "package.json"
      description: "Package manifest updated with build:css and verify:css scripts"
  phase_3_wiring:
    - "scripts/build_css.py concatenates css/01 through 10 into style.css with atomic file swap"
    - "verify_console_errors.py queries localhost on active port (8080 or 5500) across all 14 HTML pages"
    - "package.json executes scripts/build_css.py via npm run build:css and npm run verify:css"
---

<tasks>
  <task type="execute">
    <name>Pre-execution checkpoint and two-way key tracking audit</name>
    <files>keys/*, assets/keys/*, .git/*</files>
    <action>
      1. Audit already-tracked files inside root 'keys/' via 'git ls-files keys/'. Confirm zero files inside keys/ are tracked in Git index.
      2. Verify public key tracking using explicit two-way Git commands:
         - 'git ls-files --error-unmatch assets/keys/zeerak_public.asc' (must exit 0, confirming tracked status in index)
         - 'git check-ignore assets/keys/zeerak_public.asc' (must exit non-zero / return empty, confirming it is NOT ignored)
         Do not rely on git status alone.
      3. Create Git backup branch 'backup/pre-phase3-tooling' to provide an immediate rollback point before any files are modified.
      4. Ensure no private key contents or credentials are exposed in command logs.
    </action>
    <verify>
      <shell>git branch --list backup/pre-phase3-tooling && git ls-files --error-unmatch assets/keys/zeerak_public.asc</shell>
    </verify>
    <done>Backup branch created, keys/ confirmed untracked, and public key verified actively tracked and unignored.</done>
  </task>

  <task type="execute">
    <name>Harden .gitignore for cryptographic assets and verify public key preservation</name>
    <files>.gitignore</files>
    <action>
      1. Update .gitignore to exclude the entire root 'keys/' folder and generic private key extensions (*.key, *.pem, *.private.asc, *.sec.asc).
      2. Test ignore behavior: create temporary 'keys/test_fake.asc', run 'git check-ignore keys/test_fake.asc', and confirm it matches. Remove 'keys/test_fake.asc'.
      3. Re-verify that the public key remains completely untouched and tracked:
         - 'git ls-files --error-unmatch assets/keys/zeerak_public.asc'
         - 'git check-ignore assets/keys/zeerak_public.asc' (must not be ignored)
    </action>
    <verify>
      <shell>git check-ignore -v keys/zeerak_private_KEY_KEEP_SAFE.asc && git ls-files --error-unmatch assets/keys/zeerak_public.asc</shell>
    </verify>
    <done>.gitignore hardened and verified; all keys/ contents protected from Git staging; public key confirmed tracked.</done>
  </task>

  <task type="execute">
    <name>Upgrade decrypt_message.js with flexible key resolution, --help, and safe argument parsing</name>
    <files>decrypt_message.js</files>
    <action>
      1. Add dotenv support via 'dotenv.config()' to allow loading PRIVATE_KEY_PATH from .env.
      2. Implement '--help' / '-h' handling: if requested, display usage instructions and immediately exit 0 without opening keys or blocking on stdin.
      3. Implement key resolution order:
         - CLI flag: '--key <path>' or '-k <path>' (supports quotes and paths containing whitespace).
         - Environment variable: process.env.PRIVATE_KEY_PATH.
         - Default fallback: 'keys/zeerak_private_KEY_KEEP_SAFE.asc'.
      4. Decouple argument parsing so '--key <path>' can appear in any position relative to an input message file.
      5. Preserve interactive stdin paste mode when no message file argument is supplied.
      6. Output safe diagnostic guidance if the key is missing without exposing key contents, secret names, or environment variables.
    </action>
    <verify>
      <shell>node decrypt_message.js --help</shell>
    </verify>
    <done>Decryption CLI supports clean --help exit, 3-tier key resolution, whitespace-safe paths, and stdin/file input.</done>
  </task>

  <task type="execute">
    <name>Upgrade verify_console_errors.py with port auto-detection, --dump-dom, and error detection verification</name>
    <files>verify_console_errors.py</files>
    <action>
      1. Implement dynamic port detection: probe port 8080 (server.js default), then 5500 (Live Server), and accept '--port' / '--url' CLI flags.
      2. Preserve and standardize explicit console error detection via Chrome's '--enable-logging=stderr --v=1', parsing stderr for 'ERROR:CONSOLE'.
      3. Add '--dump-dom' to Chrome arguments to ensure Chrome exits deterministically without hanging on Three.js continuous animation loops.
      4. Create a temporary test fixture 'scratch/test_deliberate_error.html' containing a script that calls 'console.error("Deliberate test error")'.
      5. Run 'verify_console_errors.py' against 'scratch/test_deliberate_error.html' and verify that it detects the console error and returns a non-zero exit code (1). Remove the test fixture.
      6. Audit all 14 production HTML pages, verifying exit code 0 and recording execution time for 'index.html' to confirm loop termination under 3 seconds.
    </action>
    <verify>
      <shell>python verify_console_errors.py</shell>
    </verify>
    <done>Audit script auto-detects ports, exits cleanly on WebGL pages, verifies error detection via negative test, and audits 14 pages.</done>
  </task>

  <task type="execute">
    <name>Standardize take_screenshot.py to target scratch/screenshots/ with overwrite safety</name>
    <files>take_screenshot.py</files>
    <action>
      1. Change default screenshot output destination from project root to 'scratch/screenshots/'.
      2. Auto-create destination directories if they do not exist.
      3. Support both explicit file paths (e.g. 'scratch/screenshots/custom.png') and directory targets.
      4. Implement overwrite protection: if target file already exists, generate a safe sequential filename (e.g. 'custom_1.png') unless '--overwrite' flag is passed.
      5. Use 'os.path.abspath()' for reliable Windows Chrome headless file generation.
      6. Add dynamic port detection (8080 / 5500) or '--port' argument.
      7. Verify that no screenshot is created in the repository root.
    </action>
    <verify>
      <shell>python -c "import take_screenshot; print(take_screenshot.__file__)"</shell>
    </verify>
    <done>Screenshot script outputs cleanly to scratch/screenshots/ with overwrite protection and zero root clutter.</done>
  </task>

  <task type="execute">
    <name>Create tracked scripts/build_css.py and update package.json</name>
    <files>scripts/build_css.py, package.json</files>
    <action>
      1. Create directory 'scripts/' and file 'scripts/build_css.py'.
      2. Implement in-memory concatenation of all 10 modules ('css/01-tokens.css' through 'css/10-motion-restored-hero.css') in binary mode ('rb') to preserve exact line endings (CRLF/LF).
      3. Implement '--verify' mode: strictly read-only, compares compiled bytes against 'style.css', prints hash status, and exits 0 (match) or 1 (diff) with zero disk writes.
      4. Implement build mode: compares compiled bytes against 'style.css'. If diff exists, writes to 'style.css.tmp', flushes, and atomically replaces 'style.css' via 'os.replace'.
      5. Update 'package.json' scripts to add:
         - "build:css": "python scripts/build_css.py"
         - "verify:css": "python scripts/build_css.py --verify"
    </action>
    <verify>
      <shell>npm run verify:css</shell>
    </verify>
    <done>Tracked build and strictly read-only verify pipeline installed and confirmed byte-for-byte identical.</done>
  </task>

  <task type="execute">
    <name>Execute complete Phase 3 verification suite with safe synthetic fixtures</name>
    <files>scripts/build_css.py, decrypt_message.js, verify_console_errors.py, take_screenshot.py</files>
    <action>
      1. Decryption Safety Verification:
         - Generate a temporary synthetic OpenPGP keypair and synthetic test message inside 'scratch/test_e2ee/'. (Do not touch actual personal files in 'inbox/').
         - Create a test key path containing spaces: 'scratch/test_e2ee/test path with spaces/test_private.asc'.
         - Test CLI '--help' exits 0 immediately without waiting on stdin.
         - Test '--key' flag with path containing spaces decrypts the synthetic message.
         - Test 'PRIVATE_KEY_PATH' environment variable decrypts the synthetic message.
         - Test interactive stdin mode by piping the synthetic message into 'decrypt_message.js' with '--key'.
         - Confirm zero private key bytes or environment secrets are printed. Clean up synthetic test keys.
      2. Console Audit Verification:
         - Confirm deliberate error page detection exited with code 1.
         - Run 'python verify_console_errors.py' across all 14 pages and confirm 14/14 pass with 0 errors (exit code 0).
         - Confirm 'index.html' execution duration is under 3 seconds.
      3. Screenshot Storage Verification:
         - Capture a test screenshot of 'about.html' using 'python take_screenshot.py'.
         - Confirm file exists inside 'scratch/screenshots/', size > 10,000 bytes, and is a valid PNG.
         - Capture second screenshot to confirm overwrite protection preserves the first capture.
         - Confirm repository root contains zero new screenshot files.
      4. CSS Pipeline Verification:
         - Execute 'npm run verify:css' and confirm 100% byte-for-byte and SHA-256 match in strictly read-only mode.
    </action>
    <verify>
      <shell>npm run verify:css && python verify_console_errors.py</shell>
    </verify>
    <done>All security tests, synthetic decryption tests, 14-page console audits, and screenshot safety tests pass with 100% compliance.</done>
  </task>
</tasks>
