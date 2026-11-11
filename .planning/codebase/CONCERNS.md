# Technical Concerns, Debt & Bottlenecks

Authoritative audit of technical debt, architectural risks, performance bottlenecks, and security considerations identified in the **ZS STUDIO** codebase.

---

## 1. Critical Findings Summary

| Severity | Issue | Impact | Location |
| :--- | :--- | :--- | :--- |
| **HIGH** | **Unreferenced Heavy 3D Assets (~45 MB)** | Repository bloat, slow clone times, asset storage waste | `assets/*.json`, `assets/*.bin` |
| **MEDIUM** | **Root Directory File Pollution** | 112 `.png` test screenshots and 11 `.bak` files in root | Root directory (`./`) |
| **MEDIUM** | **Monolithic Stylesheet (9,407 LOC)** | Difficult maintenance, selector conflicts, duplicate token blocks | `style.css` |
| **MEDIUM** | **Cryptographic Key Co-location** | Risk of accidental exposure or staging of private key | `keys/zeerak_private_KEY_KEEP_SAFE.asc` |
| **LOW** | **Vendor Dependency Drift** | Unmanaged client vendor builds without security patch updates | `vendor/*.min.js` |
| **LOW** | **Local Scratch Directory Size** | Disk consumption from browser profiles and temporary audit scripts | `scratch/` |

---

## 2. In-Depth Technical Debt Analysis

### 2.1 Heavy Unreferenced 3D Point-Cloud Files (~45 MB)
- **Detail:** The `assets/` directory contains several large binary and JSON point cloud files created during previous 3D facial sculpture experiments:
  - `assets/scrolldriven-portrait.json`: **31.77 MB**
  - `assets/scrolldriven-portrait.bin`: **6.30 MB**
  - `assets/pointcloud-portrait.json`: **2.54 MB**
  - `assets/hybrid-portrait.json`: **2.22 MB**
  - `assets/sculpture-particles.json`: **1.29 MB**
  - `assets/pointcloud-portrait.bin`: **1.07 MB**
  - `assets/hybrid-portrait.bin`: **1.02 MB**
- **Code Audit:** A global regex search confirms that **none** of these files are loaded or referenced by `index.html`, `script.js`, `sculpture-intro.js`, or `style.css`. The active 3D opening engine relies entirely on procedural geometries and the textures in `assets/cosmos/`.
- **Recommendation:** Archive these files outside the repository or move them to a dedicated historical storage branch to reduce repo size by over 70%.

### 2.2 Root Directory File Pollution (Screenshots & Backups)
- **Detail:** There are **112 PNG screenshot files** (e.g., `preview_*.png`, `test_*.png`, `seq_*.png`) and **11 `.bak` backup files** residing directly in the project root directory.
- **Risk:**
  - Clutters file trees and makes navigating core project files difficult.
  - Risk of accidentally committing binary test snapshots to version control.
  - Backup files (`about.html.bak`, `index.html.bak`) represent stale code snapshots that bypass git history.
- **Recommendation:** Move all audit screenshots into an ignored folder (e.g., `scratch/screenshots/` or `tests/artifacts/`) and remove `.bak` files in favor of git commit history.

### 2.3 Monolithic Stylesheet (`style.css` — 9,407 lines)
- **Detail:** `style.css` has grown to 9,407 lines without a preprocessor or module bundler.
- **Identified Issues:**
  - Token redeclarations: Variables such as `--bg-main`, `--bg-secondary`, `--text-primary`, and `--border-subtle` are declared in multiple `:root` blocks with differing values.
  - Legacy overrides: Contains remnants of earlier sci-fi/cyan themes alongside the authoritative Swiss Minimalist system.
  - Hard to maintain: Editing component styles requires searching through thousands of lines with potential selector inheritance side effects.
- **Recommendation:** Split `style.css` into logical modular partials (e.g., `tokens.css`, `base.css`, `header.css`, `hero.css`, `components.css`, `pages.css`) or compile via PostCSS/LightningCSS.

### 2.4 Cryptographic Private Key Co-location
- **Detail:** The offline private key `keys/zeerak_private_KEY_KEEP_SAFE.asc` is stored inside the workspace.
- **Current Safeguard:** It is properly matched by `.gitignore` (`keys/*private*`), and git currently ignores it.
- **Residual Risk:** Keeping private keys on disk adjacent to a project repository carries risk of accidental force-adding (`git add -f keys/`), exposure through backup tools, or directory copying.
- **Recommendation:** Store the private key in standard GnuPG keyrings (`~/.gnupg`) or a secure password manager rather than keeping the raw `.asc` file inside the workspace folder.

### 2.5 Dual Architectural Style Tension
- **Detail:** The project bridges two distinct aesthetic philosophies:
  1. *The 3D Space Intro (`sculpture-intro.js`):* High-immersion astrophotography with stars, asteroids, gas giants, and crimson telemetry.
  2. *The Editorial Homepage (`DESIGN.md`):* Strict Swiss Minimalism, monochromatic B&W palettes, luxury serif typography, and zero flashy animations.
- **Risk:** Changes made to alignment, lighting, or scroll behavior on one side can unintentionally destabilize the transition into the other (e.g. scroll jumping or contrast flash during dissolution).

### 2.6 Self-Hosted Vendor Drift
- **Detail:** `vendor/three.min.js`, `vendor/gsap.min.js`, `vendor/ScrollTrigger.min.js`, and `vendor/openpgp.min.js` are self-hosted static files without package lockfile version pins or automated security vulnerability scanning (`npm audit`).
- **Recommendation:** Track client dependencies via `package.json` with an automated build step (or explicit version tracking documentation) so security updates to OpenPGP.js or Three.js can be applied smoothly.

