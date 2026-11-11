# Project Specification: ZS STUDIO Portfolio

Authoritative project charter, vision, scope, and technical constraints for **ZS STUDIO**.

---

## 1. Project Overview & Vision

**ZS STUDIO** is the personal portfolio of **Zeerak Siddiqui**, a Creative Developer and Bachelor of Computer Applications (BCA) student. The site combines a cinematic 3D WebGL Digital Universe opening experience, high-contrast Swiss Minimalist editorial design, an interactive 3D card blog, and client-side End-to-End Encrypted (E2EE) communication.

---

## 2. Milestones Summary

### Milestone 1: Optimization & Architecture Refinement (COMPLETED & VERIFIED)
- **Goal:** Reclaimed 94.8% of asset storage (from 59.72 MB down to 3.08 MB), cleaned 112 root-level files to 41 core files, modularized 9,407 lines of CSS into 10 structured partials, fortified private key boundaries, and completed full multi-page verification (0 console errors, 36 responsive captures, real E2EE test).

### Milestone 2: Responsive Layout Refinement (ACTIVE MILESTONE)
- **Goal:** Eliminate the known 17.42px horizontal content overflow on the three blog article pages at 390px mobile viewport width by making `.author-bio-links` responsive in `css/08-responsive-blog.css` and synchronizing `style.css`, while preserving desktop layout, visual identity, CSS modular architecture, and zero console errors.

---

## 3. Scope Boundaries (Milestone 2)

### In Scope
- Inspect `.author-bio-links` and `.article-author-card` in `css/08-responsive-blog.css`.
- Add responsive wrapping rules scoped to mobile media queries (`@media (max-width: 768px)`).
- Synchronize root `style.css` using `scripts/build_css.py`.
- Run automated read-only mobile overflow audits across all 14 pages at 390px.
- Verify visual presentation at 1440px, 768px, and 390px across dark and light modes.
- Verify 0 console errors across all 14 pages in headless Chrome.

### Out of Scope
- Modifying unrelated pages, components, or layout structures.
- Altering desktop (> 768px) layouts or visual styling.
- Introducing external CSS libraries or frameworks.
- Pushing any branch to GitHub.

---

## 4. Technical Constraints & Invariants

| Constraint | Rule | Reference |
| :--- | :--- | :--- |
| **Monochrome Foundation** | Strictly `#080808` canvas, `#111111` surfaces, `#F5F5F5` text, `#292929` borders. Zero colorful neon gradients. | `DESIGN.md` §1.1 |
| **Button Standard** | **NO RED BUTTONS**. Use Grey Button tokens (`--btn-grey-bg: #1E1E1E`) or solid white/dark fill. | `DESIGN.md` §2.1 |
| **CSS Architecture** | All edits made to `css/` modules first, compiled to `style.css` via `scripts/build_css.py`, verified with `npm run verify:css`. | `CONVENTIONS.md` §3 |
| **Zero Console Errors** | All 14 HTML pages must produce 0 console errors in headless Chrome audits. | `TESTING.md` §2.1 |
| **Zero Overflow** | `scrollWidth <= clientWidth` on all 14 pages at 390px mobile viewport. | `CONVENTIONS.md` §5 |
