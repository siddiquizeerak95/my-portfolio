
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile("c:\Users\siddi\Desktop\New folder\NEW IMAGE FOR WEBSITE.jpeg.orig")

# The inner portrait is at X: 180, Y: 160 + 180 = 340, width: 842, height: 922
$cropRect = New-Object System.Drawing.Rectangle(180, 340, 842, 922)
$cropped = $img.Clone($cropRect, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)

$cropped.Save("c:\Users\siddi\Desktop\New folder\scratch\actual_portrait.jpg", [System.Drawing.Imaging.ImageFormat]::Jpeg)
Write-Output ("Saved actual portrait: " + $cropped.Width + " x " + $cropped.Height)

$cropped.Dispose()
$img.Dispose()
