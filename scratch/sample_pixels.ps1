[System.Reflection.Assembly]::LoadWithPartialName("System.Drawing") | Out-Null
$bmp = [System.Drawing.Bitmap]::FromFile((Resolve-Path "NEW IMAGE FOR WEBSITE.jpeg").Path)
Write-Output "Dimensions: $($bmp.Width) x $($bmp.Height)"
Write-Output "Top-left (10, 10): $($bmp.GetPixel(10, 10))"
Write-Output "Top-center (420, 10): $($bmp.GetPixel(420, 10))"
Write-Output "Top-right (830, 10): $($bmp.GetPixel(830, 10))"
Write-Output "Mid-left (10, 460): $($bmp.GetPixel(10, 460))"
Write-Output "Mid-right (830, 460): $($bmp.GetPixel(830, 460))"
Write-Output "Bottom-left (10, 910): $($bmp.GetPixel(10, 910))"
Write-Output "Bottom-right (830, 910): $($bmp.GetPixel(830, 910))"
$bmp.Dispose()

