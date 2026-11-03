Add-Type -AssemblyName System.Drawing
$bmp = [System.Drawing.Bitmap]::FromFile((Resolve-Path 'NEW IMAGE FOR WEBSITE.jpeg.orig'))
Write-Output "Original Size: $($bmp.Width) x $($bmp.Height)"

for ($y = 0; $y -lt $bmp.Height; $y += 50) {
    $c = $bmp.GetPixel(600, $y)
    Write-Output "y=$($y) -> R=$($c.R) G=$($c.G) B=$($c.B)"
}

for ($x = 0; $x -lt $bmp.Width; $x += 50) {
    $c = $bmp.GetPixel($x, 600)
    Write-Output "x=$($x) -> R=$($c.R) G=$($c.G) B=$($c.B)"
}

$bmp.Dispose()
