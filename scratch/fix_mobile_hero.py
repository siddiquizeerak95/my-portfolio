path_css = r"c:\Users\siddi\Desktop\New folder\style.css"
with open(path_css, "r", encoding="utf-8") as f:
    css = f.read()

mobile_fix = """
/* Precision Mobile Hero Alignment */
@media (max-width: 768px) {
  .container.hero-container {
    padding-left: 16px !important;
    padding-right: 16px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .hero-split-grid {
    width: 100% !important;
    margin: 0 !important;
    box-sizing: border-box !important;
  }
  .hero-editorial-col {
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .hero-headline-zs {
    font-size: clamp(2rem, 8.5vw, 2.6rem) !important;
    line-height: 1.15 !important;
    word-break: normal !important;
    overflow-wrap: break-word !important;
  }
  .hero-subtitle-zs {
    font-size: 11px !important;
    letter-spacing: 0.08em !important;
    line-height: 1.4 !important;
    margin-bottom: 12px !important;
  }
  .hero-desc-zs {
    font-size: 13.5px !important;
    line-height: 1.6 !important;
    color: #B5B5B5 !important;
    margin-bottom: 24px !important;
  }
  .hero-actions-row {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: wrap !important;
    gap: 12px !important;
    margin-bottom: 28px !important;
  }
  .hero-stats-row {
    width: 100% !important;
    max-width: 340px !important;
    justify-content: flex-start !important;
    gap: 16px !important;
  }
  .hero-portrait-col {
    width: 100% !important;
    display: flex !important;
    justify-content: center !important;
    margin-top: 10px !important;
  }
  .hero-editorial-stage {
    width: 100% !important;
    display: flex !important;
    justify-content: center !important;
  }
  .hero-editorial-card {
    width: 100% !important;
    max-width: 330px !important;
    height: 440px !important;
    margin: 0 auto !important;
  }
}
"""

with open(path_css, "a", encoding="utf-8") as f:
    f.write(mobile_fix)

print("Appended mobile alignment fix to style.css!")

