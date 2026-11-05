Add-Type -AssemblyName System.Drawing

$ref = [System.Drawing.Bitmap]::FromFile("C:\Users\siddi\.gemini\antigravity\brain\4dd10c7b-bb97-46d2-a619-344ea8415c35\user_exact_reference.jpg")
Write-Output ("Ref size: " + $ref.Width + " x " + $ref.Height)

# Check colors across X axis at Y = 384 (middle)
for ($x = 0; $x -lt $ref.Width; $x += 40) {
    $p = $ref.GetPixel($x, 384)
    Write-Output ("X=" + $x + ": R=" + $p.R + " G=" + $p.G + " B=" + $p.B)
}

$ref.Dispose()

