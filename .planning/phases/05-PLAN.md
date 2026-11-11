# Phase 5 Execution Plan: Author Bio Responsive Refinement & Multi-Page Verification

**Milestone:** Milestone 2: ZS STUDIO Responsive Layout Refinement  
**Phase:** 5 of 5  
**Status:** **PLANNING (Awaiting User Review & Approval)**  
**Safety Invariant:** Zero modifications to production files until explicit user approval.

---

## 1. Task Breakdown

### Task 5.1: Pre-Execution Safety Checkpoint
- **Objective:** Create a dedicated local rollback checkpoint branch before modifying any source code.
- **Commands:**
  ```powershell
  git checkout -b backup/pre-responsive-refinement
  git checkout main
  git branch -a
  ```
- **Verification:**
  - Confirm `backup/pre-responsive-refinement` exists locally.
  - Confirm `git branch -r` shows only `origin/main` (zero remote pushes).

---

### Task 5.2: CSS Module Refinement in `css/08-responsive-blog.css`
- **Objective:** Apply responsive wrapping rules for `.author-bio-links` and refine mobile card padding inside `@media (max-width: 768px)`.
- **Target File:** `css/08-responsive-blog.css`
- **Exact Code Edit:**
  In `css/08-responsive-blog.css` around line 922:
  ```css
  @media (max-width: 768px) {
    .blog-dossier-item {
      grid-template-columns: 1fr;
      padding: 28px 24px;
      gap: 18px;
    }

    .article-pagination-grid {
      grid-template-columns: 1fr;
    }

    .article-author-card {
      flex-direction: column;
      align-items: flex-start;
      padding: 24px 20px;
    }

    .author-bio-links {
      flex-wrap: wrap;
      gap: 8px 14px;
    }
  }
  ```
- **Verification:**
  - Confirm desktop rule `.author-bio-links` (lines 879-884) remains completely untouched.
  - Confirm `.article-author-card` desktop rule (lines 837-846) remains completely untouched.
  - Confirm zero changes outside `@media (max-width: 768px)`.

---

### Task 5.3: CSS Build & Synchronization
- **Objective:** Compile `style.css` using `scripts/build_css.py` and verify byte-for-byte fidelity with in-memory modules.
- **Commands:**
  ```powershell
  python scripts/build_css.py
  npm run verify:css
  ```
- **Verification:**
  - `python scripts/build_css.py` performs atomic file replacement.
  - `npm run verify:css` exits 0 with `Exact Byte-for-Byte Match : True` and `SHA-256 Hash Match : True`.
  - Zero manual direct edits to `style.css`.

---

### Task 5.4: Mathematical Mobile Overflow Audit Across All 14 Pages at 390px
- **Objective:** Verify that `document.body.scrollWidth` and `document.documentElement.scrollWidth` are `<= 390px` on all 14 pages.
- **Script:** Execute `scratch/audit_mobile_overflow.mjs` via CDP at `390px` viewport width.
- **Verification Criteria:**
  - `blog-how-i-built-my-portfolio.html`: `body.scrollWidth === 390px` (Down from 407px).
  - `blog-my-journey-as-a-developer.html`: `body.scrollWidth === 390px` (Down from 407px).
  - `blog-why-i-prefer-minimalist-web-design.html`: `body.scrollWidth === 390px` (Down from 407px).
  - All remaining 11 pages: `scrollWidth === 390px`.
  - Exit code 0 (14 / 14 pages report `None (0px)` overflow).

---

### Task 5.5: Multi-Viewport Visual Regression Audit
- **Objective:** Capture and inspect screenshots of the author card and full pages across desktop, tablet, and mobile viewports in dark and light modes.
- **Breakpoints:**
  - Desktop: `1440 × 900`
  - Tablet: `768 × 1024`
  - Mobile: `390 × 844`
- **Output Directory:** `scratch/screenshots/phase5_refinement/`
- **Verification Criteria:**
  - At 1440px: Author card is horizontal (`flex-direction: row; align-items: center;`) with single-line links. Zero visual drift.
  - At 768px: Author card is vertical, links wrap cleanly without horizontal overflow.
  - At 390px: Author card fits cleanly inside the mobile viewport with balanced padding and readable links.

---

### Task 5.6: Headless Chrome Console Error Audit Across All 14 Pages
- **Objective:** Ensure zero JavaScript runtime console errors across all pages.
- **Command:** `python verify_console_errors.py`
- **Verification Criteria:**
  - 14 / 14 pages report `0 console errors`.
  - Exit code 0.

---

### Task 5.7: Milestone Sign-Off & Documentation Closeout
- **Objective:** Update project documentation and generate completion summary.
- **Deliverables:**
  - Create `.planning/phases/05-SUMMARY.md`.
  - Update `.planning/STATE.md` to 100% complete.
  - Update `.planning/REQUIREMENTS.md` with all requirements marked `COMPLETED & VERIFIED`.
  - Update `.planning/ROADMAP.md` with Phase 5 marked complete.

---

## 2. Measurable Acceptance Criteria

| Criteria ID | Condition | Target Metric |
|:---|:---|:---:|
| **AC-01** | `blog-how-i-built-my-portfolio.html` at 390px | `body.scrollWidth <= 390px` (0px overflow) |
| **AC-02** | `blog-my-journey-as-a-developer.html` at 390px | `body.scrollWidth <= 390px` (0px overflow) |
| **AC-03** | `blog-why-i-prefer-minimalist-web-design.html` at 390px | `body.scrollWidth <= 390px` (0px overflow) |
| **AC-04** | All 14 pages at 390px | `scrollWidth <= clientWidth` on 14/14 pages |
| **AC-05** | CSS Modular Synchronization | `npm run verify:css` exits 0 (100% byte match) |
| **AC-06** | Desktop Author Card Layout (1440px) | Horizontal row, 32px padding, 0 visual regression |
| **AC-07** | Console Error Audit | 14 / 14 pages report 0 errors via `verify_console_errors.py` |
| **AC-08** | Git Safety | Backup branch `backup/pre-responsive-refinement` local only; 0 remote pushes |

