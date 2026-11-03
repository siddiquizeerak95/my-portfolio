import os

css_block = """

/* ==========================================================================
   12. EDITORIAL RECTANGULAR HERO PORTRAIT REDESIGN
   ========================================================================== */

/* Remove any legacy circular rules */
.hero-visual-stage,
.hero-portrait-wrap,
.hero-red-halo {
  border-radius: 0 !important;
}

/* Editorial Stage Container */
.hero-editorial-stage {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 520px;
  min-height: 580px;
  margin: 0 auto;
}

/* Subtle Cinematic Studio Glow Behind Card */
.hero-editorial-ambient-glow {
  position: absolute;
  width: clamp(340px, 34vw, 480px);
  height: clamp(420px, 44vw, 600px);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: radial-gradient(ellipse at 50% 45%, rgba(229, 9, 43, 0.08) 0%, rgba(255, 255, 255, 0.035) 40%, transparent 72%);
  pointer-events: none;
  z-index: 1;
  filter: blur(28px);
}

/* Large Rectangular Editorial Portrait Card */
.hero-editorial-card {
  position: relative;
  z-index: 2;
  width: clamp(300px, 28vw, 420px);
  height: clamp(440px, 42vw, 570px);
  border-radius: 20px;
  overflow: hidden;
  background: #0A0A0A;
  border: 1px solid #353535;
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.75), 0 0 1px rgba(255, 255, 255, 0.12);
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease, border-color 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-editorial-card:hover {
  transform: translateY(-4px) scale(1.01);
  border-color: #555555;
  box-shadow: 0 32px 75px rgba(0, 0, 0, 0.88), 0 0 35px rgba(229, 9, 43, 0.12);
}

/* The Portrait Image (Exact new portrait in turtleneck & overcoat) */
.hero-editorial-img,
.hero-portrait-photo.hero-editorial-img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center 20% !important;
  display: block !important;
  filter: contrast(1.04) brightness(1.02) !important;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1) !important;
  border-radius: 19px !important;
  mask-image: none !important;
  -webkit-mask-image: none !important;
  transform: none !important;
}

.hero-editorial-card:hover .hero-editorial-img {
  transform: scale(1.03) !important;
}

/* Subtle Natural Edge Vignette Blend */
.hero-editorial-vignette {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 3;
  border-radius: 19px;
  background: radial-gradient(ellipse at 50% 35%, transparent 60%, rgba(10, 10, 10, 0.35) 85%, rgba(10, 10, 10, 0.75) 100%);
  transition: opacity 0.3s ease;
}

/* Bottom Dark Gradient Blend */
.hero-editorial-gradient-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 42%;
  pointer-events: none;
  z-index: 3;
  background: linear-gradient(to top, rgba(10, 10, 10, 0.95) 0%, rgba(10, 10, 10, 0.45) 55%, transparent 100%);
}

/* Floating Professional Philosophy Pill */
.hero-floating-badge {
  position: absolute;
  bottom: 22px;
  left: 20px;
  right: 20px;
  z-index: 5;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: rgba(18, 18, 18, 0.88);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.14);
  padding: 10px 16px;
  border-radius: 999px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
  pointer-events: auto;
  transition: background 0.3s ease, border-color 0.3s ease, transform 0.3s ease;
}

.hero-floating-badge:hover {
  background: rgba(28, 28, 28, 0.95);
  border-color: rgba(229, 9, 43, 0.4);
  transform: translateY(-1px);
}

.hero-floating-badge .badge-accent-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #E5092B;
  box-shadow: 0 0 8px rgba(229, 9, 43, 0.9);
  flex-shrink: 0;
}

.hero-floating-badge .badge-text {
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 600;
  color: #F5F5F5;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  white-space: nowrap;
}

/* Light Mode Adaptations for Editorial Portrait */
:root[data-theme="light"] .hero-editorial-card {
  background: #FFFFFF !important;
  border-color: #E2E2E6 !important;
  box-shadow: 0 20px 48px rgba(0, 0, 0, 0.08) !important;
}

:root[data-theme="light"] .hero-editorial-card:hover {
  border-color: rgba(229, 9, 43, 0.4) !important;
  box-shadow: 0 28px 60px rgba(0, 0, 0, 0.12), 0 0 25px rgba(229, 9, 43, 0.1) !important;
}

:root[data-theme="light"] .hero-editorial-vignette {
  background: radial-gradient(ellipse at 50% 35%, transparent 65%, rgba(255, 255, 255, 0.3) 90%, rgba(255, 255, 255, 0.65) 100%) !important;
}

:root[data-theme="light"] .hero-editorial-gradient-bottom {
  background: linear-gradient(to top, rgba(255, 255, 255, 0.92) 0%, rgba(255, 255, 255, 0.35) 60%, transparent 100%) !important;
}

:root[data-theme="light"] .hero-floating-badge {
  background: rgba(255, 255, 255, 0.92) !important;
  border-color: #D4D4D8 !important;
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.06) !important;
}

:root[data-theme="light"] .hero-floating-badge .badge-text {
  color: #111111 !important;
}

/* Responsive Breakpoints */
@media (max-width: 1024px) {
  .hero-editorial-stage {
    min-height: 480px;
  }
  .hero-editorial-card {
    height: 480px;
    width: clamp(280px, 32vw, 360px);
  }
}

@media (max-width: 768px) {
  .hero-split-grid {
    grid-template-columns: 1fr !important;
    gap: 40px !important;
    text-align: left;
  }
  .hero-editorial-col {
    order: 1 !important;
  }
  .hero-portrait-col {
    order: 2 !important;
    width: 100% !important;
    max-width: 100% !important;
  }
  .hero-editorial-stage {
    min-height: auto;
    margin: 16px auto 0;
  }
  .hero-editorial-card {
    width: clamp(280px, 85vw, 360px);
    height: 440px;
    margin: 0 auto;
  }
  .hero-watermark-vertical {
    display: none !important;
  }
}
"""

with open(r"c:\Users\siddi\Desktop\New folder\style.css", "a", encoding="utf-8") as f:
    f.write(css_block)

print("Appended editorial hero CSS successfully!")

