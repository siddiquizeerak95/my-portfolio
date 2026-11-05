import subprocess

out = subprocess.check_output(['git', 'log', '--stat', '-n', '10'], text=True, encoding='utf-8')
print("Recent 10 commits stat:")
print(out)

