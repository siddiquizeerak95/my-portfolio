Add-Type -AssemblyName System.Drawing

$srcPath = Resolve-Path "NEW IMAGE FOR WEBSITE.jpeg.orig"
$destPath = Resolve-Path "NEW IMAGE FOR WEBSITE.jpeg"

$bmp = [System.Drawing.Bitmap]::FromFile($srcPath)

# Exact photo bounding box:
# x=178, y=167, width=848, height=1266
$cropRect = New-Object System.Drawing.Rectangle(178, 167, 848, 1266)
$cropped = $bmp.Clone($cropRect, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$bmp.Dispose()

$encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
$encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]98)

$cropped.Save($destPath, $encoder, $encoderParams)
$cropped.Dispose()

Write-Output "Successfully saved pure portrait without any bars: 848 x 1266!"

