import subprocess

ps = """
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile("c:\\Users\\siddi\\Desktop\\New folder\\NEW IMAGE FOR WEBSITE.jpeg.orig")
Write-Output "NEW IMAGE FOR WEBSITE.jpeg.orig: $($img.Width) x $($img.Height)"
$img.Dispose()
"""

with open('scratch/inspect_orig.ps1', 'w') as f:
    f.write(ps)

res = subprocess.run(['powershell', '-File', 'scratch/inspect_orig.ps1'], capture_output=True, text=True)
print(res.stdout)

