import subprocess

ps = """
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile("c:\\Users\\siddi\\Desktop\\New folder\\NEW IMAGE FOR WEBSITE.jpeg")
Write-Output "NEW IMAGE FOR WEBSITE.jpeg: $($img.Width) x $($img.Height), Format: $($img.RawFormat)"
$img.Dispose()
"""

with open('scratch/inspect_img.ps1', 'w') as f:
    f.write(ps)

res = subprocess.run(['powershell', '-File', 'scratch/inspect_img.ps1'], capture_output=True, text=True)
print(res.stdout)

