ps = """
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile("c:\\Users\\siddi\\Desktop\\New folder\\scratch\\test_pure_portrait.jpg")
Write-Output ("Image size: " + $img.Width + " x " + $img.Height)

$pMinX = $img.Width
$pMaxX = 0
$pMinY = $img.Height
$pMaxY = 0

for ($y = 0; $y -lt $img.Height; $y += 2) {
    for ($x = 0; $x -lt $img.Width; $x += 2) {
        $c = $img.GetPixel($x, $y)
        if ($c.R -gt 15 -or $c.G -gt 15 -or $c.B -gt 15) {
            if ($x -lt $pMinX) { $pMinX = $x }
            if ($x -gt $pMaxX) { $pMaxX = $x }
            if ($y -lt $pMinY) { $pMinY = $y }
            if ($y -gt $pMaxY) { $pMaxY = $y }
        }
    }
}

Write-Output ("Inner photograph bounds: X: " + $pMinX + " to " + $pMaxX + " (width: " + ($pMaxX - $pMinX) + "), Y: " + $pMinY + " to " + $pMaxY + " (height: " + ($pMaxY - $pMinY) + ")")

$img.Dispose()
"""

with open('scratch/find_inner_photo.ps1', 'w') as f:
    f.write(ps)

import subprocess
res = subprocess.run(['powershell', '-File', 'scratch/find_inner_photo.ps1'], capture_output=True, text=True)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
