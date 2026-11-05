import subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# We will run a script in Chrome to check computed styles
test_js = """
const card = document.querySelector('.hero-reference-portrait-card');
const img = document.querySelector('.hero-reference-portrait-img');
const rectCard = card ? card.getBoundingClientRect() : null;
const rectImg = img ? img.getBoundingClientRect() : null;
const styleCard = card ? window.getComputedStyle(card) : null;
const styleImg = img ? window.getComputedStyle(img) : null;

console.log('CARD_RECT:' + JSON.stringify(rectCard));
console.log('IMG_RECT:' + JSON.stringify(rectImg));
console.log('IMG_COMPUTED_WIDTH:' + (styleImg ? styleImg.width : ''));
console.log('IMG_COMPUTED_HEIGHT:' + (styleImg ? styleImg.height : ''));
console.log('IMG_COMPUTED_OBJ_FIT:' + (styleImg ? styleImg.objectFit : ''));
console.log('IMG_COMPUTED_OBJ_POS:' + (styleImg ? styleImg.objectPosition : ''));
console.log('CARD_CHILDREN:' + (card ? card.innerHTML : ''));
"""

# Let's write an evaluation wrapper
eval_html = f"""<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="hero-reference-portrait-card">
  <img src="NEW IMAGE FOR WEBSITE.jpeg" class="hero-reference-portrait-img" width="480" height="620">
</div>
<script>
window.addEventListener('load', () => {{
  const card = document.querySelector('.hero-reference-portrait-card');
  const img = document.querySelector('.hero-reference-portrait-img');
  console.log('IMG_NATURAL:' + img.naturalWidth + 'x' + img.naturalHeight);
  console.log('IMG_OFFSET:' + img.offsetWidth + 'x' + img.offsetHeight);
  console.log('CARD_OFFSET:' + card.offsetWidth + 'x' + card.offsetHeight);
}});
</script>
</body>
</html>"""

with open('scratch/eval_hero.html', 'w', encoding='utf-8') as f:
    f.write(eval_html)

cmd = [
    CHROME,
    "--headless=new",
    "--enable-logging=stderr",
    "--v=1",
    "--virtual-time-budget=600",
    "http://127.0.0.1:5500/scratch/eval_hero.html"
]

res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
print("Stderr output:")
for line in res.stderr.splitlines():
    if any(k in line for k in ['IMG_', 'CARD_']):
        print("  ", line)

