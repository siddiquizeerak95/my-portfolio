import re

# 1. Update style.css with mobile headline & responsive refinements
path_css = r"c:\Users\siddi\Desktop\New folder\style.css"
with open(path_css, "r", encoding="utf-8") as f:
    css_content = f.read()

mobile_refinements = """
/* Mobile Hero Typography Calibration */
@media (max-width: 600px) {
  .hero-headline-zs {
    font-size: clamp(1.85rem, 8.2vw, 2.5rem) !important;
    line-height: 1.15 !important;
    letter-spacing: -0.02em !important;
  }
  .hero-subtitle-zs {
    font-size: 11px !important;
    letter-spacing: 0.06em !important;
    line-height: 1.45 !important;
  }
  .hero-container {
    padding-left: 20px !important;
    padding-right: 20px !important;
  }
  .hero-left-accent-line {
    display: none !important;
  }
}
"""

with open(path_css, "a", encoding="utf-8") as f:
    f.write(mobile_refinements)

# 2. In index.html, format the headline gracefully
path_html = r"c:\Users\siddi\Desktop\New folder\index.html"
with open(path_html, "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace:
# Hi, I'm<br><span class="text-accent-red">Zeerak Siddiqui.</span>
# With:
# Hi, I'm Zeerak<br><span class="text-accent-red">Siddiqui.</span>
old_h1 = '''            <h1 class="hero-headline-zs">
              Hi, I'm<br><span class="text-accent-red">Zeerak Siddiqui.</span>
            </h1>'''

new_h1 = '''            <h1 class="hero-headline-zs">
              Hi, I'm Zeerak<br><span class="text-accent-red">Siddiqui.</span>
            </h1>'''

if old_h1 in html_content:
    html_content = html_content.replace(old_h1, new_h1)
    with open(path_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Formatted headline in index.html!")
else:
    print("Headline already updated or not found")

print("Mobile responsive refinements applied successfully!")

