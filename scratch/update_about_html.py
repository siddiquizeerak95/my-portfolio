import re

path = r"c:\Users\siddi\Desktop\New folder\about.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update title and meta
content = re.sub(
    r'<title>.*?</title>',
    '<title>About — ZS STUDIO | UI/UX Designer &amp; Frontend Developer</title>',
    content,
    count=1
)
content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="About Zeerak Siddiqui — UI/UX Designer &amp; Frontend Developer at ZS STUDIO. Designing intuitive digital experiences and modern web interfaces.">',
    content,
    count=1
)

# 2. Update page lead
old_page_lead = '''        <p class="page-lead reveal-item">
          An authentic chronicle of Zeerak Siddiqui, a BCA student and creative developer exploring computational foundations, clean architecture, and expressive front-end engineering.
        </p>'''

new_page_lead = '''        <p class="page-lead reveal-item">
          An authentic chronicle of Zeerak Siddiqui, a UI/UX designer and frontend developer exploring human-centered usability, design systems, and modern front-end engineering.
        </p>'''

content = content.replace(old_page_lead, new_page_lead)

# 3. Update Bio paragraph
old_bio = '''            <p class="section-lead-zs">
              I'm <strong>Zeerak Siddiqui</strong>, a BCA student with a passion for web development, technology, and creative digital experiences. I enjoy transforming ideas into clean, modern, and meaningful websites through thoughtful design and code.
            </p>'''

new_bio = '''            <p class="section-lead-zs">
              I'm <strong>Zeerak Siddiqui</strong>, a UI/UX Designer &amp; Frontend Developer. I design intuitive digital experiences and build modern interfaces that combine creativity, usability, and technology. Through rigorous wireframing, design systems, and clean front-end code, I transform complex requirements into seamless, human-centered products.
            </p>'''

content = content.replace(old_bio, new_bio)

# 4. Update feature card labels
content = content.replace('<span class="about-feature-title">Web Development</span>', '<span class="about-feature-title">UI/UX Design</span>')
content = content.replace('<span class="about-feature-title">Creative Design</span>', '<span class="about-feature-title">Design Systems</span>')
content = content.replace('<span class="about-feature-title">Problem Solving</span>', '<span class="about-feature-title">UX Prototyping</span>')

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated about.html successfully!")
