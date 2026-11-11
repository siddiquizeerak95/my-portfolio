# Technology Stack

Authoritative reference for the technologies, runtimes, dependencies, and tooling that power the **ZS STUDIO** portfolio codebase.

---

## 1. Core Runtimes & Platforms

| Layer | Technology | Version / Standard | Purpose |
| :--- | :--- | :--- | :--- |
| **Client Runtime** | Modern Web Browsers | HTML5 / ES2022 / WebGL 1.0+ / Web Audio API | End-user presentation, interactive 3D rendering, audio feedback, and client-side encryption |
| **Server Runtime** | Node.js | `>= 18.0.0` (ES Modules `type: "module"`) | Local static file serving, E2EE contact API endpoint, and offline decryption tooling |
| **Scripting & Tooling** | Python | `3.9+` (Windows native) | Headless Chrome automated testing, console error audits, and visual screenshot pipelines |
| **Deployment Target** | Netlify | Static Hosting & CDN | Live deployment at [https://zsstudio.netlify.app/](https://zsstudio.netlify.app/) |

---

## 2. Frontend Technologies

### 2.1 Markup & Presentation
- **Semantic HTML5:** 14 standalone HTML documents with accessible landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<aside>`, `<footer>`), ARIA attributes, skip-navigation links, and Open Graph metadata.
- **CSS3 Architecture:** Custom Property (`--token`) design token system, CSS Grid, Flexbox, hardware-accelerated 3D transforms (`preserve-3d`, `perspective`, `translateZ`, `matrix3d`), and container queries.
  - Zero CSS frameworks (No Tailwind, Bootstrap, or Sass); pure vanilla CSS.
  - Dark mode as default with instant `data-theme` initialization to prevent FOUC (Flash of Unstyled Content).

### 2.2 Client-Side JavaScript
- **Vanilla ES6+ Modules:** `script.js` loaded via `<script type="module">` for modern scoping and dependency management.
- **Subsystem Architecture:** Object-Oriented and Class-based subsystems (`PreloaderParticleSystem`, `PortfolioSoundSystem`, `DigitalUniverse`, `Particle`).
- **Zero Heavy UI Frameworks:** No React, Vue, or Angular; all DOM operations use standard Web APIs (`IntersectionObserver`, `requestAnimationFrame`, `ResizeObserver`, `EventTarget`).

### 2.3 Vendor Libraries (Self-Hosted in `vendor/`)
| Library | Version / Build | Location | Purpose |
| :--- | :--- | :--- | :--- |
| **Three.js** | r128 (minified) | `vendor/three.min.js` | WebGL 3D rendering for the Digital Universe opening experience (`sculpture-intro.js`) |
| **GSAP** | 3.x (minified) | `vendor/gsap.min.js` | High-precision timeline orchestration and card motion |
| **ScrollTrigger** | 3.x (minified) | `vendor/ScrollTrigger.min.js` | Scroll-bound animations, 3D blog deck progression (`blog-3d.js`), and parallax effects |
| **OpenPGP.js** | 5.x (minified) | `vendor/openpgp.min.js` | 4096-bit RSA asymmetric encryption inside the visitor's browser (`contact-e2ee.js`) |

---

## 3. Backend Technologies & Dependencies

Defined in `package.json` (`zs-studio-portfolio` v1.0.0):

```json
{
  "name": "zs-studio-portfolio",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "start": "node server.js",
    "decrypt": "node decrypt_message.js"
  },
  "dependencies": {
    "dotenv": "^18.0.9",
    "nodemailer": "^10.3.1"
  }
}
```

### 3.1 Server Modules
- **`server.js`:** Native Node.js `http` module server (no Express or heavy framework required).
  - Handles static file resolution with custom MIME type dictionary (covering `.html`, `.css`, `.js`, `.json`, `.bin`, `.asc`, `.wav`, images).
  - Implements `POST /api/contact` receiver with rate limiting (5 reqs / 15 min sliding window) and honeypot validation.
  - Transports encrypted payloads via Nodemailer (Gmail SMTP) or Resend API, with local fallback (`TEST_MODE=true`).
- **`decrypt_message.js`:** CLI offline decryption utility using Node's `vm` sandbox to execute `vendor/openpgp.min.js` with the private key from `keys/`.

---

## 4. Typography & Assets Stack

### 4.1 Typography (Curated Google Fonts)
- **Cormorant Garamond:** Luxury editorial serif for hero titles, section headings, and blockquotes.
- **Inter:** Swiss neo-grotesque sans-serif for UI, navigation, body copy, and primary action buttons.
- **Space Grotesk:** Display headlines and technological headings.
- **IBM Plex Mono / JetBrains Mono:** Monospace font for telemetry, timestamps, index tags (`01`, `02`), and metadata badges.

### 4.2 Asset Ecosystem
- **Vector Icons & Marks:** Custom SVG assets (`zs-monogram.svg`, `paper-plane.svg`, feather-style inline SVGs).
- **Astrophotography Textures:** 13 photographic celestial textures in `assets/cosmos/` for Three.js sphere mappings, accretion discs, and nebula fields.
- **Audio Assets:** Waveform audio feedback (`assets/audio/mixkit-sci-fi-interface-robot-click-901.wav`) with synthesized Web Audio API fallbacks.

