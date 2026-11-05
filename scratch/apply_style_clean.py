replacement = """/* ==========================================================================
   RIGHT COLUMN: BORDERLESS SEAMLESS CINEMATIC PORTRAIT
   Exact Match to User Reference: NO borders, NO box, NO card container.
   Portrait seamlessly dissolves into #080808 background with red illumination.
   ========================================================================== */
.hero-borderless-portrait-col {
  position: relative;
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
  z-index: 2;
  width: 100%;
  height: 100%;
}

.hero-borderless-portrait-stage {
  position: relative;
  width: 100%;
  max-width: 680px;
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
  border: none !important;
  background: transparent !important;
  box-shadow: none !important;
  border-radius: 0 !important;
  overflow: visible !important;
}

/* Atmospheric Red Ambient Lighting Behind Portrait - Integrated in image */
.hero-borderless-ambient-glow {
  display: none !important;
}

/* Seamless Borderless Portrait Container — NO BORDER, NO CARD, NO BOX */
.hero-borderless-portrait-wrap {
  position: relative;
  z-index: 2;
  width: 100%;
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
  border: none !important;
  background: transparent !important;
  box-shadow: none !important;
  border-radius: 0 !important;
  overflow: visible !important;
  mask-image: none !important;
  -webkit-mask-image: none !important;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: transform;
}

/* Portrait Image: Authentic, crisp, high-resolution, perfectly blended */
.hero-borderless-portrait-img {
  width: 100% !important;
  max-width: 640px !important;
  height: auto !important;
  max-height: clamp(520px, 78vh, 760px) !important;
  object-fit: contain !important;
  object-position: right bottom !important;
  display: block !important;
  border: none !important;
  box-shadow: none !important;
  border-radius: 0 !important;
  filter: contrast(1.04) brightness(1.0);
}

/* Directional Cinematic Red Window & Rim Illumination - handled in photo */
.hero-borderless-window-light {
  display: none !important;
}

/* Soft Vignette Blending Subject & Coat Seamlessly into #080808 */
.hero-borderless-vignette {
  display: none !important;
}
"""

with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "/* ==========================================================================\n   RIGHT COLUMN: BORDERLESS SEAMLESS CINEMATIC PORTRAIT"
end_marker = "/* ==========================================================================\n   LIGHT MODE ADAPTATIONS"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + replacement + "\n" + content[end_idx:]
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated style.css!")
else:
    print(f"Indices not found: start={start_idx}, end={end_idx}")

