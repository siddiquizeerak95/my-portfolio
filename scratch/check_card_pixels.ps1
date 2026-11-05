
Add-Type -AssemblyName System.Drawing
$bmp = [System.Drawing.Bitmap]::FromFile("c:\Users\siddi\Desktop\New folder\test_hero_with_orig.png")

# Card is around x: 800 to 1250, y: 200 to 750
# Let's inspect pixel at x: 1000, y: 280 (the top of the card)
$cTop = $bmp.GetPixel(1000, 280)
Write-Output "Pixel at (1000, 280): R=$($cTop.R), G=$($cTop.G), B=$($cTop.B)"

# Pixel at x: 1000, y: 350
$cMid = $bmp.GetPixel(1000, 350)
Write-Output "Pixel at (1000, 350): R=$($cMid.R), G=$($cMid.G), B=$($cMid.B)"

# Pixel at x: 1000, y: 500
$cFace = $bmp.GetPixel(1000, 500)
Write-Output "Pixel at (1000, 500): R=$($cFace.R), G=$($cFace.G), B=$($cFace.B)"

$bmp.Dispose()
