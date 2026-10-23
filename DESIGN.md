# DESIGN SPECIFICATION: OBSIDIAN GOLD — THE DIGITAL ATELIER
### Creative Direction, Architectural Blueprint & High-Craft Interaction System
**Project:** Zeerak Shafique — Personal Luxury Creative Developer Portfolio  
**Role:** Bachelor of Computer Applications (BCA) Student & Aspiring Creative Developer  
**Status:** Authoritative Design Specification (v3.0 Master Redesign)  
**Brand Direction:** OBSIDIAN GOLD — The Digital Atelier  
**Author:** Creative Director, Senior UI/UX Designer & 3D Web Architect  

---

## 1. BRAND IDENTITY & CREATIVE CONCEPT

### 1.1 Project Identity & Core Narrative
- **Name:** Zeerak Shafique
- **Professional Stance:** BCA Student / Aspiring Creative Developer
- **Brand Identity Concept:** **OBSIDIAN GOLD — The Digital Atelier**
- **Core Vision:** The digital atelier is a private, architectural sanctuary where mathematical computation meets luxury editorial craftsmanship. Rather than presenting as an amateur junior developer with neon game aesthetics or generic corporate cards, Zeerak’s presence is established as an artisan of code—disciplined in the rigors of C systems programming and passionate about high-fidelity, spatial web experiences.
- **Narrative Resonance:** Honest, academic, and technologically refined. No fabricated accolades, no fake client lists. Authentic pride in computer science fundamentals, semantic web craft, and sculptural digital spaces.

### 1.2 Creative Direction & Atmospheric Pillars
1. **The Private Digital Atelier:** A high-end editorial environment characterized by deep obsidian stone (`#080808`), warm textured surfaces (`#101010`, `#171614`), and fine architectural hairline dividers (`#302A20`).
2. **Restrained Metallic Gold:** Strategic Champagne Gold (`#D6B46A`) and Muted Antique Gold (`#9D7B3C`) utilized strictly as typographic accents, active states, precision monograms, and warm volumetric light rays. Zero cheap yellow gradients, zero garish glitter.
3. **Haute Horlogerie / Editorial Precision:** Monospaced technical telemetry, Roman numerals, bespoke crop lines, and curated negative space inspired by luxury horology and architectural monographs.
4. **Sculptural Spatial 3D:** An interactive 3D centerpiece featuring brushed dark obsidian and champagne-gold geometric lattice forms reacting smoothly to cursor parallax and device orientation.

---

## 2. VISUAL REFERENCES & INSPIRATION PRINCIPLES

```
+-----------------------------------------------------------------------------------------+
|                               OBSIDIAN GOLD DESIGN PILLARS                              |
+-----------------------------------------------------------------------------------------+
| 1. ARCHITECTURAL RESTRAINT | Vast negative space; razor-thin hairline borders (#302A20);|
|                            | asymmetrical editorial grid compositions.                  |
| 2. STRATEGIC METALLIC CRAFT| Gold is a precious accent, not a background wash. Applied  |
|                            | to emblems, key monograms, and subtle light reflections.   |
| 3. AUTHENTIC DISCIPLINE    | Genuine BCA student focus: HTML5, CSS3, JS (ES6+), and C.  |
|                            | Absolute transparency; zero inflated credentials.          |
| 4. EDITORIAL TYPOGRAPHY    | Cormorant Garamond display serif paired with crisp Manrope |
|                            | sans-serif and clinical JetBrains Mono technical metadata. |
| 5. HARDWARE VELOCITY       | 60 FPS performance, lightweight Three.js & CSS 3D fallback,|
|                            | clean vanilla multipage architecture, zero framework bloat.|
+-----------------------------------------------------------------------------------------+
```

---

## 3. EXACT COLOR TOKEN SYSTEM

The color architecture is built around calibrated HSL/HEX values ensuring WCAG 2.1 AA/AAA contrast ratios against deep dark obsidian surfaces.

### 3.1 Color Palette Matrix

| Token Name | Exact HEX | RGBA Equivalent | Architectural Purpose / Application |
| :--- | :--- | :--- | :--- |
| `--bg-obsidian` | `#080808` | `rgba(8, 8, 8, 1)` | Primary canvas & body backdrop |
| `--bg-surface-secondary` | `#101010` | `rgba(16, 16, 16, 1)` | Secondary surface: large cards, sections |
| `--bg-surface-elevated` | `#171614` | `rgba(23, 22, 20, 1)` | Elevated state: interactive cards, drawer, nav capsule |
| `--gold-champagne` | `#D6B46A` | `rgba(214, 180, 106, 1)` | Primary brand accent: active links, hero highlights, emblem |
| `--gold-antique` | `#9D7B3C` | `rgba(157, 123, 60, 1)` | Muted metallic tone: secondary rules, sub-tags, subtle borders |
| `--gold-glow` | `#D6B46A` | `rgba(214, 180, 106, 0.18)`| Atmospheric specular aura & focused ring shadows |
| `--text-ivory` | `#F3EFE6` | `rgba(243, 239, 230, 1)` | High-contrast headlines & primary editorial text |
| `--text-secondary` | `#A7A198` | `rgba(167, 161, 152, 1)` | Narrative body copy & descriptive prose |
| `--text-muted` | `#666056` | `rgba(102, 96, 86, 1)` | Telemetry timestamps, indexing, code annotations |
| `--border-subtle` | `#302A20` | `rgba(48, 42, 32, 0.85)` | Inactive architectural lines, card frames, dividers |
| `--border-gold` | `#D6B46A` | `rgba(214, 180, 106, 0.45)`| Interactive focus states, hover borders, active badges |
| `--status-live` | `#D6B46A` | `rgba(214, 180, 106, 1)` | Live status pulse & availability indicator |

### 3.2 CSS Custom Properties Block
```css
:root {
  /* Obsidian & Gold Color System */
  --bg-obsidian: #080808;
  --bg-surface-secondary: #101010;
  --bg-surface-elevated: #171614;
  --bg-surface-translucent: rgba(23, 22, 20, 0.85);

  --gold-champagne: #D6B46A;
  --gold-antique: #9D7B3C;
  --gold-glow: rgba(214, 180, 106, 0.18);
  --gold-sheen: linear-gradient(135deg, #F3EFE6 0%, #D6B46A 50%, #9D7B3C 100%);

  --text-ivory: #F3EFE6;
  --text-secondary: #A7A198;
  --text-muted: #666056;

  --border-subtle: #302A20;
  --border-gold: rgba(214, 180, 106, 0.45);
  --border-hairline: 1px solid var(--border-subtle);

  /* Typography Stacks */
  --font-serif: 'Cormorant Garamond', Georgia, serif;
  --font-sans: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;

  /* Spatial Scale */
  --space-3xs: 4px;
  --space-2xs: 8px;
  --space-xs: 12px;
  --space-sm: 16px;
  --space-md: 24px;
  --space-lg: 32px;
  --space-xl: 48px;
  --space-2xl: 64px;
  --space-3xl: 96px;
  --space-4xl: 128px;
  --space-5xl: 160px;

  /* Layout Constraints */
  --container-max-width: 1360px;
  --container-gutter: clamp(20px, 4.5vw, 56px);
  --header-height: 84px;

  /* Elevation & Shadows */
  --shadow-subtle: 0 4px 24px -2px rgba(0, 0, 0, 0.6);
  --shadow-elevated: 0 16px 40px -8px rgba(0, 0, 0, 0.85);
  --shadow-gold-glow: 0 0 32px -4px rgba(214, 180, 106, 0.22);

  /* Motion Curves */
  --ease-editorial: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-smooth: cubic-bezier(0.4, 0, 0.2, 1);
  --duration-fast: 180ms;
  --duration-normal: 350ms;
  --duration-slow: 750ms;
}
```

---

## 4. TYPOGRAPHY SYSTEM

The typographic identity balances haute editorial serif with architectural geometry and monospaced computational rigor.

### 4.1 Typeface Selection
1. **Display & Editorial Serif:** `Cormorant Garamond` (Weights: 400, 500, 600, 700, Italic).
   *Character:* Classical Roman letterforms, elegant calligraphic contrast, aristocratic luxury presence for hero headlines, section titles, and highlighted pull quotes.
2. **Body & Interface Sans-Serif:** `Manrope` (Weights: 300, 400, 500, 600).
   *Character:* Modern semi-geometric grotesque, immaculate legibility, generous x-height, refined kerning for long-form reading and interactive labels.
3. **Technical Telemetry & Code:** `JetBrains Mono` (Weights: 400, 500, 600).
   *Character:* Monospaced developer precision, crisp punctuation, tabular numeral alignment for world clock, telemetry coordinates, and code snippets.

### 4.2 Typographic Hierarchy & Fluid Scaling

| Hierarchy Level | Font Family | Fluid Clamp Expression | Desktop Value | Mobile Value | Weight | Line Height | Tracking |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Hero Monogram Title**| Serif | `clamp(3.5rem, 8.5vw + 0.5rem, 8.5rem)` | 136px | 56px | 600 | 0.92 | `-0.03em` |
| **Section H1 Title** | Serif | `clamp(2.5rem, 5.5vw + 0.25rem, 5rem)` | 80px | 40px | 600 | 1.05 | `-0.02em` |
| **Subhead H2** | Serif | `clamp(1.75rem, 3.2vw + 0.25rem, 3rem)` | 48px | 28px | 500 | 1.15 | `-0.01em` |
| **Card H3** | Sans | `clamp(1.2rem, 1.6vw + 0.4rem, 1.65rem)` | 26px | 20px | 600 | 1.30 | `-0.01em` |
| **Editorial Lead** | Serif / Sans | `clamp(1.15rem, 1.2vw + 0.2rem, 1.45rem)`| 23px | 18px | 400 | 1.60 | `0.01em` |
| **Body Regular** | Sans | `clamp(0.95rem, 0.4vw + 0.65rem, 1.05rem)`| 16.5px | 15px | 400 | 1.70 | `normal` |
| **Technical Label / Tag**| Mono | `0.8125rem (13px)` | 13px | 12px | 500 | 1.40 | `+0.08em` (Caps) |
| **Telemetry Fine** | Mono | `0.75rem (12px)` | 12px | 11px | 400 | 1.35 | `+0.12em` (Caps) |

---

## 5. SPACING & LAYOUT SYSTEM

### 5.1 Editorial Grid Architecture
- **Max Container Width:** `1360px` with fluid gutters `clamp(20px, 4.5vw, 56px)`.
- **Asymmetric Split System:** 12-column CSS Grid with non-standard distribution (e.g. 7-column editorial left vs 5-column showcase right; or 4-column index vs 8-column narrative).
- **Hairline Dividers:** Structural borders (`1px solid var(--border-subtle)`) defining sections, removing generic card pills and replacing them with tailored editorial enclosures.
- **Negative Space Breathing Room:** Section vertical padding set to `clamp(96px, 12vw, 170px)`.

### 5.2 Responsive Viewport Rules
1. **Ultra-Wide (> 1440px):** Full 12-column layout, luxury margin offsets, 3D golden sculpture beside hero portrait.
2. **Desktop / Laptop (1024px – 1439px):** Split hero composition with portrait on right and oversized serif typography on left.
3. **Tablet (768px – 1023px):** Fluid vertical stacking with preserved editorial proportions and accessible floating navigation.
4. **Mobile (< 768px):** Intentionally designed single-column atelier layout; portrait cleanly framed with `aspect-ratio: 1 / 1` or `4 / 5`, touch targets >= 48px, zero horizontal overflow.

---

## 6. ASSET TREATMENT & BRAND PRESERVATION

### 6.1 The Hexagonal ZS Monogram Logo (`ZS fav icon.png`)
- **Authentic Asset:** Located at root as `ZS fav icon.png`. Features an intricate champagne-gold geometric monogram encased in a sharp hexagonal emblem.
- **Role:** Primary brand insignia.
- **Integration Points:**
  1. **Site Navigation:** Crisp 42px x 42px brand emblem with subtle warm gold border accent and active home link.
  2. **Footer:** Prominent 52px x 52px brand insignia anchoring the architectural closing.
  3. **Preloader / Loading Experience:** Centered gold emblem with gentle breathing illumination during initial load.
  4. **Favicon:** Directly referenced across all HTML documents with `<link rel="icon" type="image/png" href="ZS%20fav%20icon.png">`.
- **Integrity Rule:** Do NOT redraw, replace, or alter the geometry of this supplied asset. Maintain 1:1 aspect ratio.

### 6.2 The Official Profile Portrait (`Profile Pic.jpg`)
- **Authentic Asset:** Located at root as `Profile Pic.jpg`. Features Zeerak Shafique in an artistic black-and-white portrait with natural lighting.
- **Homepage Hero Role:** Visually striking, high-impact editorial placement positioned adjacent to the oversized name typography.
- **Framing & Curation:**
  - Ratio: `aspect-ratio: 1 / 1` (or `4 / 5` on vertical viewports) with `object-fit: cover; object-position: center 28%;` ensuring Zeerak's face and eyes are commanding and sharp.
  - Border Framing: Deliberate `#302A20` hairline border with micro-corner tick marks (`+`) in Champagne Gold.
  - Subtle Lighting: Warm gold vignette overlay (`rgba(214, 180, 106, 0.08)`) and soft obsidian gradient fade at the bottom.
  - Interactive Depth: Refined 3D mouse tilt tracking (`max: 4deg`) on desktop.
  - Accessibility: Full semantic `<img alt="Zeerak Shafique — Portrait of BCA Student and Aspiring Creative Developer">` with explicit width and height to prevent CLS.

---

## 7. 3D SCENE SPECIFICATIONS: THE OBSIDIAN & GOLD SCULPTURE

### 7.1 Visual Concept: "The Golden Gyroscope & Obsidian Core"
To complement Zeerak's portrait without causing visual clutter, the 3D centerpiece is an **architectural kinetic sculpture**:
- **Obsidian Core:** A faceted dark obsidian polyhedron (dodecahedron or beveled prism) with high specular reflectivity and dark onyx material.
- **Champagne-Gold Orbital Girdles:** Two concentric, razor-thin metallic gold rings with brushed finish and subtle wireframe coordinate ticks orbiting the core at 38° and -25° angles.
- **Symbolism:** The unyielding obsidian core represents algorithmic logic and low-level C programming; the luminous, fluid gold orbits represent creative frontend web craftsmanship.

### 7.2 Technical Implementation (Three.js WebGL with Graceful Fallback)
- **Library:** Native ES Module Three.js loaded asynchronously via CDN.
- **Lighting Setup:**
  - Ambient base: `#14120E` (low-intensity warm shadow).
  - Main Key Light: Warm Champagne Gold (`#D6B46A`, intensity `2.8`) casting crisp specular highlights across the metallic facets.
  - Subtle Rim Light: Soft Ivory (`#F3EFE6`, intensity `1.2`) separating the core from the obsidian background.
- **Interactivity:**
  - Inertial mouse parallax: Tilts and rotates gently toward cursor position with smooth damping (`lerp: 0.05`).
  - Scroll observer: Automatically suspends `requestAnimationFrame` render loop when scrolled out of viewport.
- **Fallback Guarantee:**
  - On devices with WebGL disabled or `prefers-reduced-motion: reduce`, displays an elegant CSS 3D gold geometric emblem with subtle pulsing radial aura.

---

## 8. PAGE-BY-PAGE DETAILED ARCHITECTURAL BLUEPRINTS

```
+-----------------------------------------------------------------------------------------+
|                               PAGE FLOW & MULTIPAGE ROUTING                             |
+-----------------------------------------------------------------------------------------+
|  [ index.html ]    --> Hero with Portrait & 3D, Overview, Selected Works, Contact Invite|
|  [ about.html ]    --> Editorial Narrative, BCA Studies, C & Web Foundations, Dossier   |
|  [ projects.html ] --> Portfolio Case Study, C Algorithm Engine, Shader Lab Concepts    |
|  [ skills.html ]   --> 4 Architectural Pillars: HTML5, CSS3, JavaScript, C Programming  |
|  [ contact.html ]  --> Transmission Terminal, +91 9580912686, Instagram @_siddiqui_._zeerak_
+-----------------------------------------------------------------------------------------+
```

### 8.1 Shared Architecture (Across All Pages)

#### Header & Navigation
- Fixed / sticky top navigation capsule with glassmorphism backdrop (`rgba(23, 22, 20, 0.85)` + `backdrop-filter: blur(16px)`).
- Left: Embedded **ZS gold hexagonal emblem** (`ZS fav icon.png`) + `ZEERAK SHAFIQUE` wordmark in `Cormorant Garamond`.
- Center: Multipage links: `HOME`, `ABOUT`, `PROJECTS`, `SKILLS`, `CONTACT`.
- Right:
  - Live availability beacon: Gold pulsing dot + `AVAILABLE FOR COLLAB // BCA '26`.
  - Telephone quick action: `+91 9580912686`.
  - Instagram shortcut: `@_siddiqui_._zeerak_`.
  - Mobile hamburger menu button opening an editorial fullscreen overlay.

#### Footer & Colophon
- Architectural hairline separator in `#302A20`.
- Left: ZS Gold Hexagonal Emblem + summary of Zeerak's focus.
- Center: Directory links to all pages.
- Right: **Live Indian Standard Time Clock** (`Asia/Kolkata` with live seconds).
- Bottom: Copyright `© 2026 Zeerak Shafique. All Rights Reserved.` + "Built with Vanilla HTML5, CSS3 & ES6+ JavaScript. Zero Framework Bloat." + Smooth "Return to Apex" button.

### 8.2 Page 1: Homepage (`index.html`)
- **Section 0: Preloader:** Fast (~800ms) luxury boot sequence featuring the gold ZS emblem, progress counter (`00%` -> `100%`), and a 1.2s hard failsafe.
- **Section 1: Hero:**
  - Split editorial grid:
    - Left Column: Telemetry tags (`IST // ASIA/KOLKATA`), oversized serif headline:
      ```
      ZEERAK
      SHAFIQUE
      ```
      Sub-headline in Champagne Gold: `BCA STUDENT / ASPIRING CREATIVE DEVELOPER`.
      Short, authentic introduction about learning programming and crafting digital experiences.
      CTA Cluster: `"EXPLORE PROJECTS"` (Gold pill) and `"ABOUT ME"` (Hairline ghost button).
    - Right Column: Zeerak's genuine portrait (`Profile Pic.jpg`) set in a gold-detailed architectural frame, paired with the interactive Three.js 3D golden sculpture.
- **Section 2: The Philosophy Statement:**
  - Oversized typography quote: *"I study how low-level computational logic transforms into sensory digital experiences."*
- **Section 3: Selected Skills Overview:**
  - 4 architectural cards: HTML5, CSS3, JavaScript (ES6+), C Programming with live code tags.
- **Section 4: Featured Creations Preview:**
  - Project 01: The Living Portfolio (Obsidian Gold edition) with live status chip and repository link.
- **Section 5: Direct Contact Invitation:**
  - Monumental display: *"LET'S BUILD SOMETHING EXTRAORDINARY."*
  - Instant phone line `+91 9580912686` and Instagram link `@_siddiqui_._zeerak_`.

### 8.3 Page 2: About (`about.html`)
- **Subpage Hero:** Large serif headline: *"The Architecture of Learning."*
- **Scholastic Dossier:**
  - Authentic academic status: Bachelor of Computer Applications (BCA) candidate.
  - Core philosophy: "Respect the machine first." Learning memory management, pointers, and data structures in C before relying on web frameworks.
  - Bridging the gap: Connecting procedural algorithms with accessible, responsive modern web design.
- **Portrait Inclusion:** Secondary editorial treatment of `Profile Pic.jpg` integrated into the personal narrative with an architectural caption.
- **System Specifications Sheet:**
  - Standardized technical card listing location (`South Asia / IST`), current curriculum, key focus areas, and coding methodology.

### 8.4 Page 3: Projects (`projects.html`)
- **Subpage Hero:** Large serif headline: *"Selected Works & Experiments."*
- **Filter Controls:** Category pills (`ALL WORKS`, `CREATIVE WEB`, `SYSTEMS & ALGORITHMS`).
- **Project 01 (Featured Showcase):**
  - Title: *Obsidian Gold // Personal Digital Atelier*
  - Category: *Creative Engineering / Multipage Experience*
  - Year: *2026*
  - Detailed narrative of first-principles engineering, responsive clamp formulas, Three.js spatial visualizer, zero external framework runtime.
  - Active links: `[ ACTIVE DEMO ]` and `[ REPOSITORY ↗ ]`.
- **Project 02 (Structured Concept):**
  - Title: *Algo.Core // C Algorithm Visualizer*
  - Category: *Systems Programming & Canvas Logic*
  - Description: Upcoming project bridging sorting algorithms and memory models in C with interactive web canvas animation.
  - Status: Clearly labeled `[ IN DEVELOPMENT // PROTOTYPE ]`.
- **Project 03 (Creative Laboratory):**
  - Title: *Kinetic Geometry // Spatial Shader Lab*
  - Category: *WebGL & Procedural Mathematics*
  - Status: Clearly labeled `[ RESEARCH & EXPERIMENTATION ]`.

### 8.5 Page 4: Skills (`skills.html`)
- **Subpage Hero:** Large serif headline: *"Foundational Disciplines."*
- **Core Engineering Pillars (No Fake Percentages):**
  1. **HTML5 Architecture:** Semantic document structure, DOM trees, accessibility (WCAG AA), SEO metadata.
  2. **CSS3 & Design Tokens:** Architectural layouts, CSS Grid, fluid clamp typography, metallic gradients, 3D transforms.
  3. **JavaScript (ES6+):** Vanilla DOM manipulation, event loops, async promise chains, WebGL rendering pipelines, zero-bloat state.
  4. **C Programming:** Computational foundations, memory allocation (`malloc`/`free`), pointer arithmetic, structs, data structures (linked lists, stacks, queues).
- **Curriculum & Growth Vector:**
  - Clear overview of current learning topics and future exploration frontiers (e.g. GLSL shaders, TypeScript fundamentals).

### 8.6 Page 5: Contact (`contact.html`)
- **Subpage Hero:** Large serif headline: *"Initialize Communication."*
- **Genuine Contact Details:**
  - Phone: `+91 9580912686` with clickable `tel:+919580912686` action.
  - Instagram: `@_siddiqui_._zeerak_` with link `https://www.instagram.com/_siddiqui_._zeerak_/`.
  - Zero fabricated emails or unauthorized social media profiles.
- **Interactive Transmission Terminal:**
  - Client-side validated form (Name, Return Email, Subject, Message) that generates a clean mailto payload with immediate user confirmation.
- **Availability Telemetry:** Live Indian Standard Time status, response window (< 24 hours), and secure communication standards.

---

## 9. PRESERVATION OF INDIAN STANDARD TIME (IST)

- **IANA Timezone Standard:** `Asia/Kolkata` (UTC+05:30).
- **Implementation Mechanism:** Native JavaScript `Intl.DateTimeFormat`:
  ```javascript
  const istFormatter = new Intl.DateTimeFormat('en-IN', {
    timeZone: 'Asia/Kolkata',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false
  });
  ```
- **Integrity Rule:** No manual arithmetic (+5.5 hours). Automatic daylight calculation handled by standard IANA database.
- **Geographical Coordinates:** Telemetry readouts updated to Indian coordinates (`28.6139° N, 77.2090° E // IST (UTC+05:30)`). Zero old foreign timezone or coordinate remnants.

---

## 10. ANIMATION & MOTION LANGUAGE

1. **Editorial Stagger Reveals:**
   - Elements enter on scroll via `IntersectionObserver` using `opacity: 0; transform: translateY(28px);` transitioning smoothly with `cubic-bezier(0.16, 1, 0.3, 1)` over 600ms.
2. **Hairline Gold Expansions:**
   - Architectural divider lines expand horizontally on scroll to establish editorial boundaries.
3. **Card & Portrait 3D Perspective Tilt:**
   - Mouse hover tilts cards smoothly by up to 4° on X and Y axes, reflecting subtle gold specular light.
4. **Precision Dual-State Cursor (Desktop):**
   - Fine champagne gold center dot (4px) surrounded by a floating metallic ring (32px), expanding to 54px when hovering over links and buttons. Disabled on touch devices.
5. **Reduced Motion Safeguards:**
   - Full compliance with `@media (prefers-reduced-motion: reduce)`. Animations are immediately cleared, and 3D scenes gracefully display static gold geometric artwork.

---

## 11. ACCESSIBILITY, SEO & PERFORMANCE METRICS

- **Semantic HTML5:** Strict single `<h1>` per page, hierarchical `<h2>` and `<h3>`, semantic landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`).
- **Contrast Ratios:** Text ivory (`#F3EFE6`) on obsidian (`#080808`) delivers an exceptional contrast ratio of **18.5:1**, far exceeding WCAG AAA standards. Champagne gold accents meet AA standards for large text and UI markers.
- **Focus Rings:** Distinctive `:focus-visible` outline in Champagne Gold (`#D6B46A`) with a 3px offset.
- **SEO & Social Sharing:**
  - Descriptive titles, meta descriptions, Open Graph cards referencing `Profile Pic.jpg`.
  - Canonical links and favicon tags referencing `ZS fav icon.png`.
- **Zero Framework Runtime:** 100% vanilla HTML, CSS, and modern JavaScript. Fast First Contentful Paint (< 0.8s) and smooth 60 FPS scrolling.

---

## 12. IMPLEMENTATION ACCEPTANCE CHECKLIST

Before concluding the project, every item in this checklist must be satisfied:

- [ ] `DESIGN.md` reflects the complete OBSIDIAN GOLD — The Digital Atelier creative direction.
- [ ] Global design tokens in `style.css` updated to Obsidian (`#080808`), Champagne Gold (`#D6B46A`), Antique Gold (`#9D7B3C`), and Warm Ivory (`#F3EFE6`).
- [ ] Typography upgraded with Google Fonts: `Cormorant Garamond`, `Manrope`, and `JetBrains Mono`.
- [ ] Hexagonal gold ZS monogram logo (`ZS fav icon.png`) integrated into site navigation, footer, and preloader.
- [ ] Favicon verified and functioning across all pages (`ZS fav icon.png`).
- [ ] Profile photo (`Profile Pic.jpg`) prominently featured in the homepage hero and about narrative with editorial framing.
- [ ] Homepage hero features oversized typography: `ZEERAK SHAFIQUE` and `BCA STUDENT / ASPIRING CREATIVE DEVELOPER`.
- [ ] Interactive 3D metallic golden sculpture implemented with Three.js and graceful CSS fallback.
- [ ] Multipage architecture preserved: `index.html`, `about.html`, `projects.html`, `skills.html`, `contact.html` all redesigned and fully functional.
- [ ] Genuine contact information preserved: phone `+91 9580912686` and Instagram `@_siddiqui_._zeerak_` (`https://www.instagram.com/_siddiqui_._zeerak_/`). No fabricated emails or socials.
- [ ] Indian Standard Time clock running accurately using `Asia/Kolkata` across footers.
- [ ] All old Pakistan latitude/timezone references completely replaced with Indian coordinates.
- [ ] Mobile and desktop layouts tested and verified with zero horizontal scroll overflow.
- [ ] Local static server tested and working cleanly.

---
**END OF SPECIFICATION: DESIGN.md**
