Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile((Resolve-Path 'NEW IMAGE FOR WEBSITE.jpeg'))
Write-Output "Dimensions: $($img.Width) x $($img.Height)"
$cTop = $img.GetPixel(600, 10)
Write-Output "Top Pixel: R=$($cTop.R) G=$($cTop.G) B=$($cTop.B)"

$firstY = 0
for ($y = 0; $y -lt $img.Height; $y += 2) {
    $c = $img.GetPixel(600, $y)
    if ($c.R -lt 240 -or $c.G -lt 240 -or $c.B -lt 240) {
        $firstY = $y
        break
    }
}

$lastY = $img.Height
for ($y = $img.Height - 1; $y -ge 0; $y -= 2) {
    $c = $img.GetPixel(600, $y)
    if ($c.R -lt 240 -or $c.G -lt 240 -or $c.B -lt 240) {
        $lastY = $y
        break
    }
}

$firstX = 0
for ($x = 0; $x -lt $img.Width; $x += 2) {
    $c = $img.GetPixel($x, 800)
    if ($c.R -lt 240 -or $c.G -lt 240 -or $c.B -lt 240) {
        $firstX = $x
        break
    }
}

$lastX = $img.Width
for ($x = $img.Width - 1; $x -ge 0; $x -= 2) {
    $c = $img.GetPixel($x, 800)
    if ($c.R -lt 240 -or $c.G -lt 240 -or $c.B -lt 240) {
        $lastX = $x
        break
    }
}

$h = $lastY - $firstY
$w = $lastX - $firstX
Write-Output "X range: $firstX to $lastX (width: $w)"
Write-Output "Y range: $firstY to $lastY (height: $h)"
$img.Dispose()

