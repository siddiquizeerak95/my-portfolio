import re

path = r"c:\Users\siddi\Desktop\New folder\skills.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update title & meta
content = re.sub(
    r'<title>.*?</title>',
    '<title>Skills &amp; Capabilities — ZS STUDIO | UI/UX Designer &amp; Frontend Developer</title>',
    content,
    count=1
)
content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="UI/UX Design skills, Design Tools, and Frontend Development capabilities of Zeerak Siddiqui at ZS STUDIO.">',
    content,
    count=1
)

# 2. Update page hero
old_hero = '''        <h1 class="page-title reveal-item">
          Technologies I Work <span class="text-accent-red">With.</span>
        </h1>
        <p class="page-lead reveal-item">
          Technologies, systems logic, and architectural tools I use to build modern, high-performance digital experiences with zero framework bloat.
        </p>'''

new_hero = '''        <h1 class="page-title reveal-item">
          Design &amp; Engineering <span class="text-accent-red">Capabilities.</span>
        </h1>
        <p class="page-lead reveal-item">
          Core UI/UX design methodologies, modern creative tools, and frontend engineering principles I utilize to craft intuitive, human-centered digital experiences.
        </p>'''

content = content.replace(old_hero, new_hero)

# 3. Update filter pills on pedestal
old_pills = '''        <!-- Category Filter Pills -->
        <div class="skills-filter-row reveal-item" role="tablist" aria-label="Skill category filters">
          <button class="skills-filter-pill active" data-category="all" role="tab" aria-selected="true">All</button>
          <button class="skills-filter-pill" data-category="frontend" role="tab" aria-selected="false">Frontend</button>
          <button class="skills-filter-pill" data-category="backend" role="tab" aria-selected="false">Backend</button>
          <button class="skills-filter-pill" data-category="tools" role="tab" aria-selected="false">Tools</button>
          <button class="skills-filter-pill" data-category="other" role="tab" aria-selected="false">Other</button>
        </div>'''

new_pills = '''        <!-- Category Filter Pills -->
        <div class="skills-filter-row reveal-item" role="tablist" aria-label="Skill category filters">
          <button class="skills-filter-pill active" data-category="all" role="tab" aria-selected="true">All Skills</button>
          <button class="skills-filter-pill" data-category="uiux" role="tab" aria-selected="false">UI/UX Design</button>
          <button class="skills-filter-pill" data-category="tools" role="tab" aria-selected="false">Design Tools</button>
          <button class="skills-filter-pill" data-category="frontend" role="tab" aria-selected="false">Frontend Development</button>
        </div>'''

content = content.replace(old_pills, new_pills)

# 4. Update 3D pedestal cards
old_cards = '''          <!-- Cards Row floating above the pedestal -->
          <div class="skills-cards-stage-grid grid-6" id="skills-cards-container">
            <!-- Card 1: HTML & CSS -->
            <article class="skill-card-3d" data-category="frontend" data-tilt>
              <div class="skill-card-glass">
                <div class="skill-card-icon-wrap icon-code">
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <polyline points="16 18 22 12 16 6"></polyline>
                    <polyline points="8 6 2 12 8 18"></polyline>
                  </svg>
                </div>
                <h3 class="skill-card-title">HTML &amp; CSS</h3>
                <span class="skill-card-role">FRONTEND &bull; LAYOUT</span>
                <p class="skill-card-desc">Semantic DOM, CSS Grid, spatial mathematical clamp() scaling.</p>
                <div class="skill-card-status">
                  <span class="status-indicator-bar" style="--bar-level: 90%;"></span>
                  <span class="status-text">90%</span>
                </div>
              </div>
            </article>

            <!-- Card 2: JavaScript -->
            <article class="skill-card-3d" data-category="frontend" data-tilt>
              <div class="skill-card-glass">
                <div class="skill-card-icon-wrap icon-js">
                  <span class="js-badge-text">JS</span>
                </div>
                <h3 class="skill-card-title">JavaScript</h3>
                <span class="skill-card-role">FRONTEND &bull; ES6+</span>
                <p class="skill-card-desc">Asynchronous promises, DOM reactivity, hardware canvas engines.</p>
                <div class="skill-card-status">
                  <span class="status-indicator-bar" style="--bar-level: 80%;"></span>
                  <span class="status-text">80%</span>
                </div>
              </div>
            </article>

            <!-- Card 3: React -->
            <article class="skill-card-3d" data-category="frontend" data-tilt>
              <div class="skill-card-glass">
                <div class="skill-card-icon-wrap icon-react">
                  <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">
                    <ellipse cx="12" cy="12" rx="10" ry="4"></ellipse>
                    <ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(60 12 12)"></ellipse>
                    <ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(120 12 12)"></ellipse>
                    <circle cx="12" cy="12" r="2" fill="currentColor"></circle>
                  </svg>
                </div>
                <h3 class="skill-card-title">React</h3>
                <span class="skill-card-role">FRONTEND &bull; COMPONENT</span>
                <p class="skill-card-desc">Modular component hierarchies, state management, and modern hooks.</p>
                <div class="skill-card-status">
                  <span class="status-indicator-bar" style="--bar-level: 75%;"></span>
                  <span class="status-text">75%</span>
                </div>
              </div>
            </article>

            <!-- Card 4: Node.js -->
            <article class="skill-card-3d" data-category="backend" data-tilt>
              <div class="skill-card-glass">
                <div class="skill-card-icon-wrap icon-node">
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <path d="M12 2L3 7v10l9 5 9-5V7l-9-5z"></path>
                    <path d="M12 22V12"></path>
                    <path d="M12 12L3 7"></path>
                    <path d="M12 12l9-5"></path>
                  </svg>
                </div>
                <h3 class="skill-card-title">Node.js</h3>
                <span class="skill-card-role">BACKEND &bull; RUNTIME</span>
                <p class="skill-card-desc">Event-driven asynchronous server runtimes, REST APIs, and microservices.</p>
                <div class="skill-card-status">
                  <span class="status-indicator-bar" style="--bar-level: 70%;"></span>
                  <span class="status-text">70%</span>
                </div>
              </div>
            </article>

            <!-- Card 5: Figma -->
            <article class="skill-card-3d" data-category="tools" data-tilt>
              <div class="skill-card-glass">
                <div class="skill-card-icon-wrap icon-figma">
                  <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">
                    <circle cx="12" cy="12" r="3.5"></circle>
                    <path d="M5 5.5A3.5 3.5 0 0 1 8.5 2H12v7H8.5A3.5 3.5 0 0 1 5 5.5z"></path>
                    <path d="M12 2h3.5a3.5 3.5 0 1 1 0 7H12V2z"></path>
                    <path d="M12 12.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 1 1-7 0z"></path>
                    <path d="M5 19.5A3.5 3.5 0 0 1 8.5 16H12v3.5a3.5 3.5 0 1 1-7 0z"></path>
                    <path d="M5 12.5A3.5 3.5 0 0 1 8.5 9H12v7H8.5A3.5 3.5 0 0 1 5 12.5z"></path>
                  </svg>
                </div>
                <h3 class="skill-card-title">Figma</h3>
                <span class="skill-card-role">TOOLS &bull; DESIGN</span>
                <p class="skill-card-desc">UI/UX wireframing, design tokens, auto-layout, and interactive prototypes.</p>
                <div class="skill-card-status">
                  <span class="status-indicator-bar" style="--bar-level: 85%;"></span>
                  <span class="status-text">85%</span>
                </div>
              </div>
            </article>

            <!-- Card 6: C Programming -->
            <article class="skill-card-3d" data-category="other" data-tilt>
              <div class="skill-card-glass">
                <div class="skill-card-icon-wrap" style="font-family: var(--font-mono); font-weight: 700; font-size: 18px; color: #FFFFFF;">
                  <span>[C]</span>
                </div>
                <h3 class="skill-card-title">C Language</h3>
                <span class="skill-card-role">SYSTEMS &bull; LOGIC</span>
                <p class="skill-card-desc">Dynamic memory allocation (malloc/free), pointers, and core data structures.</p>
                <div class="skill-card-status">
                  <span class="status-indicator-bar" style="--bar-level: 85%;"></span>
                  <span class="status-text">85%</span>
                </div>
              </div>
            </article>
          </div>'''

new_cards = '''          <!-- Cards Row floating above the pedestal -->
          <div class="skills-cards-stage-grid grid-6" id="skills-cards-container">
            <!-- Card 1: UI/UX Design -->
            <article class="skill-card-3d" data-category="uiux" data-tilt>
              <div class="skill-card-glass">
                <div class="skill-card-icon-wrap icon-code" style="color: #E5092B;">
                  <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                    <line x1="8" y1="21" x2="16" y2="21"></line>
                    <line x1="12" y1="17" x2="12" y2="21"></line>
                  </svg>
                </div>
                <h3 class="skill-card-title">UI/UX Design</h3>
                <span class="skill-card-role">EXPERIENCE &bull; USABILITY</span>
                <p class="skill-card-desc">User research, wireframing, high-fidelity prototypes, and user flows.</p>
                <div class="skill-card-status">
                  <span class="status-indicator-bar" style="--bar-level: 88%;"></span>
                  <span class="status-text">Skilled</span>
                </div>
              </div>
            </article>

            <!-- Card 2: Design Systems -->
            <article class="skill-card-3d" data-category="uiux" data-tilt>
              <div class="skill-card-glass">
                <div class="skill-card-icon-wrap" style="color: #61DAFB;">
                  <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
                    <polyline points="2 17 12 22 22 17"></polyline>
                    <polyline points="2 12 12 17 22 12"></polyline>
                  </svg>
                </div>
                <h3 class="skill-card-title">Design Systems</h3>
                <span class="skill-card-role">TOKENS &bull; COMPONENTS</span>
                <p class="skill-card-desc">Modular typography scales, accessible color palettes, and auto-layout.</p>
                <div class="skill-card-status">
                  <span class="status-indicator-bar" style="--bar-level: 85%;"></span>
                  <span class="status-text">Skilled</span>
                </div>
              </div>
            </article>

            <!-- Card 3: Figma -->
            <article class="skill-card-3d" data-category="tools" data-tilt>
              <div class="skill-card-glass">
                <div class="skill-card-icon-wrap icon-figma">
                  <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">
                    <circle cx="12" cy="12" r="3.5"></circle>
                    <path d="M5 5.5A3.5 3.5 0 0 1 8.5 2H12v7H8.5A3.5 3.5 0 0 1 5 5.5z"></path>
                    <path d="M12 2h3.5a3.5 3.5 0 1 1 0 7H12V2z"></path>
                    <path d="M12 12.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 1 1-7 0z"></path>
                    <path d="M5 19.5A3.5 3.5 0 0 1 8.5 16H12v3.5a3.5 3.5 0 1 1-7 0z"></path>
                    <path d="M5 12.5A3.5 3.5 0 0 1 8.5 9H12v7H8.5A3.5 3.5 0 0 1 5 12.5z"></path>
                  </svg>
                </div>
                <h3 class="skill-card-title">Figma</h3>
                <span class="skill-card-role">TOOLS &bull; PROTOTYPING</span>
                <p class="skill-card-desc">Interactive micro-interactions, responsive variants, and design specs.</p>
                <div class="skill-card-status">
                  <span class="status-indicator-bar" style="--bar-level: 90%;"></span>
                  <span class="status-text">Primary Tool</span>
                </div>
              </div>
            </article>

            <!-- Card 4: Framer -->
            <article class="skill-card-3d" data-category="tools" data-tilt>
              <div class="skill-card-glass">
                <div class="skill-card-icon-wrap" style="color: #FFFFFF; font-family: var(--font-mono); font-weight: 700; font-size: 16px;">
                  <span>FR</span>
                </div>
                <h3 class="skill-card-title">Framer</h3>
                <span class="skill-card-role">TOOLS &bull; MOTION</span>
                <p class="skill-card-desc">Interactive web prototypes, scroll interactions, and visual layout publishing.</p>
                <div class="skill-card-status">
                  <span class="status-indicator-bar" style="--bar-level: 75%;"></span>
                  <span class="status-text">Intermediate</span>
                </div>
              </div>
            </article>

            <!-- Card 5: HTML5 &amp; CSS3 -->
            <article class="skill-card-3d" data-category="frontend" data-tilt>
              <div class="skill-card-glass">
                <div class="skill-card-icon-wrap icon-code">
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <polyline points="16 18 22 12 16 6"></polyline>
                    <polyline points="8 6 2 12 8 18"></polyline>
                  </svg>
                </div>
                <h3 class="skill-card-title">HTML5 &amp; CSS3</h3>
                <span class="skill-card-role">FRONTEND &bull; SEMANTICS</span>
                <p class="skill-card-desc">Responsive web development, CSS Grid, clamp() scaling, and WCAG accessibility.</p>
                <div class="skill-card-status">
                  <span class="status-indicator-bar" style="--bar-level: 90%;"></span>
                  <span class="status-text">Proficient</span>
                </div>
              </div>
            </article>

            <!-- Card 6: JavaScript &amp; React -->
            <article class="skill-card-3d" data-category="frontend" data-tilt>
              <div class="skill-card-glass">
                <div class="skill-card-icon-wrap icon-js">
                  <span class="js-badge-text">JS</span>
                </div>
                <h3 class="skill-card-title">JavaScript &amp; React</h3>
                <span class="skill-card-role">FRONTEND &bull; LOGIC</span>
                <p class="skill-card-desc">ES6+ DOM manipulation, event pipelines, and foundational React components.</p>
                <div class="skill-card-status">
                  <span class="status-indicator-bar" style="--bar-level: 80%;"></span>
                  <span class="status-text">Competent</span>
                </div>
              </div>
            </article>
          </div>'''

content = content.replace(old_cards, new_cards)

# 5. Insert the Complete UI/UX Skills Directory (Editable & Structured)
skills_directory_html = '''    <!-- =========================================================================
         DEDICATED UI/UX & FRONTEND SKILLS DIRECTORY (EDITABLE)
         ========================================================================= -->
    <section class="section" style="padding-top: 20px;" aria-label="Structured Skills Directory">
      <div class="container">
        <div class="section-tag-row reveal-item">
          <span class="section-red-dot" aria-hidden="true"></span>
          <span class="section-tag-text">SKILLS DIRECTORY</span>
        </div>
        <h2 class="section-heading-zs reveal-item" style="font-size: clamp(2rem, 3.5vw, 2.8rem); margin-bottom: 8px;">
          Disciplines &amp; <span class="text-accent-red">Toolkit.</span>
        </h2>
        <p class="section-lead-zs reveal-item" style="margin-bottom: 36px;">
          A transparent overview of my UI/UX design capabilities and frontend web development skills.
        </p>

        <div class="skills-category-showcase reveal-item">
          <!-- Category 1: UI/UX Design -->
          <div class="skills-category-group">
            <h3 class="skills-category-heading">
              <span>UI/UX Design</span>
              <span class="cat-badge">8 Core Disciplines</span>
            </h3>
            <div class="skills-pills-wrap">
              <!-- Editable Skill Chips -->
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

          <!-- Category 2: Design Tools -->
          <div class="skills-category-group">
            <h3 class="skills-category-heading">
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

          <!-- Category 3: Frontend Development -->
          <div class="skills-category-group">
            <h3 class="skills-category-heading">
              <span>Frontend Development</span>
              <span class="cat-badge">Engineering &bull; Web Standards</span>
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
      </div>
    </section>
'''

# Insert directory right before SECTION: 4 CORE ARCHITECTURAL PILLARS
content = content.replace(
    '<!-- SECTION: 4 CORE ARCHITECTURAL PILLARS (DEEP DIVE MATRIX) -->',
    skills_directory_html + '\n    <!-- SECTION: 4 CORE ARCHITECTURAL PILLARS (DEEP DIVE MATRIX) -->'
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated skills.html successfully!")
