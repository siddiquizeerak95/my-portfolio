import subprocess

ps = """
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile("c:\\Users\\siddi\\Desktop\\New folder\\NEW IMAGE FOR WEBSITE.jpeg.orig")

# Let's inspect along Y = 165 (just inside the top)
# What are the colors across X at Y = 170?
$xMin = 0
$xMax = $img.Width - 1

for ($x = 0; $x -lt $img.Width; $x += 10) {
    $c = $img.GetPixel($x, 170)
    # Check if not white (white is > 240)
    if ($c.R -lt 230) {
        $xMin = $x
        break
    }
}

for ($x = $img.Width - 1; $x -ge 0; $x -= 10) {
    $c = $img.GetPixel($x, 170)
    if ($c.R -lt 230) {
        $xMax = $x
        break
    }
}

Write-Output "At Y=170, non-white X range is $xMin to $xMax"

# Check across multiple Y values: 200, 400, 600, 800, 1000, 1200, 1400
foreach ($testY in @(200, 400, 600, 800, 1000, 1200, 1400)) {
    $min = 0
    $max = 0
    for ($x = 0; $x -lt $img.Width; $x++) {
        $c = $img.GetPixel($x, $testY)
        if ($c.R -lt 230 -or $c.G -lt 230 -or $c.B -lt 230) {
            $min = $x
            break
        }
    }
    for ($x = $img.Width - 1; $x -ge 0; $x--) {
        $c = $img.GetPixel($x, $testY)
        if ($c.R -lt 230 -or $c.G -lt 230 -or $c.B -lt 230) {
            $max = $x
            break
        }
    }
    Write-Output "At Y=$testY : X=$min to $max (width: $($max - $min))"
}

$img.Dispose()
"""

with open('scratch/scan_x.ps1', 'w') as f:
    f.write(ps)

res = subprocess.run(['powershell', '-File', 'scratch/scan_x.ps1'], capture_output=True, text=True)
print(res.stdout)

