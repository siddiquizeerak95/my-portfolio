# Phase 2 Context: Cascade-Preserving Modular CSS Architecture

Authoritative implementation decisions, sequential boundary specifications, build pipeline verification, and rollback safeguards locked for Phase 2.

---

## 1. Core Principle: Strict Cascade Order Preservation

The primary goal of Phase 2 is **safe modular architecture**, not visual redesign or aggressive optimization.
- **Cascade Specificity Rule:** In CSS, when selectors have identical specificity, the **last rule in the source file wins**.
- **Invariant:** **Zero rules will be reordered, removed, or consolidated by category if doing so alters their original sequence.**
- **Safe Modularization:** Slicing `style.css` into 10 contiguous sequential modules (`01` through `10`) ensures that concatenating them produces a stylesheet that is **100% byte-for-byte and rule-for-rule identical to the original `style.css`**.

---

## 2. Locked Technical Decisions

| Area | Decision | Specification |
| :--- | :--- | :--- |
| **Extraction Strategy** | **Sequential Contiguous Slices** | 10 modular source files in `css/` preserving exact original line order (lines 1 to 9407). |
| **Rule Order & Cascade** | **100% Preserved** | Zero reordering of historical overrides. All overrides remain in their exact source positions. |
| **Token Consolidation Policy** | **Deferred to Computed Audit** | Conflicting tokens will **NOT** be prematurely altered until computed browser styles in Dark and Light modes are audited. |
| **Build & Bundling** | **Python Concatenator (`scratch/build_css.py`)** | Assembles `css/01` through `10` into root `style.css`. Zero reliance on native `@import` in production. |
| **Automated Equality Check** | **Byte-for-Byte & Hash Comparison** | The build script verifies that the generated `style.css` matches the original pre-migration stylesheet. |
| **External Stylesheets** | **Strictly Untouched** | `sculpture-intro.css` (3D Cosmos) and `blog-3d.css` (3D Blog Deck) remain completely unmodified. |
| **Rollback Safeguard** | **Triple Redundancy** | 1) Git backup branch `backup/pre-phase2-css`, 2) Disk backup `scratch/archive/style.css.pre-phase2.bak`, 3) Original hash manifest. |
| **Multi-Theme Testing** | **Dark Mode & Light Mode Audit** | All 14 HTML pages verified with 0 console errors and visual render comparisons at 1440px, 768px, and 390px. |

---

## 3. 10 Sequential Modular Slices (Contiguous Boundaries)

```
css/
├── 01-tokens.css                  # Lines 1–344    (344 lines)  : Initial Design tokens & :root properties
├── 02-base-reset.css              # Lines 345–505  (161 lines)  : CSS reset, typography base, precision cursor
├── 03-preloader.css               # Lines 506–800  (295 lines)  : Canvas 2D preloader & brand reveal
├── 04-header-nav.css              # Lines 801–1374 (574 lines)  : Header navigation, sound FX, mobile drawer
├── 05-buttons-layout.css          # Lines 1375–1502(128 lines)  : Button system, editorial layout grid
├── 06-hero-orbit.css              # Lines 1503–2388(886 lines)  : Hero section, orbital cards, data-tilt 3D
├── 07-sections.css                # Lines 2389–3467(1079 lines) : Skills, Projects, About, Contact, Footer, Scroll reveals
├── 08-responsive-blog.css         # Lines 3468–4469(1002 lines) : Responsive breakpoints, Blog listing & articles
├── 09-3d-redesign.css             # Lines 4470–7410(2941 lines) : Master 3D redesign, sections 01-07, light theme rules
└── 10-motion-restored-hero.css    # Lines 7411–9407(1997 lines) : Motion system, UI/UX case studies, restored hero & spiral card
```

*Concatenating `01` through `10` reproduces the exact 9,407-line original stylesheet with zero selector deviation.*

---

## 4. Verification & Testing Matrix

1. **Pre-Migration:**
   - Dedicated Git backup branch created.
   - Exact pre-migration SHA-256 hash recorded.
   - Baseline screenshots captured across desktop (`1440 × 900`), tablet (`768 × 1024`), and mobile (`390 × 844`) in both Dark and Light themes.
2. **Post-Extraction & Build:**
   - Content comparison: Rebuilt `style.css` compared against original `style.css` (Character-for-character equality check).
   - Console error audit: `verify_console_errors.py` run across all 14 HTML pages (14/14 pass gate).
   - Visual screenshot diff: Captured post-build screenshots compared against pre-migration baselines.
