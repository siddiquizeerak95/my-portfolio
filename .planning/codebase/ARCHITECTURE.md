# System Architecture

Authoritative technical breakdown of the architecture, component hierarchy, rendering pipeline, and lifecycle flows of **ZS STUDIO**.

---

## 1. High-Level Architecture Overview

ZS STUDIO employs a high-performance **Multi-Page Application (MPA)** architecture designed around zero-framework vanilla web standards, client-side WebGL/Canvas graphics pipelines, and a lightweight Node.js cryptographic micro-backend.

```
+-----------------------------------------------------------------------------------------+
|                                    CLIENT BROWSER                                       |
|                                                                                         |
|  +--------------------+   +-----------------------+   +------------------------------+  |
|  |   Zero-Flash Head  |-->|  2D Canvas Preloader  |-->|  3D WebGL Digital Universe   |  |
|  | Theme Initializer  |   | (PreloaderParticleSys)|   |  (DigitalUniverse / Three.js)|  |
|  +--------------------+   +-----------------------+   +------------------------------+  |
|                                                                      |                  |
|                                       [ Scroll Threshold >= 88% OR "Enter" Click ]      |
|                                                                      v                  |
|  +-----------------------------------------------------------------------------------+  |
|  |                    INTERACTIVE EDITORIAL HOMEPAGE & SUBPAGES                      |  |
|  |  * Two-Column Hero (Monochrome Portrait + Editorial Typography)                   |  |
|  |  * Hybrid 3D Perspective Tilt with Dynamic Specular Glare                         |  |
|  |  * Precision Custom Cursor & Canvas Particle Dust                                 |  |
|  |  * Audio Feedback Engine (Web Audio API + Mixkit WAV)                             |  |
|  |  * IntersectionObserver Scroll Reveals & Category Filtering                      |  |
|  |  * Client-Side E2EE Contact Encryption (OpenPGP.js 4096-bit RSA)                 |  |
|  +-----------------------------------------------------------------------------------+  |
+-----------------------------------------------------------------------------------------+
                                          |
                                    HTTP POST (Encrypted Ciphertext)
                                          |
                                          v
+-----------------------------------------------------------------------------------------+
|                                  NODE.JS BACKEND                                        |
|                                                                                         |
|  [ server.js ]                                                                          |
|    |-- Static Asset Server (Custom MIME dictionary, security headers)                   |
|    |-- Rate Limiting (5 requests / 15 minutes per IP sliding window)                     |
|    |-- Honeypot Anti-Spam Field Verification                                            |
|    |-- Dispatcher: Gmail SMTP / Resend API / Local Test Mode Disk Store                 |
|                                                                                         |
|  [ decrypt_message.js ]                                                                 |
|    |-- Offline Local Decryption Tool (Node.js vm sandbox + private key)                 |
+-----------------------------------------------------------------------------------------+
```

---

## 2. Homepage Execution Lifecycle (`index.html`)

The entry experience operates across five sequential states:

```
[ State 0: Bootstrap ]
  └─ Inline <script> checks localStorage('zs_theme') -> Sets data-theme="dark" immediately.
       │
[ State 1: Particle Preloader ]
  ├─ Canvas 2D engine initializes in #preloader-particle-canvas.
  ├─ Tracks document.readyState, Google Fonts readiness, and critical image assets.
  └─ Smooth progress bar counts 0% -> 100% with telemetry updates.
       │
[ State 2: Digital Universe 3D Awakening ]
  ├─ Preloader fades out (display: none).
  ├─ Three.js initializes #sculpture-canvas full-screen WebGL viewport.
  ├─ Builds 6-layer celestial scene (Galaxy, Nebula, Starfields, Gas Giant, Asteroids, Singularity).
  └─ Visitor scrolls through 9 calibrated waypoints controlling camera position & roll.
       │
[ State 3: Transition & Dissolution ]
  ├─ Trigger: Scroll progress p >= 0.88 OR user clicks #btn-enter-website.
  ├─ CSS class .dissolved applied to #sculpture-intro-stage (opacity 0, pointer-events none).
  └─ Native body scroll unlocked; main content container revealed.
       │
[ State 4: Interactive Editorial Portfolio ]
  ├─ Header, Hero, About, Skills, Projects, Journey, Blog, and Contact sections mount.
  ├─ GSAP ScrollTrigger and IntersectionObservers bind reveal transitions.
  └─ Card tilt, audio events, and cursor engines begin active frame loop.
```

---

## 3. Rendering Pipelines & Subsystems

### 3.1 2D Canvas Preloader (`PreloaderParticleSystem`)
- **File:** `script.js` (lines 16–285)
- **Technology:** HTML5 Canvas 2D Context with device pixel ratio (DPR) scaling (capped at `2.0`).
- **Dynamics:** Polar coordinate particle seeding (`r`, `theta`) with sinusoidal wave oscillation (`wavePhase`), simulating gentle orbital dust around the central ZS logo.
- **Accessibility:** Detects `prefers-reduced-motion` and skips animation loop to display static progress state.

### 3.2 3D Digital Universe Engine (`DigitalUniverse`)
- **File:** `sculpture-intro.js` (3,070 lines)
- **Technology:** Three.js WebGL Renderer with custom geometries, procedural shaders, and photographic textures (`assets/cosmos/`).
- **Layered Multi-Plane Hierarchy:**
  1. *Layer 1 (Z = -1400 AU):* 4-Arm Spiral Galaxy disc with photorealistic dust map and central bulge.
  2. *Layer 2 (Z = -900 AU):* Volumetric H-Alpha nebula clouds and dark Bok globules.
  3. *Layer 3 (Z = -550 AU):* 3-Strata multi-spectral starfields (blue giants, stellar white, deep red dwarfs).
  4. *Layer 4 (Z = -345 AU):* Kepler ringed gas giant with polar shadows and sunward illumination limb.
  5. *Layer 5 (Z = -140 AU):* 3D faceted Chondrite asteroid belt with interactive boulder meshes.
  6. *Layer 6 (Z = -10 AU):* High-speed micrometeorite foreground dust.
  7. *Finale:* Gravitational Singularity with accretion disc and gravitational lens distortion.
- **Navigation Waypoints:** 9 spatial waypoints interpolating camera coordinates `[x, y, z]`, look-at target `[tx, ty, tz]`, and camera roll angle based on normalized scroll progress `p` (0.00 to 1.00).

### 3.3 Audio Engine (`PortfolioSoundSystem`)
- **File:** `script.js` (lines 1500–1740)
- **Architecture:** Dual-tier audio pipeline:
  1. *Primary Tier:* Web Audio API `AudioContext` with procedurally synthesized audio nodes (sine, triangle, and bandpass filtered oscillators).
  2. *Asset Tier:* Preloaded HTMLAudioElement (`assets/audio/mixkit-sci-fi-interface-robot-click-901.wav`).
- **Events:** Subtle UI ticks on navigation clicks, theme toggle transitions, filter selection, and modal openings. Master audio toggle stored in session state.

### 3.4 Hybrid 3D Perspective & Card Tilt
- **File:** `script.js` (`initCardTilt`, `initHeroPerspective`)
- **Math:** Calculates mouse offset from card bounding rect `(x - center_x) / (width / 2)` and maps to subtle rotation matrix (clamped to `±4.5°`).
- **Specular Glare:** Updates CSS custom properties `--glare-x` and `--glare-y` driving dynamic radial gradient lighting highlights across card surfaces.

---

## 4. Security Architecture

```
[ Visitor Contact Form ]
        │
   [ Validation ] (Name, valid email format, honeypot spam check, message length)
        │
   [ OpenPGP Client Encryption ] (4096-bit RSA asymmetric public key)
        │
   [ Transmission Payload ] -> { name, email, subject, encrypted_message }
        │
        v
[ POST /api/contact ]
        │
   [ Rate Limiter ] (Max 5 requests per 15 minutes per client IP)
        │
   [ Security Headers ] (X-Content-Type-Options: nosniff, X-Frame-Options: SAMEORIGIN)
        │
   [ Dispatch Path ] -> (Live SMTP / Resend API / Local Test Mode inbox/)
```

- **Client Privacy:** The plain text of the message is never transmitted over the wire in cleartext; encryption occurs in browser memory before network transmission.
- **Server Safety:** The server cannot read the contents of the message; it acts as a blind relay.
- **Offline Decryption:** The private key remains strictly offline on Zeerak's local development machine.

