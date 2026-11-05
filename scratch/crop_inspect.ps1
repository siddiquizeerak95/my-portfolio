
Add-Type -AssemblyName System.Drawing
$bmp = [System.Drawing.Bitmap]::FromFile("c:\Users\siddi\Desktop\New folder\test_hero_with_orig.png")

$rect = New-Object System.Drawing.Rectangle(800, 150, 450, 650)
$cropped = $bmp.Clone($rect, $bmp.PixelFormat)
$cropped.Save("c:\Users\siddi\Desktop\New folder\scratch\hero_card_crop.png", [System.Drawing.Imaging.ImageFormat]::Png)

for ($y = 160; $y -le 750; $y += 20) {
    $c = $bmp.GetPixel(1000, $y)
    Write-Output ("y=" + $y + " R=" + $c.R + " G=" + $c.G + " B=" + $c.B)
}

$bmp.Dispose()
$cropped.Dispose()
