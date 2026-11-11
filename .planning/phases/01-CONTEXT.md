# Phase 1 Context: Repository Hygiene & Storage Pruning

Authoritative implementation decisions, file targets, and verification criteria locked during the Phase 1 discussion.

---

## 1. Locked Technical Decisions

| Area | Decision | Rationale |
| :--- | :--- | :--- |
| **Point-Cloud Assets (~45 MB)** | **Direct Permanent Deletion** from `assets/` | Git commit history retains complete historical records; removing them directly immediately cuts clone times and drops repository size by >70%. |
| **Root Screenshots (112 PNGs)** | **Move to `scratch/screenshots/`** | `scratch/` is already gitignored. Moving these files clears root clutter instantly while keeping visual test history available locally for reference. |
| **Stale Backup Files (`.bak`, `.orig`)** | **Permanent Deletion** | All 11 `.bak` files and `.orig` files are stale snapshot duplicates. Full version history is safely managed in Git commits. |
| **Lightweight SVGs & Storyboards** | **Preserve in `assets/`** | Files like `assets/footer-horizon-waves.svg` and `assets/reference_intro_storyboard.jpg` are lightweight (<400 KB) and preserved for future UI enhancements. |

---

## 2. File Execution Targets

### 2.1 Target Unreferenced 3D Point-Cloud Files to Delete
```
assets/scrolldriven-portrait.json      (31.77 MB)
assets/scrolldriven-portrait.bin       (6.30 MB)
assets/pointcloud-portrait.json        (2.54 MB)
assets/hybrid-portrait.json            (2.22 MB)
assets/sculpture-particles.json        (1.29 MB)
assets/pointcloud-portrait.bin         (1.07 MB)
assets/hybrid-portrait.bin             (1.02 MB)
--------------------------------------------------
Total Space to Reclaim:                ~46.21 MB
```

### 2.2 Target Root PNG Screenshots to Move into `scratch/screenshots/`
All 112 root-level PNG captures matching:
- `preview_*.png`
- `test_*.png`
- `seq_*.png`
- `current_hero_screenshot.png`

*(Note: Production brand assets `New fav icon.png`, `portrait photograph.png`, `zeerak-portrait-clean.png`, and `zeerak_daniel_transparent.png` remain preserved).*

### 2.3 Target Stale Backup Files to Delete
```
about.html.bak
blog.html.bak
blog-how-i-built-my-portfolio.html.bak
blog-my-journey-as-a-developer.html.bak
blog-why-i-prefer-minimalist-web-design.html.bak
contact.html.bak
index.html.bak
projects.html.bak
sculpture-intro.css.bak
sculpture-intro.js.bak
skills.html.bak
NEW IMAGE FOR WEBSITE.jpeg.orig
```

---

## 3. Preserved Asset Verification Checklist

The following active production assets must **NOT** be touched:
- [x] All 13 celestial textures in `assets/cosmos/`
- [x] Interface audio in `assets/audio/mixkit-sci-fi-interface-robot-click-901.wav`
- [x] Public key in `assets/keys/zeerak_public.asc`
- [x] All vector diagrams and icons in `assets/*.svg`
- [x] Production photography (`new image.jpeg`, `New fav icon.png`, `zs-monogram.svg`)

---

## 4. Phase 1 Verification Exit Gate

1. `assets/` total size drops from **62.6 MB** to under **17 MB**.
2. Root directory is clean of test PNGs and `.bak` files.
3. Run `python verify_console_errors.py` against local server: **14/14 pages must report 0 console errors**.

