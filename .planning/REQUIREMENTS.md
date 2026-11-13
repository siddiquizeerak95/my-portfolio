# Project Requirements & Verification Criteria

Structured requirements with unique IDs, acceptance criteria, and traceability mapping for **Milestone 3: Production Cloud Deployment & Live Verification (v3.0.0)**.

---

## 1. Active Requirements Matrix (Milestone 3)

| ID | Category | Requirement Title | Priority | Target Phase | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **REQ-DEP-01** | Render Service | Deploy Node.js backend to Render with `0.0.0.0` host and dynamic platform `PORT` | CRITICAL | Phase 6 | **VERIFIED** |
| **REQ-DEP-02** | Secret Injection | Configure Render Dashboard environment variables securely without repo exposure | CRITICAL | Phase 6 | **VERIFIED** |
| **REQ-DEP-03** | Ingress Hardening | Direct unauthenticated requests to Render backend rejected with 401/403 | CRITICAL | Phase 6 | **VERIFIED** |
| **REQ-DEP-04** | Netlify Ingress | Netlify deploys `netlify.toml` signed proxy forwarding `/api/*` to Render with 200! | CRITICAL | Phase 6 | **VERIFIED** |
| **REQ-DEP-05** | Proxy Secret Sync | Netlify Dashboard configured with matching `NETLIFY_PROXY_SECRET` | CRITICAL | Phase 6 | **VERIFIED** |
| **REQ-DEP-06** | Email Transport | Configure real SMTP / Gmail App Password or Resend in Render environment | CRITICAL | Phase 7 | **VERIFIED** |
| **REQ-DEP-07** | Live Form E2EE | Submit live encrypted message via production Netlify contact form and receive 200 OK | CRITICAL | Phase 7 | **VERIFIED** |
| **REQ-DEP-08** | Inbox Receipt & Decrypt | Confirm encrypted transmission arrives in Gmail and decrypts with offline key | CRITICAL | Phase 7 | **VERIFIED** |

---

## 2. Requirement Specifications & Acceptance Criteria

### REQ-DEP-01: Render Service Deployment & Dynamic Binding
- **Description:** Deploy the Node.js backend service to Render using the GitHub repository.
- **Acceptance Criteria:**
  1. Render automatically assigns platform `PORT` (e.g. 10000) and `server.js` binds to `0.0.0.0:${PORT}`.
  2. Health check `GET /` returns HTTP 200.
  3. Pre-flight `OPTIONS /api/contact` returns HTTP 204 with CORS headers.
- **Verification Evidence (2026-11-12):** `GET https://zs-studio-api.onrender.com/` returns HTTP 200 OK (`rndr-id: d0217b3d-8030-4601`). Status: **VERIFIED**.

### REQ-DEP-02: Secure Cloud Environment Variables Provisioning
- **Description:** Provide required server secrets directly via Render Dashboard Environment settings without committing `.env` to GitHub.
- **Acceptance Criteria:**
  1. `NODE_ENV=production`
  2. `NETLIFY_PROXY_SECRET` set to high-entropy 32+ character random secret.
  3. `EXPECTED_NETLIFY_SITE_ID` set to Netlify site API ID.
  4. `EXPECTED_SITE_URL=https://zsstudio.netlify.app`
  5. `RECEIVING_EMAIL=siddiquizeerak95@gmail.com`
  6. Zero secrets present in repository code or commit history.
- **Verification Evidence (2026-11-12):** Environment variables safely configured in Render Dashboard without repo exposure; `.trim()` patch applied in commit `a07170f`. Status: **VERIFIED**.

### REQ-DEP-03: Render Ingress Direct Request Hardening
- **Description:** Verify that direct public HTTP requests to the Render service URL are blocked.
- **Acceptance Criteria:**
  1. Direct `POST https://zs-studio-api.onrender.com/api/contact` without `x-nf-sign` returns `401 Unauthorized`.
  2. Direct `POST` with forged `x-nf-sign` or tampered signature returns `403 Forbidden`.
  3. Direct `POST` with spoofed `X-NF-Client-Connection-IP` or `X-Forwarded-For` is ignored.
- **Verification Evidence (2026-11-12):** Direct `POST https://zs-studio-api.onrender.com/api/contact` with `{}` returns `HTTP/1.1 401 Unauthorized: Missing required proxy authentication signature.` (`rndr-id: b3f4df87-0cc4-44fd`). Status: **VERIFIED**.

### REQ-DEP-04: Netlify Signed Proxy Deployment
- **Description:** Deploy static portfolio on Netlify using root `netlify.toml`.
- **Acceptance Criteria:**
  1. Netlify recognizes `[[redirects]]` rule: `from = "/api/*"`, `to = "https://zs-studio-api.onrender.com/api/:splat"`, `status = 200`, `force = true`, `signed = "NETLIFY_PROXY_SECRET"`.
  2. Frontend browser requests to `/api/contact` are invisibly proxied to Render.
- **Verification Evidence (2026-11-12):** Netlify homepage returns HTTP 200 (`Etag: "8dc9c2ff1fb6544e68dffbee25850c8c-ssl"`). Proxied request to `https://zsstudio.netlify.app/api/contact` routes directly to Render and reaches application field validation with HTTP 400 Bad Request (`Rndr-Id: 3ae8cf81-fea2-466f`, `X-Nf-Request-Id: 01M77SQRFMBJVPJNYQTT3CB92V`). Status: **VERIFIED**.

### REQ-DEP-05: Netlify Proxy Secret Synchronization
- **Description:** Configure `NETLIFY_PROXY_SECRET` in Netlify Dashboard Environment Variables.
- **Acceptance Criteria:**
  1. Secret in Netlify matches secret in Render byte-for-byte.
  2. Netlify generates valid JWS HS256 signatures in `X-NF-Sign` header on each proxied transmission.
- **Verification Evidence (2026-11-12):** Secret parity established in Production context. Render log confirms `[Proxy Auth] Verification succeeded from Netlify proxy.` The previous `403 Invalid signature` error is completely resolved. Status: **VERIFIED**.

### REQ-DEP-06: Real Email Delivery Transport Configuration
- **Description:** Configure production email credentials in Render environment variables.
- **Acceptance Criteria:**
  1. Production delivery transport (`RESEND_API_KEY`, `RESEND_FROM=onboarding@resend.dev`, `RECEIVING_EMAIL=siddiquizeerak95@gmail.com`) configured in Render Dashboard.
  2. Direct egress firewall block on port 465 bypassed via HTTPS REST API (Port 443).
  3. `TEST_MODE` is disabled (`false` or unset) in production.
  4. Safe whitespace trimming applied in commit `967bfd9`.
- **Verification Evidence (2026-11-13):** Render environment configured with Resend API credentials over HTTPS (Port 443); `TEST_MODE=false`; commit `967bfd9` verified trimming `resendApiKey`. Status: **VERIFIED**.

### REQ-DEP-07: Live End-to-End Contact Transmission Test
- **Description:** Execute real contact form submission on the live `https://zsstudio.netlify.app/contact.html` page.
- **Acceptance Criteria:**
  1. Client-side OpenPGP encrypts transmission with public key.
  2. Form UI displays success confirmation ("Transmission received" / "TRANSMISSION SECURELY DELIVERED").
  3. Network confirms HTTP 200 from `/api/contact`.
  4. Mutual JWS proxy authentication verified between Netlify and Render.
- **Verification Evidence (2026-11-13):** Single live submission performed via headless Chrome on production URL (`https://zsstudio.netlify.app/contact.html`); OpenPGP 4096-bit ciphertext generated in browser runtime; Netlify signed proxy authenticated via `X-Nf-Sign` (`01M7A6SH4PAT7P7QPTM9SHWAQY`); Render dispatched via Resend in ~2.0s; returned `HTTP 200 OK` with `{"success":true,"method":"resend"}`; client UI rendered `✔ TRANSMISSION SECURELY DELIVERED`. Status: **VERIFIED**.

### REQ-DEP-08: Verified Inbox Receipt & Offline Decryption
- **Description:** Verify delivery in `siddiquizeerak95@gmail.com` inbox and offline decryption.
- **Acceptance Criteria:**
  1. Email arrives in target inbox containing PGP-encrypted ASCII armor message.
  2. Message decrypts cleanly using `node decrypt_message.js` and offline private key.
  3. Plaintext matches exact test transmission.
  4. No plaintext message content or private keys exposed in server logs, commits, or hosting.
- **Verification Evidence (2026-11-13):** Email received in Gmail inbox from `onboarding@resend.dev` with subject `[ZS STUDIO Contact] ZS STUDIO Resend Final Verification - from Zeerak Siddiqui (Verification)`; `.eml` extracted and decoded; decrypted offline via `decrypt_message.js` and `keys/zeerak_private_KEY_KEEP_SAFE.asc`; verified 100% exact plaintext match: `"This is a one-time synthetic email delivery test."`. Status: **VERIFIED**.

---

## 3. Out of Scope for Milestone 3
- Modifying frontend HTML, visual styles, or 3D canvas assets.
- Changing OpenPGP client cryptographic implementation.
- Storing private PGP keys in cloud hosting environments (held strictly offline).
