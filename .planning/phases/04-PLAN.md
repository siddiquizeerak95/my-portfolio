---
phase: 4
wave: 1
requirements:
  - REQ-VER-01
  - REQ-VER-02
  - REQ-VER-03
must_haves:
  phase_4_truths:
    - "Active Node process on port 8080 is verified listening strictly on 127.0.0.1 (not 0.0.0.0 or external interfaces)"
    - "TEST_MODE=true is explicitly verified in the active running server process environment before transmitting any payload"
    - "The /api/contact code path is verified to write locally to inbox/ and return before any SMTP, Gmail, Resend, or external webhook dispatch"
    - "test_e2ee_pipeline.js identifies the exact transmission file by diffing against pre-snapshot and verifying sent ciphertext match"
    - "If request times out, timeout recovery repeats directory snapshot comparison and ciphertext verification"
    - "Full path is assigned only when exactly 1 file is conclusively identified; if ambiguous, nothing is deleted and limitation is reported"
    - "test_e2ee_pipeline.js uses try/finally to guarantee cleanup of the exact test file even if decryption or assertion fails"
    - "Cleanup deletes only the verified exact file via its full path; broad wildcards are prohibited; all historical files are preserved"
    - "Cleanup errors are reported separately without masking the underlying test failure; non-zero exit code on any failure"
    - "No private key contents or environment secrets are printed, exposed, or committed"
    - "All 14 HTML pages report 0 console errors and index.html terminates under 3 seconds"
    - "All 36 visual combinations (6 pages × 3 viewports × 2 themes) captured and validated with PNG signatures and size > 10 KB"
    - "All 14 HTML pages verified for zero mobile horizontal overflow at 390px width (scrollWidth <= clientWidth)"
    - "npm run verify:css passes with 100% byte-for-byte and SHA-256 match in strictly read-only mode"
    - "All four local backup branches exist and zero backup branches are pushed to GitHub remote"
    - "All website visuals, HTML, CSS modules, Three.js 3D cosmos stage, and animations remain 100% untouched"
  phase_4_artifacts:
    - path: "scratch/screenshots/phase4_verification/run_*"
      description: "Run-specific directory containing the 36-image responsive and theme verification matrix"
    - path: "scratch/screenshots/phase4_verification/run_*/manifest.json"
      description: "Manifest tracking all 36 screenshot captures with dimensions and themes"
    - path: "scratch/verify_screenshots.py"
      description: "Validation script verifying all 36 PNG signatures, sizes > 10 KB, and root cleanliness"
    - path: "scratch/audit_mobile_overflow.py"
      description: "Automated script measuring scrollWidth vs clientWidth at 390px across all 14 pages"
    - path: "scratch/test_e2ee_pipeline.js"
      description: "Guaranteed-cleanup E2EE client encryption, local dispatch, offline decryption, and verification script"
    - path: "scratch/verify_milestone_integrity.py"
      description: "Final milestone integrity runner asserting backup branches, remote status, and requirement gates"
    - path: ".planning/STATE.md"
      description: "Milestone state tracking updated to 100% completion"
    - path: ".planning/REQUIREMENTS.md"
      description: "Requirements matrix updated with all 9 requirements verified"
    - path: ".planning/ROADMAP.md"
      description: "Roadmap updated with all 4 phases marked completed and verified"
  phase_4_wiring:
    - "verify_console_errors.py audits all 14 pages on http://127.0.0.1:8080"
    - "test_e2ee_pipeline.js POSTs client-encrypted payload to http://127.0.0.1:8080/api/contact and decrypts resulting transmission"
    - "verify_screenshots.py validates 36 PNGs in scratch/screenshots/phase4_verification/run_*/"
    - "verify_milestone_integrity.py verifies local backup branches and unpushed remote state"
---

<tasks>
  <task type="execute">
    <name>Pre-execution checkpoint, explicit active server verification, and branch creation</name>
    <files>.env, server.js, inbox/*, .git/*</files>
    <action>
      1. Identify the Node process listening on port 8080 via:
         $pid8080 = (Get-NetTCPConnection -LocalPort 8080 -State Listen).OwningProcess | Select-Object -Unique
      2. Verify that the listening address is strictly '127.0.0.1':
         (Get-NetTCPConnection -LocalPort 8080 -State Listen).LocalAddress -eq '127.0.0.1'
         If the server process is bound to wildcard '::' or '0.0.0.0', stop the process and restart server.js with host bound strictly to '127.0.0.1' so loopback isolation is guaranteed.
      3. Inspect the actual process environment of the running Node process:
         Execute 'python scratch/read_proc_env.py <pid>' to directly read the Process Environment Block (PEB) from process memory via Windows NtQueryInformationProcess and ReadProcessMemory.
         Assert that env['TEST_MODE'] == 'true'.
      4. Conclusively audit the /api/contact code path in server.js:
         Confirm that lines 164-182 ('if (TEST_MODE)') write locally to 'inbox/' and immediately return '{ success: true, method: \"test_mode\" }' before any SMTP, Gmail, Resend API, or external webhook dispatch can occur.
      5. Abort immediately before transmitting any payload if any check cannot be conclusively confirmed.
      6. Record existing historical files in 'inbox/' via:
         Get-ChildItem -Path inbox | Select-Object Name, Length, LastWriteTime
      7. Create local Git backup branch 'backup/pre-phase4-verification'.
    </action>
    <verify>
      <shell>git branch --list backup/pre-phase4-verification && python scratch/read_proc_env.py</shell>
    </verify>
    <done>Active server verified bound to 127.0.0.1, PEB memory verified TEST_MODE=true, external delivery immunity confirmed, and backup branch created.</done>
  </task>

  <task type="execute">
    <name>Automated 14-page headless Chrome console audit (REQ-VER-01)</name>
    <files>verify_console_errors.py</files>
    <action>
      1. Execute 'python verify_console_errors.py' against 'http://127.0.0.1:8080'.
      2. Verify that all 14 production HTML pages report 0 console errors.
      3. Confirm that 'index.html' (Three.js / Canvas loop) completes and terminates under 3.0 seconds.
      4. Assert exit code 0.
    </action>
    <verify>
      <shell>python verify_console_errors.py</shell>
    </verify>
    <done>All 14 pages verified with 0 console errors and deterministic sub-3s termination.</done>
  </task>

  <task type="execute">
    <name>36-combination responsive and theme visual capture (REQ-VER-02)</name>
    <files>scratch/screenshots/phase4_verification/*</files>
    <action>
      1. Create a run-specific directory 'scratch/screenshots/phase4_verification/run_<timestamp>/'.
      2. Capture the 6 key representative layouts:
         - index.html
         - about.html
         - projects.html
         - skills.html
         - contact.html
         - blog.html
      3. Across 3 standard breakpoints:
         - Desktop: 1440 × 900
         - Tablet: 768 × 1024
         - Mobile: 390 × 844
      4. In both Dark Mode (default) and Light Mode (data-theme="light").
      5. Write 'scratch/verify_screenshots.py' to assert that all 36 combinations exist, every file has a valid PNG binary signature (\x89PNG\r\n\x1a\n), every file size exceeds 10 KB, and zero screenshots exist in root.
    </action>
    <verify>
      <shell>python scratch/verify_screenshots.py</shell>
    </verify>
    <done>All 36 responsive and theme screenshots captured, validated for PNG integrity and size > 10 KB, and verified collision-safe.</done>
  </task>

  <task type="execute">
    <name>Mathematical mobile horizontal overflow audit across all 14 pages</name>
    <files>scratch/audit_mobile_overflow.py</files>
    <action>
      1. Write 'scratch/audit_mobile_overflow.py' to evaluate document.documentElement.scrollWidth vs clientWidth at 390px mobile viewport width across all 14 HTML pages.
      2. Execute the script and record the exact scrollWidth and clientWidth measurements in a structured table.
      3. Confirm that scrollWidth &lt;= clientWidth on every page (zero horizontal scroll overflow).
      4. Report any discrepancies with exact pixel values without auto-modifying CSS or website code.
    </action>
    <verify>
      <shell>python scratch/audit_mobile_overflow.py</shell>
    </verify>
    <done>All 14 pages mathematically confirmed to have zero horizontal scroll overflow at 390px mobile viewport.</done>
  </task>

  <task type="execute">
    <name>Real E2EE contact form client encryption, offline decryption, and guaranteed cleanup (REQ-VER-03)</name>
    <files>scratch/test_e2ee_pipeline.js, inbox/*</files>
    <action>
      1. Write 'scratch/test_e2ee_pipeline.js' implementing guaranteed cleanup and safety checks:
         - Pre-flight check: Verify that server at 127.0.0.1:8080 responds, process environment has TEST_MODE=true, and server is bound strictly to 127.0.0.1; abort if not conclusive.
         - Pre-transmission snapshot: Record Set of existing files in 'inbox/' via 'const preSnapshot = new Set(fs.readdirSync("inbox"))'.
         - Encrypt synthetic test payload client-side using 'assets/keys/zeerak_public.asc' via OpenPGP to produce 'armoredCiphertext'.
         - Wrap the request, ciphertext-based file detection, decryption, and comparison in try/catch/finally:
           * In try:
             - POST encrypted payload '{ name, email, subject, encrypted_message: armoredCiphertext }' to 'http://127.0.0.1:8080/api/contact'.
             - Assert HTTP 200 response contains '{ success: true, method: \"test_mode\" }'. Abort if method is not test_mode.
             - Conclusive Ciphertext Identification:
               a) Diff current 'fs.readdirSync("inbox")' against 'preSnapshot' to find candidate new 'transmission_*.txt' files.
               b) Filter candidate files to those whose content contains the exact 'armoredCiphertext' string sent in the request.
               c) If exactly one file matches: assign its full absolute path to 'createdTransmissionFile'.
               d) If identification is ambiguous (0 or >1 matches): leave 'createdTransmissionFile = null', do NOT delete anything, and report the cleanup limitation to stderr.
             - Execute offline decryption using 'keys/zeerak_private_KEY_KEEP_SAFE.asc'.
             - Assert decrypted plaintext matches the original synthetic message byte-for-byte.
           * In catch(err):
             - If request times out or an error occurs after file creation, repeat the directory diff against 'preSnapshot' and the ciphertext-based verification check.
             - Assign the full absolute path to 'createdTransmissionFile' only if exactly one candidate file conclusively contains 'armoredCiphertext'. If ambiguous, leave null.
             - Store 'testError = err'.
           * In finally:
             - Guaranteed surgical deletion: If 'createdTransmissionFile' is set AND '!preSnapshot.has(path.basename(createdTransmissionFile))', delete ONLY that exact file via 'fs.unlinkSync(createdTransmissionFile)'.
             - If identification was ambiguous or null, do NOT delete any file. Every historical file in 'preSnapshot' remains strictly preserved.
             - If cleanup throws, catch in a nested try/catch and log to stderr without overwriting 'testError'.
             - If 'testError' is set, log failure details and exit with non-zero exit code (1).
      2. Execute the test command: 'node scratch/test_e2ee_pipeline.js'.
      3. Remove 'scratch/test_e2ee_pipeline.js'.
    </action>
    <verify>
      <shell>node scratch/test_e2ee_pipeline.js</shell>
    </verify>
    <done>Real E2EE client encryption, local test-mode dispatch, offline decryption, exact plaintext comparison, and guaranteed surgical cleanup verified.</done>
  </task>

  <task type="execute">
    <name>CSS build integrity and storage reduction metrics audit</name>
    <files>scripts/build_css.py, assets/*</files>
    <action>
      1. Run 'npm run verify:css' to confirm 100% byte-for-byte and SHA-256 equality (0c5f1c4c...) between css/01-10 modules and root style.css.
      2. Audit total storage of 'assets/' directory and verify it is under 17 MB (currently 3.08 MB).
      3. Audit project root directory and confirm zero loose test PNG files, zero .bak files, and zero .orig files.
    </action>
    <verify>
      <shell>npm run verify:css</shell>
    </verify>
    <done>CSS cascade fidelity confirmed byte-for-byte; storage reduction metrics verified.</done>
  </task>

  <task type="execute">
    <name>Final milestone verification, backup branch safety, and documentation closeout</name>
    <files>.planning/STATE.md, .planning/REQUIREMENTS.md, .planning/ROADMAP.md, scratch/verify_milestone_integrity.py</files>
    <action>
      1. Write 'scratch/verify_milestone_integrity.py' to programmatically verify:
         - All four local backup branches exist: 'backup/pre-phase1-checkpoint', 'backup/pre-phase2-css', 'backup/pre-phase3-tooling', 'backup/pre-phase4-verification'.
         - No backup branch was pushed to GitHub remote ('git branch -r' contains 0 backup branches).
         - All requirements in '.planning/REQUIREMENTS.md' and phases in '.planning/ROADMAP.md' are accurately reported.
      2. Update '.planning/REQUIREMENTS.md': mark REQ-VER-01, REQ-VER-02, and REQ-VER-03 as 'COMPLETED &amp; VERIFIED'.
      3. Update '.planning/ROADMAP.md': mark Phase 4 as 'COMPLETED &amp; VERIFIED'.
      4. Update '.planning/STATE.md': mark overall progress as 100% (Complete), active phase as Complete, and record all final metrics and verification checkpoints.
      5. Execute 'python scratch/verify_milestone_integrity.py' and assert exit code 0.
    </action>
    <verify>
      <shell>python scratch/verify_milestone_integrity.py</shell>
    </verify>
    <done>All four local backup branches confirmed unpushed, all requirements verified, and documentation updated to 100% complete.</done>
  </task>
</tasks>
