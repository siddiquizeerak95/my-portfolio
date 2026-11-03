# DESIGN SPECIFICATION: HYBRID 3D PERSPECTIVE & SWISS MINIMALISM
### Authoritative Architecture for ZEERAK — Zeerak Siddiqui

**Project:** ZS Studio — Zeerak Siddiqui Personal Portfolio  
**Live Site:** [https://zsstudio.netlify.app/](https://zsstudio.netlify.app/)  
**Role:** Creative Developer & Bachelor of Computer Applications (BCA) Student  
**Status:** Authoritative Master Design Specification (v10.0 Hybrid 3D Perspective Edition)  
**Direction:** Hybrid 3D Perspective + Swiss Minimalism + Elegant Luxury Typography + Cinematic Monochrome  

---

## 1. DESIGN PHILOSOPHY & DIRECTION

### 1.1 Core Principles
1. **Editorial Sophistication over Sci-Fi/Gaming Dashboard:** The website must look sophisticated, modern, clean, and professional—not like a gaming interface, cybernetic HUD, or sci-fi dashboard.
2. **Strictly Monochromatic:** Use ONLY black, white, and neutral gray. Zero cyan, blue, gold, yellow, or colorful gradients. Zero neon glows or artificial telemetry badges.
3. **Generous Whitespace & Balance:** Large confident headings, readable body paragraphs, clean rectangular geometry, and subtle borders.
4. **Natural Grayscale Imagery:** Monochromatic portrait photography with natural tone curves rather than artificial glowing borders.
5. **Cinematic Particle Loading Screen & Purposeful Motion:** A signature full-screen Canvas 2D particle loading screen (`#050505`) with gentle orbital monochrome dust, centered ZS logo, ZEERAK wordmark, "LOADING EXPERIENCE" telemetry, and real asset tracking (DOM, fonts, critical images) that transitions seamlessly into the homepage hero. Gentle fade-in scroll reveals, restrained 3D card tilt with specular glare, and desktop hero mouse parallax.

### 1.2 Truthfulness & Content Authenticity
- Authentic academic context: Undergraduate BCA student studying computer applications, low-level programming in C, and modern web standards.
- Real verified contact: Direct phone (`+91 9580912686`), Instagram (`@_siddiqui_._zeerak_`), and verified mailto client dispatch.
- Zero fabricated client logos, invented years of experience, or artificial proficiency bars.

---

## 2. COLOR TOKEN SYSTEM & HYBRID 3D MATRICES

### 2.1 Dark Mode Tokens (Primary Atmospheric Canvas)
| Token Name | Exact HEX | Architectural Purpose |
| :--- | :--- | :--- |
| `--bg-main` | `#080808` | Primary canvas backdrop / dark cinematic space |
| `--bg-secondary` | `#111111` | Secondary backgrounds, elevated cards, and footer |
| `--bg-surface` | `#111111` | Elevated cards, project dossiers, input fields |
| `--bg-surface-hover` | `#1C1C1C` | Card hover state and interactive highlight |
| `--text-primary` | `#F5F5F5` | Primary text: crisp headlines, brand mark, buttons |
| `--text-secondary` | `#A0A0A0` | Secondary text: narrative prose, subtitles, tags |
| `--text-muted` | `#707070` | Subtle timestamps, telemetry, breadcrumb separators |
| `--border-subtle` | `#292929` | Hairline structural borders, section dividers, card frames |
| `--border-hover` | `#444444` | Hover state for interactive cards and secondary buttons |
| `--border-focus` | `#F5F5F5` | Accessible keyboard focus ring |
| `--btn-bg` | `#F5F5F5` | High-contrast primary button fill |
| `--btn-text` | `#080808` | Dark button typography |

### 2.2 Light Mode Tokens (Clean Swiss Minimalist Paper)
| Token Name | Exact HEX | Architectural Purpose |
| :--- | :--- | :--- |
| `--bg-main` | `#FFFFFF` | Primary white paper canvas |
| `--bg-secondary` | `#F5F5F5` | Secondary backgrounds and elevated surfaces |
| `--bg-surface` | `#FFFFFF` | Crisp white cards on secondary ground |
| `--text-primary` | `#111111` | High-contrast charcoal/black typography |
| `--text-secondary` | `#666666` | Secondary body text and subtitles |
| `--border-subtle` | `#E5E5E5` | Minimal light hairline dividers |
| `--btn-bg` | `#111111` | Solid dark button fill |
| `--btn-text` | `#FFFFFF` | Crisp white button typography |

### 2.3 Hybrid 3D Spatial Properties
- `--perspective-camera: 1100px;` (Human eye optical focal length)
- `--card-shadow-3d: 0 16px 36px -10px rgba(0, 0, 0, 0.75), 0 2px 10px rgba(0, 0, 0, 0.35);`
- Smooth dynamic specular glare reflection using radial gradient tracking cursor position (`--glare-x`, `--glare-y`).
- Internal 3D depth layering with distinct `translateZ` offsets for badges (`16px`), titles (`12px`), and action buttons (`20px`).

## 3. TYPOGRAPHY SYSTEM (ELEGANT LUXURY & SWISS MINIMALISM)

- **Luxury Editorial Headings:** `Cormorant Garamond` (weights 400, 500, 600, 700, and italic). High-contrast, razor-sharp serif used selectively for important headings, hero name focal point ("Zeerak Siddiqui"), page titles, and editorial blockquotes.
- **Swiss Sans-Serif Body & UI:** `Inter` (weights 300, 400, 500, 600, 700). Clean Swiss neo-grotesque sans-serif for body prose, lead lines ("Hi, I'm"), card descriptions, buttons, and navigation with 1.65–1.8 line height and optimal legibility.
- **Architectural Monospace:** `IBM Plex Mono` (weights 400, 500, 600). Rationalist monospace for numbering, section indices (`01`, `02`), technical focus tags, telemetry chips, and metadata.
- **Custom ZEERAK Wordmark:** `Inter` uppercase with refined Swiss tracking (`letter-spacing: 0.22em`), semibold weight, optical alignment, and restrained hover transition.
- **Custom ZS Monogram:** Interlocking geometric vector monogram (`zs-monogram.svg`) based on 45° Swiss diagonal weave, uniform stroke geometry, and central focal axis dot.

---

## 4. COMPONENT & SECTION SPECIFICATIONS

### 4.1 Slim Reference Header & Theme System (All 9 Pages)
- **Left Side:**
  - **ZS Logo Brand Mark:** Existing high-resolution ZS logo image (`New fav icon.png`), 50×50px on desktop with `object-fit: contain` and 1:1 aspect ratio.
  - **Subtle Architectural Divider:** Hairline vertical divider (`1px × 22px`, `var(--border-subtle)`).
  - **ZEERAK Wordmark:** Elegant Swiss uppercase lettering with `letter-spacing: 0.22em`, semibold weight, linked to the homepage.
  - **Theme Adaptation:** Seamless Dark Mode blending via `mix-blend-mode: screen;` (pure black background becomes transparent, white/silver emblem renders crisp and sharp); Light Mode adaptation via `filter: invert(1); mix-blend-mode: multiply;` (turns white background transparent and emblem deep black).
  - **Responsive Scaling:** Reduced to `40×40px` on mobile (<860px) and `36×36px` on narrow mobile (<420px).
- **Center Navigation:**
  - Horizontal row of navigation links across valid project routes:
    1. **Home** (`index.html`)
    2. **About** (`about.html`)
    3. **Projects** (`projects.html`)
    4. **Skills** (`skills.html`)
    5. **Contact** (`contact.html`)
  - **Active State Highlight:** Small rounded light-colored pill highlight (`background: rgba(255, 255, 255, 0.12)`, `border-radius: 6px`, color `#FFFFFF`, font-weight 500).
  - Inactive links: `#929292` (`rgba(255, 255, 255, 0.65)`), hover state: `#FFFFFF` (`background: rgba(255, 255, 255, 0.06)`).
- **Right-Side Controls:**
  - **Bidirectional Theme Toggle Button:** `#theme-toggle` with a small circular indicator dot (`.theme-indicator-dot`) and clean SVG moon icon (in dark mode) / SVG sun icon (in light mode).
  - Works in both directions immediately, persists preference in `localStorage`, and applies with zero flash via inline `<head>` script.
  - Light mode palette: `#FAFAFA` canvas, `#FFFFFF` cards, `#0A0A0A` text, `#E0E0E0` borders, `#0A0A0A` solid buttons.
- **Header Dimensions & Visual Style:**
  - Slim height: `58px` (`min-height: 58px`).
  - Dark navy/black translucent background: `rgba(9, 13, 20, 0.85)` with `backdrop-filter: blur(14px)`.
  - Subtle bottom border: `1px solid rgba(255, 255, 255, 0.08)`.
  - Sticky at top: `position: sticky; top: 0; z-index: 1000;`.
- **Responsive Mobile Navigation:**
  - Accessible hamburger button (`.mobile-toggle`) displayed on viewports < 860px.
  - Clean slide-out drawer overlay with identical 5 links and direct contact actions.

### 4.2 Hero Section (`index.html`) — Minimalist B&W Editorial Architecture
- **Layout:** Sophisticated two-column split layout directly below the header; vertically centered and responsive.
- **Background & Lighting:**
  - Dark Mode: `#080808` canvas with subtle radial grayscale spotlight behind the portrait (`rgba(255, 255, 255, 0.035)`), `#292929` bottom border.
  - Light Mode: `#FFFFFF` canvas with subtle neutral radial spotlight (`rgba(0, 0, 0, 0.025)`), `#E5E7EB` bottom border.
  - Strictly monochromatic; zero gold, cyan, blue, neon, city skylines, or 3D particles.
- **Left Column:**
  1. *Small uppercase label:* `CREATIVE DEVELOPER` (`12px`, letter-spacing `2.5px`, color `var(--hero-text-secondary)`).
  2. *Large confident heading:* `Hi, I'm <span class="hero-name-glow">Zeerak Siddiqui</span>` (modern bold display typography, `clamp(2.25rem, 5vw, 4.25rem)`, color `var(--hero-text-primary)` with subtle crisp contrast on the name, wrapping naturally without clipping).
  3. *Supporting description:* `"I build clean, modern digital experiences with thoughtful design and code."` (color `var(--hero-text-secondary)`, line-height `1.7`, max-width `520px`).
  4. *Two aligned call-to-action buttons:*
     - **Primary:** `View My Work →` (Dark: `#F5F5F5` bg, `#080808` text; Light: `#0A0A0A` bg, `#FFFFFF` text; `border-radius: 4px`, links to `projects.html`).
     - **Secondary:** `Contact Me` (transparent background, subtle `1px` border, smooth hover transition, links to `contact.html`).
- **Right Column:**
  - Authentic profile photograph (`new%20image.jpeg`) with natural facial proportions.
  - Large circular frame: desktop size `clamp(320px, 26vw, 360px)`, tablet `clamp(280px, 30vw, 320px)`, mobile `clamp(190px, 48vw, 220px)`.
  - Tasteful black-and-white conversion: `filter: grayscale(100%) contrast(1.06) brightness(0.96);`.
  - Thin subtle circular border (`var(--hero-portrait-border)`).
  - Soft white rim lighting / restrained grayscale halo behind portrait via `::before` radial halo.
  - Gentle micro-animation: subtle float `@keyframes heroPortraitFloat` (6s ease-in-out), fully disabled under `prefers-reduced-motion`.
- **Mobile Responsive Layout:**
  - Clean vertical stack with portrait above text (`order: -1`).
  - Heading and greeting remain fully visible and naturally wrap without clipping.
  - Full-width tappable CTA buttons with comfortable touch targets.
  - Zero horizontal overflow.

### 4.3 About Section
- Clean narrative on academic journey, systems programming in C, and modern full-stack web engineering.
- Clean rectangular metadata tags (`#0D0D0D`, `1px solid #252525`, `#929292` text).
- Link to full `about.html`.

### 4.4 Skills Section
- Clean architectural grid with subtle borders `#252525` and dark background `#0D0D0D`.
- Pillars: HTML5 Semantic Systems, CSS3 Architecture & Layout, JavaScript (ES6+) & Modern Web, C Programming & Systems Core.

### 4.5 Projects Section
- Clean rectangular cards with monochrome previews, concise descriptions, and working links (`View Project`, `GitHub Code`).

### 4.6 Contact Section & Footer
- Strong headline: `HAVE AN IDEA? LET'S BUILD IT.`
- Verified phone: `+91 9580912686` (`tel:+919580912686`).
- Verified Instagram: `@_siddiqui_._zeerak_`.
- Footer with thin divider `1px solid #252525`, ZS logo, copyright, navigation links, and real-time IST clock.

---

## 5. SUBPAGE CONSISTENCY (ABOUT, PROJECTS, SKILLS, CONTACT)

All 4 dedicated subpages adhere to the identical monochromatic design system:
- `about.html`: Clean editorial dossier with education timeline and technical philosophy.
- `projects.html`: Interactive category filters (`ALL CREATIONS`, `ACTIVE EXPERIENCES`, `UPCOMING LABS`) with grayscale preview cards and working links.
- `skills.html`: Clean 4-pillar technical architecture grid with low-level to high-level duality.
- `contact.html`: Clean transmission form with real-time validation and direct voice/social links.

---

## 6. VERIFICATION CHECKLIST

| Verification Item | Specification Standard | Status |
| :--- | :--- | :--- |
| **Monochrome Palette** | `#080808` main, `#0D0D0D` section, `#F5F5F5` text, `#929292` secondary, `#252525` borders. | **VERIFIED** |
| **No Colorful Accents** | All cyan, blue, gold, yellow, and colorful gradients removed. | **VERIFIED** |
| **Clean Minimal Header** | ZS logo, brand ZEERAK, links: Home, About, Projects, Skills, Contact, thin border `#252525`. | **VERIFIED** |
| **Two-Column Hero** | CREATIVE DEVELOPER label, ZEERAK SIDDIQUI headline, supporting text, View My Work & Contact Me buttons, monochrome portrait. | **VERIFIED** |
| **Natural Portrait** | Grayscale portrait with natural contrast and subtle border `#252525`; zero neon glow. | **VERIFIED** |
| **Subpages Redesign** | About, Projects, Skills, Contact all redesigned using black and white minimalism. | **VERIFIED** |
| **Particle Loading Screen** | Canvas 2D orbital particle preloader with centered ZS logo, ZEERAK wordmark, LOADING EXPERIENCE subtitle, real progress gauge, and 2-step transition. | **VERIFIED** |
| **Default Dark Theme** | Unconditional `#080808` Dark Mode for first-time visitors; working bidirectional toggle + persistent localStorage. | **VERIFIED** |
| **Soft White Radial Backlight** | Luminous white radial backlight blooming behind head & shoulders in portrait frame. | **VERIFIED** |
| **Universal Name Accuracy** | All 9 pages, metadata, copy, titles, and footer corrected to "Zeerak Siddiqui". | **VERIFIED** |
| **Harmonized 6 Sections** | About, Skills, Projects, Developer Journey, Blog, and Contact sharing identical Swiss Minimalist tokens and hairline borders. | **VERIFIED** |
| **Subtle 3D Perspective & Motion** | Restrained ±4.5° card perspective tilt, dynamic specular glare, hero spatial tracking, and IntersectionObserver scroll reveals. | **VERIFIED** |
| **Preserved Functionality** | Real phone, real Instagram, working project links, multipage routes preserved. | **VERIFIED** |
| **Responsive Design** | Tested on desktop (1440px), tablet (1024px & 768px), and mobile (390px & 320px); zero overflow. | **VERIFIED** |
