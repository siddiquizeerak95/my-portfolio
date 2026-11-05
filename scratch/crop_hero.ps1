
Add-Type -AssemblyName System.Drawing

$bmp = [System.Drawing.Bitmap]::FromFile("c:\Users\siddi\Desktop\New folder\test_hero_debug.png")
Write-Output "Image size: $($bmp.Width) x $($bmp.Height)"

# The hero portrait is on the right side of the screen, around x: 800 to 1250, y: 150 to 650.
# Let's crop that region and save it to test_hero_cropped.png
$rect = New-Object System.Drawing.Rectangle(750, 150, 500, 600)
$cropped = $bmp.Clone($rect, $bmp.PixelFormat)
$cropped.Save("c:\Users\siddi\Desktop\New folder\test_hero_cropped.png", [System.Drawing.Imaging.ImageFormat]::Png)

# Let's sample colors in the center of the card: x=1000, y=400
$c = $bmp.GetPixel(1000, 400)
Write-Output "Center pixel at (1000, 400): R=$($c.R), G=$($c.G), B=$($c.B), A=$($c.A)"

$bmp.Dispose()
$cropped.Dispose()
