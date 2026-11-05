import subprocess

# Let's test with headless Chrome on index.html with each variant
# We will create test_path1.html, test_path2.html, etc. and load them via file:/// and http://127.0.0.1:5500/

variants = [
    ("v1_encoded.html", "./NEW%20IMAGE%20FOR%20WEBSITE.jpeg"),
    ("v2_spaces.html", "./NEW IMAGE FOR WEBSITE.jpeg"),
    ("v3_clean.html", "NEW%20IMAGE%20FOR%20WEBSITE.jpeg"),
    ("v4_clean_spaces.html", "NEW IMAGE FOR WEBSITE.jpeg"),
]

for filename, src in variants:
    html = f"""<!DOCTYPE html>
<html>
<head><title>Test</title></head>
<body>
<img id="test-img" src="{src}" style="width: 300px; height: 400px; object-fit: cover;">
<div id="result"></div>
<script>
const img = document.getElementById('test-img');
img.onload = () => {{ document.getElementById('result').innerText = 'LOADED:' + img.naturalWidth + 'x' + img.naturalHeight; }};
img.onerror = () => {{ document.getElementById('result').innerText = 'ERROR'; }};
</script>
</body>
</html>"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Created test files")

