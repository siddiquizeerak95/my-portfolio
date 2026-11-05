with open('style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Main Portrait Block
start_marker = '.hero-reference-portrait-col {'
end_marker = '/* ==========================================================================\n   BOTTOM REFERENCE TICKER BAR'
idx1 = text.find(start_marker)
idx2 = text.find(end_marker)

if idx1 == -1 or idx2 == -1:
    print(f"Error: could not find main portrait block in style.css: idx1={idx1}, idx2={idx2}")
    exit(1)

new_portrait_css = """/* ==========================================================================
   CINEMATIC EDITORIAL PORTRAIT (Cinematic Red & Black Visual Direction)
   Reference: Cinematic red rim lighting on dark background
   ========================================================================== */
.hero-reference-portrait-col,
.hero-cinematic-portrait-col {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
}

.hero-reference-portrait-stage,
.hero-cinematic-portrait-stage {
  position: relative;
  width: 100%;
  max-width: 480px;
  display: flex;
  justify-content: center;
  align-items: center;
  perspective: 1200px;
}

/* Atmospheric Red Ambient Lighting Behind Portrait Frame */
.hero-portrait-ambient-glow,
.hero-cinematic-ambient-glow {
  position: absolute;
  width: clamp(380px, 44vw, 560px);
  height: clamp(480px, 52vw, 680px);
  top: 50%;
  left: 48%;
  transform: translate(-50%, -50%);
  background: radial-gradient(ellipse at 38% 46%, rgba(229, 9, 43, 0.28) 0%, rgba(229, 9, 43, 0.08) 48%, transparent 72%);
  pointer-events: none;
  z-index: 1;
  filter: blur(52px);
  border-radius: 50%;
  transition: transform 0.25s ease-out;
}

/* Main Cinematic Rectangular Portrait Frame */
.hero-reference-portrait-card,
.hero-cinematic-portrait-card {
  position: relative;
  z-index: 2;
  width: clamp(320px, 32vw, 440px);
  height: clamp(460px, 44vw, 580px);
  border-radius: 18px;
  overflow: hidden;
  background: #060606;
  /* Thin restrained red accent border with soft crimson atmospheric glow */
  border: 1px solid rgba(229, 9, 43, 0.42);
  box-shadow: 
    0 28px 75px rgba(0, 0, 0, 0.95),
    0 0 38px rgba(229, 9, 43, 0.2),
    inset 0 0 1px 1px rgba(229, 9, 43, 0.16);
  transform-style: preserve-3d;
  transition: border-color 0.4s ease, box-shadow 0.4s ease;
  will-change: transform;
}

.hero-reference-portrait-card:hover,
.hero-cinematic-portrait-card:hover {
  border-color: rgba(229, 9, 43, 0.72);
  box-shadow: 
    0 36px 90px rgba(0, 0, 0, 0.98),
    0 0 55px rgba(229, 9, 43, 0.32),
    inset 0 0 2px 1px rgba(229, 9, 43, 0.28);
}

/* Portrait Image — Preserving authentic facial features, skin tone and appearance */
.hero-reference-portrait-img,
.hero-cinematic-portrait-img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: 50% 16% !important;
  display: block !important;
  filter: contrast(1.04) brightness(0.98);
  transform: translateZ(0);
}

/* Directional Cinematic Red Rim Lighting Layer (Matching reference aesthetic) */
.hero-cinematic-rim-light {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 3;
  background: 
    radial-gradient(ellipse at 10% 34%, rgba(229, 9, 43, 0.82) 0%, rgba(229, 9, 43, 0.26) 28%, transparent 58%),
    linear-gradient(90deg, rgba(229, 9, 43, 0.44) 0%, rgba(229, 9, 43, 0.14) 10%, transparent 28%),
    radial-gradient(ellipse at 92% 52%, rgba(180, 200, 220, 0.16) 0%, transparent 36%);
  mix-blend-mode: screen;
  transform: translateZ(8px);
}

/* Atmospheric Vignette & Soft Grounding Fade */
.hero-portrait-vignette,
.hero-cinematic-vignette {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 4;
  background: 
    radial-gradient(ellipse at 50% 38%, transparent 58%, rgba(6, 6, 6, 0.6) 100%),
    linear-gradient(to right, transparent 75%, rgba(6, 6, 6, 0.7) 100%);
  transform: translateZ(12px);
}

.hero-portrait-fade-bottom,
.hero-cinematic-fade-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 28%;
  background: linear-gradient(to top, #0A0A0A 0%, rgba(10, 10, 10, 0.5) 50%, transparent 100%);
  pointer-events: none;
  z-index: 5;
  transform: translateZ(16px);
}

/* Precision Luxury Inner Accent Rim */
.hero-cinematic-inner-rim {
  position: absolute;
  inset: 0;
  border-radius: 18px;
  pointer-events: none;
  z-index: 6;
  border: 1px solid rgba(255, 255, 255, 0.06);
  box-shadow: inset 1px 1px 0 rgba(229, 9, 43, 0.45);
  transform: translateZ(20px);
}

"""

text = text[:idx1] + new_portrait_css + text[idx2:]

# 2. Light theme updates
light_target = ':root[data-theme="light"] .hero-reference-portrait-card {'
light_idx = text.find(light_target)
if light_idx != -1:
    light_end = text.find('/* ==========================================================================\n   RESPONSIVE BREAKPOINTS', light_idx)
    new_light = """:root[data-theme="light"] .hero-reference-portrait-card,
:root[data-theme="light"] .hero-cinematic-portrait-card {
  background: #0E0E0E;
  border-color: rgba(229, 9, 43, 0.55);
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.16), 0 0 35px rgba(229, 9, 43, 0.18);
}

:root[data-theme="light"] .hero-portrait-ambient-glow,
:root[data-theme="light"] .hero-cinematic-ambient-glow {
  background: radial-gradient(ellipse at 38% 46%, rgba(229, 9, 43, 0.18) 0%, rgba(229, 9, 43, 0.04) 48%, transparent 70%);
  filter: blur(40px);
}

:root[data-theme="light"] .hero-portrait-fade-bottom,
:root[data-theme="light"] .hero-cinematic-fade-bottom {
  background: linear-gradient(to top, rgba(14, 14, 14, 0.95) 0%, rgba(14, 14, 14, 0.45) 50%, transparent 100%);
}

:root[data-theme="light"] .hero-reference-bottom-bar {
  border-top-color: #E2E2E6;
  color: #666668;
}

"""
    text = text[:light_idx] + new_light + text[light_end:]

# 3. Responsive updates
resp_target = '.hero-reference-portrait-card {\n    width: 100% !important;\n    max-width: 340px !important;\n    height: 440px !important;\n    margin: 0 auto !important;\n  }'
new_resp = """.hero-reference-portrait-card,
  .hero-cinematic-portrait-card {
    width: 100% !important;
    max-width: 360px !important;
    height: 480px !important;
    margin: 0 auto !important;
  }"""
if resp_target in text:
    text = text.replace(resp_target, new_resp)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated style.css with cinematic styling!")

