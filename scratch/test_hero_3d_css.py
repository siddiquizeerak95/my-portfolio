# Test script to prepare 3D perspective hero CSS
css_content = """/* ==========================================================================
   12. 3D PERSPECTIVE HERO SHOWCASE & FLOATING MOCKUP RIG
   ========================================================================== */

/* Hero Section Base Spacing & Container */
.hero-3d-perspective-section {
  position: relative;
  overflow: hidden;
  padding-top: clamp(100px, 14vh, 150px);
  padding-bottom: clamp(70px, 9vh, 110px);
}

.hero-3d-split-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 1.15fr);
  align-items: center;
  gap: clamp(32px, 5vw, 64px);
  width: 100%;
}

.hero-3d-text-col {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  z-index: 3;
}

/* 3D Viewport Stage */
.hero-3d-viewport-col {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
}

.hero-3d-stage {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 600px;
  min-height: 560px;
  perspective: 1300px;
  transform-style: preserve-3d;
  margin: 0 auto;
}

/* Atmospheric Studio Ambient Glows */
.hero-3d-ambient-glow {
  position: absolute;
  width: clamp(360px, 42vw, 560px);
  height: clamp(360px, 42vw, 560px);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: radial-gradient(circle at 50% 50%, rgba(229, 9, 43, 0.14) 0%, rgba(229, 9, 43, 0.04) 45%, transparent 72%);
  pointer-events: none;
  z-index: 1;
  filter: blur(48px);
  border-radius: 50%;
}

.hero-3d-radial-crimson {
  position: absolute;
  width: 340px;
  height: 340px;
  top: 25%;
  right: 5%;
  background: radial-gradient(circle, rgba(229, 9, 43, 0.16) 0%, transparent 68%);
  filter: blur(52px);
  pointer-events: none;
  z-index: 1;
}

/* Master 3D Rig (Tilted, Floating & Interactive) */
.hero-3d-rig {
  position: relative;
  width: 100%;
  max-width: 520px;
  transform-style: preserve-3d;
  transform: rotateY(-15deg) rotateX(9deg) rotateZ(-2deg) translateZ(0);
  transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1);
  animation: hero3DFloat 7s ease-in-out infinite alternate;
  z-index: 2;
  display: flex;
  justify-content: center;
}

@keyframes hero3DFloat {
  0% {
    transform: rotateY(-15deg) rotateX(9deg) rotateZ(-2deg) translateY(-8px);
  }
  100% {
    transform: rotateY(-11deg) rotateX(6deg) rotateZ(-1deg) translateY(12px);
  }
}

/* Master Floating 3D Browser Window Mockup */
.mockup-window {
  position: relative;
  width: 100%;
  max-width: 500px;
  background: #141416;
  border: 1px solid #353535;
  border-radius: 18px;
  box-shadow: 
    0 35px 80px -15px rgba(0, 0, 0, 0.92),
    0 15px 35px -8px rgba(0, 0, 0, 0.75),
    0 0 45px rgba(229, 9, 43, 0.12),
    inset 0 1px 0 rgba(255, 255, 255, 0.15);
  overflow: hidden;
  transform-style: preserve-3d;
  transform: translateZ(0);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.mockup-window:hover {
  border-color: #555555;
  box-shadow: 
    0 45px 95px -15px rgba(0, 0, 0, 0.95),
    0 20px 45px -8px rgba(0, 0, 0, 0.8),
    0 0 55px rgba(229, 9, 43, 0.18),
    inset 0 1px 0 rgba(255, 255, 255, 0.22);
}

/* Browser Window Header Chrome */
.mockup-window-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 11px 16px;
  background: #19191B;
  border-bottom: 1px solid #2B2B2F;
}

.mockup-traffic-lights {
  display: flex;
  align-items: center;
  gap: 6px;
}

.light-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  display: inline-block;
}

.light-red {
  background: #E5092B;
  box-shadow: 0 0 6px rgba(229, 9, 43, 0.65);
}

.light-dim {
  background: #38383C;
}

.mockup-url-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border-radius: 20px;
  background: #0D0D0F;
  border: 1px solid #28282B;
  font-family: var(--font-mono, "SF Mono", Consolas, monospace);
  font-size: 11px;
  color: #A0A0A0;
  letter-spacing: 0.03em;
}

.url-lock-icon {
  color: #E5092B;
}

.mockup-header-actions {
  display: flex;
  align-items: center;
  gap: 6px;
  opacity: 0.5;
}

.action-dash {
  width: 8px;
  height: 1.5px;
  background: #888888;
  display: inline-block;
}

.action-square {
  width: 7px;
  height: 7px;
  border: 1px solid #888888;
  display: inline-block;
}

/* Mockup Screen Viewport Body */
.mockup-screen-body {
  padding: 16px;
  background: #101012;
}

.mockup-screen-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.95fr;
  gap: 14px;
  align-items: stretch;
}

/* Left Sub-panel: Design Architecture & Metrics */
.mockup-design-panel {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: #161619;
  border: 1px solid #2B2B2F;
  border-radius: 12px;
  padding: 14px;
}

.mockup-eyebrow {
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-mono, "SF Mono", monospace);
  font-size: 9.5px;
  color: #A0A0A0;
  letter-spacing: 0.08em;
  font-weight: 600;
  margin-bottom: 6px;
}

.mockup-red-dot {
  width: 5px;
  height: 5px;
  background: #E5092B;
  border-radius: 50%;
  box-shadow: 0 0 5px #E5092B;
}

.mockup-project-title {
  font-family: var(--font-display, "Space Grotesk", sans-serif);
  font-size: 15px;
  font-weight: 700;
  color: #F5F5F5;
  margin: 0 0 4px 0;
  line-height: 1.25;
}

.mockup-project-meta {
  font-size: 11px;
  color: #8E8E93;
  margin: 0 0 12px 0;
  line-height: 1.35;
}

/* Micro Preview Graph */
.mockup-preview-graph {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  background: #0E0E10;
  border: 1px solid #242427;
  border-radius: 8px;
  padding: 8px 10px;
  margin-bottom: 12px;
  gap: 8px;
}

.graph-bars-group {
  display: flex;
  align-items: flex-end;
  gap: 4px;
  height: 32px;
}

.preview-graph-bar {
  width: 5px;
  border-radius: 2px;
  background: #353538;
}

.preview-graph-bar.bar-1 { height: 14px; }
.preview-graph-bar.bar-2 { height: 22px; background: #55555C; }
.preview-graph-bar.bar-3 { height: 18px; }
.preview-graph-bar.bar-4 { height: 30px; background: #E5092B; box-shadow: 0 0 6px rgba(229, 9, 43, 0.6); }

.preview-metric-card {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.metric-val {
  font-family: var(--font-display, sans-serif);
  font-size: 13px;
  font-weight: 700;
  color: #F5F5F5;
  line-height: 1.1;
}

.metric-lbl {
  font-size: 9px;
  color: #8E8E93;
  letter-spacing: 0.02em;
}

.mockup-tag-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
}

.mockup-chip {
  font-family: var(--font-mono, monospace);
  font-size: 9px;
  color: #D1D1D6;
  background: #202024;
  border: 1px solid #333338;
  padding: 2px 7px;
  border-radius: 4px;
}

/* Right Sub-panel: High-Res Profile Portrait */
.mockup-portrait-panel {
  display: flex;
  align-items: stretch;
}

.mockup-portrait-frame {
  position: relative;
  width: 100%;
  min-height: 180px;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #2B2B2F;
  background: #0A0A0A;
}

.mockup-portrait-photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 50% 18%;
  display: block;
}

.mockup-portrait-vignette {
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 30%, transparent 60%, rgba(10, 10, 10, 0.45) 100%);
  pointer-events: none;
}

.mockup-portrait-gradient {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(10, 10, 10, 0.92) 0%, rgba(10, 10, 10, 0.3) 40%, transparent 70%);
  pointer-events: none;
}

.mockup-portrait-meta {
  position: absolute;
  bottom: 8px;
  left: 8px;
  right: 8px;
  display: flex;
  flex-direction: column;
  z-index: 2;
}

.portrait-name {
  font-family: var(--font-display, sans-serif);
  font-size: 11.5px;
  font-weight: 700;
  color: #FFFFFF;
  line-height: 1.2;
}

.portrait-role {
  font-size: 9px;
  color: #B5B5B5;
  letter-spacing: 0.02em;
}

/* Specular Glare On Window */
.mockup-specular-glare {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.06) 0%, transparent 40%, rgba(255, 255, 255, 0.02) 100%);
  pointer-events: none;
  z-index: 5;
}

/* ==========================================================================
   LAYERED FLOATING GLASS UI PANELS (True 3D translateZ Depth)
   ========================================================================== */
.floating-panel {
  position: absolute;
  z-index: 10;
  pointer-events: auto;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: transform;
}

.glass-panel-content {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  border-radius: 14px;
  background: rgba(22, 22, 25, 0.88);
  border: 1px solid rgba(255, 255, 255, 0.14);
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.75),
    0 6px 14px rgba(0, 0, 0, 0.5),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  white-space: nowrap;
}

/* Panel 1: Top-Left Design System Badge (translateZ: 75px) */
.floating-panel-topleft {
  top: -24px;
  left: -28px;
  transform: translateZ(75px);
  animation: floatPanelLeft 6s ease-in-out infinite alternate;
}

@keyframes floatPanelLeft {
  0% { transform: translateZ(75px) translateY(-5px); }
  100% { transform: translateZ(75px) translateY(7px); }
}

.panel-icon-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: #242428;
  border: 1px solid #38383D;
  color: #F5F5F5;
}

.panel-text-wrap {
  display: flex;
  flex-direction: column;
}

.panel-title {
  font-family: var(--font-display, sans-serif);
  font-size: 12px;
  font-weight: 700;
  color: #F5F5F5;
  line-height: 1.2;
}

.panel-subtitle {
  font-size: 10px;
  color: #A0A0A0;
}

.panel-status-dot {
  width: 6px;
  height: 6px;
  background: #30D158;
  border-radius: 50%;
  box-shadow: 0 0 6px rgba(48, 209, 88, 0.7);
  margin-left: 4px;
}

/* Panel 2: Bottom-Right Live Availability Card (translateZ: 95px) */
.floating-panel-bottomright {
  bottom: -24px;
  right: -24px;
  transform: translateZ(95px);
  animation: floatPanelRight 6.5s ease-in-out infinite alternate-reverse;
}

@keyframes floatPanelRight {
  0% { transform: translateZ(95px) translateY(-6px); }
  100% { transform: translateZ(95px) translateY(8px); }
}

.panel-avatar-wrap {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  overflow: hidden;
  border: 1.5px solid #E5092B;
  box-shadow: 0 0 8px rgba(229, 9, 43, 0.4);
  flex-shrink: 0;
}

.panel-avatar-thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 50% 15%;
}

.panel-badge-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 2px;
}

.panel-status-pulse {
  width: 6px;
  height: 6px;
  background: #E5092B;
  border-radius: 50%;
  box-shadow: 0 0 8px #E5092B;
  animation: pulseDot 2s infinite ease-in-out;
}

@keyframes pulseDot {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.4); opacity: 0.6; }
}

.panel-live-text {
  font-family: var(--font-mono, monospace);
  font-size: 9.5px;
  font-weight: 700;
  color: #E5092B;
  letter-spacing: 0.06em;
}

.panel-desc-highlight {
  font-size: 11px;
  font-weight: 500;
  color: #F5F5F5;
}

/* Panel 3: Top-Right Minimalist Code Tag (translateZ: 50px) */
.floating-panel-topright {
  top: 16px;
  right: -32px;
  transform: translateZ(50px);
  animation: floatPanelChip 5.5s ease-in-out infinite alternate;
}

@keyframes floatPanelChip {
  0% { transform: translateZ(50px) translateY(-4px); }
  100% { transform: translateZ(50px) translateY(6px); }
}

.glass-panel-content.chip-compact {
  padding: 6px 12px;
  border-radius: 20px;
  gap: 7px;
  border-color: rgba(229, 9, 43, 0.35);
}

.chip-code-symbol {
  font-family: var(--font-mono, monospace);
  font-size: 10.5px;
  font-weight: 700;
  color: #E5092B;
}

.chip-label {
  font-family: var(--font-mono, monospace);
  font-size: 10px;
  color: #E5E5EA;
  letter-spacing: 0.03em;
}

/* ==========================================================================
   LIGHT MODE ADAPTATIONS FOR 3D PERSPECTIVE HERO
   ========================================================================== */
:root[data-theme="light"] .mockup-window {
  background: #FFFFFF;
  border-color: #E2E2E6;
  box-shadow: 
    0 35px 80px -15px rgba(0, 0, 0, 0.15),
    0 15px 35px -8px rgba(0, 0, 0, 0.08),
    0 0 35px rgba(229, 9, 43, 0.08),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
}

:root[data-theme="light"] .mockup-window-header {
  background: #F4F4F6;
  border-bottom-color: #E5E5EA;
}

:root[data-theme="light"] .light-dim {
  background: #D1D1D6;
}

:root[data-theme="light"] .mockup-url-pill {
  background: #FFFFFF;
  border-color: #E0E0E4;
  color: #666668;
}

:root[data-theme="light"] .mockup-screen-body {
  background: #FAFAFC;
}

:root[data-theme="light"] .mockup-design-panel {
  background: #FFFFFF;
  border-color: #E5E5EA;
}

:root[data-theme="light"] .mockup-project-title {
  color: #111111;
}

:root[data-theme="light"] .mockup-project-meta {
  color: #666668;
}

:root[data-theme="light"] .mockup-preview-graph {
  background: #F3F3F6;
  border-color: #E5E5EA;
}

:root[data-theme="light"] .preview-graph-bar {
  background: #D1D1D6;
}

:root[data-theme="light"] .preview-graph-bar.bar-2 {
  background: #8E8E93;
}

:root[data-theme="light"] .metric-val {
  color: #111111;
}

:root[data-theme="light"] .mockup-chip {
  background: #F0F0F3;
  border-color: #E0E0E5;
  color: #333333;
}

:root[data-theme="light"] .mockup-portrait-frame {
  background: #F0F0F3;
  border-color: #E5E5EA;
}

:root[data-theme="light"] .glass-panel-content {
  background: rgba(255, 255, 255, 0.92);
  border-color: rgba(0, 0, 0, 0.08);
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.1),
    0 6px 14px rgba(0, 0, 0, 0.05),
    inset 0 1px 0 rgba(255, 255, 255, 1);
}

:root[data-theme="light"] .panel-icon-wrap {
  background: #F0F0F4;
  border-color: #E0E0E5;
  color: #111111;
}

:root[data-theme="light"] .panel-title {
  color: #111111;
}

:root[data-theme="light"] .panel-desc-highlight {
  color: #111111;
}

:root[data-theme="light"] .chip-label {
  color: #111111;
}

/* ==========================================================================
   RESPONSIVE BREAKPOINTS FOR 3D PERSPECTIVE HERO
   ========================================================================== */

/* Tablet (1024px and below) */
@media (max-width: 1024px) {
  .hero-3d-split-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .hero-3d-text-col {
    align-items: center;
    text-align: center;
  }

  .hero-3d-text-col .section-tag-row {
    margin-left: auto;
    margin-right: auto;
  }

  .hero-3d-text-col .hero-actions-row {
    justify-content: center;
  }

  .hero-3d-text-col .hero-stats-row {
    justify-content: center;
  }

  .hero-3d-stage {
    max-width: 500px;
    min-height: 500px;
  }

  .hero-3d-rig {
    transform: rotateY(-10deg) rotateX(6deg) scale(0.92);
  }

  .floating-panel-topleft {
    left: -14px;
  }

  .floating-panel-bottomright {
    right: -14px;
  }

  .floating-panel-topright {
    right: -16px;
  }
}

/* Mobile (768px and below) */
@media (max-width: 768px) {
  .hero-3d-perspective-section {
    padding-top: 90px;
    padding-bottom: 50px;
  }

  .hero-3d-split-grid {
    display: flex !important;
    flex-direction: column !important;
    gap: 32px !important;
    text-align: left !important;
  }

  .hero-3d-text-col {
    width: 100% !important;
    align-items: flex-start !important;
    text-align: left !important;
  }

  .hero-3d-text-col .section-tag-row {
    margin-left: 0 !important;
    margin-right: 0 !important;
  }

  .hero-3d-text-col .hero-actions-row {
    width: 100% !important;
    flex-direction: column !important;
    gap: 12px !important;
  }

  .hero-3d-text-col .hero-actions-row .btn-pill-grey {
    width: 100% !important;
    justify-content: center !important;
  }

  .hero-3d-text-col .hero-stats-row {
    width: 100% !important;
    justify-content: space-between !important;
    gap: 8px !important;
  }

  .hero-3d-viewport-col {
    width: 100% !important;
    overflow: visible !important;
  }

  .hero-3d-stage {
    width: 100% !important;
    max-width: 360px !important;
    min-height: 420px !important;
    perspective: 1000px !important;
  }

  .hero-3d-rig {
    max-width: 340px !important;
    transform: rotateY(-6deg) rotateX(4deg) translateZ(0) !important;
    animation: none !important;
  }

  .mockup-window {
    max-width: 340px !important;
    border-radius: 14px !important;
  }

  .mockup-window-header {
    padding: 8px 12px !important;
  }

  .mockup-url-pill {
    padding: 2px 8px !important;
    font-size: 9.5px !important;
  }

  .mockup-screen-body {
    padding: 10px !important;
  }

  .mockup-screen-grid {
    grid-template-columns: 1fr !important;
    gap: 10px !important;
  }

  .mockup-portrait-frame {
    height: 180px !important;
    min-height: 180px !important;
  }

  /* Safe positioning for floating panels on mobile without overflow */
  .floating-panel-topleft {
    top: -16px !important;
    left: -6px !important;
    transform: translateZ(40px) scale(0.85) !important;
    animation: none !important;
  }

  .floating-panel-bottomright {
    bottom: -16px !important;
    right: -6px !important;
    transform: translateZ(50px) scale(0.85) !important;
    animation: none !important;
  }

  .floating-panel-topright {
    display: none !important; /* Hide extra chip on small phones to prevent clutter */
  }

  .hero-watermark-vertical {
    display: none !important;
  }
}

/* Reduced Motion Preference */
@media (prefers-reduced-motion: reduce) {
  .hero-3d-rig,
  .floating-panel-topleft,
  .floating-panel-bottomright,
  .floating-panel-topright {
    animation: none !important;
    transform: none !important;
    transition: none !important;
  }
  .mockup-window {
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5) !important;
  }
}
"""

with open(r'c:\Users\siddi\Desktop\New folder\scratch\hero_3d_perspective.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("hero_3d_perspective.css written successfully!")

