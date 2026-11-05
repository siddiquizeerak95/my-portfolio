import subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

test_code = """
<!DOCTYPE html>
<html>
<body>
<script>
async function run() {
  // fetch blog.html
  // or test directly
}
</script>
</body>
</html>
"""

# Let's write a script that opens blog.html, scrolls, and outputs the exact state of each card

