with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

depth = 0
for idx in range(8144, 8250):
    line = lines[idx]
    old_depth = depth
    for c in line:
        if c == '{': depth += 1
        elif c == '}': depth -= 1
    if depth != old_depth:
        print(f"Line {idx+1} (depth {old_depth} -> {depth}): {line.strip()[:80]}")

