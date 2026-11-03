import subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
script = """
const docW = document.documentElement.offsetWidth;
console.log('DOC_WIDTH:', docW);
const all = document.querySelectorAll('*');
for (let el of all) {
  const r = el.getBoundingClientRect();
  if (r.right > docW + 2) {
    console.log('OVERFLOW_RIGHT:', el.tagName, el.className, 'right:', r.right, 'width:', r.width);
  }
}
"""

# Inject into index.html test
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
    if "DOC_WIDTH" in l or "OVERFLOW_RIGHT" in l:
        print(l)

