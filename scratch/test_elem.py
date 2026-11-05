test_script = """
<script>
window.addEventListener('load', () => {
  const el = document.elementFromPoint(1000, 280);
  console.log('ELEMENT_AT_1000_280: ' + (el ? el.tagName + '.' + el.className : 'null'));
  const card = document.querySelector('.hero-reference-portrait-card');
  console.log('CARD_RECT:' + JSON.stringify(card.getBoundingClientRect()));
  const img = document.querySelector('.hero-reference-portrait-img');
  console.log('IMG_RECT:' + JSON.stringify(img.getBoundingClientRect()));
  const stage = document.querySelector('.hero-reference-portrait-stage');
  console.log('STAGE_RECT:' + JSON.stringify(stage.getBoundingClientRect()));
  const glow = document.querySelector('.hero-portrait-ambient-glow');
  console.log('GLOW_RECT:' + JSON.stringify(glow.getBoundingClientRect()));
});
</script>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

test_html = html.replace('</body>', test_script + '</body>')
with open('scratch_elem.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

import subprocess
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    CHROME,
    "--headless=new",
    "--enable-logging=stderr",
    "--v=1",
    "--virtual-time-budget=800",
    "http://127.0.0.1:5500/scratch_elem.html?skip_preloader=1"
]

res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
for line in res.stderr.splitlines():
    if 'ELEMENT_AT' in line or 'RECT:' in line:
        print(line)

