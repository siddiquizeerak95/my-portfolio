---
phase: 1
wave: 1
requirements:
  - REQ-AST-01
  - REQ-HYG-01
  - REQ-HYG-02
must_haves:
  phase_1_truths:
    - "All 138 unreferenced assets, root screenshots, and backup files are safely moved to gitignored scratch/ archives"
    - "100% of moved files verified with identical pre/post SHA-256 hashes"
    - "Zero active HTML, CSS, JavaScript, or production assets modified"
    - "All 14 HTML pages continue to load with zero console errors"
  phase_1_artifacts:
    - path: "scratch/archive/recovery_manifest.json"
      description: "Full SHA-256 recovery manifest mapping original and destination paths"
    - path: "scratch/archive/phase1_asset_backup/"
      description: "Archive of 18 unreferenced 3D binary and point cloud assets"
    - path: "scratch/screenshots/"
      description: "Archive of 108 root-level PNG test screenshots"
    - path: "scratch/archive/backup_files/"
      description: "Archive of 12 stale backup and orig files"
  phase_1_wiring:
    - "Local Git backup branch 'backup/pre-phase1-checkpoint' created with working tree commit 555d544"
---

<tasks>
  <task type="execute">
    <name>Create Git backup checkpoint branch</name>
    <files>index.html, sculpture-intro.css, sculpture-intro.js, assets/cosmos/</files>
    <action>
      Created local backup branch 'backup/pre-phase1-checkpoint' and committed current working tree changes. Did not push to GitHub.
    </action>
    <verify>
      <shell>git log -1 backup/pre-phase1-checkpoint</shell>
    </verify>
    <done>Branch created with commit 555d544 successfully.</done>
  </task>

  <task type="execute">
    <name>Generate SHA-256 hashes and move files to scratch/ archive</name>
    <files>assets/*, root/*.png, root/*.bak</files>
    <action>
      Generated pre-move SHA-256 manifest for all 138 target files. Moved files into scratch/archive/ and scratch/screenshots/. Computed and verified post-move SHA-256 hashes.
    </action>
    <verify>
      <shell>python -c "import json; m = json.load(open('scratch/archive/recovery_manifest.json')); assert m['verified_identical'] and m['total_files'] == 138"</shell>
    </verify>
    <done>All 138 files moved and verified with 100% identical SHA-256 hashes.</done>
  </task>

  <task type="execute">
    <name>Automated console error and visual render verification</name>
    <files>scratch/run_full_verification.py, take_screenshot.py</files>
    <action>
      Executed headless Chrome console error audit across all 14 HTML pages and captured visual render screenshots.
    </action>
    <verify>
      <shell>python scratch/run_full_verification.py</shell>
    </verify>
    <done>All 14 pages passed with 0 console errors. Render screenshots verified clean.</done>
  </task>
</tasks>

