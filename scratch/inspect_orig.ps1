
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile("c:\Users\siddi\Desktop\New folder\NEW IMAGE FOR WEBSITE.jpeg.orig")
Write-Output "NEW IMAGE FOR WEBSITE.jpeg.orig: $($img.Width) x $($img.Height)"
$img.Dispose()
