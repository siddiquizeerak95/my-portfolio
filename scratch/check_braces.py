with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's count open vs close braces up to line 8529
lines = css.splitlines()
depth = 0
for idx, line in enumerate(lines, 1):
    # Strip comments
    line_clean = line
    # Simple brace counting
    for char in line:
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
    if idx in [8140, 8145, 8200, 8300, 8350, 8400, 8450, 8500, 8525, 8530, 8640]:
        print(f"Line {idx}: depth = {depth}")

print("Final depth at end of file:", depth)

