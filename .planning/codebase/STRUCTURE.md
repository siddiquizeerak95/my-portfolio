# Codebase Structure

Authoritative directory layout, file mapping, and architectural boundaries for the **ZS STUDIO** codebase.

---

## 1. Directory Tree Overview

```
ZS STUDIO Repository Root
├── .env                              # Active environment configuration (gitignored)
├── .env.example                      # Configuration template with setup instructions
├── .gitignore                        # Git ignore rules (secrets, scratch, node_modules)
├── package.json                      # Node package manifest (v1.0.0, ES modules)
├── package-lock.json                 # Dependency lockfile
├── server.js                         # Production/development HTTP server & contact API
├── decrypt_message.js                # Offline OpenPGP message decryption CLI
├── DESIGN.md                         # Authoritative master design specification (v10.0)
│
├── [ HTML Documents (14 Pages) ]
│   ├── index.html                    # Homepage (Preloader + 3D Universe + Editorial Hero)
│   ├── about.html                    # Academic journey, philosophy & timeline
│   ├── projects.html                 # Filterable portfolio creations & labs
│   ├── skills.html                   # 4-pillar technical architecture grid
│   ├── blog.html                     # 3D interactive card deck & article archive
│   ├── contact.html                  # Secure communication form with client E2EE
│   ├── blog-how-i-built-my-portfolio.html
│   ├── blog-my-journey-as-a-developer.html
│   ├── blog-why-i-prefer-minimalist-web-design.html
│   ├── case-study.html               # Master Case Study (Modern E-commerce App)
│   ├── case-study-ecommerce.html     # E-commerce App deep-dive
│   ├── case-study-finance.html       # Personal Finance Dashboard case study
│   ├── case-study-banking.html       # Digital Banking Mobile App case study
│   └── case-study-portfolio.html     # Portfolio Architecture case study
│
├── [ Core Stylesheets ]
│   ├── style.css                     # Master stylesheet (9,407 lines): tokens, layout, typography
│   ├── sculpture-intro.css           # 3D digital universe HUD, stage, and animation styles
│   └── blog-3d.css                   # 3D interactive card stack styles for blog.html
│
├── [ Core Client JavaScript ]
│   ├── script.js                     # Main orchestrator: preloader, cursor, audio, tilt, navigation
│   ├── sculpture-intro.js            # Three.js Digital Universe 3D engine (3,070 lines)
│   ├── blog-3d.js                    # GSAP ScrollTrigger 3D card deck engine for blog.html
│   └── contact-e2ee.js               # Client-side OpenPGP form validation & encryption
│
├── assets/                           # Production static assets (62.6 MB total)
│   ├── audio/                        # Interface sound effects (.wav)
│   ├── cosmos/                       # 13 high-resolution celestial textures for Three.js
│   ├── keys/                         # zeerak_public.asc (OpenPGP 4096-bit public key)
│   └── *.svg, *.png, *.jpg           # Portfolio photography, brand SVGs, project diagrams
│
├── vendor/                           # Self-hosted client-side libraries
│   ├── three.min.js                  # Three.js 3D WebGL engine (r128)
│   ├── gsap.min.js                   # GreenSock animation platform
│   ├── ScrollTrigger.min.js          # GSAP scroll interaction plugin
│   └── openpgp.min.js                # OpenPGP.js client-side cryptography
│
├── keys/                             # Local offline cryptographic storage (gitignored)
│   └── zeerak_private_KEY_KEEP_SAFE.asc # 4096-bit RSA private decryption key
│
├── inbox/                            # Local test-mode transmission archive
│   └── transmission_*.txt            # Captured encrypted contact form transmissions
│
├── scratch/                          # Development scripts, audit tools, test captures (gitignored)
├── ZS-Galaxy-Review/                 # Storyboards, comparison GIFs, and visual polish reports
├── _legacy_starter/                  # Archived original starter files
└── .planning/                        # GSD codebase mapping and project documentation
    └── codebase/
        ├── STACK.md
        ├── INTEGRATIONS.md
        ├── ARCHITECTURE.md
        ├── STRUCTURE.md
        ├── CONVENTIONS.md
        ├── TESTING.md
        └── CONCERNS.md
```

---

## 2. Page Hierarchy & Routing

The application functions as a static Multi-Page Application (MPA) where all pages share common structural conventions:

| Route / File | Title | `data-page` | Primary Responsibilities |
| :--- | :--- | :--- | :--- |
| `index.html` | ZS STUDIO — UI/UX Designer & Frontend Dev | `home` | Full preloader, 3D universe opening sequence, 2-column hero, snapshot sections |
| `about.html` | About — Zeerak Siddiqui | `about` | Full educational background (BCA), core values, milestones timeline |
| `projects.html` | Projects & Selected Works | `projects` | Interactive category filters (`ALL`, `FEATURED`, `LABS`), responsive dossier cards |
| `skills.html` | Technical Architecture & Skills | `skills` | 4-pillar architectural breakdown: HTML5, CSS3, JS/ES6+, C Systems Programming |
| `blog.html` | Editorial & Technical Blog | `blog` | GSAP ScrollTrigger 3D rotating card deck + full article repository |
| `contact.html` | Contact & Transmission Interface | `contact` | OpenPGP encrypted contact form, direct phone link, Instagram profile |
| `case-study*.html` (5 pages) | UI/UX Case Studies | `case-study` | Comprehensive UX case studies (Problem, User Research, Wireframes, Final UI) |
| `blog-*.html` (3 pages) | Blog Post Deep Dives | `blog-article` | Full-length technical essays with monospace code blocks and typography |

---

## 3. JavaScript Module Responsibilities

```
+-----------------------------------------------------------------------------------------+
|                                  JAVASCRIPT MODULE MAP                                  |
+-----------------------------------------------------------------------------------------+
| Module               | Runtime     | Main Responsibilities                             |
+----------------------+-------------+---------------------------------------------------+
| script.js            | Browser ESM | • Particle preloader animation loop               |
|                      |             | • Custom dual-ring precision cursor & particle dust|
|                      |             | • Web Audio & WAV interface sound effects         |
|                      |             | • 3D card tilt & specular glare calculations      |
|                      |             | • Global navigation, mobile drawer & active states|
|                      |             | • Theme toggle persistence and synchronization     |
|                      |             | • IntersectionObserver scroll reveals             |
+----------------------+-------------+---------------------------------------------------+
| sculpture-intro.js   | Browser     | • Three.js WebGL scene, camera & lighting setup   |
|                      |             | • Procedural starfield generation                 |
|                      |             | • 6-layer celestial bodies & orbital motion       |
|                      |             | • 9-waypoint scroll camera choreography           |
|                      |             | • Intro dissolution and homepage handoff          |
+----------------------+-------------+---------------------------------------------------+
| blog-3d.js           | Browser     | • GSAP ScrollTrigger card stack pinning           |
|                      |             | • 3D card rotation & z-index cycling              |
|                      |             | • Active category telemetry & counter updates     |
+----------------------+-------------+---------------------------------------------------+
| contact-e2ee.js      | Browser     | • Form field validation & honeypot spam guard     |
|                      |             | • Dynamic public key loading & fallback handling  |
|                      |             | • OpenPGP 4096-bit RSA client encryption          |
|                      |             | • Async fetch transmission to /api/contact        |
+----------------------+-------------+---------------------------------------------------+
| server.js            | Node.js     | • Static file server with custom MIME mapping     |
|                      |             | • In-memory IP rate limiter (5 reqs / 15 min)     |
|                      |             | • Nodemailer SMTP / Resend dispatch               |
|                      |             | • Local test mode filesystem persistence          |
+----------------------+-------------+---------------------------------------------------+
| decrypt_message.js   | Node.js CLI | • Reads private key from keys/ directory          |
|                      |             | • Executes isolated OpenPGP sandbox via vm module |
|                      |             | • Decrypts ASCII armor ciphertext from terminal   |
+----------------------+-------------+---------------------------------------------------+
```

---

## 4. Stylesheet Architecture

- **`style.css` (9,407 lines):** Master monolithic stylesheet containing:
  1. CSS Custom Properties / Design Tokens (`:root` and `[data-theme="light"]`)
  2. CSS Reset & Typography declarations
  3. Header & Navigation styling (Desktop navbar + Mobile drawer)
  4. Hero Section & Portrait frame geometry
  5. Content Sections (About, Skills, Projects, Blog, Contact, Footer)
  6. Subpage styles (About dossier, Projects grid, Skills architecture, Case studies)
  7. Interactive effects (Card tilt, specular glare, custom cursor, magnetic buttons)
  8. Responsive Media Queries (`1200px`, `992px`, `860px`, `768px`, `480px`, `360px`)
- **`sculpture-intro.css` (515 lines):** Isolated CSS rules for the 3D Digital Universe opening stage, holographic HUD panels, telemetry displays, enter buttons, and exit transitions.
- **`blog-3d.css` (320 lines):** Specialized 3D perspective rules (`perspective: 1200px`, `transform-style: preserve-3d`) for the interactive card deck on `blog.html`.

