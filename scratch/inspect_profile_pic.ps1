
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile("c:\Users\siddi\Desktop\New folder\scratch\profile_pic_git.jpg")
Write-Output "Profile Pic.jpg: $($img.Width) x $($img.Height)"
$img.Dispose()
