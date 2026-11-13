# Milestone Roadmap: ZS STUDIO Portfolio

Authoritative execution roadmap mapping requirements to sequential deliverables, dependencies, and verification gates.

---

## Roadmap Overview

```
[ Milestone 1: Optimization & Architecture Refinement ] ────> COMPLETED & VERIFIED (v1.0.0)
[ Milestone 2: Responsive Layout Refinement & API Security ] ─> COMPLETED & VERIFIED (v2.0.0)
[ Milestone 3: Production Cloud Deployment & Live Verification ] ──> COMPLETED & VERIFIED (v3.0.0)
  ├─ Phase 6: Cloud Ingress Setup & Secure Environment Provisioning (REQ-DEP-01 to REQ-DEP-05) ─> COMPLETED
  └─ Phase 7: Live Email Delivery Integration & End-to-End Verification (REQ-DEP-06 to REQ-DEP-08) ─> COMPLETED
```

---

## Active Milestone: Milestone 3 (v3.0.0)
**Goal:** Deploy the Node.js backend to Render and static portfolio to Netlify, configure secure cloud environment variables and signed proxy routing, and verify real live end-to-end encrypted contact form delivery.

---

## Phase Breakdown (Milestone 3)

### Phase 6: Cloud Ingress Setup & Secure Environment Provisioning
- **Goal:** Deploy the Node.js backend Web Service to Render, connect Netlify signed proxy redirect, configure cloud dashboard environment variables without exposing secrets, and verify mutual proxy authentication.
- **Requirements Covered:** `REQ-DEP-01`, `REQ-DEP-02`, `REQ-DEP-03`, `REQ-DEP-04`, `REQ-DEP-05`
- **Dependencies:** Milestone 2 (Commit `612a43a`)
- **Status:** **COMPLETED & VERIFIED (2026-11-12)**
- **Success Criteria:**
  1. Render Web Service successfully builds and binds to `0.0.0.0:${PORT}` &mdash; `VERIFIED` (`200 OK` on `/`).
  2. Netlify static site deploys with `netlify.toml` signed proxy rule active &mdash; `VERIFIED` (`200 OK`, `Server: Netlify`).
  3. Direct unauthenticated requests to Render backend return 401 Unauthorized &mdash; `VERIFIED` (`401 Unauthorized`).
  4. Proxied requests from Netlify with valid JWS signature are accepted &mdash; `VERIFIED` (`400 Bad Request` at application validation; Render log confirms `Proxy Auth Verification succeeded`).

### Phase 7: Live Email Delivery Integration & End-to-End Verification
- **Goal:** Configure real delivery credentials in Render, execute live contact form submission on production URL, verify email delivery in Gmail inbox, and decrypt transmission with offline PGP key.
- **Requirements Covered:** `REQ-DEP-06`, `REQ-DEP-07`, `REQ-DEP-08`
- **Dependencies:** Phase 6
- **Status:** **COMPLETED & VERIFIED (2026-11-13)**
- **Success Criteria:**
  1. Delivery credentials configured in Render dashboard (`RESEND_API_KEY`, `RESEND_FROM=onboarding@resend.dev`, `RECEIVING_EMAIL`, `TEST_MODE=false`) &mdash; `VERIFIED` (Port 443 HTTPS REST API; commit `967bfd9` whitespace trimming).
  2. Live contact form submission on `https://zsstudio.netlify.app/contact.html` returns 200 OK &mdash; `VERIFIED` (`HTTP 200 OK`, `method: "resend"`, ~2.0s latency).
  3. PGP-encrypted transmission arrives in `siddiquizeerak95@gmail.com` &mdash; `VERIFIED` (Delivered via Resend with valid DKIM/SPF/DMARC; `.eml` archived).
  4. Message decrypts cleanly using `decrypt_message.js` with offline private key &mdash; `VERIFIED` (Exact 100% word-for-word plaintext match).
  5. Zero credentials, plaintext messages, or private keys logged &mdash; `VERIFIED` (Private key held strictly offline).

---

## Historical Milestones Completed

### Milestone 2: ZS STUDIO Responsive Layout Refinement & API Security (v2.0.0)
- **Status:** **COMPLETED & VERIFIED (2026-11-11)**
- **Archive:** [`.planning/milestones/v2.0-ROADMAP.md`](file:///c:/Users/siddi/Desktop/New%20folder/.planning/milestones/v2.0-ROADMAP.md) | [Requirements Archive](file:///c:/Users/siddi/Desktop/New%20folder/.planning/milestones/v2.0-REQUIREMENTS.md)

### Milestone 1: ZS STUDIO Optimization & Architecture Refinement (v1.0.0)
- **Status:** **COMPLETED & VERIFIED (2026-11-10)**
- **Archive:** 94.8% storage reduction, CSS modularization, security hardening, and 14-page regression verification.
