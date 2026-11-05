code = """/* ==========================================================================
   RESPONSIVE BREAKPOINTS (DANIEL SMITH CINEMATIC SHOWCASE)
   ========================================================================== */
@media (max-width: 1024px) {
  .hero-cinematic-grid {
    display: flex !important;
    flex-direction: column !important;
    gap: 36px !important;
    padding-top: 100px !important;
    padding-bottom: 30px !important;
    min-height: auto !important;
  }

  .hero-content-col {
    order: 1 !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
    max-width: 640px !important;
    margin: 0 auto !important;
  }

  .hero-desc-daniel {
    margin-left: auto !important;
    margin-right: auto !important;
    text-align: center !important;
  }

  .hero-actions-daniel {
    justify-content: center !important;
    margin: 0 auto !important;
  }

  .hero-borderless-portrait-col {
    order: 2 !important;
    width: 100% !important;
    height: auto !important;
    justify-content: center !important;
    align-items: center !important;
  }

  .hero-borderless-portrait-stage {
    width: 100% !important;
    max-width: 480px !important;
    height: auto !important;
    margin: 0 auto !important;
    justify-content: center !important;
    align-items: center !important;
    overflow: visible !important;
  }

  .hero-borderless-portrait-wrap {
    width: 100% !important;
    height: auto !important;
    justify-content: center !important;
    align-items: center !important;
  }

  .hero-borderless-portrait-img {
    max-width: 440px !important;
    max-height: clamp(380px, 55vh, 480px) !important;
    width: 100% !important;
    height: auto !important;
    object-position: center bottom !important;
    margin: 0 auto !important;
  }
}

@media (max-width: 768px) {
  .hero-cinematic-reference-section {
    padding-top: 80px !important;
    padding-bottom: 30px !important;
  }

  .hero-cinematic-grid {
    gap: 28px !important;
    padding: 16px 0 30px 0 !important;
  }

  .hero-content-col {
    align-items: flex-start !important;
    text-align: left !important;
  }

  .hero-desc-daniel {
    margin-left: 0 !important;
    margin-right: 0 !important;
    text-align: left !important;
    font-size: 14.5px !important;
    line-height: 1.6 !important;
    margin-bottom: 22px !important;
  }

  .hero-actions-daniel {
    justify-content: flex-start !important;
    margin: 0 !important;
    gap: 12px !important;
  }

  .hero-headline-daniel {
    font-size: clamp(1.85rem, 7.2vw, 2.5rem) !important;
    line-height: 1.15 !important;
    margin-bottom: 14px !important;
    text-align: left !important;
  }

  .btn-daniel-primary,
  .btn-daniel-outline {
    padding: 12px 26px !important;
    font-size: 14px !important;
  }

  .hero-borderless-portrait-stage {
    max-width: 400px !important;
  }

  .hero-borderless-portrait-img {
    max-width: 380px !important;
    max-height: clamp(320px, 52vh, 440px) !important;
  }
}

@media (max-width: 440px) {
  .hero-headline-daniel {
    font-size: clamp(1.75rem, 7.5vw, 2.15rem) !important;
  }

  .hero-actions-daniel {
    flex-direction: column !important;
    width: 100% !important;
    gap: 10px !important;
  }

  .btn-daniel-primary,
  .btn-daniel-outline {
    width: 100% !important;
    text-align: center !important;
    justify-content: center !important;
  }
}
"""

with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "/* ==========================================================================\n   RESPONSIVE BREAKPOINTS\n   ========================================================================== */"
start_idx = content.find(start_marker)

if start_idx != -1:
    new_content = content[:start_idx] + code
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated responsive CSS in style.css successfully!")
else:
    print("start_marker not found!")

