import subprocess

out = subprocess.check_output(['git', 'log', '--name-only', '--oneline'], text=True, encoding='utf-8')
print("Git log files:")
for line in out.splitlines():
    if any(ext in line.lower() for ext in ['.jpg', '.jpeg', '.png']):
        print(" ", line)

