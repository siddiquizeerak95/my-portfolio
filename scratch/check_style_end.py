with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print("Lines in style.css:", len(lines))
print("Last 30 lines:")
for l in lines[-30:]:
    print(l, end='')

