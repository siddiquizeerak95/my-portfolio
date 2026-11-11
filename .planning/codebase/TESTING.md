# Testing & Verification Patterns

Authoritative documentation of testing methodologies, automation scripts, visual regression workflows, and validation commands for the **ZS STUDIO** codebase.

---

## 1. Testing Frameworks & Philosophy

ZS STUDIO utilizes a pragmatic, zero-overhead testing strategy consisting of:
1. **Automated Headless Chrome Console Audits:** Inspecting runtime logs across all 14 HTML pages for zero JavaScript errors and broken asset references.
2. **Visual Regression & Screenshot Pipelines:** Headless Chrome rendering audits at exact responsive viewports.
3. **Cryptographic End-to-End (E2EE) Contact Verification:** Local sandbox testing for OpenPGP client encryption, API submission, and offline private key decryption.

---

## 2. Test Suites & Tooling

### 2.1 Automated Console Error Audit (`verify_console_errors.py`)
- **Engine:** Headless Google Chrome (`chrome.exe`) controlled via Python `subprocess`.
- **Target Matrix:** Audits all 14 project pages:
  - `index.html`
  - `about.html`
  - `projects.html`
  - `skills.html`
  - `blog.html`
  - `contact.html`
  - 3 Blog Posts (`blog-how-i-built-my-portfolio.html`, etc.)
  - 5 Case Studies (`case-study.html`, `case-study-banking.html`, etc.)
- **Execution Command:**
  ```powershell
  python verify_console_errors.py
  ```
- **Verification Rule:** Every page must output `0 console errors`. Any `ERROR:CONSOLE` line flags a build or runtime failure.

### 2.2 Programmatic Screenshot Tool (`take_screenshot.py`)
- **Engine:** Headless Chrome with virtual time budgeting:
  ```powershell
  chrome.exe --headless=new --disable-gpu --hide-scrollbars --window-size=1440,900 --screenshot=output.png --virtual-time-budget=2500 <url>
  ```
- **CLI Usage:**
  ```powershell
  # Default (captures about.html to preview_redesigned_about.png at 1440x900)
  python take_screenshot.py

  # Custom URL, filename, and dimensions
  python take_screenshot.py http://127.0.0.1:8080/projects.html preview_projects.png 1440,900
  python take_screenshot.py http://127.0.0.1:8080/index.html preview_mobile.png 390,844
  ```

### 2.3 End-to-End Cryptographic Contact Verification
Tests the complete security pipeline from browser encryption to offline private-key recovery:

```
[ Step 1: Enable Test Mode ]
  Set TEST_MODE=true in .env

[ Step 2: Start Server ]
  npm start (Runs node server.js on port 8080)

[ Step 3: Transmit Form ]
  Open http://localhost:8080/contact.html
  Fill out Name, Email, Subject, Message -> Click "Transmit Encrypted Message"
  Ciphertext is saved to: inbox/transmission_<timestamp>.txt

[ Step 4: Verify Decryption ]
  node decrypt_message.js inbox/transmission_<timestamp>.txt
  Confirm that decrypted message matches original plain text.
```

---

## 3. Responsive Verification Matrix

Manual and automated verification must cover these standard viewports:

| Device Category | Target Viewport | Critical Focus Areas |
| :--- | :--- | :--- |
| **Desktop Widescreen** | `1440 × 900` | Full 2-column hero, custom cursor, 3D card tilt, horizontal navbar |
| **Standard Laptop** | `1280 × 800` | Header padding, card grid column wrap, typography balance |
| **Tablet Landscape** | `1024 × 768` | Section padding, 3D universe camera distance, blog card deck |
| **Tablet Portrait** | `768 × 1024` | Navigation collapse to hamburger menu, hero portrait stack order |
| **Mobile Standard** | `390 × 844` (iPhone 14) | Drawer menu toggle, full-width buttons, zero horizontal overflow |
| **Mobile Narrow** | `320 × 568` (iPhone SE) | Text wrap on headings, touch target minimums (44px), portrait scale |

---

## 4. Key Verification Commands Reference

```powershell
# 1. Start development server
npm start

# 2. Run console error audit across all 14 pages
python verify_console_errors.py

# 3. Capture desktop screenshot
python take_screenshot.py http://localhost:8080/index.html test_index_desktop.png 1440,900

# 4. Capture mobile screenshot
python take_screenshot.py http://localhost:8080/index.html test_index_mobile.png 390,844

# 5. Decrypt captured contact message
node decrypt_message.js inbox/transmission_<timestamp>.txt
```

