# Coding Conventions & Design Guidelines

Authoritative standards, design rules, naming conventions, and architectural constraints governing the **ZS STUDIO** codebase.

---

## 1. Visual & Design System Constraints (Authoritative DESIGN.md)

All user interface modifications must strictly adhere to **`DESIGN.md` (v10.0 Master Design Specification)**:

### 1.1 Strict Monochromatic Palette
- **Rule:** The UI is strictly monochromatic (Black, White, Neutral Grays).
- **Prohibited:** No cyan, blue, gold, yellow, purple, or multi-color gradients on UI elements.
- **Allowed Exception:** Pure Crimson (`#E5092B`) is restricted exclusively to the 3D astrophotography space stage (`sculpture-intro.js`) and small accent highlights (such as the footer heart symbol).

### 1.2 Button Color Constraint: NO RED BUTTONS
- **Rule:** Interactive buttons and calls-to-action must **never** be rendered in red.
- **Standards:**
  - **Primary CTA:** High-contrast solid fill (Dark mode: `#F5F5F5` bg, `#080808` text; Light mode: `#0A0A0A` bg, `#FFFFFF` text).
  - **Secondary CTA / Grey Buttons:** Grey tokens (`--btn-grey-bg: #1E1E1E`, `--btn-grey-border: #3A3A3A`, `--btn-grey-text: #F5F5F5`, hover `#2A2A2A`).

### 1.3 Natural Portrait Photography
- **Rule:** Profile imagery (`new%20image.jpeg`) must retain natural human proportions.
- **Styling:** Tasteful black-and-white conversion (`filter: grayscale(100%) contrast(1.06) brightness(0.96);`), subtle hairline borders (`#292929`), and soft radial backlighting (`::before` grayscale halo). No neon glow or glowing sci-fi borders.

### 1.4 Universal Identity Accuracy
- **Rule:** All titles, copyright notices, headers, metadata, and colophons must universally read **"Zeerak Siddiqui"** (Brand mark: **"ZEERAK"** / **"ZS STUDIO"**).

---

## 2. Design Token System (CSS Custom Properties)

Tokens are declared on `:root` (dark default) and overridden under `[data-theme="light"]`:

```css
:root {
  /* Surfaces */
  --bg-main: #080808;
  --bg-secondary: #111111;
  --bg-card: #1A1A1A;
  --bg-card-elevated: #222222;

  /* Typography */
  --text-primary: #F5F5F5;
  --text-secondary: #A0A0A0;
  --text-muted: #707070;

  /* Hairline Borders */
  --border-subtle: #292929;
  --border-divider: #292929;
  --border-hover: #444444;

  /* Grey Button System */
  --btn-grey-bg: #1E1E1E;
  --btn-grey-border: #3A3A3A;
  --btn-grey-text: #F5F5F5;
  --btn-grey-hover-bg: #2A2A2A;

  /* 3D Spatial Properties */
  --perspective-camera: 1100px;
  --card-shadow-3d: 0 16px 36px -10px rgba(0, 0, 0, 0.75), 0 2px 10px rgba(0, 0, 0, 0.35);
}

[data-theme="light"] {
  --bg-main: #FFFFFF;
  --bg-secondary: #F5F5F5;
  --bg-card: #FFFFFF;
  --text-primary: #111111;
  --text-secondary: #666666;
  --border-subtle: #E5E5E5;
  --btn-grey-bg: #F0F0F0;
  --btn-grey-border: #D0D0D0;
  --btn-grey-text: #111111;
}
```

---

## 3. Typography Standards

| Font Family | Applied Elements | Loading Strategy |
| :--- | :--- | :--- |
| **`Cormorant Garamond`** | Hero focal name ("Zeerak Siddiqui"), page titles, editorial quotes | Google Fonts `preconnect` |
| **`Inter`** | Navigation, body copy, lead descriptions, buttons, sub-labels | Google Fonts `preconnect` |
| **`Space Grotesk`** | Display headlines, card titles, category headers | Google Fonts `preconnect` |
| **`IBM Plex Mono` / `JetBrains Mono`** | Telemetry, section numbers (`01`, `02`), technical badges, metadata | Google Fonts `preconnect` |

- **ZEERAK Wordmark Standard:** `Inter` uppercase, `letter-spacing: 0.22em`, semibold (`font-weight: 600`).
- **Section Label Standard:** Monospace uppercase with tracking (`12px`, letter-spacing `2.5px`).

---

## 4. HTML & Accessibility Standards

- **Zero Flash Theme Init:** Every HTML file must include this synchronous script in `<head>` before any stylesheet link:
  ```html
  <script>
    (function () {
      const savedTheme = localStorage.getItem('zs_theme') || 'dark';
      document.documentElement.setAttribute('data-theme', savedTheme);
    })();
  </script>
  ```
- **Skip Links:** Primary landmark link `<a href="#main-content" class="skip-link">Skip to Primary Content [Tab]</a>` placed directly below `<body>`.
- **Landmarks & ARIA:**
  - Decorative canvases and background SVGs must include `aria-hidden="true"`.
  - Live status telemetry must use `aria-live="polite"`.
  - Icon-only links and buttons must carry explicit `aria-label` attributes.
- **Page Categorization:** The `<body>` tag must define a `data-page` attribute corresponding to its route (`home`, `about`, `projects`, `skills`, `blog`, `contact`, `case-study`).

---

## 5. CSS Coding Standards

- **Naming Convention:** BEM-inspired hyphenated lowercase naming (`.site-header`, `.header-container`, `.nav-item`, `.card-title`, `.btn-primary`).
- **Responsive Breakpoints:**
  - `1200px`: Desktop widescreen container max-width.
  - `992px`: Medium desktop / tablet landscape adjustments.
  - `860px`: Critical navigation switch point (desktop horizontal navbar collapses to mobile drawer toggle).
  - `768px`: Tablet portrait vertical stack.
  - `480px`: Mobile card full-width padding.
  - `360px`: Narrow phone typography clamping.
- **Accessibility & Reduced Motion:** All animations, floating loops, and particle transforms must be disabled or simplified inside `@media (prefers-reduced-motion: reduce)`:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
      scroll-behavior: auto !important;
    }
  }
  ```

---

## 6. JavaScript Coding Standards

- **Modular Encapsulation:** Group distinct functional systems into ES6 classes or self-contained initialization functions (`initHeaderScroll`, `initCardTilt`, `initCustomCursor`).
- **Defensive DOM Querying:** Always guard DOM operations to prevent errors on pages where specific elements do not exist:
  ```javascript
  const target = document.getElementById('target-element');
  if (!target) return;
  ```
- **Performance Optimization:**
  - Passive event listeners on high-frequency events: `window.addEventListener('scroll', fn, { passive: true });`.
  - Canvas drawing operations locked to `requestAnimationFrame`.
  - Dynamic scaling factoring `window.devicePixelRatio`, capped at `2.0` to preserve mobile GPU performance.
- **Formatting & Banners:** Use standardized section comment banners:
  ```javascript
  // -----------------------------------------------------------------------------
  // 01. SUBSYSTEM NAME (PURPOSE AND RESPONSIBILITY)
  // -----------------------------------------------------------------------------
  ```

