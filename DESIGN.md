# DESIGN SPECIFICATION: DIGITAL AFTERDARK
### Creative Direction, Architectural Blueprint & Interaction System
**Project:** Zeerak Shafique — Personal Creative Developer Portfolio  
**Role:** Bachelor of Computer Applications (BCA) Student & Aspiring Creative Developer  
**Status:** Authoritative Design Specification (v2.6)  
**Author:** Creative Director & Frontend Architect  

---

## 1. EXECUTIVE SUMMARY & CREATIVE VISION

### 1.1 Project Identity & Core Objective
- **Name:** Zeerak Shafique
- **Identity:** BCA Student | Aspiring Creative Developer
- **Purpose:** Transform an ordinary student portfolio into an extraordinary, futuristic, museum-grade digital experience that commands attention from creative directors, engineering leads, and technology pioneers.
- **Core Narrative:** A creative developer exploring the duality between **computational logic** (low-level systems, C programming, algorithmic rigor) and **sensory digital aesthetics** (modern web standards, interactive graphics, cinematic interfaces).

### 1.2 The Creative Concept: "DIGITAL AFTERDARK"
The web is saturated with repetitive, formulaic portfolios: black backgrounds with generic purple gradients, standard rounded cards, and uninspired center-aligned text. 

**DIGITAL AFTERDARK** rejects generic templates. It visualizes Zeerak's portfolio as an **interactive computational universe**:
- **Atmosphere:** Deep obsidian space punctuated by cinematic atmospheric lighting, technical telemetry, and laser-precise edge lines.
- **Tone:** Enigmatic, mathematically disciplined, technologically progressive, and unapologetically refined.
- **Spatial Dimension:** Layered spatial architecture featuring a live 3D geometric monolith enveloped in orbital kinetic rings, reacting fluidly to cursor physics and scroll velocity.
- **Swiss Precision:** Monospaced technical data tags, asymmetric editorial grids, and oversized display typography coexisting in harmony.

---

## 2. ART DIRECTION & DESIGN PRINCIPLES

Inspired by the design craftsmanship of **Awwwards Site of the Year** nominees, **Bruno Simon**, and high-craft creative studios, this experience adheres to five foundational pillars:

```
+-----------------------------------------------------------------------------------+
|                            THE 5 CORE DESIGN PILLARS                              |
+-----------------------------------------------------------------------------------+
| 1. ARCHITECTURAL HONESTY  | Authentic student journey; zero fabricated client     |
|                           | accolades; genuine pride in computer science basics.  |
| 2. SPATIAL DEPTH          | Multi-plane Z-index layering: background telemetry -> |
|                           | ambient light -> 3D canvas -> editorial layout -> HUD.|
| 3. EDITORIAL TYPOGRAPHY   | Brutalist display scales paired with hyper-legible    |
|                           | system sans and monospaced technical metadata.        |
| 4. RESTRAINED KINETICS    | Physics-based spring curves; micro-interactions with  |
|                           | purpose; zero gratuitous bouncing or novelty particles|
| 5. ZERO RUNTIME BLOAT     | 60 FPS hardware-accelerated performance via native    |
|                           | Web APIs and lightweight, purposeful dependencies.    |
+-----------------------------------------------------------------------------------+
```

---

## 3. DESIGN TOKEN SYSTEM & PALETTE

All colors are formulated to provide high contrast (WCAG 2.1 AA/AAA compliance), cinematic glow thresholds, and distinct visual hierarchy.

### 3.1 Color Palette Matrix

| Token Name | Exact HEX | RGBA Equivalent | Purpose / Application |
| :--- | :--- | :--- | :--- |
| `--bg-obsidian` | `#060709` | `rgba(6, 7, 9, 1)` | Primary canvas background |
| `--bg-surface-1` | `#0C0E14` | `rgba(12, 14, 20, 1)` | Secondary surface: cards, modals, nav capsule |
| `--bg-surface-2` | `#141722` | `rgba(20, 23, 34, 1)` | Elevated state: card hover, active pill buttons |
| `--bg-surface-subtle`| `#1A1D2B` | `rgba(26, 29, 43, 0.6)`| Translucent glassmorphism base |
| `--accent-violet` | `#8B5CF6` | `rgba(139, 92, 246, 1)`| Primary accent: brand markers, focus highlights |
| `--accent-violet-glow`| `#7C3AED` | `rgba(124, 58, 237, 0.28)`| Volumetric atmospheric glow, box-shadow pulses |
| `--accent-cyan` | `#00F2FE` | `rgba(0, 242, 254, 1)` | Secondary accent: telemetry, live status, active markers |
| `--accent-cyan-glow` | `#06B6D4` | `rgba(6, 182, 212, 0.22)` | Ambient specular highlights, secondary glows |
| `--text-primary` | `#F8FAFC` | `rgba(248, 250, 252, 1)`| High-contrast headlines & primary copy |
| `--text-secondary` | `#94A3B8` | `rgba(148, 163, 184, 1)`| Descriptive body text, metadata paragraphs |
| `--text-muted` | `#64748B` | `rgba(100, 116, 139, 1)`| Technical tags, timestamps, coordinate readouts |
| `--border-subtle` | `#1E2230` | `rgba(255, 255, 255, 0.07)`| Inactive card borders, grid separator lines |
| `--border-highlight`| `#3B4259` | `rgba(255, 255, 255, 0.18)`| Hover state borders, input field focus |
| `--border-cyan` | `#00F2FE` | `rgba(0, 242, 254, 0.45)` | Interactive focus states, active HUD borders |
| `--status-online` | `#10B981` | `rgba(16, 185, 129, 1)` | Live availability beacon dot |

### 3.2 CSS Custom Properties Block
```css
:root {
  /* Color System */
  --bg-obsidian: #060709;
  --bg-surface-1: #0c0e14;
  --bg-surface-2: #141722;
  --bg-surface-subtle: rgba(26, 29, 43, 0.65);
  
  --accent-violet: #8b5cf6;
  --accent-violet-glow: rgba(139, 92, 246, 0.28);
  --accent-cyan: #00f2fe;
  --accent-cyan-glow: rgba(0, 242, 254, 0.22);
  
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-highlight: rgba(255, 255, 255, 0.22);
  --border-cyan: rgba(0, 242, 254, 0.45);
  --status-online: #10b981;

  /* Typography Stacks */
  --font-display: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;

  /* Spacing Scale */
  --space-2xs: 4px;
  --space-xs: 8px;
  --space-sm: 16px;
  --space-md: 24px;
  --space-lg: 32px;
  --space-xl: 48px;
  --space-2xl: 64px;
  --space-3xl: 96px;
  --space-4xl: 128px;
  --space-5xl: 160px;

  /* Spatial Constraints */
  --container-max-width: 1400px;
  --container-gutter: clamp(20px, 4vw, 48px);
  --header-height: 80px;

  /* Elevation & Glassmorphism */
  --glass-backdrop: blur(16px) saturate(180%);
  --shadow-elevation-1: 0 4px 20px -2px rgba(0, 0, 0, 0.5);
  --shadow-elevation-2: 0 12px 32px -4px rgba(0, 0, 0, 0.7);
  --shadow-glow-violet: 0 0 35px -5px rgba(139, 92, 246, 0.35);
  --shadow-glow-cyan: 0 0 35px -5px rgba(0, 242, 254, 0.3);

  /* Transitions */
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out-smooth: cubic-bezier(0.65, 0, 0.35, 1);
  --duration-fast: 200ms;
  --duration-normal: 400ms;
  --duration-slow: 700ms;
}
```

---

## 4. TYPOGRAPHY SYSTEM

The typography pairs brutalist geometry with clinical legibility and developer-terminal telemetry.

### 4.1 Typeface Selection
1. **Display Headings:** `Space Grotesk` (Google Fonts, Weights: 500, 700).  
   *Character:* Geometric, confident, slightly eccentric ink-traps that deliver editorial presence.
2. **Body & UI Elements:** `Inter` (Google Fonts, Weights: 400, 500, 600).  
   *Character:* Ultra-clean, neutral, optimized for micro-legibility at 14px–18px.
3. **Technical Telemetry & Labels:** `JetBrains Mono` (Google Fonts, Weights: 400, 600).  
   *Character:* Monospaced code aesthetics, distinct punctuation, and clinical computational feel.

### 4.2 Fluid Typography Hierarchy

| Style Level | Typeface | Fluid Clamp Definition | Desktop Reference | Mobile Reference | Line Height | Letter Spacing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Hero Title** | Display | `clamp(2.75rem, 8vw + 1rem, 7.5rem)` | 120px | 44px | 0.95 | `-0.04em` |
| **H1 (Section)**| Display | `clamp(2.25rem, 5vw + 0.5rem, 4.5rem)`| 72px | 36px | 1.05 | `-0.03em` |
| **H2 (Subhead)**| Display | `clamp(1.75rem, 3vw + 0.5rem, 2.75rem)`| 44px | 28px | 1.15 | `-0.02em` |
| **H3 (Card Title)**| Display| `clamp(1.25rem, 1.5vw + 0.5rem, 1.75rem)`| 28px | 20px | 1.25 | `-0.01em` |
| **Lead Paragraph**| Body | `clamp(1.05rem, 1vw + 0.25rem, 1.35rem)` | 21px | 17px | 1.65 | `-0.005em` |
| **Body Regular** | Body | `clamp(0.95rem, 0.5vw + 0.5rem, 1.05rem)`| 16px | 15px | 1.70 | `normal` |
| **Mono Badge/Tag**| Mono | `0.8125rem (13px)` | 13px | 12px | 1.40 | `+0.08em` (Uppercase) |
| **Telemetry Fine**| Mono | `0.75rem (12px)` | 12px | 11px | 1.30 | `+0.1em` (Uppercase) |

---

## 5. LAYOUT ARCHITECTURE & SPATIAL COMPOSITION

### 5.1 Grid & Spatial Container
- **12-Column Swiss Responsive Grid:** Max width `1400px`, centered with fluid side gutters `clamp(20px, 4vw, 48px)`.
- **Column Gap:** `clamp(16px, 2.5vw, 32px)`.
- **Section Vertical Rhythm:** `clamp(80px, 12vw, 160px)` padding top/bottom.
- **Horizontal Overflow Prevention Rule:**
  ```css
  html, body {
    width: 100%;
    max-width: 100%;
    overflow-x: hidden;
    position: relative;
  }
  ```

### 5.2 Responsive Breakpoints
1. **Desktop Ultra-Wide:** `>= 1440px` (Full 12-column expansive editorial layouts).
2. **Desktop Standard / Laptop:** `1024px – 1439px` (Structured 12-column with proportioned 3D canvas).
3. **Tablet (Portrait & Landscape):** `768px – 1023px` (8-column grid, stacked hero visual, docked bottom or floating nav).
4. **Mobile Standard:** `480px – 767px` (4-column grid, 3D canvas centered background, full-screen mobile drawer).
5. **Mobile Compact:** `< 480px` (Single column linear flow, optimized touch targets >= 48px).

### 5.3 Z-Index Elevation Matrix
```
Layer 0: Background Canvas (#060709 + Ambient Radial Gradients) -> z-index: 0
Layer 1: Three.js Interactive 3D WebGL Scene                     -> z-index: 1
Layer 2: Subtle Telemetry Grid Lines & Coordinate Overlays       -> z-index: 2
Layer 3: Primary Content & Section Components                    -> z-index: 10
Layer 4: Floating Glass Navigation Bar                           -> z-index: 100
Layer 5: Mobile Navigation Drawer & Modals                      -> z-index: 200
Layer 6: System Preloader HUD                                    -> z-index: 999
Layer 7: Custom Interactive Cursor Follower                      -> z-index: 9999
```

---

## 6. SECTION-BY-SECTION DETAILED SPECIFICATIONS

```
+-----------------------------------------------------------------------------------+
|                           PAGE COMPONENT FLOW MAP                                 |
+-----------------------------------------------------------------------------------+
|  [ PRELOADER HUD (1.2s auto-dismiss) ]                                            |
|  [ FLOATING CAPSULE NAVIGATION (Sticky / Glassmorphism) ]                         |
|  [ SECTION 01: HERO - The Signature Kinetic Experience (Three.js Monolith) ]      |
|  [ SECTION 02: ABOUT - Editorial Manifesto & Engineering Core ]                   |
|  [ SECTION 03: SKILLS - The Technical Architecture Matrix (HTML, CSS, JS, C) ]    |
|  [ SECTION 04: SELECTED WORKS - Interactive Project Dossiers ]                    |
|  [ SECTION 05: TRAJECTORY - Current Explorations & Growth Vector ]                |
|  [ SECTION 06: CONTACT - Transmission Terminal & Direct Connection ]              |
|  [ FOOTER - Colophon, System Telemetry & Back-to-Top Elevator ]                   |
+-----------------------------------------------------------------------------------+
```

---

### SECTION 00: THE PRELOADER (SYSTEM BOOT HUD)
**Intent:** Establish immediate atmosphere and technical polish within 1200 milliseconds. Failsafe guarantees the user is never blocked.

- **Visual Architecture:**
  - Fullscreen overlay (`#060709`).
  - Centered technical terminal box with crisp glowing cyan border.
  - Live progress counter (`00%` to `100%`) ticking upward in ~1000ms.
  - Monospaced readout:
    ```
    [ SYS.BOOT // ZEERAK.SHF_KERNEL_V2.6 ]
    >> LOADING ASSETS... OK
    >> COMPILING SHADERS... OK
    >> GEOMETRY BUFFER: READY
    >> STATUS: ONLINE
    ```
- **Exit Choreography:**
  - Counter reaches 100%.
  - The preloader splits vertically (top/bottom shutter) or smoothly fades out with `transform: scale(1.04); opacity: 0; pointer-events: none;` over 400ms.
  - Hero typography immediately staggers upward.
- **Failsafe Rule:** If asset loading or WebGL encounters delay, a hardcoded `setTimeout(1500)` forces the preloader to terminate, guaranteeing immediate accessibility.

---

### SECTION 01: FLOATING CAPSULE NAVIGATION
**Intent:** Minimalist, glassmorphism floating island that remains accessible without obstructing content.

- **Layout & Positioning:**
  - Centered floating capsule: `position: fixed; top: 24px; left: 50%; transform: translateX(-50%); z-index: 100;`.
  - Max width: `920px`, width: `calc(100% - 48px)`.
  - Background: `var(--bg-surface-subtle)` with `backdrop-filter: blur(16px) saturate(180%)`.
  - Border: `1px solid var(--border-subtle)` with subtle top border highlight `rgba(255, 255, 255, 0.15)`.
  - Border radius: `9999px` (pill).
  - Padding: `10px 24px`.
- **Navigation Elements:**
  1. **Personal Brand Mark:**
     - Left-aligned: `ZS // 26` in `JetBrains Mono` bold with an electric cyan indicator dot (`#00F2FE`).
  2. **Navigation Links (Desktop):**
     - Links: `// 01. ABOUT`, `// 02. SKILLS`, `// 03. PROJECTS`, `// 04. TRAJECTORY`.
     - Styling: `JetBrains Mono` 13px, uppercase, `var(--text-secondary)`.
     - Hover: `var(--text-primary)` with electric violet underline glow.
     - Active indicator: Dynamic indicator sliding pill or cyan dot.
  3. **Live Status Indicator:**
     - Pulsing beacon dot: `8px x 8px`, `#10B981` (emerald green) with a continuous pinging radar ring.
     - Label: `AVAILABLE FOR COLLAB` (Hidden on mobile).
  4. **Primary CTA Button:**
     - Compact pill button: `"TRANSMIT"` / `"CONTACT"`.
     - Background: `rgba(139, 92, 246, 0.15)`, Border: `1px solid var(--accent-violet)`.
     - Hover: Background `#8B5CF6`, Text `#FFFFFF`, Box shadow `var(--shadow-glow-violet)`.
- **Mobile Responsive Drawer:**
  - On screens `< 768px`, the center links hide. A sleek hamburger trigger `[MENU]` appears.
  - Tapping opens a full-screen blurred obsidian overlay with oversized vertical editorial links (`Space Grotesk` 32px), soundless stagger transition, and device battery/time telemetry at bottom.

---

### SECTION 02: HERO — THE SIGNATURE KINETIC EXPERIENCE
**Intent:** The emotional centerpiece of the site. Immediately communicates technical ambition, spatial depth, and artistic craftsmanship.

```
+-----------------------------------------------------------------------------------+
|  [TELEMETRY TAG: SECTOR 01 // SYS.INIT]             [LAT: 31.5204° N // IST]      |
|                                                                                   |
|  ZEERAK SHAFIQUE                                   +---------------------------+  |
|  CREATIVE DEVELOPER                                |                           |  |
|                                                    |     3D HYPER-MONOLITH     |  |
|  "Bridging low-level computational logic           |     & ORBITAL KINETIC     |  |
|   and high-fidelity digital experiences."          |     RINGS (THREE.JS)      |  |
|                                                    |                           |  |
|  [ EXPLORE ARCHIVE ↓ ]    [ INITIALIZE CONTACT ↗ ] |                           |  |
|                                                    +---------------------------+  |
|  [SCROLL TELEMETRY // 0.00%]                                                      |
+-----------------------------------------------------------------------------------+
```

- **Asymmetric Composition (12-Column Split):**
  - **Left Column (Span 7 Columns):**
    - **Telemetry Chip:** Monospace pill `[ SYSTEM.INIT // DEV_SECTOR.01 ]` with cyan border and subtle scanline pulse.
    - **Name Display Headline:**
      ```
      ZEERAK
      SHAFIQUE
      ```
      Typeface: `Space Grotesk`, Bold, `clamp(3rem, 7.5vw, 6.75rem)`, letter spacing `-0.04em`.
      Text styling: Soft white with subtle gradient sheen (`linear-gradient(180deg, #FFFFFF 60%, #94A3B8 100%)`).
    - **Subtitle / Role Definition:**
      `ASPIRING CREATIVE DEVELOPER & BCA SCHOLAR`  
      Typeface: `JetBrains Mono`, 15px, letter spacing `+0.05em`, color `var(--accent-cyan)`.
    - **Manifesto Blurb (Concise & Honest):**
      `"Undergraduate student in Computer Applications exploring the synthesis of systems programming and interactive web design. Crafting digital spaces with architectural discipline."`
    - **Action Button Cluster:**
      - **Primary Button:** `EXPLORE ARCHIVE [↓]` — Obsidian pill with violet border, smooth hover fill, magnetic cursor reaction.
      - **Secondary Button:** `INITIALIZE CONTACT [↗]` — Subtle ghost button with border highlight and arrow translate on hover.
  - **Right Column (Span 5 Columns — Interactive 3D Canvas Container):**
    - An interactive Three.js viewport hosting **"The Obsidian Monolith & Dual Orbital Rings"** (detailed in Section 7).
    - Mouse parallax: Moving the cursor tilts the monolith in real-time with smooth inertia (lerp smoothing).
    - Mobile behavior: Canvas moves behind the hero text at 40% opacity with pointer interaction disabled to ensure silky 60 FPS scrolling.

---

### SECTION 03: ABOUT — EDITORIAL MANIFESTO & SYSTEM ARCHITECTURE
**Intent:** Tell Zeerak's genuine story as a BCA student with intellectual gravitas, zero buzzword inflation, and authentic pride in computational foundations.

- **Layout (Asymmetric Editorial Spread):**
  - **Left Column (Span 5 Columns) — The Philosophy:**
    - Section Index: `// 01. INTROSPECTION`
    - Large Editorial Lead:
      `"I don't just assemble interfaces. I study how computational engines translate logic into human emotion."`
    - Authentic Bio Copy:
      `"Currently pursuing my Bachelor of Computer Applications (BCA). While many enter development solely through high-level abstractions, my journey is anchored in foundational programming: understanding memory allocations in C, data structures, and the document object model before reaching for heavy frameworks.`
      `My goal is to evolve into a creative technologist who builds high-performance, aesthetically arresting experiences on the open web."`
  - **Right Column (Span 7 Columns) — System Profile Dossier:**
    - Structured like a high-end technical specification sheet:
      ```
      +-------------------------------------------------------------+
      | SYSTEM DOSSIER: ZEERAK SHAFIQUE                             |
      +-------------------------------------------------------------+
      | [01] DEGREE CANDIDATE | Bachelor of Computer Applications   |
      | [02] FOCUS DOMAINS    | Interactive Frontend, Creative Web  |
      |                       | Graphics, Systems Programming       |
      | [03] METHODOLOGY      | Semantic HTML, Mathematical Layouts,|
      |                       | Clean C Code, Zero-Bloat Vanilla JS |
      | [04] LOCATION         | South Asia (IST / UTC+05:30)        |
      | [05] STATUS           | Open to Collaborations & Internships |
      +-------------------------------------------------------------+
      ```
    - Styling: Dark graphite card background (`#0C0E14`), crisp `1px solid var(--border-subtle)`, corner crosshair markers (`+`), and monospaced typography.

---

### SECTION 04: SKILLS — THE TECHNICAL ARCHITECTURE MATRIX
**Intent:** Showcase HTML, CSS, JavaScript, and C Programming as deliberate, foundational engineering pillars rather than arbitrary progress percentages (e.g., no meaningless "CSS: 90%").

- **Visual Concept: 4 Structural Architecture Pillars:**
  Presented as interactive architectural modules in a responsive 4-column (or 2x2 tablet) layout.

```
+------------------------------------------------------------------------------------+
|  [01] FOUNDATION             [02] SPATIAL STYLING   [03] ENGINE LOGIC   [04] LOW-LEVEL     |
|  HTML5 ARCHITECTURE          CSS3 / COMPUTATIONAL   JAVASCRIPT (ES6+)   C PROGRAMMING      |
|  ------------------          --------------------   -----------------   -------------      |
|  Semantic Structuring        Custom Design Tokens   DOM Engine Ops      Memory Allocations |
|  Accessible DOM Trees        Fluid Clamp Systems    Async Pipelines     Pointers & Structs |
|  SEO Microdata Standards     Matrix Animations      Canvas & WebGL API  Algorithmic Logic  |
|  Clean Document Flow         Backdrop Compositing   Event Architecture  Data Structures    |
|                                                                                            |
|  [TAG: DOM_CORE]             [TAG: RENDER_SPEC]     [TAG: EVENT_LOOP]   [TAG: BINARY_CORE] |
+------------------------------------------------------------------------------------+
```

- **Interactive State for Each Card:**
  - Base: Matte graphite card with subtle coordinate tag in upper-right corner.
  - Hover: Border ignites with electric violet (`#8B5CF6`) or cyan (`#00F2FE`), card tilts subtly in 3D perspective (`perspective(1000px) rotateX(...) rotateY(...)`), and a micro terminal window at the bottom of the card illuminates with a live code snippet or architectural note:
    - *HTML Card:* `<!-- <main role="main" aria-label="core"> -->`
    - *CSS Card:* `grid-template-columns: repeat(12, 1fr);`
    - *JavaScript Card:* `const render = (time) => requestAnimationFrame(render);`
    - *C Card:* `int *ptr = (int*)malloc(sizeof(int) * 64);`

---

### SECTION 05: SELECTED WORKS — PROJECT SHOWCASES
**Intent:** Frame every project as a bespoke case study. Give the existing personal portfolio pride of place as Project 01, followed by carefully structured concepts for upcoming works.

- **Dossier Layout:** Each project is an expansive, horizontal editorial block with an index counter (`[ 01 / 03 ]`).

#### Project 01: The Living Portfolio (Featured Showcase)
- **Title:** `DIGITAL AFTERDARK // PERSONAL PORTFOLIO V1`
- **Category:** `Creative Engineering / Interactive Experience`
- **Year:** `2026`
- **Narrative:** The website the visitor is currently experiencing. Designed and engineered from the ground up as an editorial, futuristic universe combining Three.js 3D kinetic visuals, Swiss typography, and pure semantic performance.
- **Technologies Used:** `HTML5`, `Modern CSS3 (Tokens & Grid)`, `Vanilla JavaScript`, `Three.js (WebGL)`, `Mathematical Motion`.
- **Visual Treatment:** A split-screen interactive viewport with an animated wireframe preview and live telemetry overlay (`60 FPS`, `0 RUNTIME FRAMEWORK BLOAT`).
- **Action CTAs:**
  - Live Demo: `[ ACTIVE EXPERIENCE ]` (Pulsing green indicator).
  - Source Code: `[ VIEW REPOSITORY ↗ ]` (Link placeholder: `https://github.com/zeerak-shafique/portfolio`).

#### Project 02: Algorithmic Logic Engine (Structured Concept)
- **Title:** `ALGO.CORE // COMPUTATIONAL VISUALIZER`
- **Category:** `Systems Logic & Visual Computing`
- **Year:** `2026 (In Development)`
- **Narrative:** An upcoming interactive visualizer bridging C algorithms with web canvas rendering. Designed to illustrate sorting dynamics, tree traversals, and memory stack behaviors in real time.
- **Technologies Used:** `C Programming (Logic)`, `JavaScript`, `Canvas 2D API`, `Web Workers`.
- **Visual Treatment:** Abstract vector visualization card showing dynamic sorting nodes with cyan glowing connection lines.
- **Action CTAs:**
  - Status: `[ PROTOTYPE PHASE // COMING SOON ]`
  - Repository: `[ ARCHIVE IN PROGRESS ↗ ]`

#### Project 03: Spatial Canvas Experiment (Creative Laboratory)
- **Title:** `KINETIC GEOMETRY // WEBGL SHADER LAB`
- **Category:** `Experimental Creative Coding`
- **Year:** `2026 (Upcoming Focus)`
- **Narrative:** Exploration into mathematical geometry, procedural noise, and hardware-accelerated fluid shaders running in the browser.
- **Technologies Used:** `WebGL`, `GLSL Shaders`, `Three.js`, `Math Modeling`.
- **Visual Treatment:** Geometric wireframe torus with kinetic wave displacement preview.
- **Action CTAs:**
  - Status: `[ RESEARCH & DISCOVERY ]`

---

### SECTION 06: TRAJECTORY — CURRENT LEARNING FOCUS
**Intent:** Provide an authentic, compelling roadmap of what Zeerak is actively studying and building towards.

- **Visual Architecture: The Growth Vector Timeline:**
  A horizontal or staggered vertical roadmap featuring three vectors:
  1. **Active Mastery (In Progress):**
     - Modern JavaScript Engine Internals (V8 execution context, closures, event loop).
     - Responsive Grid & Subgrid Systems in Modern CSS.
     - Pointers, Dynamic Memory, and Linked Lists in C.
  2. **Next Frontier (Imminent Horizon):**
     - Custom GLSL Shaders & Three.js Post-Processing.
     - Web Accessibility (WCAG AAA Compliance & Assistive Navigation).
     - Component Architecture & Build Tooling (Vite, TypeScript fundamentals).
  3. **Vision:**
     - Becoming an award-winning creative technologist contributing to world-class interactive digital experiences.

---

### SECTION 07: CONTACT — TRANSMISSION TERMINAL
**Intent:** Monumental closing statement that makes initiating contact effortless, memorable, and visually dramatic.

- **Visual Design:**
  - Giant Display Typography:
    ```
    LET'S BUILD
    THE FUTURE.
    ```
    `Space Grotesk` Bold, `clamp(2.5rem, 7vw, 6rem)`, with subtle ambient violet backlighting.
  - Subhead: `"Have an opportunity, creative inquiry, or shared passion for code? My transmission line is always open."`
  - **One-Click Email Capsule:**
    - An oversized interactive pill element:
      `zeerak.shafique.dev@gmail.com` *(or configurable personal email token)*.
    - Features an interactive **"COPY TRANSMISSION ADDRESS"** button with dynamic feedback (`"COPIED TO CLIPBOARD // OK"`).
    - Secondary direct mail action: `[ OPEN IN CLIENT ↗ ]`.
  - **Direct Voice & Telemetry:**
    - Direct Phone Line: `+91 9580912686` (`tel:+919580912686`).
  - **Social Coordinates Cluster:**
    - GitHub: `[ GITHUB // REPOSITORIES ↗ ]` (`https://github.com/zeerak-shafique`)
    - LinkedIn: `[ LINKEDIN // NETWORK ↗ ]` (`https://linkedin.com/in/zeerak-shafique`)
    - Instagram / Creative Archive: `[ INSTAGRAM // VISUALS ↗ ]` (`@_siddiqui_._zeerak_` -> `https://www.instagram.com/_siddiqui_._zeerak_/`)
  - **System Telemetry Status:**
    - `RESPONSE TIME: < 24 HOURS`
    - `ENCRYPTION: TLS 1.3 STANDARD`

---

### SECTION 08: FOOTER & COLOPHON
**Intent:** Clean, editorial architectural closing.

- **Elements:**
  1. **Brand Signature:** `ZEERAK SHAFIQUE — CREATIVE DEVELOPER & BCA SCHOLAR`.
  2. **Colophon Specifications:** `CRAFTED WITH VANILLA HTML5, MODERN CSS & THREE.JS. ZERO FRAMEWORK OVERHEAD. 60 FPS.`
  3. **Real-Time World Clock:** `LOCAL TIME: NEW DELHI / IST (UTC+05:30) — [HH:MM:SS LIVE]`.
  4. **Back to Top Elevator Button:** `[ RETURN TO APEX ↑ ]` with smooth native scroll reset.
  5. **Copyright:** `© 2026 ZEERAK SHAFIQUE. ALL RIGHTS RESERVED.`

---

## 7. 3D GRAPHICS & VISUAL IMPLEMENTATION STRATEGY

### 7.1 Visual Concept: The Obsidian Monolith & Dual Orbital Rings
Rather than a generic rotating cube or random particle field, the signature hero visual is **"The Monolith of Logic & The Rings of Creativity"**:
- **The Core Monolith:** A tall, slender beveled rectangular prism (or stylized icosahedron) rendered in near-black obsidian material.
- **The Dual Orbital Rings:** Two concentric, delicate wireframe rings (torus or ring geometry) orbiting the monolith on intersecting axes (35° and -25° inclinations).
- **Metaphor:** The solid dark monolith represents the foundational, unyielding logic of **C and computer science**; the luminous, spinning orbital rings represent the fluid, expressive dynamism of **modern front-end development**.

```
             .----------------.
          .-'   .----------.   '-.
        .'    .'            '.    '.
       /     /                \     \       <-- Orbital Ring 1 (Electric Violet Wireframe)
      ;     ;   +----------+   ;     ;
      |     |   |          |   |     |
      |     |   | OBSIDIAN |   |     |      <-- Central Monolith (Specular Obsidian Mesh)
      |     |   | MONOLITH |   |     |
      ;     ;   +----------+   ;     ;
       \     \                /     /       <-- Orbital Ring 2 (Icy Cyan Wireframe)
        '.    '.            .'    .'
          '-.   '----------'   .-'
             '----------------'
```

### 7.2 Technical Implementation (Three.js via ESM / CDN)
- **Library Choice:** Vanilla Three.js loaded via native ES Module CDN (`https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.module.js` or `unpkg`).
- **Why this choice?**
  - Instant loading without requiring complex Node.js build pipelines or bundler configuration.
  - Zero lock-in: runs cleanly in vanilla HTML/CSS/JS.
  - Delivers hardware-accelerated WebGL performance.
- **Scene Composition:**
  1. **Renderer:**
     - `antialias: true` on desktop; `alpha: true` (transparent background allowing CSS radial gradients to shine through).
     - Device Pixel Ratio clamped strictly to `Math.min(window.devicePixelRatio, 2)` to eliminate GPU thermal throttling.
     - `powerPreference: "high-performance"`.
  2. **Materials & Shading:**
     - Monolith: `THREE.MeshStandardMaterial` with `color: 0x0C0E14`, `roughness: 0.15`, `metalness: 0.85`, with edge wireframe lines rendered in `0x8B5CF6`.
     - Rings: `THREE.MeshBasicMaterial` with `color: 0x00F2FE`, `wireframe: true`, and semi-transparent opacity `0.65`.
  3. **Cinematic Lighting:**
     - Ambient light: Low intensity (`0x111122`, intensity `0.4`).
     - Point Light 1 (Upper Left): Electric Violet (`0x8B5CF6`, intensity `2.5`, distance `10`).
     - Point Light 2 (Lower Right): Icy Cyan (`0x00F2FE`, intensity `2.0`, distance `10`).
  4. **Kinetic Behavior & Physics:**
     - Continuous slow resting gyration on Y and X axes.
     - **Pointer Interaction (Parallax):** Mouse coordinates mapped to normalized `-1` to `+1`. The camera or monolith targets the mouse position using smooth linear interpolation (Lerp):
       ```javascript
       mesh.rotation.y += (targetRotationY - mesh.rotation.y) * 0.05;
       mesh.rotation.x += (targetRotationX - mesh.rotation.x) * 0.05;
       ```
  5. **Scroll & Visibility Optimization:**
     - An `IntersectionObserver` monitors `#hero`. When scrolled out of the viewport, the `requestAnimationFrame` loop **pauses completely**, saving 100% GPU cycles while the visitor reads other sections.
  6. **Mobile & Graceful Degradation Fallback:**
     - On devices with WebGL disabled or mobile devices with battery saver active, the scene automatically hides and falls back to a pure CSS luminous geometric emblem (a pulsing glowing SVG wireframe polygon with animated CSS rotation).

---

## 8. INTERACTION & MOTION DESIGN LANGUAGE

### 8.1 Motion Philosophy
Animations must be **editorial, fluid, and purposeful**. No bouncing, no rubber-banding, no chaotic particle explosions. Every transition communicates structural solidity.

### 8.2 Standard Easing & Duration Tokens
- **Primary Fluid Ease:** `cubic-bezier(0.16, 1, 0.3, 1)` (Ultra-smooth deceleration, inspired by Apple & Awwwards best-in-class UI).
- **Fast Micro-interaction:** `180ms` (buttons, link highlights, border shifts).
- **Standard Transition:** `350ms` (card elevation, navigation drawer, accordion reveals).
- **Editorial Reveal:** `800ms – 1100ms` (section titles, hero typography, staggered text).

### 8.3 Interaction Specifications
1. **Magnetic Interactive Buttons:**
   - Buttons calculate cursor offset on `mousemove` and shift toward the cursor by up to 6px:
     ```javascript
     const deltaX = (e.clientX - rect.left - rect.width / 2) * 0.2;
     const deltaY = (e.clientY - rect.top - rect.height / 2) * 0.2;
     button.style.transform = `translate(${deltaX}px, ${deltaY}px)`;
     ```
2. **Scroll-Triggered Stagger Reveals:**
   - Uses `IntersectionObserver` with `threshold: 0.15`.
   - Elements enter with `opacity: 0; transform: translateY(32px);`.
   - When active: `opacity: 1; transform: translateY(0);` staggered by `80ms` per child.
3. **Card Perspective Hover Tilt:**
   - Skill cards and project showcases feature subtle 3D rotational tilt (`max: 5deg`) tracking cursor position, paired with a specular radial glare overlay.
4. **Custom Dual-State Cursor (Desktop Only):**
   - Inner dot (`4px x 4px`, `#00F2FE`).
   - Outer ring (`32px x 32px`, `rgba(139, 92, 246, 0.4)` border).
   - On hovering links or buttons, the outer ring expands to `56px` with `backdrop-filter: invert(1)` or violet glow.
   - Automatically disabled on touch screens and mobile devices (`@media (hover: none)`).

### 8.4 Reduced Motion Compliance (`prefers-reduced-motion`)
```css
@media (prefers-reduced-motion: reduce) {
  *, ::before, ::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
  .custom-cursor { display: none !important; }
  #three-hero-canvas { display: none !important; }
  .css-hero-fallback { display: block !important; }
}
```

---

## 9. ACCESSIBILITY (A11Y) REQUIREMENTS

1. **Semantic HTML5 DOM:**
   - Single `<h1>` on page (Hero section).
   - Hierarchical `<h2>` for each primary section, `<h3>` for nested cards.
   - Semantic landmarks: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`.
2. **Color Contrast:**
   - All body text (`#F8FAFC` and `#94A3B8`) on `#060709` and `#0C0E14` surfaces delivers contrast ratios exceeding **7:1** (AAA standard).
   - Accent cyan and violet meet AA standard (>= 4.5:1) for interactive elements and headlines.
3. **Keyboard Navigability & Focus Rings:**
   - All interactive elements (`<a>`, `<button>`, inputs) have distinct focus states:
     ```css
     :focus-visible {
       outline: 2px solid var(--accent-cyan);
       outline-offset: 4px;
       border-radius: 4px;
     }
     ```
   - Skip to main content link:
     ```html
     <a href="#main-content" class="skip-link">Skip to Content [Tab]</a>
     ```
4. **Screen Reader Transparency:**
   - Decorative visual elements (3D canvas, ambient background glows, technical ASCII lines) marked with `aria-hidden="true"`.
   - Live availability badge equipped with descriptive label:
     `<span class="status-dot" aria-hidden="true"></span><span class="sr-only">Status: Available for collaborations</span>`

---

## 10. PERFORMANCE & ENGINEERING STANDARDS

1. **Zero Framework Bloat / Vanilla Stack:**
   - The entire experience is engineered using **clean Vanilla HTML5, Modern CSS, and modular ES6+ JavaScript**.
   - No React, no Next.js, no bulky component library dependencies.
   - Initial HTML payload < 25KB, total CSS bundle < 35KB, JS logic < 40KB (excluding CDN Three.js).
2. **Core Web Vitals Thresholds:**
   - **Largest Contentful Paint (LCP):** < 1.2s.
   - **First Input Delay / INP:** < 50ms.
   - **Cumulative Layout Shift (CLS):** `0.00` (all dimensions explicitly reserved).
3. **Asset Optimization:**
   - Google Fonts loaded with `display=swap` and preconnect hints:
     ```html
     <link rel="preconnect" href="https://fonts.googleapis.com">
     <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
     ```
   - Vector graphics utilized for all telemetry badges and icons (inline SVG, zero HTTP roundtrips).
4. **Frame Budget:** Strict 60 FPS target maintained by leveraging `transform` and `opacity` exclusively for animations, triggering GPU compositing without layout recalculations.

---

## 11. RECOMMENDED PROJECT DIRECTORY ARCHITECTURE

To resolve the existing duplicate/nested folder anomaly cleanly during implementation, the codebase will adhere to this standard, professional file hierarchy:

```
c:\Users\siddi\Desktop\New folder\
├── DESIGN.md                   # Authoritative Design Specification (this document)
├── index.html                  # Root semantic HTML5 document
├── style.css                   # Master CSS architecture (design tokens, layout, styling)
├── script.js                   # Main application orchestration & lifecycle entry
└── assets/                     # Media & modular resources (optional future growth)
    ├── js/
    │   ├── scene3d.js          # Three.js scene setup, shaders, monolith & orbital rings
    │   ├── interactions.js     # Magnetic cursor, tilt physics, smooth scroll-spy
    │   └── telemetry.js        # World clock, preloader counter, clipboard transmission
    └── images/                 # Optimized project preview graphics (WebP format)
```

*(Note: During Phase 1 implementation, the AI agent will consolidate the project files directly at root level and clean up the empty nested directories).*

---

## 12. STEP-BY-STEP IMPLEMENTATION ACCEPTANCE CHECKLIST

Any AI coding agent or engineer implementing this website must satisfy every item on this checklist before marking the project complete:

### A. Preloader & Foundation
- [ ] Root `index.html` configured with proper meta tags, UTF-8 encoding, responsive viewport, SEO description, and Google Fonts (`Space Grotesk`, `Inter`, `JetBrains Mono`).
- [ ] CSS token system defined in `:root` with all exact HEX/RGBA colors, fluid clamp scales, and spacing constants.
- [ ] Fast, technical preloader HUD initializes, ticks to 100% in ~1s, and smoothly reveals the page.
- [ ] Preloader failsafe timeout (`1500ms`) present and tested.

### B. Navigation & Header
- [ ] Floating glassmorphism capsule navigation anchored at top of viewport with backdrop blur.
- [ ] Personal wordmark `ZS // 26` rendered with pulsing emerald status dot.
- [ ] Desktop navigation links functional with smooth scroll targets (`#about`, `#skills`, `#projects`, `#contact`).
- [ ] Active section scroll-spy updates navigation indicators as user scrolls.
- [ ] Fullscreen mobile navigation overlay responsive, tested, and functional on `< 768px`.

### C. Hero Section
- [ ] High-contrast, oversized typography introducing Zeerak Shafique with fluid responsive scaling.
- [ ] Subheading accurately portrays Zeerak as an aspiring creative developer and BCA student.
- [ ] Asymmetrical layout with telemetry coordinates and monospace sector badges.
- [ ] Dual action CTAs: `EXPLORE ARCHIVE [↓]` and `INITIALIZE CONTACT [↗]`.
- [ ] Three.js 3D canvas active, rendering the Obsidian Monolith with dual wireframe orbital rings.
- [ ] Mouse parallax smoothly tilts the 3D scene on desktop.
- [ ] `IntersectionObserver` halts Three.js render loop when scrolled past hero section.
- [ ] Pure CSS geometric fallback renders seamlessly if WebGL is unavailable.

### D. About Section
- [ ] Editorial two-column layout with authentic, dignified personal story.
- [ ] Honest depiction of BCA student journey; zero fabricated corporate experience or fake awards.
- [ ] Structured System Dossier with monospace telemetry tags and crosshair styling.

### E. Skills & Technology Section
- [ ] 4 Core Architectural Pillars displayed: HTML5, CSS3, JavaScript (ES6+), C Programming.
- [ ] Zero arbitrary percentage progress bars.
- [ ] Hover micro-interactions reveal live architectural code snippets and perspective tilt.

### F. Selected Works Section
- [ ] Bespoke project dossiers with index counters `[ 01 / 03 ]`.
- [ ] Project 01 features this living portfolio with live status tag and repository placeholder.
- [ ] Projects 02 and 03 present structured upcoming concepts (C algorithm visualizer, WebGL shader lab).
- [ ] Technologies, metadata, and preview treatments fully populated without broken links.

### G. Trajectory & Learning Focus
- [ ] Clear growth vector showing active focus areas and next learning horizons.
- [ ] Genuine, ambitious, and technically accurate tone.

### H. Contact Section & Footer
- [ ] Monumental display headline: `LET'S BUILD THE FUTURE.`
- [ ] One-click email copy capsule with clipboard confirmation feedback.
- [ ] Verified direct channels: Direct Phone Line (+91 9580912686) and Instagram (@_siddiqui_._zeerak_).
- [ ] Live Indian Standard Time (IST) world clock in footer.
- [ ] Smooth "Return to Apex" back-to-top button.

### I. Interactions, a11y & Performance
- [ ] Custom dual-state cursor active on desktop, hidden on touch screens.
- [ ] Complete `@media (prefers-reduced-motion: reduce)` support.
- [ ] Semantic HTML5 elements and full keyboard tab navigation verified.
- [ ] Zero horizontal scroll overflow on any screen size from 320px to 2560px.
- [ ] Smooth 60 FPS animations and fast page load times.

---

**END OF SPECIFICATION: DESIGN.md**  
*Ready for immediate implementation by any AI coding agent without requiring further design clarification.*
