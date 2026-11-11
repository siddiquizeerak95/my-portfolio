# External Integrations & Services

Authoritative documentation of all external APIs, third-party services, cryptographic boundaries, storage mechanisms, and outbound communication channels in **ZS STUDIO**.

---

## 1. Email & Transmission Services

The contact subsystem (`contact.html`, `contact-e2ee.js`, and `server.js`) utilizes a tiered outbound dispatch architecture:

```
[ Visitor Browser (contact.html) ]
                |
     OpenPGP Client Encryption (4096-bit RSA)
                |
                v
       POST /api/contact
                |
      [ Node.js server.js ]
         /           \
        /             \
[ Option A: SMTP ]   [ Option B: Resend ]   [ Option C: Local Dev ]
Gmail App Password     Resend HTTP API        TEST_MODE=true
smtp.gmail.com:465     api.resend.com/emails  Writes to ./inbox/
        \                     /
         \                   /
          v                 v
     [ siddiquizeerak95@gmail.com ]
```

### 1.1 Live SMTP (Primary Production Path)
- **Host:** `smtp.gmail.com` (configurable via `process.env.SMTP_HOST`)
- **Port:** `465` (SSL/TLS direct connection, or `587` with STARTTLS)
- **Authentication:** Gmail account username (`SMTP_USER`) paired with a Google App Password (`SMTP_PASS`).
- **Recipient:** `RECEIVING_EMAIL` (default: `siddiquizeerak95@gmail.com`).
- **Sender Format:** `"${name} (via ZS STUDIO)" <${SMTP_USER}>`, with `replyTo` set to the visitor's verified email.

### 1.2 Resend API (Secondary Cloud Provider)
- **Endpoint:** `POST https://api.resend.com/emails`
- **Authentication:** Bearer token via `process.env.RESEND_API_KEY`
- **Payload:** JSON document containing `from`, `to`, `reply_to`, `subject`, and the ASCII-armored PGP ciphertext `text`.

### 1.3 Local Test Mode Sink
- **Trigger:** `process.env.TEST_MODE === 'true'`
- **Behavior:** Bypasses live network email dispatch. Encrypted payloads are formatted and written to disk under `inbox/transmission_<timestamp>.txt`.
- **Purpose:** Enables end-to-end testing of form validation, PGP encryption, and offline decryption without live credentials or spamming real inboxes.

---

## 2. Cryptographic Infrastructure (Client-Side E2EE)

| Component | File / Asset | Specification | Responsibility |
| :--- | :--- | :--- | :--- |
| **Public Key File** | `assets/keys/zeerak_public.asc` | 4096-bit RSA OpenPGP Public Key | Fetched dynamically by `contact-e2ee.js` via HTTP GET |
| **In-Memory Fallback** | `contact-e2ee.js` (`ZEERAK_PUBLIC_KEY_FALLBACK`) | Identical 4096-bit ASCII block | Embedded directly in JavaScript to ensure encryption succeeds even if asset fetch fails |
| **Private Key File** | `keys/zeerak_private_KEY_KEEP_SAFE.asc` | 4096-bit RSA OpenPGP Private Key | Stored offline in local environment, gitignored; used exclusively by `decrypt_message.js` |
| **Decryption Sandbox** | `decrypt_message.js` | Node.js `vm.runInNewContext` | Executes `openpgp.min.js` in an isolated execution sandbox to decrypt messages locally |

---

## 3. CDN & Font Integrations

All 14 HTML pages establish preconnections to Google Fonts infrastructure:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

- **Endpoint:** `https://fonts.googleapis.com/css2`
- **Family Distribution:**
  - `Inter`: Weights 300, 400, 500, 600, 700, 800 (display & body)
  - `Space Grotesk`: Weights 400, 500, 600, 700 (headings)
  - `IBM Plex Mono` / `JetBrains Mono`: Weights 400, 500, 600, 700 (telemetry, tags)
  - `Cormorant Garamond`: Weights 400, 500, 600, 700, italic (luxury editorial titles on subpages)

---

## 4. Client Storage & Persistence

| Mechanism | Key / Location | Lifecycle | Purpose |
| :--- | :--- | :--- | :--- |
| **`localStorage`** | `zs_theme` (`"dark"` or `"light"`) | Persistent across browser sessions | Stores visitor's theme preference. Synchronously evaluated in `<head>` inline script on every page to prevent flashing |
| **In-Memory State** | `window.sculptureIntroInstance` | Single session / page life | Holds 3D digital universe camera position, scene progress, and waypoint references |
| **Rate Limit Store** | `server.js` `rateLimitMap` (`Map<string, {count, resetTime}>`) | Process lifetime (cleaned every 10 min) | Tracks client IP submission frequency; allows max 5 requests per 15-minute sliding window |

---

## 5. Third-Party Social & Direct Uplinks

- **Instagram:** Direct link to verified profile `@_siddiqui_._zeerak_` (`https://www.instagram.com/_siddiqui_._zeerak_/`).
- **Direct Voice / Telephony:** Verified telephone action `tel:+919580912686`.
- **Direct Mailto Client:** Fallback mail client dispatch `mailto:zeeraksiddiqui@gmail.com` and `mailto:siddiquizeerak95@gmail.com`.
- **External Code Repositories:** Links to GitHub repositories for open-source case studies and experiments.

