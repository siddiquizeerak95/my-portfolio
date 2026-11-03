import re

path = r"c:\Users\siddi\Desktop\New folder\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update title and meta
content = re.sub(
    r'<title>.*?</title>',
    '<title>ZS STUDIO — UI/UX Designer &amp; Frontend Developer | Zeerak Siddiqui</title>',
    content,
    count=1
)
content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Portfolio of Zeerak Siddiqui — UI/UX Designer &amp; Frontend Developer at ZS STUDIO. Designing intuitive digital experiences and modern web interfaces.">',
    content,
    count=1
)

# 2. Update Hero Subtitle & Description
old_hero_intro = '''            <p class="hero-subtitle-zs">
              BCA STUDENT | WEB DEVELOPER | DIGITAL CREATOR
            </p>

            <p class="hero-desc-zs">
              I build modern and responsive websites with clean design and meaningful user experiences.
            </p>'''

new_hero_intro = '''            <p class="hero-subtitle-zs">
              UI/UX DESIGNER &amp; FRONTEND DEVELOPER
            </p>

            <p class="hero-desc-zs">
              I design intuitive digital experiences and build modern interfaces that combine creativity, usability, and technology.
            </p>'''

content = content.replace(old_hero_intro, new_hero_intro)

# 3. Clean up the accidental duplicate slider controls inside #hero and #home-about and #preview-skills
# Notice in #hero:
hero_stray_controls = '''          <!-- Slider Navigation Controls -->
          <div class="projects-slider-controls">
            <button class="slider-nav-btn prev" id="projects-slider-prev" aria-label="Previous Project">&larr;</button>
            <div class="projects-slider-dots" id="projects-pagination-dots" role="tablist" aria-label="Project slider pagination">
              <button class="slider-dot active" data-index="0" role="tab" aria-selected="true" aria-label="Project 1"></button>
              <button class="slider-dot" data-index="1" role="tab" aria-selected="false" aria-label="Project 2"></button>
              <button class="slider-dot" data-index="2" role="tab" aria-selected="false" aria-label="Project 3"></button>
            </div>
            <button class="slider-nav-btn next" id="projects-slider-next" aria-label="Next Project">&rarr;</button>
          </div>'''

# We want to keep ONLY the one inside #preview-projects!
# Let's count occurrences
parts = content.split(hero_stray_controls)
if len(parts) > 1:
    # The last occurrence is the one inside #preview-projects!
    # Reassemble keeping only the last occurrence
    content = "".join(parts[:-1]) + hero_stray_controls + parts[-1]
    print(f"Removed {len(parts)-2} duplicate slider controls")

# 4. Update About preview section in index.html
old_about_lead = '''            <p class="section-lead-zs">
              I'm <strong>Zeerak Siddiqui</strong>, a BCA student with a passion for web development, technology, and creative digital experiences. I enjoy transforming ideas into clean, modern, and meaningful websites through thoughtful design and code.
            </p>'''

new_about_lead = '''            <p class="section-lead-zs">
              I'm <strong>Zeerak Siddiqui</strong>, a UI/UX Designer &amp; Frontend Developer passionate about crafting intuitive digital experiences and high-performance web interfaces. I combine user research, wireframing, and design systems with modern front-end engineering.
            </p>'''

content = content.replace(old_about_lead, new_about_lead)

# Update feature card titles in #home-about
content = content.replace('<span class="about-feature-title">Web Development</span>', '<span class="about-feature-title">UI/UX Design</span>')
content = content.replace('<span class="about-feature-title">Creative Design</span>', '<span class="about-feature-title">Design Systems</span>')

# 5. Insert "Selected Design Works" section directly before #preview-projects
design_works_section_html = '''    <!-- =========================================================================
         02. SELECTED DESIGN WORKS — DEDICATED UI/UX CASE STUDIES
         ========================================================================= -->
    <section id="selected-design-works" class="section design-works-section" aria-label="Selected Design Works Showcase">
      <div class="container">
        <!-- Section Header -->
        <div class="projects-header-flex reveal-item">
          <div>
            <div class="section-tag-row">
              <span class="section-red-dot" aria-hidden="true"></span>
              <span class="section-tag-text">UI/UX PORTFOLIO</span>
            </div>
            <h2 class="section-heading-zs">Selected Design <span class="text-accent-red">Works.</span></h2>
          </div>
          <div style="text-align: right; max-width: 460px;">
            <p class="section-lead-zs" style="margin-bottom: 14px; text-align: left;">
              Intuitive mobile and web concepts engineered around user research, wireframing, design systems, and rapid prototyping.
            </p>
            <a href="projects.html" class="btn-pill-grey">Explore All Case Studies &rarr;</a>
          </div>
        </div>

        <!-- 2x2 Grid of UI/UX Concept Cards -->
        <div class="design-works-grid">
          <!-- Card 1: Modern E-commerce App -->
          <article class="design-project-card reveal-item" data-tilt>
            <div class="design-card-preview">
              <img src="assets/project-ecommerce-preview.svg" alt="Modern E-commerce App Concept" width="560" height="350" loading="eager">
            </div>
            <div class="design-card-header">
              <span class="design-card-category">Mobile App &bull; E-commerce</span>
              <span class="concept-tag-badge"><span class="concept-dot"></span> CONCEPT DESIGN</span>
            </div>
            <h3 class="design-card-title">Modern E-commerce App</h3>
            <p class="design-card-desc">
              An end-to-end mobile shopping experience crafted with intuitive product discovery, micro-interactions, seamless checkout flow, and an accessible design system.
            </p>
            <div class="design-tools-row">
              <span class="design-tool-pill">Figma</span>
              <span class="design-tool-pill">User Research</span>
              <span class="design-tool-pill">Prototyping</span>
              <span class="design-tool-pill">Design System</span>
            </div>
            <a href="case-study-ecommerce.html" class="btn-case-study">
              <span>View Case Study</span>
              <span>&rarr;</span>
            </a>
          </article>

          <!-- Card 2: Personal Finance Dashboard -->
          <article class="design-project-card reveal-item" data-tilt>
            <div class="design-card-preview">
              <img src="assets/project-finance-preview.svg" alt="Personal Finance Dashboard Concept" width="560" height="350" loading="eager">
            </div>
            <div class="design-card-header">
              <span class="design-card-category">Web App UI &bull; FinTech</span>
              <span class="concept-tag-badge"><span class="concept-dot"></span> CONCEPT DESIGN</span>
            </div>
            <h3 class="design-card-title">Personal Finance Dashboard</h3>
            <p class="design-card-desc">
              A clean financial management dashboard visualizing cash flow, asset allocation, and spending trends with dark/light data visualization patterns.
            </p>
            <div class="design-tools-row">
              <span class="design-tool-pill">Figma</span>
              <span class="design-tool-pill">Data Visualization</span>
              <span class="design-tool-pill">Design System</span>
              <span class="design-tool-pill">Wireframing</span>
            </div>
            <a href="case-study-finance.html" class="btn-case-study">
              <span>View Case Study</span>
              <span>&rarr;</span>
            </a>
          </article>

          <!-- Card 3: Mobile Banking App -->
          <article class="design-project-card reveal-item" data-tilt>
            <div class="design-card-preview">
              <img src="assets/project-banking-preview.svg" alt="Mobile Banking App Concept" width="560" height="350" loading="eager">
            </div>
            <div class="design-card-header">
              <span class="design-card-category">FinTech UX &bull; Mobile</span>
              <span class="concept-tag-badge"><span class="concept-dot"></span> CONCEPT DESIGN</span>
            </div>
            <h3 class="design-card-title">Mobile Banking App</h3>
            <p class="design-card-desc">
              A security-focused mobile banking interface prioritizing effortless peer-to-peer transfers, biometric authorization flows, and friction-free card management.
            </p>
            <div class="design-tools-row">
              <span class="design-tool-pill">Figma</span>
              <span class="design-tool-pill">UX Architecture</span>
              <span class="design-tool-pill">Interactive Prototyping</span>
              <span class="design-tool-pill">User Flows</span>
            </div>
            <a href="case-study-banking.html" class="btn-case-study">
              <span>View Case Study</span>
              <span>&rarr;</span>
            </a>
          </article>

          <!-- Card 4: Creative Portfolio Website -->
          <article class="design-project-card reveal-item" data-tilt>
            <div class="design-card-preview">
              <img src="assets/project-designportfolio-preview.svg" alt="Creative Portfolio Website Concept" width="560" height="350" loading="eager">
            </div>
            <div class="design-card-header">
              <span class="design-card-category">Brand &bull; Editorial Web</span>
              <span class="concept-tag-badge"><span class="concept-dot"></span> CONCEPT DESIGN</span>
            </div>
            <h3 class="design-card-title">Creative Portfolio Website</h3>
            <p class="design-card-desc">
              A minimalist editorial portfolio concept designed for creative studios, featuring brutalist spatial grids, typographic rhythm, and interactive 3D showcases.
            </p>
            <div class="design-tools-row">
              <span class="design-tool-pill">Figma</span>
              <span class="design-tool-pill">Framer</span>
              <span class="design-tool-pill">Design Tokens</span>
              <span class="design-tool-pill">Responsive Design</span>
            </div>
            <a href="case-study-portfolio.html" class="btn-case-study">
              <span>View Case Study</span>
              <span>&rarr;</span>
            </a>
          </article>
        </div>
      </div>
    </section>

'''

if '<section id="selected-design-works"' not in content:
    content = content.replace(
        '<!-- =========================================================================\n         02. PROJECTS SECTION — EXACT REFERENCE IMAGE 3',
        design_works_section_html + '<!-- =========================================================================\n         02.2 FEATURED CODE PROJECTS & 3D SLIDER'
    )

# 6. Update #preview-skills section to include UI/UX Design, Design Tools, and Frontend Development
skills_overview_html = '''        <!-- Structured Categories Overview -->
        <div class="skills-category-showcase reveal-item" style="margin-bottom: 36px;">
          <!-- UI/UX Design -->
          <div class="skills-category-group" style="margin-bottom: 24px;">
            <h3 class="skills-category-heading" style="font-size: 16px;">
              <span>UI/UX Design</span>
              <span class="cat-badge">Core Disciplines</span>
            </h3>
            <div class="skills-pills-wrap">
              <span class="skill-editable-chip"><span class="chip-dot"></span> User Interface Design</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> User Experience Design</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> Wireframing</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> Prototyping</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> User Research</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> Design Systems</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> Responsive Design</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> Visual Design</span>
            </div>
          </div>

          <!-- Design Tools -->
          <div class="skills-category-group" style="margin-bottom: 24px;">
            <h3 class="skills-category-heading" style="font-size: 16px;">
              <span>Design Tools</span>
              <span class="cat-badge">Creative Suite</span>
            </h3>
            <div class="skills-pills-wrap">
              <span class="skill-editable-chip"><span class="chip-dot"></span> Figma</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> Adobe Photoshop</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> Adobe Illustrator</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> Framer</span>
            </div>
          </div>

          <!-- Frontend Development -->
          <div class="skills-category-group">
            <h3 class="skills-category-heading" style="font-size: 16px;">
              <span>Frontend Development</span>
              <span class="cat-badge">Engineering &bull; Web</span>
            </h3>
            <div class="skills-pills-wrap">
              <span class="skill-editable-chip"><span class="chip-dot"></span> HTML5</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> CSS3</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> JavaScript</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> Responsive Web Development</span>
              <span class="skill-editable-chip"><span class="chip-dot"></span> Basic React</span>
            </div>
          </div>
        </div>
'''

if '<!-- Structured Categories Overview -->' not in content:
    content = content.replace(
        '<!-- Squircle Modern Tech Grid (From Reference 4) -->',
        skills_overview_html + '\n        <!-- Squircle Modern Tech Grid (From Reference 4) -->'
    )

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html successfully!")
