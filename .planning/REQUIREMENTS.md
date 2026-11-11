# Project Requirements & Verification Criteria

Structured requirements with unique IDs, acceptance criteria, and traceability mapping for **Milestone 2: ZS STUDIO Responsive Layout Refinement**.

---

## 1. Active Requirements Matrix (Milestone 2)

| ID | Category | Requirement Title | Priority | Target Phase | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **REQ-RES-01** | Responsiveness | Make `.author-bio-links` responsive under `@media (max-width: 768px)` | HIGH | Phase 5 | **COMPLETED & VERIFIED** |
| **REQ-RES-02** | Overflow Defense | Eliminate +17.42px content overflow: `body.scrollWidth <= 390px` on all 3 blog pages | HIGH | Phase 5 | **COMPLETED & VERIFIED** |
| **REQ-RES-03** | Architecture | Preserve CSS modularity and synchronize `style.css` via `scripts/build_css.py` | HIGH | Phase 5 | **COMPLETED & VERIFIED** |
| **REQ-REG-01** | Visual Fidelity | Preserve desktop (1440px) and tablet (768px) author card layouts 100% | HIGH | Phase 5 | **COMPLETED & VERIFIED** |
| **REQ-REG-02** | Regression Defense | Maintain 0 console errors across all 14 HTML pages in headless Chrome | HIGH | Phase 5 | **COMPLETED & VERIFIED** |
| **REQ-BCK-01** | Safe Deployment | Create local backup checkpoint `backup/pre-responsive-refinement` (0 remote pushes) | HIGH | Phase 5 | **COMPLETED & VERIFIED** |

---

## 2. Requirement Specifications & Acceptance Criteria

### REQ-RES-01: Responsive Author Bio Links
- **Description:** Update `css/08-responsive-blog.css` under the `@media (max-width: 768px)` block to enable wrapping for `.author-bio-links` and reduce excessive mobile card padding.
- **Target File:** `css/08-responsive-blog.css`
- **Acceptance Criteria:**
  1. `.author-bio-links` enables `flex-wrap: wrap;` on viewports `<= 768px`. *(Verified: lines 928-931)*
  2. Spacing between wrapped links remains consistent and adheres to Swiss Minimalist design (`gap: 8px 14px;`). *(Verified)*
  3. Typography (`var(--font-mono)`, `11px`), colors (`var(--text-primary)`), and underline styles remain preserved. *(Verified)*
- **Status:** **COMPLETED & VERIFIED**

### REQ-RES-02: Zero Horizontal Content Overflow at 390px
- **Description:** Eliminate the measured 17.42px content protrusion on all three affected blog article pages.
- **Affected Pages:**
  1. `blog-how-i-built-my-portfolio.html`
  2. `blog-my-journey-as-a-developer.html`
  3. `blog-why-i-prefer-minimalist-web-design.html`
- **Acceptance Criteria:**
  1. At 390px viewport width, `document.body.scrollWidth <= 390px` on all 3 pages. *(Verified: 390px / 390px on all 3 pages)*
  2. At 390px viewport width, `document.documentElement.scrollWidth <= 390px` on all 14 pages. *(Verified: 14/14 pass)*
  3. No horizontal scrollbar or lateral page shifting occurs. *(Verified)*
- **Status:** **COMPLETED & VERIFIED**

### REQ-RES-03: CSS Modularity & Build Synchronization
- **Description:** Keep the 10 CSS modules in `css/` as the single source of truth and compile `style.css` using `scripts/build_css.py`.
- **Acceptance Criteria:**
  1. `python scripts/build_css.py` executes successfully with atomic file write. *(Verified: 225,742 bytes, SHA-256 `7d5d381a...`)*
  2. `npm run verify:css` passes with exact byte-for-byte and SHA-256 match. *(Verified: Exact match = True)*
  3. Zero manual edits made directly to `style.css` without source module sync. *(Verified)*
- **Status:** **COMPLETED & VERIFIED**

### REQ-REG-01: Desktop & Tablet Visual Preservation
- **Description:** Ensure that the desktop (1440px) and tablet (768px) visual presentation of `.article-author-card` remains 100% identical to pre-change state.
- **Acceptance Criteria:**
  1. At 1440px, `.article-author-card` remains horizontal (`flex-direction: row; align-items: center;`) with `padding: 32px;` and unwrapped single-line bio links. *(Verified)*
  2. Visual regression screenshots at 1440px and 768px confirm zero unintended drift. *(Verified across 18 captures in run_1794378029)*
- **Status:** **COMPLETED & VERIFIED**

### REQ-REG-02: Zero Console Errors
- **Description:** Run headless Chrome console error audit across all 14 HTML pages.
- **Acceptance Criteria:**
  1. 14 / 14 pages report `0 console errors` via `verify_console_errors.py`. *(Verified: 14/14 pass in 28.75s)*
- **Status:** **COMPLETED & VERIFIED**

### REQ-BCK-01: Local Backup Checkpoint
- **Description:** Create local git branch `backup/pre-responsive-refinement` before modifying any files.
- **Acceptance Criteria:**
  1. Local branch `backup/pre-responsive-refinement` exists. *(Verified)*
  2. Zero backup branches pushed to GitHub remote. *(Verified: origin/main only)*
- **Status:** **COMPLETED & VERIFIED**

---

## 3. Historical Completed Requirements (Milestone 1)

| ID | Title | Final Status |
|:---|:---|:---:|
| **REQ-AST-01** | Prune unreferenced 3D binary & JSON files (~45 MB) | **COMPLETED & VERIFIED** |
| **REQ-HYG-01** | Relocate 112 root-level PNG screenshots to test artifacts | **COMPLETED & VERIFIED** |
| **REQ-HYG-02** | Purge stale `.bak` and `.orig` backup files | **COMPLETED & VERIFIED** |
| **REQ-CSS-01** | Deduplicate conflicting `:root` token blocks in stylesheet | **COMPLETED & VERIFIED** |
| **REQ-CSS-02** | Modularize monolithic `style.css` into structured partials | **COMPLETED & VERIFIED** |
| **REQ-SEC-01** | Harden offline private key storage and update CLI paths | **COMPLETED & VERIFIED** |
| **REQ-VER-01** | Verify zero console errors across all 14 pages in headless Chrome | **COMPLETED & VERIFIED** |
| **REQ-VER-02** | Verify responsive visual fidelity across 1440px, 768px, and 390px | **COMPLETED & VERIFIED** |
| **REQ-VER-03** | Verify client-side E2EE contact transmission & decryption | **COMPLETED & VERIFIED** |
