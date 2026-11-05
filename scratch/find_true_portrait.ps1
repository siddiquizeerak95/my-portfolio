
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile("c:\Users\siddi\Desktop\New folder\NEW IMAGE FOR WEBSITE.jpeg.orig")
Write-Output "Image size: $($img.Width) x $($img.Height)"

# Check where top white bar ends
$topY = 0
for ($y = 0; $y -lt $img.Height; $y++) {
    $c = $img.GetPixel($($img.Width / 2), $y)
    # Check if pixel is white or near white (R>240, G>240, B>240)
    if ($c.R -lt 230 -or $c.G -lt 230 -or $c.B -lt 230) {
        $topY = $y
        break
    }
}
Write-Output "Top white bar ends at Y = $topY"

# Check where bottom white bar begins
$bottomY = $img.Height - 1
for ($y = $img.Height - 1; $y -ge 0; $y--) {
    $c = $img.GetPixel($($img.Width / 2), $y)
    if ($c.R -lt 230 -or $c.G -lt 230 -or $c.B -lt 230) {
        $bottomY = $y
        break
    }
}
Write-Output "Bottom white bar starts at Y = $bottomY"

# Check left and right bounds along Y = 800 (mid portrait)
$leftX = 0
for ($x = 0; $x -lt $img.Width; $x++) {
    $c = $img.GetPixel($x, 800)
    # Not black
    if ($c.R -gt 25 -or $c.G -gt 25 -or $c.B -gt 25) {
        $leftX = $x
        break
    }
}
Write-Output "Left non-black at Y=800: X = $leftX"

$rightX = $img.Width - 1
for ($x = $img.Width - 1; $x -ge 0; $x--) {
    $c = $img.GetPixel($x, 800)
    if ($c.R -gt 25 -or $c.G -gt 25 -or $c.B -gt 25) {
        $rightX = $x
        break
    }
}
Write-Output "Right non-black at Y=800: X = $rightX"

# Now let's inspect the entire portrait region between topY and bottomY
Write-Output "Portrait bounds: Y: $topY to $bottomY (height: $($bottomY - $topY))"

$img.Dispose()
