import re

path = r"c:\Users\siddi\Desktop\New folder\projects.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update title and meta
content = re.sub(
    r'<title>.*?</title>',
    '<title>Projects &amp; Selected Works — ZS STUDIO | UI/UX Designer &amp; Frontend Developer</title>',
    content,
    count=1
)
content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Selected UI/UX Design Works and Frontend Development projects by Zeerak Siddiqui, UI/UX Designer &amp; Frontend Developer at ZS STUDIO.">',
    content,
    count=1
)

# 2. Update page hero
old_hero = '''        <h1 class="page-title reveal-item">
          Featured <span class="text-accent-red">Projects.</span>
        </h1>
        <p class="page-lead reveal-item">
          A collection of real-world projects and software laboratories engineered from first principles—combining procedural systems logic with luxury creative web experiences.
        </p>'''

new_hero = '''        <h1 class="page-title reveal-item">
          Selected Works &amp; <span class="text-accent-red">Creations.</span>
        </h1>
        <p class="page-lead reveal-item">
          A curated portfolio of UI/UX design case studies and procedural frontend engineering—combining human-centered usability with modern creative web experiences.
        </p>'''

content = content.replace(old_hero, new_hero)

# 3. Update category filter pills and insert 4 Selected Design Works cards
old_filters = '''        <!-- Category Filter Pills -->
        <div class="skills-filter-row reveal-item" style="justify-content: flex-start; margin-bottom: 40px;" role="tablist" aria-label="Project categories">
          <button class="skills-filter-pill active" data-filter="all" role="tab" aria-selected="true">All Creations</button>
          <button class="skills-filter-pill" data-filter="active" role="tab" aria-selected="false">Active Experiences</button>
          <button class="skills-filter-pill" data-filter="lab" role="tab" aria-selected="false">Upcoming Labs</button>
        </div>'''

new_filters_and_design_cards = '''        <!-- Category Filter Pills -->
        <div class="skills-filter-row reveal-item" style="justify-content: flex-start; margin-bottom: 40px;" role="tablist" aria-label="Project categories">
          <button class="skills-filter-pill active" data-filter="all" role="tab" aria-selected="true">All Works</button>
          <button class="skills-filter-pill" data-filter="design" role="tab" aria-selected="false">Selected Design Works</button>
          <button class="skills-filter-pill" data-filter="frontend" role="tab" aria-selected="false">Frontend &amp; Engineering</button>
        </div>'''

content = content.replace(old_filters, new_filters_and_design_cards)

# Add the 4 design works cards before Project 01 in projects-showcase-grid
design_cards_html = '''          <!-- =========================================================================
               SELECTED DESIGN WORKS (UI/UX DESIGN CONCEPTS)
               ========================================================================= -->
          
          <!-- Design Project 01: Modern E-commerce App -->
          <article class="project-card-glass-body reveal-item" data-category="design" data-tilt>
            <div class="project-card-top-meta">
              <span class="project-counter-tag">DESIGN 01 / 04</span>
              <div class="concept-tag-badge">
                <span class="concept-dot"></span>
                <span>CONCEPT DESIGN</span>
              </div>
            </div>

            <div class="project-preview-mockup">
              <img src="assets/project-ecommerce-preview.svg" alt="Modern E-commerce App Mockup" class="project-preview-img" width="560" height="315" loading="eager">
            </div>

            <div class="design-card-category" style="margin-top: 14px; margin-bottom: 6px;">Mobile App &bull; E-commerce</div>
            <h2 class="project-headline-title">Modern E-commerce App</h2>
            <p class="project-summary-copy">
              An end-to-end mobile shopping experience crafted with intuitive product discovery, micro-interactions, seamless checkout flow, and an accessible design system. Designed to reduce purchase friction through contextual bottom drawers and instant biometric authorization.
            </p>

            <div class="project-tags-capsule-row">
              <span class="capsule-tag">Figma</span>
              <span class="capsule-tag">User Research</span>
              <span class="capsule-tag">Prototyping</span>
              <span class="capsule-tag">Design System</span>
            </div>

            <div class="project-action-links">
              <a href="case-study-ecommerce.html" class="btn-case-study">
                <span>View Case Study</span>
                <span>&rarr;</span>
              </a>
            </div>
          </article>

          <!-- Design Project 02: Personal Finance Dashboard -->
          <article class="project-card-glass-body reveal-item" data-category="design" data-tilt>
            <div class="project-card-top-meta">
              <span class="project-counter-tag">DESIGN 02 / 04</span>
              <div class="concept-tag-badge">
                <span class="concept-dot"></span>
                <span>CONCEPT DESIGN</span>
              </div>
            </div>

            <div class="project-preview-mockup">
              <img src="assets/project-finance-preview.svg" alt="Personal Finance Dashboard Mockup" class="project-preview-img" width="560" height="315" loading="eager">
            </div>

            <div class="design-card-category" style="margin-top: 14px; margin-bottom: 6px;">Web App UI &bull; FinTech</div>
            <h2 class="project-headline-title">Personal Finance Dashboard</h2>
            <p class="project-summary-copy">
              A clean financial management dashboard visualizing cash flow, asset allocation, and spending trends with dark/light data visualization patterns. Built around clear visual hierarchy, accessible data charts, and modular telemetry widgets.
            </p>

            <div class="project-tags-capsule-row">
              <span class="capsule-tag">Figma</span>
              <span class="capsule-tag">Data Visualization</span>
              <span class="capsule-tag">Design System</span>
              <span class="capsule-tag">Wireframing</span>
            </div>

            <div class="project-action-links">
              <a href="case-study-finance.html" class="btn-case-study">
                <span>View Case Study</span>
                <span>&rarr;</span>
              </a>
            </div>
          </article>

          <!-- Design Project 03: Mobile Banking App -->
          <article class="project-card-glass-body reveal-item" data-category="design" data-tilt>
            <div class="project-card-top-meta">
              <span class="project-counter-tag">DESIGN 03 / 04</span>
              <div class="concept-tag-badge">
                <span class="concept-dot"></span>
                <span>CONCEPT DESIGN</span>
              </div>
            </div>

            <div class="project-preview-mockup">
              <img src="assets/project-banking-preview.svg" alt="Mobile Banking App Mockup" class="project-preview-img" width="560" height="315" loading="eager">
            </div>

            <div class="design-card-category" style="margin-top: 14px; margin-bottom: 6px;">FinTech UX &bull; Mobile</div>
            <h2 class="project-headline-title">Mobile Banking App</h2>
            <p class="project-summary-copy">
              A security-focused mobile banking interface prioritizing effortless peer-to-peer transfers, biometric authorization flows, and friction-free card management. Engineered with tactile feedback and high-contrast numerical legibility.
            </p>

            <div class="project-tags-capsule-row">
              <span class="capsule-tag">Figma</span>
              <span class="capsule-tag">UX Architecture</span>
              <span class="capsule-tag">Interactive Prototyping</span>
              <span class="capsule-tag">User Flows</span>
            </div>

            <div class="project-action-links">
              <a href="case-study-banking.html" class="btn-case-study">
                <span>View Case Study</span>
                <span>&rarr;</span>
              </a>
            </div>
          </article>

          <!-- Design Project 04: Creative Portfolio Website -->
          <article class="project-card-glass-body reveal-item" data-category="design" data-tilt>
            <div class="project-card-top-meta">
              <span class="project-counter-tag">DESIGN 04 / 04</span>
              <div class="concept-tag-badge">
                <span class="concept-dot"></span>
                <span>CONCEPT DESIGN</span>
              </div>
            </div>

            <div class="project-preview-mockup">
              <img src="assets/project-designportfolio-preview.svg" alt="Creative Portfolio Website Mockup" class="project-preview-img" width="560" height="315" loading="eager">
            </div>

            <div class="design-card-category" style="margin-top: 14px; margin-bottom: 6px;">Brand &amp; Web Design &bull; Editorial</div>
            <h2 class="project-headline-title">Creative Portfolio Website</h2>
            <p class="project-summary-copy">
              A minimalist editorial portfolio concept designed for creative studios, featuring brutalist spatial grids, typographic rhythm, and interactive 3D showcases. Focuses on effortless project exploration and brand authority.
            </p>

            <div class="project-tags-capsule-row">
              <span class="capsule-tag">Figma</span>
              <span class="capsule-tag">Framer</span>
              <span class="capsule-tag">Design Tokens</span>
              <span class="capsule-tag">Responsive Design</span>
            </div>

            <div class="project-action-links">
              <a href="case-study-portfolio.html" class="btn-case-study">
                <span>View Case Study</span>
                <span>&rarr;</span>
              </a>
            </div>
          </article>

          <!-- =========================================================================
               ENGINEERING & FRONTEND LABORATORIES
               ========================================================================= -->
'''

target_marker = '<div class="projects-showcase-grid">\n          <!-- Project 01: The Living Portfolio -->'
if target_marker in content:
    content = content.replace(target_marker, '<div class="projects-showcase-grid">\n' + design_cards_html + '          <!-- Project 01: The Living Portfolio -->')
else:
    # Alternative match
    content = re.sub(
        r'(<div class="projects-showcase-grid">\s*)(<!-- Project 01)',
        r'\1' + design_cards_html + r'\2',
        content,
        count=1
    )

# Update existing projects categories to 'frontend'
content = content.replace('data-category="active"', 'data-category="frontend"')
content = content.replace('data-category="lab"', 'data-category="frontend"')

# Remove duplicate </html> at the end
content = re.sub(r'</html>\s*</html>', '</html>', content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated projects.html successfully!")
