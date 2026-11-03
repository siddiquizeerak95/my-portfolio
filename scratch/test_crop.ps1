Add-Type -AssemblyName System.Drawing

$srcPath = Resolve-Path "NEW IMAGE FOR WEBSITE.jpeg"
$bakPath = "NEW IMAGE FOR WEBSITE.jpeg.orig"

if (-not (Test-Path $bakPath)) {
    Copy-Item $srcPath $bakPath
    Write-Output "Created original backup: $bakPath"
}

$bmp = [System.Drawing.Bitmap]::FromFile($srcPath)
Write-Output "Original Size: $($bmp.Width) x $($bmp.Height)"

# Crop rect: x=0, y=160, width=1203, height=1281
$cropRect = New-Object System.Drawing.Rectangle(0, 160, $bmp.Width, 1281)
$cropped = $bmp.Clone($cropRect, $bmp.PixelFormat)

$bmp.Dispose()

# Save high quality JPEG
$encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
$encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]98)

$cropped.Save($srcPath, $encoder, $encoderParams)
$cropped.Dispose()

Write-Output "Successfully saved cropped portrait without white letterboxing bars!"

