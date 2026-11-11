---
phase: 2
wave: 1
requirements:
  - REQ-CSS-01
  - REQ-CSS-02
must_haves:
  phase_2_truths:
    - "10 modular CSS source files created in css/ preserving 100% of the original rule sequence"
    - "Zero CSS rules reorganized by category or reordered across cascade boundaries"
    - "Python build script concatenates css/01 through 10 in exact order to reproduce root style.css"
    - "Generated style.css is verified equal to original style.css via content and hash comparison"
    - "No native CSS @import statements used in production style.css"
    - "sculpture-intro.css and blog-3d.css remain standalone and completely untouched"
    - "All 14 HTML pages continue linking directly to style.css with zero HTML edits"
    - "All 14 HTML pages verified in Dark Mode and Light Mode with zero console errors"
    - "Desktop (1440px), tablet (768px), and mobile (390px) screenshots match baseline renders"
  phase_2_artifacts:
    - path: "css/01-tokens.css"
      description: "Lines 1–344: Initial tokens, system properties, and root properties"
    - path: "css/02-base-reset.css"
      description: "Lines 345–505: CSS reset, typography base, precision cursor"
    - path: "css/03-preloader.css"
      description: "Lines 506–800: Canvas 2D preloader and brand reveal styles"
    - path: "css/04-header-nav.css"
      description: "Lines 801–1374: Header navigation, sound FX, mobile drawer"
    - path: "css/05-buttons-layout.css"
      description: "Lines 1375–1502: Button system and editorial layout grid"
    - path: "css/06-hero-orbit.css"
      description: "Lines 1503–2388: Hero section, orbital cards, data-tilt 3D"
    - path: "css/07-sections.css"
      description: "Lines 2389–3467: Skills, Projects, About, Contact, Footer, Scroll reveals"
    - path: "css/08-responsive-blog.css"
      description: "Lines 3468–4469: Responsive breakpoints, Blog listing and articles"
    - path: "css/09-3d-redesign.css"
      description: "Lines 4470–7410: Master 3D redesign, sections 01–07, light theme rules"
    - path: "css/10-motion-restored-hero.css"
      description: "Lines 7411–9407: Motion system, UI/UX case studies, restored hero & spiral card"
    - path: "scratch/build_css.py"
      description: "Build script that concatenates css/01 through 10 into root style.css and verifies content match"
    - path: "style.css"
      description: "Compiled production master stylesheet with exact original cascade order"
  phase_2_wiring:
    - "scratch/build_css.py reads css/01 through 10 in exact numerical order and outputs root style.css"
    - "Build script performs automated character-for-character comparison against pre-migration style.css"
---

<tasks>
  <task type="execute">
    <name>Create Git backup checkpoint and capture baseline screenshots</name>
    <files>style.css, scratch/baselines/*</files>
    <action>
      Create Git backup branch 'backup/pre-phase2-css' and make a physical disk copy at 'scratch/archive/style.css.pre-phase2.bak'.
      Record pre-migration SHA-256 hash of style.css.
      Capture visual baseline screenshots of index.html, projects.html, skills.html, about.html, and contact.html across 1440px, 768px, and 390px in both Dark and Light themes into scratch/baselines/.
    </action>
    <verify>
      <shell>python -c "import os; assert os.path.exists('scratch/archive/style.css.pre-phase2.bak')"</shell>
    </verify>
    <done>Branch created, backup file archived, and full visual baseline renders stored.</done>
  </task>

  <task type="execute">
    <name>Create Python CSS build and content comparison script</name>
    <files>scratch/build_css.py</files>
    <action>
      Write 'scratch/build_css.py' to:
      1. Define the 10 sequential module paths in exact numerical order.
      2. Concatenate them into root 'style.css'.
      3. Compare the assembled text character-for-character and hash-for-hash against 'scratch/archive/style.css.pre-phase2.bak'.
      4. If any character differs or line count mismatches, halt with an error.
    </action>
    <verify>
      <shell>python -c "import os; assert os.path.exists('scratch/build_css.py')"</shell>
    </verify>
    <done>Build script ready with built-in content verification gate.</done>
  </task>

  <task type="execute">
    <name>Perform safe sequential extraction into css/01 through css/10</name>
    <files>css/*.css</files>
    <action>
      Extract the 10 contiguous sequential slices from style.css into the dedicated css/ directory:
      - css/01-tokens.css                 (Lines 1–344)
      - css/02-base-reset.css             (Lines 345–505)
      - css/03-preloader.css              (Lines 506–800)
      - css/04-header-nav.css             (Lines 801–1374)
      - css/05-buttons-layout.css         (Lines 1375–1502)
      - css/06-hero-orbit.css             (Lines 1503–2388)
      - css/07-sections.css               (Lines 2389–3467)
      - css/08-responsive-blog.css        (Lines 3468–4469)
      - css/09-3d-redesign.css            (Lines 4470–7410)
      - css/10-motion-restored-hero.css   (Lines 7411–9407)
      Preserve 100% of original rule order, comments, and historical overrides without modification.
    </action>
    <verify>
      <shell>python -c "import os; assert len(os.listdir('css')) == 10"</shell>
    </verify>
    <done>All 10 sequential modules created with exact line-for-line fidelity.</done>
  </task>

  <task type="execute">
    <name>Compile production style.css and verify exact content equality</name>
    <files>style.css</files>
    <action>
      Execute 'python scratch/build_css.py' to concatenate the 10 modules into root 'style.css'.
      Verify that the generated 'style.css' matches 'scratch/archive/style.css.pre-phase2.bak' character-for-character.
    </action>
    <verify>
      <shell>python scratch/build_css.py</shell>
    </verify>
    <done>Production style.css compiled and verified 100% equal to the original pre-migration stylesheet.</done>
  </task>

  <task type="execute">
    <name>Execute 14-page automated console error audit</name>
    <files>scratch/run_full_verification.py</files>
    <action>
      Run headless Chrome audit across all 14 HTML pages in both Dark Mode and Light Mode.
      Confirm 14 / 14 pages report zero console errors.
    </action>
    <verify>
      <shell>python scratch/run_full_verification.py</shell>
    </verify>
    <done>All 14 pages pass with 0 console errors.</done>
  </task>

  <task type="execute">
    <name>Multi-device visual render verification (1440px, 768px, 390px)</name>
    <files>scratch/post_migration_renders/*</files>
    <action>
      Capture post-migration screenshots of index.html, projects.html, skills.html, about.html, and contact.html across 1440px, 768px, and 390px viewports in both Dark Mode and Light Mode.
      Perform pixel-comparison diff against baseline screenshots.
    </action>
    <verify>
      <shell>python -c "import os; assert len(os.listdir('scratch/post_migration_renders')) >= 6"</shell>
    </verify>
    <done>Screenshots confirmed identical with zero layout shifts or visual regressions.</done>
  </task>
</tasks>
