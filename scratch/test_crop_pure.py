import subprocess
import os

ps = """
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile("c:\\Users\\siddi\\Desktop\\New folder\\NEW IMAGE FOR WEBSITE.jpeg.orig")

# Clean crop: remove the 160px top white bar and 158px bottom white bar
$cropRect = New-Object System.Drawing.Rectangle(0, 160, 1203, 1282)
$cropped = $img.Clone($cropRect, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)

# Save as test_pure_portrait.jpg
$cropped.Save("c:\\Users\\siddi\\Desktop\\New folder\\scratch\\test_pure_portrait.jpg", [System.Drawing.Imaging.ImageFormat]::Jpeg)

Write-Output "Cropped portrait: $($cropped.Width) x $($cropped.Height)"

$cropped.Dispose()
$img.Dispose()
"""

with open('scratch/crop_pure.ps1', 'w') as f:
    f.write(ps)

res = subprocess.run(['powershell', '-File', 'scratch/crop_pure.ps1'], capture_output=True, text=True)
print(res.stdout)

