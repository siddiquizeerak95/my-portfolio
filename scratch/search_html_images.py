import os
import glob

html_files = glob.glob('*.html')
for h in sorted(html_files):
    with open(h, 'r', encoding='utf-8') as f:
        text = f.read()
    for line_num, line in enumerate(text.splitlines(), 1):
        if any(ext in line.lower() for ext in ['.jpg', '.jpeg', '.png']) and 'fav' not in line.lower() and 'icon' not in line.lower() and 'preview' not in line.lower():
            print(f"{h}:{line_num}: {line.strip()[:100]}")

