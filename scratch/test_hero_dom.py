import subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

test_script = """
const card = document.querySelector('.hero-reference-portrait-card');
console.log('CARD_HTML:' + card.outerHTML);
const children = card.children;
for (let i = 0; i < children.length; i++) {
  const el = children[i];
  const rect = el.getBoundingClientRect();
  const cs = window.getComputedStyle(el);
  console.log(`CHILD_${i}_${el.tagName}_${el.className}: rect=${JSON.stringify(rect)}, bg=${cs.backgroundColor}, bgImage=${cs.backgroundImage}`);
}
"""

with open('scratch/debug_index.js', 'w') as f:
    f.write(test_script)

cmd = [
    CHROME,
    "--headless=new",
    "--enable-logging=stderr",
    "--v=1",
    "--virtual-time-budget=800",
    "http://127.0.0.1:5500/index.html?skip_preloader=1"
]

res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
for line in res.stderr.splitlines():
    if 'CHILD_' in line or 'CARD_HTML:' in line:
        print(line)

