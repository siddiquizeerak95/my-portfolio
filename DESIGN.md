# DESIGN SPECIFICATION: DARK CINEMATIC MINIMALISM — BLACK & WHITE EDITION
### Authoritative Architecture for ZS Studio — Zeerak Shafique

**Project:** ZS Studio — Zeerak Shafique Personal Portfolio  
**Live Site:** [https://zsstudio.netlify.app/](https://zsstudio.netlify.app/)  
**Role:** Creative Developer & Bachelor of Computer Applications (BCA) Student  
**Status:** Authoritative Master Design Specification (v9.0 Black & White Minimalist Edition)  
**Direction:** Dark Cinematic Minimalism inspired by premium editorial portfolios  

---

## 1. DESIGN PHILOSOPHY & DIRECTION

### 1.1 Core Principles
1. **Editorial Sophistication over Sci-Fi/Gaming Dashboard:** The website must look sophisticated, modern, clean, and professional—not like a gaming interface, cybernetic HUD, or sci-fi dashboard.
2. **Strictly Monochromatic:** Use ONLY black, white, and neutral gray. Zero cyan, blue, gold, yellow, or colorful gradients. Zero neon glows or artificial telemetry badges.
3. **Generous Whitespace & Balance:** Large confident headings, readable body paragraphs, clean rectangular geometry, and subtle borders.
4. **Natural Grayscale Imagery:** Monochromatic portrait photography with natural tone curves rather than artificial glowing borders.
5. **Immediate Access & Purposeful Motion:** Zero distracting loading preloader screens that delay content. Gentle fade-in scroll reveals, smooth link transitions, and hardware-accelerated micro-interactions.

### 1.2 Truthfulness & Content Authenticity
- Authentic academic context: Undergraduate BCA student studying computer applications, low-level programming in C, and modern web standards.
- Real verified contact: Direct phone (`+91 9580912686`), Instagram (`@_siddiqui_._zeerak_`), and verified mailto client dispatch.
- Zero fabricated client logos, invented years of experience, or artificial proficiency bars.

---

## 2. COLOR TOKEN SYSTEM

| Token Name | Exact HEX | Architectural Purpose |
| :--- | :--- | :--- |
| `--bg-main` | `#080808` | Primary canvas backdrop / dark cinematic field |
| `--bg-section` | `#0D0D0D` | Alternating section backgrounds, elevated cards, and footer |
| `--bg-surface` | `#121212` | Elevated cards, project dossiers, input fields |
| `--bg-surface-hover` | `#1A1A1A` | Card hover state and interactive element highlight |
| `--text-primary` | `#F5F5F5` | Primary text: crisp headlines, brand mark, button text |
| `--text-secondary` | `#929292` | Secondary text: narrative prose, subtitles, metadata |
| `--text-muted` | `#666666` | Subtle timestamps, indices, breadcrumb separators |
| `--border-subtle` | `#252525` | Hairline structural borders, section dividers, card frames |
| `--border-hover` | `#444444` | Hover state for interactive cards and secondary buttons |
| `--border-focus` | `#F5F5F5` | Accessible keyboard focus ring |
| `--btn-primary-bg` | `#F5F5F5` | Solid primary button background |
| `--btn-primary-text` | `#080808` | High-contrast dark text on primary button |
| `--btn-primary-hover` | `#E0E0E0` | Subtle brightness shift on primary button hover |
| `--btn-secondary-bg` | `transparent` | Secondary button transparent surface |
| `--btn-secondary-border` | `#252525` | Subtle hairline boundary on secondary button |
| `--btn-secondary-text` | `#F5F5F5` | Crisp white text on secondary button |

---

## 3. TYPOGRAPHY SYSTEM

- **Display Headlines:** `Space Grotesk` (weights 600, 700). Confident, large, architectural editorial headings.
- **Body & Prose:** `Inter` (weights 400, 500, 600). Highly readable, clean sans-serif body copy with 1.65–1.75 line height.
- **Metadata & Indices:** `JetBrains Mono` (weights 400, 500). Minimal monospace for numbering (`01`, `02`) and breadcrumbs in neutral gray `#929292`.

---

## 4. COMPONENT & SECTION SPECIFICATIONS

### 4.1 Slim Reference Header & Theme System (All 5 Pages)
- **Left Side:**
  - Dedicated reserved empty slot (`44×44px`) reserved for future custom logo.
  - Zero placeholder text, initials, dummy icons, or images.
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
  - Authentic profile photograph (`Profile Pic.jpg`) with natural facial proportions.
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
| **Two-Column Hero** | CREATIVE DEVELOPER label, ZEERAK SHAFIQUE headline, supporting text, View My Work & Contact Me buttons, monochrome portrait. | **VERIFIED** |
| **Natural Portrait** | Grayscale portrait with natural contrast and subtle border `#252525`; zero neon glow. | **VERIFIED** |
| **Subpages Redesign** | About, Projects, Skills, Contact all redesigned using black and white minimalism. | **VERIFIED** |
| **No Intrusive Preloader** | Decorative loading preloader removed for immediate content access. | **VERIFIED** |
| **No Three.js 3D Clutter** | Unnecessary 3D gyroscopes and kinetic sculpture removed. | **VERIFIED** |
| **Preserved Functionality** | Real phone, real Instagram, working project links, multipage routes preserved. | **VERIFIED** |
| **Responsive Design** | Tested on desktop (1440px), tablet (1024px & 768px), and mobile (390px & 320px); zero overflow. | **VERIFIED** |
