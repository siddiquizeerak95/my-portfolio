import subprocess

ps = """
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile("c:\\Users\\siddi\\Desktop\\New folder\\NEW IMAGE FOR WEBSITE.jpeg")

$minX = $img.Width
$maxX = 0
$minY = $img.Height
$maxY = 0

for ($y = 0; $y -lt $img.Height; $y += 5) {
    for ($x = 0; $x -lt $img.Width; $x += 5) {
        $pixel = $img.GetPixel($x, $y)
        # If not pure black (R>15 or G>15 or B>15)
        if ($pixel.R -gt 15 -or $pixel.G -gt 15 -or $pixel.B -gt 15) {
            if ($x -lt $minX) { $minX = $x }
            if ($x -gt $maxX) { $maxX = $x }
            if ($y -lt $minY) { $minY = $y }
            if ($y -gt $maxY) { $maxY = $y }
        }
    }
}

Write-Output "Non-black bounds: X from $minX to $maxX (width: $($maxX - $minX)), Y from $minY to $maxY (height: $($maxY - $minY))"
Write-Output "Total image: $($img.Width) x $($img.Height)"
Write-Output "Top black padding: $minY px ($([math]::Round($minY / $img.Height * 100, 1))%)"
Write-Output "Bottom black padding: $($img.Height - $maxY) px ($([math]::Round(($img.Height - $maxY) / $img.Height * 100, 1))%)"

$img.Dispose()
"""

with open('scratch/find_bounds.ps1', 'w') as f:
    f.write(ps)

res = subprocess.run(['powershell', '-File', 'scratch/find_bounds.ps1'], capture_output=True, text=True)
print(res.stdout)

