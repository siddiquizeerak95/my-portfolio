import re

# 1. Update index.html
import subprocess
subprocess.run(['python', r'c:\Users\siddi\Desktop\New folder\scratch\implement_video_reference_hero.py'])

# 2. Update style.css
with open(r'c:\Users\siddi\Desktop\New folder\scratch\hero_video_reference.css', 'r', encoding='utf-8') as f:
    new_css = f.read()

with open(r'c:\Users\siddi\Desktop\New folder\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

sec12_pattern = re.compile(r'/\*\s*=+\s*12\..*', re.DOTALL)
if sec12_pattern.search(css):
    css = sec12_pattern.sub(new_css, css)
    with open(r'c:\Users\siddi\Desktop\New folder\style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("style.css updated with exact video reference CSS!")
else:
    print("Could not find section 12 in style.css")

# 3. Update script.js
with open(r'c:\Users\siddi\Desktop\New folder\script.js', 'r', encoding='utf-8') as f:
    js = f.read()

spiral_flip_js = """// -----------------------------------------------------------------------------
// 05.2 SPIRAL NOTEBOOK 3D FLIP CARD ANIMATION (EXACT REFERENCE VIDEO)
// -----------------------------------------------------------------------------
function initSpiralFlipCard() {
  const items = document.querySelectorAll('.spiral-role-text');
  const pageIndicator = document.getElementById('spiral-card-page');
  if (!items || items.length === 0) return;

  let currentIndex = 0;
  const total = items.length;

  setInterval(() => {
    const prev = items[currentIndex];
    prev.classList.remove('active');
    prev.classList.add('exit-up');

    setTimeout(() => {
      prev.classList.remove('exit-up');
    }, 550);

    currentIndex = (currentIndex + 1) % total;
    const next = items[currentIndex];
    next.classList.add('active');

    if (pageIndicator) {
      pageIndicator.textContent = `0${currentIndex + 1} / 0${total}`;
    }
  }, 2800);
}
"""

if 'initSpiralFlipCard' not in js:
    # Insert before bootPortfolio
    target = 'function bootPortfolio() {'
    js = js.replace(target, spiral_flip_js + '\n' + target)
    js = js.replace('initHeroPerspective();', 'initHeroPerspective();\n  initSpiralFlipCard();')
    with open(r'c:\Users\siddi\Desktop\New folder\script.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("script.js updated with initSpiralFlipCard()!")
else:
    print("initSpiralFlipCard already in script.js")

