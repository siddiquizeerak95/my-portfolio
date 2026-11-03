# Script to update style.css and script.js for the exact Video Reference Hero

css_content = """/* ==========================================================================
   12. EXACT VIDEO REFERENCE HERO REDESIGN (ZS STUDIO)
   ========================================================================== */

.hero-video-reference-section {
  position: relative;
  overflow: hidden;
  padding-top: clamp(100px, 13vh, 140px);
  padding-bottom: clamp(50px, 7vh, 80px);
}

.hero-reference-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr);
  align-items: center;
  gap: clamp(32px, 5vw, 64px);
  width: 100%;
}

.hero-reference-text-col {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  z-index: 3;
}

/* "I am a" Connector phrase from video */
.hero-iam-connector {
  font-family: var(--font-display, "Space Grotesk", sans-serif);
  font-size: clamp(26px, 3vw, 38px);
  font-weight: 500;
  color: #8E8E93;
  margin: 4px 0 16px 0;
  line-height: 1.1;
  letter-spacing: -0.01em;
}

/* ==========================================================================
   THE 3D SPIRAL NOTEBOOK / FLIP CARD (Exact from reference video)
   ========================================================================== */
.hero-spiral-3d-stage {
  position: relative;
  width: 100%;
  max-width: 440px;
  perspective: 1100px;
  transform-style: preserve-3d;
  margin-bottom: 24px;
}

.hero-spiral-card {
  position: relative;
  width: 100%;
  height: 82px;
  background: #FFFFFF;
  border-radius: 14px;
  border: 1px solid rgba(0, 0, 0, 0.08);
  box-shadow: 
    0 24px 50px -10px rgba(0, 0, 0, 0.85),
    0 10px 20px -5px rgba(0, 0, 0, 0.5),
    0 0 35px rgba(229, 9, 43, 0.12),
    inset 0 -2px 0 rgba(0, 0, 0, 0.08);
  transform: rotateZ(-1.2deg) rotateX(4deg) translateZ(0);
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease;
  overflow: visible;
  display: flex;
  align-items: center;
  padding: 0 24px;
}

.hero-spiral-card:hover {
  transform: rotateZ(-0.5deg) rotateX(1deg) translateY(-3px) scale(1.02);
  box-shadow: 
    0 30px 65px -10px rgba(0, 0, 0, 0.9),
    0 15px 25px -5px rgba(0, 0, 0, 0.6),
    0 0 45px rgba(229, 9, 43, 0.18);
}

/* 10 Metallic Spiral Binding Rings */
.spiral-binding-rings {
  position: absolute;
  top: -16px;
  left: 20px;
  right: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  pointer-events: none;
  z-index: 10;
}

.spiral-ring-item {
  position: relative;
  width: 10px;
  height: 28px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.ring-wire {
  position: absolute;
  top: 0;
  width: 8px;
  height: 24px;
  border-radius: 6px;
  border: 2px solid #55555C;
  background: linear-gradient(135deg, #DDDDDF 0%, #444448 40%, #77777D 75%, #FFFFFF 100%);
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.45);
}

.ring-hole {
  position: absolute;
  top: 14px;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #222226;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.8);
}

/* Spiral Card Body & Flip Content */
.spiral-card-body {
  position: relative;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 6px;
}

.spiral-card-content {
  position: relative;
  height: 42px;
  display: flex;
  align-items: center;
  perspective: 800px;
}

.spiral-role-text {
  position: absolute;
  left: 0;
  font-family: var(--font-display, "Space Grotesk", sans-serif);
  font-size: clamp(24px, 2.7vw, 34px);
  font-weight: 700;
  color: #111111;
  letter-spacing: -0.02em;
  white-space: nowrap;
  opacity: 0;
  transform: rotateX(80deg) translateY(10px);
  transform-origin: 50% 100%;
  transition: opacity 0.45s ease, transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  pointer-events: none;
}

.spiral-role-text.active {
  opacity: 1;
  transform: rotateX(0deg) translateY(0);
  pointer-events: auto;
}

.spiral-role-text.exit-up {
  opacity: 0;
  transform: rotateX(-80deg) translateY(-10px);
  transform-origin: 50% 0%;
}

.spiral-card-corner-page {
  font-family: var(--font-mono, monospace);
  font-size: 11px;
  font-weight: 600;
  color: #8E8E93;
  letter-spacing: 0.04em;
}

.spiral-card-sheen {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.4) 0%, transparent 40%, rgba(0, 0, 0, 0.03) 100%);
  pointer-events: none;
  border-radius: 14px;
}

/* ==========================================================================
   RIGHT COLUMN: EDITORIAL PORTRAIT (Exact from reference video)
   ========================================================================== */
.hero-reference-portrait-col {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
}

.hero-reference-portrait-stage {
  position: relative;
  width: 100%;
  max-width: 460px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-portrait-ambient-glow {
  position: absolute;
  width: clamp(340px, 38vw, 500px);
  height: clamp(400px, 44vw, 580px);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: radial-gradient(ellipse at 50% 45%, rgba(229, 9, 43, 0.12) 0%, rgba(255, 255, 255, 0.03) 40%, transparent 72%);
  pointer-events: none;
  z-index: 1;
  filter: blur(40px);
  border-radius: 50%;
}

.hero-reference-portrait-card {
  position: relative;
  z-index: 2;
  width: clamp(300px, 30vw, 420px);
  height: clamp(440px, 42vw, 560px);
  border-radius: 22px;
  overflow: hidden;
  background: #0A0A0A;
  border: 1px solid #353535;
  box-shadow: 0 30px 70px rgba(0, 0, 0, 0.85), 0 0 40px rgba(229, 9, 43, 0.08);
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease;
}

.hero-reference-portrait-card:hover {
  transform: translateY(-4px) scale(1.01);
  box-shadow: 0 36px 85px rgba(0, 0, 0, 0.95), 0 0 50px rgba(229, 9, 43, 0.14);
}

.hero-reference-portrait-img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: 50% 18% !important;
  display: block !important;
}

.hero-portrait-vignette {
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 32%, transparent 62%, rgba(10, 10, 10, 0.5) 100%);
  pointer-events: none;
}

.hero-portrait-fade-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 38%;
  background: linear-gradient(to top, #0A0A0A 0%, rgba(10, 10, 10, 0.45) 60%, transparent 100%);
  pointer-events: none;
}

/* Floating Ability Badge on Chest/Jacket (Exact from reference video) */
.hero-floating-ability-badge {
  position: absolute;
  bottom: 24px;
  left: 20px;
  z-index: 5;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: 20px;
  background: rgba(18, 18, 20, 0.88);
  border: 1px solid rgba(255, 255, 255, 0.16);
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
}

.badge-status-dot {
  width: 7px;
  height: 7px;
  background: #E5092B;
  border-radius: 50%;
  box-shadow: 0 0 8px #E5092B;
  animation: pulseDot 2s infinite ease-in-out;
}

.badge-ability-text {
  font-family: var(--font-display, sans-serif);
  font-size: 11px;
  font-weight: 600;
  color: #F5F5F5;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

/* ==========================================================================
   BOTTOM REFERENCE TICKER BAR (Exact from reference video)
   ========================================================================== */
.hero-reference-bottom-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  margin-top: clamp(40px, 6vh, 64px);
  padding-top: 18px;
  border-top: 1px solid #262626;
  font-family: var(--font-mono, monospace);
  font-size: 11px;
  color: #8E8E93;
  letter-spacing: 0.05em;
}

.bottom-bar-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.status-pulse-dot {
  width: 6px;
  height: 6px;
  background: #30D158;
  border-radius: 50%;
  box-shadow: 0 0 6px rgba(48, 209, 88, 0.75);
}

/* ==========================================================================
   LIGHT MODE ADAPTATIONS
   ========================================================================== */
:root[data-theme="light"] .hero-iam-connector {
  color: #666668;
}

:root[data-theme="light"] .hero-spiral-card {
  background: #FFFFFF;
  border-color: #E2E2E6;
  box-shadow: 
    0 20px 45px -10px rgba(0, 0, 0, 0.12),
    0 8px 16px -5px rgba(0, 0, 0, 0.06),
    0 0 25px rgba(229, 9, 43, 0.06);
}

:root[data-theme="light"] .ring-wire {
  border-color: #C0C0C6;
  background: linear-gradient(135deg, #FFFFFF 0%, #B8B8C0 50%, #E8E8EE 100%);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
}

:root[data-theme="light"] .ring-hole {
  background: #D8D8DE;
}

:root[data-theme="light"] .spiral-role-text {
  color: #111111;
}

:root[data-theme="light"] .hero-reference-portrait-card {
  background: #FFFFFF;
  border-color: #E2E2E6;
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.08);
}

:root[data-theme="light"] .hero-portrait-fade-bottom {
  background: linear-gradient(to top, #FFFFFF 0%, rgba(255, 255, 255, 0.4) 60%, transparent 100%);
}

:root[data-theme="light"] .hero-floating-ability-badge {
  background: rgba(255, 255, 255, 0.92);
  border-color: rgba(0, 0, 0, 0.08);
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.08);
}

:root[data-theme="light"] .badge-ability-text {
  color: #111111;
}

:root[data-theme="light"] .hero-reference-bottom-bar {
  border-top-color: #E2E2E6;
  color: #666668;
}

/* ==========================================================================
   RESPONSIVE BREAKPOINTS
   ========================================================================== */
@media (max-width: 1024px) {
  .hero-reference-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .hero-reference-text-col {
    align-items: center;
    text-align: center;
  }

  .hero-reference-text-col .section-tag-row {
    margin-left: auto;
    margin-right: auto;
  }

  .hero-spiral-3d-stage {
    margin-left: auto;
    margin-right: auto;
  }

  .hero-reference-text-col .hero-actions-row {
    justify-content: center;
  }

  .hero-reference-text-col .hero-stats-row {
    justify-content: center;
  }
}

@media (max-width: 768px) {
  .hero-video-reference-section {
    padding-top: 90px;
    padding-bottom: 50px;
  }

  .hero-reference-grid {
    display: flex !important;
    flex-direction: column !important;
    gap: 32px !important;
    text-align: left !important;
  }

  .hero-reference-text-col {
    order: 1 !important;
    width: 100% !important;
    align-items: flex-start !important;
    text-align: left !important;
  }

  .hero-reference-text-col .section-tag-row {
    margin-left: 0 !important;
    margin-right: 0 !important;
  }

  .hero-spiral-3d-stage {
    max-width: 100% !important;
    margin-left: 0 !important;
  }

  .hero-spiral-card {
    height: 74px !important;
    padding: 0 18px !important;
  }

  .spiral-role-text {
    font-size: 24px !important;
  }

  .hero-reference-text-col .hero-actions-row {
    width: 100% !important;
    flex-direction: column !important;
    gap: 12px !important;
  }

  .hero-reference-text-col .hero-actions-row .btn-pill-grey {
    width: 100% !important;
    justify-content: center !important;
  }

  .hero-reference-text-col .hero-stats-row {
    width: 100% !important;
    justify-content: space-between !important;
    gap: 8px !important;
  }

  .hero-reference-portrait-col {
    order: 2 !important;
    width: 100% !important;
  }

  .hero-reference-portrait-card {
    width: 100% !important;
    max-width: 340px !important;
    height: 440px !important;
    margin: 0 auto !important;
  }

  .hero-reference-bottom-bar {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 8px !important;
  }

  .hero-watermark-vertical {
    display: none !important;
  }
}
"""

with open(r'c:\Users\siddi\Desktop\New folder\scratch\hero_video_reference.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("hero_video_reference.css created!")

