
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile("c:\Users\siddi\Desktop\New folder\NEW IMAGE FOR WEBSITE.jpeg")
Write-Output "Image size: $($img.Width) x $($img.Height)"

# Sample top-left, top-center, middle, bottom
$top = $img.GetPixel($($img.Width / 2), 20)
Write-Output "Top-center (x=$($img.Width / 2), y=20): R=$($top.R), G=$($top.G), B=$($top.B)"

$face = $img.GetPixel($($img.Width / 2), $($img.Height / 2))
Write-Output "Face (x=$($img.Width / 2), y=$($img.Height / 2)): R=$($face.R), G=$($face.G), B=$($face.B)"

$bottom = $img.GetPixel($($img.Width / 2), $($img.Height - 20))
Write-Output "Bottom-center: R=$($bottom.R), G=$($bottom.G), B=$($bottom.B)"

# Let's also check Profile Pic.jpg in git
$img.Dispose()
