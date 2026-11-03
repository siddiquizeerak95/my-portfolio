import subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
script = """
window.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    const all = document.querySelectorAll('*');
    for (let el of all) {
      const r = el.getBoundingClientRect();
      if (r.width > 390 || r.right > 390) {
        console.log('WIDE_EL:', el.tagName, el.className || el.id, 'w=' + Math.round(r.width), 'right=' + Math.round(r.right));
      }
    }
  }, 100);
});
"""

with open("index.html", "r", encoding="utf-8") as f:
    orig = f.read()

temp = orig.replace("</head>", f"<script>{script}</script></head>")
with open("index.html", "w", encoding="utf-8") as f:
    f.write(temp)

cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=390,844", "--enable-logging=stderr", "--v=1", "--virtual-time-budget=8500", "http://127.0.0.1:5500/index.html"]
res = subprocess.run(cmd, capture_output=True, text=True, timeout=20)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(orig)

for l in res.stderr.splitlines():
    if "WIDE_EL:" in l:
        print(l)

