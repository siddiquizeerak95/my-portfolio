with open(r'c:\Users\siddi\Desktop\New folder\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if '<section id="hero"' in l:
        print('Hero starts line:', i + 1)
    if '<section id="home-about"' in l:
        print('About starts line:', i + 1)

