import re

path = r"c:\Users\siddi\Desktop\New folder\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old_hero_grid = '''        <div class="hero-split-grid">
          <!-- Left Column: Typography & Actions -->
          <div class="hero-editorial-col reveal-item">
            <div class="section-tag-row">
              <span class="section-red-dot" aria-hidden="true"></span>
              <span class="section-tag-text">HELLO, I'M</span>
            </div>

            <h1 class="hero-headline-zs">
              Zeerak<br><span class="text-accent-red">Siddiqui.</span>
            </h1>

            <p class="hero-subtitle-zs">
              UI/UX DESIGNER &amp; FRONTEND DEVELOPER
            </p>

            <p class="hero-desc-zs">
              I design intuitive digital experiences and build modern interfaces that combine creativity, usability, and technology.
            </p>

            <!-- Grey Pill Buttons (STRICTLY NO RED BUTTONS) -->
            <div class="hero-actions-row">
              <a href="#preview-projects" class="btn-pill-grey" id="btn-hero-work" aria-label="View My Work">
                <span>View My Work &rarr;</span>
              </a>
              <a href="contact.html" class="btn-pill-grey" id="btn-hero-contact" aria-label="Contact Me">
                <span>Contact Me</span>
              </a>
            </div>

            <!-- Subtle Statistics Row Below Buttons -->
            <div class="hero-stats-row">
              <div class="hero-stat-item">
                <span class="stat-num">10+</span>
                <span class="stat-lbl">Projects</span>
              </div>
              <div class="hero-stat-sep" aria-hidden="true"></div>
              <div class="hero-stat-item">
                <span class="stat-num">BCA</span>
                <span class="stat-lbl">Student</span>
              </div>
              <div class="hero-stat-sep" aria-hidden="true"></div>
              <div class="hero-stat-item">
                <span class="stat-num">Always</span>
                <span class="stat-lbl">Learning</span>
              </div>
            </div>
          </div>

          <!-- Right Column: Profile Portrait & Crimson Halo Stage -->
          <div class="hero-portrait-col reveal-item">
            <div class="hero-visual-stage" id="hero-3d-stage">
              <!-- Glowing Crimson Red Halo Ring -->
              <div class="hero-red-halo" aria-hidden="true"></div>

              <!-- Monochromatic Authentic Portrait Frame -->
              <div class="hero-portrait-wrap">
                <img src="./new%20image.jpeg" alt="Zeerak Siddiqui" class="hero-portrait-photo" width="370" height="370" loading="eager">
              </div>

              <!-- Vertical Watermark Typography on Far Right -->
              <div class="hero-watermark-vertical" aria-hidden="true">
                <span>CODE</span>
                <span class="wm-slash">/</span>
                <span>DESIGN</span>
                <span class="wm-slash">/</span>
                <span>CREATE</span>
                <span class="wm-slash">/</span>
                <span>EXPLORE</span>
              </div>
            </div>
          </div>


        </div>'''

new_hero_grid = '''        <div class="hero-split-grid">
          <!-- Left Column: Typography & Actions (Editorial Composition) -->
          <div class="hero-editorial-col reveal-item">
            <div class="section-tag-row">
              <span class="section-red-dot" aria-hidden="true"></span>
              <span class="section-tag-text">AVAILABLE FOR CREATIVE PROJECTS</span>
            </div>

            <h1 class="hero-headline-zs">
              Hi, I'm<br><span class="text-accent-red">Zeerak Siddiqui.</span>
            </h1>

            <p class="hero-subtitle-zs">
              UI/UX DESIGNER &amp; FRONTEND DEVELOPER
            </p>

            <p class="hero-desc-zs">
              I design intuitive digital experiences and build modern interfaces that combine creativity, usability, and technology.
            </p>

            <!-- Grey Pill Buttons (STRICTLY NO RED BUTTONS) -->
            <div class="hero-actions-row">
              <a href="#selected-design-works" class="btn-pill-grey" id="btn-hero-work" aria-label="Explore My Work">
                <span>Explore My Work &rarr;</span>
              </a>
              <a href="contact.html" class="btn-pill-grey" id="btn-hero-contact" aria-label="Let's Talk">
                <span>Let's Talk</span>
              </a>
            </div>

            <!-- Subtle Statistics Row Below Buttons -->
            <div class="hero-stats-row">
              <div class="hero-stat-item">
                <span class="stat-num">10+</span>
                <span class="stat-lbl">Projects</span>
              </div>
              <div class="hero-stat-sep" aria-hidden="true"></div>
              <div class="hero-stat-item">
                <span class="stat-num">UI/UX</span>
                <span class="stat-lbl">&amp; Code</span>
              </div>
              <div class="hero-stat-sep" aria-hidden="true"></div>
              <div class="hero-stat-item">
                <span class="stat-num">Always</span>
                <span class="stat-lbl">Learning</span>
              </div>
            </div>
          </div>

          <!-- Right Column: Large Rectangular Editorial Portrait Showcase -->
          <div class="hero-portrait-col reveal-item">
            <div class="hero-editorial-stage" id="hero-editorial-stage">
              <!-- Soft Cinematic Studio Ambient Glow Behind Card -->
              <div class="hero-editorial-ambient-glow" aria-hidden="true"></div>

              <!-- Main Rectangular Editorial Portrait Card (No Circular Frames) -->
              <div class="hero-editorial-card" data-tilt>
                <!-- Subtle Edge Vignette & Natural Dark Gradient Blends -->
                <div class="hero-editorial-vignette" aria-hidden="true"></div>
                <div class="hero-editorial-gradient-bottom" aria-hidden="true"></div>

                <!-- Portrait in Black Turtleneck & Overcoat -->
                <img src="./NEW%20IMAGE%20FOR%20WEBSITE.jpeg" alt="Zeerak Siddiqui — UI/UX Designer &amp; Frontend Developer" class="hero-editorial-img hero-portrait-img hero-portrait-photo" width="460" height="580" loading="eager">

                <!-- Small Floating Professional Philosophy Label Badge -->
                <div class="hero-floating-badge" aria-label="Professional Philosophy">
                  <span class="badge-accent-dot" aria-hidden="true"></span>
                  <span class="badge-text">DESIGNING DIGITAL EXPERIENCES</span>
                </div>
              </div>

              <!-- Minimalist Discipline Spine on Far Right -->
              <div class="hero-watermark-vertical" aria-hidden="true">
                <span>UI/UX</span>
                <span class="wm-slash">/</span>
                <span>SYSTEMS</span>
                <span class="wm-slash">/</span>
                <span>CREATIVE</span>
                <span class="wm-slash">/</span>
                <span>CODE</span>
              </div>
            </div>
          </div>
        </div>'''

if old_hero_grid in content:
    content = content.replace(old_hero_grid, new_hero_grid)
    print("Exact old_hero_grid replaced!")
else:
    # Use regex replacement
    pattern = r'<div class="hero-split-grid">.*?</div>\s*</div>\s*</div>\s*(?=<!-- =========================================================================\s*01\. ABOUT SECTION)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_hero_grid + '\n      </div>\n    </section>\n\n    ' + content[match.end():]
        print("Regex replaced hero split grid successfully!")
    else:
        print("Could not match hero split grid, check content!")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html hero markup successfully!")

