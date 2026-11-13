# Project Specification: ZS STUDIO Portfolio

Authoritative project charter, vision, scope, and technical constraints for **ZS STUDIO**.

---

## 1. Project Overview & Vision

**ZS STUDIO** is the personal portfolio of **Zeerak Siddiqui**, a Creative Developer and Bachelor of Computer Applications (BCA) student. The site combines a cinematic 3D WebGL Digital Universe opening experience, high-contrast Swiss Minimalist editorial design, an interactive 3D card blog, and client-side End-to-End Encrypted (E2EE) communication.

---

## 2. Current Milestone: v3.0 Production Cloud Deployment & Live Verification

**Goal:** Deploy the Node.js backend Web Service to Render and static portfolio to Netlify, configure secure cloud dashboard environment variables and signed proxy routing, integrate real SMTP email delivery, and verify live end-to-end encrypted contact form transmissions.

### Target Features & Capabilities:
- **Render Web Service Ingress:** Dynamic platform `PORT` handling, `HOST=0.0.0.0`, production mode.
- **Mutual Proxy Authentication:** Netlify JWS HMAC-SHA256 signature verification in `server.js` using `NETLIFY_PROXY_SECRET` and `EXPECTED_NETLIFY_SITE_ID`.
- **Secret & Key Isolation:** Server secrets stored strictly in hosting provider dashboards; offline private PGP key kept out of git and cloud hosting.
- **Live Email Transport:** Real SMTP dispatch (Gmail App Password or Resend) to `siddiquizeerak95@gmail.com`.
- **Full End-to-End Verification:** Live contact submission on `https://zsstudio.netlify.app/contact.html`, real inbox delivery, and offline decryption.

---

## 3. Milestones Summary

### Milestone 1: Optimization & Architecture Refinement (v1.0.0 — COMPLETED & VERIFIED)
- **Delivered:** Reclaimed 94.8% of asset storage, cleaned root files, modularized 9,407 lines of CSS into 10 partials, fortified private key boundaries, and completed full multi-page verification.

### Milestone 2: Responsive Layout Refinement & API Security (v2.0.0 — COMPLETED & VERIFIED)
- **Delivered:** Eliminated mobile content overflow across all 14 pages (`scrollWidth <= clientWidth` at 390px), synchronized modular CSS to `style.css`, verified 0 console errors, and implemented Netlify signed proxy JWS HMAC-SHA256 ingress security in `server.js` and `netlify.toml`.

### Milestone 3: Production Cloud Deployment & Live Verification (v3.0.0 — COMPLETED & VERIFIED)
- **Delivered:** Connected Netlify and Render in production with JWS HS256 proxy signatures, configured cloud secrets safely, integrated Resend HTTPS REST API email delivery, verified live 4096-bit OpenPGP form submission (`200 OK`), confirmed Gmail inbox receipt, and decrypted offline with 100% exact plaintext match.

---

## 4. Technical Constraints & Invariants

| Constraint | Rule | Reference |
| :--- | :--- | :--- |
| **Monochrome Foundation** | Strictly `#080808` canvas, `#111111` surfaces, `#F5F5F5` text, `#292929` borders. Zero colorful neon gradients. | `DESIGN.md` §1.1 |
| **Button Standard** | **NO RED BUTTONS**. Use Grey Button tokens (`--btn-grey-bg: #1E1E1E`) or solid white/dark fill. | `DESIGN.md` §2.1 |
| **CSS Architecture** | All edits made to `css/` modules first, compiled to `style.css` via `scripts/build_css.py`, verified with `npm run verify:css`. | `CONVENTIONS.md` §3 |
| **Zero Console Errors** | All 14 HTML pages must produce 0 console errors in headless Chrome audits. | `TESTING.md` §2.1 |
| **Zero Overflow** | `scrollWidth <= clientWidth` on all 14 pages at 390px mobile viewport. | `CONVENTIONS.md` §5 |
| **API Ingress Security** | Production `/api/contact` requires valid Netlify JWS HMAC-SHA256 signature; reject unauthenticated direct requests. | `server.js` |
| **Secret Protection** | Zero credentials, plaintext passwords, or private keys committed to git or logged to console. | Security Rule |

---

## 5. Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state
