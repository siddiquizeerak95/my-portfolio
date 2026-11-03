import re

for fname, title_str in [
    ("blog.html", "Blog &amp; Insights — ZS STUDIO | UI/UX Designer &amp; Frontend Developer"),
    ("contact.html", "Contact — ZS STUDIO | UI/UX Designer &amp; Frontend Developer")
]:
    with open(fname, "r", encoding="utf-8") as f:
        c = f.read()
    c = re.sub(r'<title>.*?</title>', f'<title>{title_str}</title>', c, count=1)
    with open(fname, "w", encoding="utf-8") as f:
        f.write(c)

print("Updated blog.html and contact.html titles!")
