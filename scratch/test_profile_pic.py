import subprocess

# Extract Profile Pic.jpg from commit 8e612e5
res = subprocess.run(['git', 'show', '8e612e5:Profile Pic.jpg'], capture_output=True)
with open('scratch/profile_pic_git.jpg', 'wb') as f:
    f.write(res.stdout)

ps = """
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile("c:\\Users\\siddi\\Desktop\\New folder\\scratch\\profile_pic_git.jpg")
Write-Output "Profile Pic.jpg: $($img.Width) x $($img.Height)"
$img.Dispose()
"""

with open('scratch/inspect_profile_pic.ps1', 'w') as f:
    f.write(ps)

res2 = subprocess.run(['powershell', '-File', 'scratch/inspect_profile_pic.ps1'], capture_output=True, text=True)
print(res2.stdout)

