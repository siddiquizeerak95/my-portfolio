
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile("c:\Users\siddi\Desktop\New folder\NEW IMAGE FOR WEBSITE.jpeg")
Write-Output "NEW IMAGE FOR WEBSITE.jpeg: $($img.Width) x $($img.Height), Format: $($img.RawFormat)"
$img.Dispose()
