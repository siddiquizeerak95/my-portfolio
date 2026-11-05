
Add-Type -AssemblyName System.Drawing
$imgPadded = [System.Drawing.Bitmap]::FromFile("c:\Users\siddi\Desktop\New folder\NEW IMAGE FOR WEBSITE.jpeg")
$imgOrig = [System.Drawing.Bitmap]::FromFile("c:\Users\siddi\Desktop\New folder\NEW IMAGE FOR WEBSITE.jpeg.orig")

Write-Output "Padded: $($imgPadded.Width) x $($imgPadded.Height)"
Write-Output "Orig: $($imgOrig.Width) x $($imgOrig.Height)"

# In padded, non-black was Y: 175 to 1095 (height 920). 
# Aspect ratio of content in padded: 835 / 920 = 0.907.
# Aspect ratio of orig: 1203 / 1600 = 0.751 (standard 3:4 portrait!).

$imgPadded.Dispose()
$imgOrig.Dispose()
