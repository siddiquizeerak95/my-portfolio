with open('style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Hero section background
hero_marker = '.hero-section {'
idx_hero = text.find(hero_marker)
if idx_hero != -1:
    end_hero = text.find('}', idx_hero)
    # Check if background is set
    print("Found hero-section at", idx_hero)

# 2. Main Portrait CSS block
start_marker = '/* ==========================================================================\n   CINEMATIC EDITORIAL PORTRAIT (Cinematic Red & Black Visual Direction)'
end_marker = '/* ==========================================================================\n   BOTTOM REFERENCE TICKER BAR'

idx1 = text.find(start_marker)
idx2 = text.find(end_marker)

if idx1 == -1 or idx2 == -1:
    print(f"Error: could not find portrait markers in style.css: {idx1}, {idx2}")
    exit(1)

new_portrait_css = """/* ==========================================================================
   BORDERLESS SEAMLESS CINEMATIC EDITORIAL PORTRAIT
   Exact Match to User Reference: NO borders, NO box, NO card container.
   Portrait seamlessly dissolves into #080808 background with red window illumination.
   ========================================================================== */
#hero.hero-section {
  background-color: #080808 !important;
  background-image: radial-gradient(circle at 75% 42%, rgba(229, 9, 43, 0.08) 0%, transparent 55%), radial-gradient(circle at 20% 20%, rgba(255, 255, 255, 0.02) 0%, transparent 40%) !important;
}

.hero-reference-portrait-col,
.hero-cinematic-portrait-col,
.hero-borderless-portrait-col {
  position: relative;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  z-index: 2;
  width: 100%;
}

.hero-reference-portrait-stage,
.hero-cinematic-portrait-stage,
.hero-borderless-portrait-stage {
  position: relative;
  width: 100%;
  max-width: 620px;
  height: clamp(520px, 58vw, 700px);
  display: flex;
  justify-content: center;
  align-items: center;
  border: none !important;
  background: transparent !important;
  box-shadow: none !important;
  border-radius: 0 !important;
  overflow: visible !important;
}

/* Atmospheric Red Ambient Lighting Concentrated Behind Window & Portrait */
.hero-portrait-ambient-glow,
.hero-cinematic-ambient-glow,
.hero-borderless-ambient-glow {
  position: absolute;
  width: clamp(380px, 44vw, 560px);
  height: clamp(460px, 52vw, 640px);
  top: 48%;
  left: 28%;
  transform: translate(-50%, -50%);
  background: radial-gradient(ellipse at 42% 45%, rgba(229, 9, 43, 0.52) 0%, rgba(229, 9, 43, 0.2) 44%, transparent 72%);
  filter: blur(56px);
  pointer-events: none;
  z-index: 1;
  border-radius: 50%;
  animation: cinematicRedBreathe 7s infinite ease-in-out;
  transition: transform 0.25s ease-out;
}

@keyframes cinematicRedBreathe {
  0%, 100% {
    opacity: 0.85;
    transform: translate(-50%, -50%) scale(1);
  }
  50% {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1.05);
  }
}

/* Seamless Borderless Portrait Container — NO BORDER, NO CARD, NO BOX */
.hero-reference-portrait-card,
.hero-cinematic-portrait-card,
.hero-borderless-portrait-wrap {
  position: relative;
  z-index: 2;
  width: 100%;
  height: 100%;
  border: none !important;
  background: transparent !important;
  box-shadow: none !important;
  border-radius: 0 !important;
  overflow: visible !important;
  /* Advanced Feathered Edge Masking: 
     Leaves hair and facial features crisp and fully visible while feathering 
     the outer rectangular boundaries smoothly into #080808 */
  -webkit-mask-image: 
    radial-gradient(ellipse 74% 84% at 52% 46%, #000 52%, rgba(0, 0, 0, 0.85) 70%, transparent 100%),
    linear-gradient(to top, transparent 0%, #000 12%, #000 95%, transparent 100%),
    linear-gradient(to right, transparent 0%, #000 10%, #000 86%, transparent 100%);
  -webkit-mask-composite: source-in;
  mask-image: 
    radial-gradient(ellipse 74% 84% at 52% 46%, #000 52%, rgba(0, 0, 0, 0.85) 70%, transparent 100%),
    linear-gradient(to top, transparent 0%, #000 12%, #000 95%, transparent 100%),
    linear-gradient(to right, transparent 0%, #000 10%, #000 86%, transparent 100%);
  mask-composite: intersect;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: transform;
}

/* Portrait Image: Authentic, crisp, high-resolution */
.hero-reference-portrait-img,
.hero-cinematic-portrait-img,
.hero-borderless-portrait-img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: 50% 15% !important;
  display: block !important;
  border: none !important;
  box-shadow: none !important;
  border-radius: 0 !important;
  filter: contrast(1.04) brightness(0.98);
}

/* Dramatic Cinematic Red Window Illumination (Left window glow from reference) */
.hero-cinematic-rim-light,
.hero-borderless-window-light {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 3;
  background: 
    radial-gradient(ellipse at 16% 36%, rgba(229, 9, 43, 0.92) 0%, rgba(229, 9, 43, 0.38) 32%, transparent 60%),
    linear-gradient(90deg, rgba(229, 9, 43, 0.58) 0%, rgba(229, 9, 43, 0.2) 16%, transparent 36%);
  mix-blend-mode: screen;
}

/* Soft Vignette Blending Subject & Coat Seamlessly into #080808 */
.hero-portrait-vignette,
.hero-cinematic-vignette,
.hero-borderless-vignette {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 4;
  background: 
    linear-gradient(to top, #080808 0%, rgba(8, 8, 8, 0.85) 12%, transparent 32%),
    linear-gradient(to right, transparent 66%, rgba(8, 8, 8, 0.95) 100%),
    linear-gradient(to left, transparent 72%, rgba(8, 8, 8, 0.85) 100%),
    linear-gradient(to bottom, transparent 82%, rgba(8, 8, 8, 0.55) 100%);
}

/* Absolutely NO Borders, Badges, or Floating Cards */
.hero-cinematic-inner-rim,
.hero-floating-ability-badge,
.hero-portrait-fade-bottom,
.hero-cinematic-fade-bottom,
.hero-watermark-vertical {
  display: none !important;
}

"""

text = text[:idx1] + new_portrait_css + text[idx2:]

# 3. Light theme updates
light_target = ':root[data-theme="light"] .hero-reference-portrait-card,'
light_idx = text.find(light_target)
if light_idx != -1:
    light_end = text.find('/* ==========================================================================\n   RESPONSIVE BREAKPOINTS', light_idx)
    new_light = """:root[data-theme="light"] #hero.hero-section {
  background-color: #F8F8FA !important;
  background-image: radial-gradient(circle at 75% 42%, rgba(229, 9, 43, 0.05) 0%, transparent 55%) !important;
}

:root[data-theme="light"] .hero-reference-portrait-card,
:root[data-theme="light"] .hero-cinematic-portrait-card,
:root[data-theme="light"] .hero-borderless-portrait-wrap {
  border: none !important;
  background: transparent !important;
  box-shadow: none !important;
  -webkit-mask-image: 
    radial-gradient(ellipse 74% 84% at 52% 46%, #000 52%, rgba(0, 0, 0, 0.85) 70%, transparent 100%),
    linear-gradient(to top, transparent 0%, #000 12%, #000 95%, transparent 100%),
    linear-gradient(to right, transparent 0%, #000 10%, #000 86%, transparent 100%);
  mask-image: 
    radial-gradient(ellipse 74% 84% at 52% 46%, #000 52%, rgba(0, 0, 0, 0.85) 70%, transparent 100%),
    linear-gradient(to top, transparent 0%, #000 12%, #000 95%, transparent 100%),
    linear-gradient(to right, transparent 0%, #000 10%, #000 86%, transparent 100%);
}

:root[data-theme="light"] .hero-portrait-ambient-glow,
:root[data-theme="light"] .hero-cinematic-ambient-glow,
:root[data-theme="light"] .hero-borderless-ambient-glow {
  background: radial-gradient(ellipse at 42% 45%, rgba(229, 9, 43, 0.22) 0%, rgba(229, 9, 43, 0.06) 48%, transparent 70%);
  filter: blur(44px);
}

:root[data-theme="light"] .hero-borderless-vignette {
  background: 
    linear-gradient(to top, #F8F8FA 0%, rgba(248, 248, 250, 0.85) 12%, transparent 32%),
    linear-gradient(to right, transparent 66%, rgba(248, 248, 250, 0.95) 100%),
    linear-gradient(to left, transparent 72%, rgba(248, 248, 250, 0.85) 100%),
    linear-gradient(to bottom, transparent 82%, rgba(248, 248, 250, 0.55) 100%);
}

:root[data-theme="light"] .hero-reference-bottom-bar {
  border-top-color: #E2E2E6;
  color: #666668;
}

"""
    text = text[:light_idx] + new_light + text[light_end:]

# 4. Responsive updates
resp_target = """.hero-reference-portrait-card,
  .hero-cinematic-portrait-card {
    width: 100% !important;
    max-width: 360px !important;
    height: 480px !important;
    margin: 0 auto !important;
  }"""

new_resp = """.hero-reference-portrait-col,
  .hero-cinematic-portrait-col,
  .hero-borderless-portrait-col {
    order: 2 !important;
    width: 100% !important;
    justify-content: center !important;
  }

  .hero-reference-portrait-stage,
  .hero-cinematic-portrait-stage,
  .hero-borderless-portrait-stage {
    max-width: 480px !important;
    height: 520px !important;
    margin: 0 auto !important;
  }

  .hero-reference-portrait-card,
  .hero-cinematic-portrait-card,
  .hero-borderless-portrait-wrap {
    width: 100% !important;
    max-width: 480px !important;
    height: 100% !important;
    margin: 0 auto !important;
  }"""

if resp_target in text:
    text = text.replace(resp_target, new_resp)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated style.css with borderless seamless portrait rules!")

