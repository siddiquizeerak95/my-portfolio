import subprocess

# Check what Profile Pic.jpg was in commit 8e612e5
res = subprocess.run(['git', 'show', '8e612e5:Profile Pic.jpg'], capture_output=True)
print("Profile Pic.jpg in 8e612e5 length:", len(res.stdout))

# Check what NEW IMAGE FOR WEBSITE.jpeg in 7492284 is
res2 = subprocess.run(['git', 'show', '7492284:NEW IMAGE FOR WEBSITE.jpeg'], capture_output=True)
print("NEW IMAGE FOR WEBSITE.jpeg in 7492284 length:", len(res2.stdout))

# Compare with current NEW IMAGE FOR WEBSITE.jpeg
with open('NEW IMAGE FOR WEBSITE.jpeg', 'rb') as f:
    cur = f.read()
print("Current NEW IMAGE FOR WEBSITE.jpeg length:", len(cur))

