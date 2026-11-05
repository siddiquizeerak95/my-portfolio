with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

debug_script = """
<script>
window.addEventListener('load', () => {
  const card = document.querySelector('.hero-reference-portrait-card');
  const img = document.querySelector('.hero-reference-portrait-img');
  console.log('--- DEBUG START ---');
  console.log('CARD_RECT:' + JSON.stringify(card.getBoundingClientRect()));
  console.log('IMG_RECT:' + JSON.stringify(img.getBoundingClientRect()));
  console.log('IMG_NATURAL:' + img.naturalWidth + 'x' + img.naturalHeight);
  console.log('IMG_SRC:' + img.currentSrc);
  for (let i = 0; i < card.children.length; i++) {
    const el = card.children[i];
    const r = el.getBoundingClientRect();
    const cs = window.getComputedStyle(el);
    console.log('ELEM_' + el.tagName + '_' + el.className + ': top=' + r.top + ', left=' + r.left + ', w=' + r.width + ', h=' + r.height + ', pos=' + cs.position + ', z=' + cs.zIndex + ', bg=' + cs.backgroundColor + ', bgImg=' + cs.backgroundImage);
  }
  console.log('--- DEBUG END ---');
});
</script>
"""

test_html = html.replace('</body>', debug_script + '</body>')
with open('scratch_test_index.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

import subprocess
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    CHROME,
    "--headless=new",
    "--enable-logging=stderr",
    "--v=1",
    "--virtual-time-budget=1000",
    "http://127.0.0.1:5500/scratch_test_index.html?skip_preloader=1"
]

res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
for line in res.stderr.splitlines():
    if any(k in line for k in ['CARD_', 'IMG_', 'ELEM_']):
        print(line)

