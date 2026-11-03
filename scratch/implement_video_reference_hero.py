import re

# 1. Update index.html
with open(r'c:\Users\siddi\Desktop\New folder\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

hero_video_html = """    <!-- =========================================================================
         00. HERO SECTION — EXACT REFERENCE VIDEO DESIGN (ZS STUDIO)
         ========================================================================= -->
    <section id="hero" class="section hero-section hero-video-reference-section" aria-label="Hero Introduction">
      <!-- Far Left Accent Line with Node 01 -->
      <div class="hero-left-accent-line" aria-hidden="true">
        <span class="hero-left-node">01</span>
      </div>

      <div class="container hero-container">
        <div class="hero-split-grid hero-reference-grid">
          
          <!-- Left Column: Typography, 3D Spiral Flip Card, and CTAs -->
          <div class="hero-editorial-col hero-reference-text-col reveal-item">
            
            <!-- Eyebrow status tag from reference -->
            <div class="section-tag-row">
              <span class="section-red-dot" aria-hidden="true"></span>
              <span class="section-tag-text">AVAILABLE FOR CREATIVE PROJECTS</span>
            </div>

            <!-- Main Heading from reference -->
            <h1 class="hero-headline-zs">
              Hi, I'm Zeerak<br><span class="text-accent-red">Siddiqui.</span>
            </h1>

            <!-- Connector phrase from reference video: "I am a" -->
            <p class="hero-iam-connector">I am a</p>

            <!-- THE 3D SPIRAL NOTEBOOK / FLIP CARD (Exact from reference video) -->
            <div class="hero-spiral-3d-stage" id="hero-spiral-stage" data-tilt>
              <div class="hero-spiral-card" id="hero-spiral-card">
                
                <!-- 10 Metallic Spiral Binding Rings Along the Top Edge -->
                <div class="spiral-binding-rings" aria-hidden="true">
                  <div class="spiral-ring-item"><span class="ring-hole"></span><span class="ring-wire"></span></div>
                  <div class="spiral-ring-item"><span class="ring-hole"></span><span class="ring-wire"></span></div>
                  <div class="spiral-ring-item"><span class="ring-hole"></span><span class="ring-wire"></span></div>
                  <div class="spiral-ring-item"><span class="ring-hole"></span><span class="ring-wire"></span></div>
                  <div class="spiral-ring-item"><span class="ring-hole"></span><span class="ring-wire"></span></div>
                  <div class="spiral-ring-item"><span class="ring-hole"></span><span class="ring-wire"></span></div>
                  <div class="spiral-ring-item"><span class="ring-hole"></span><span class="ring-wire"></span></div>
                  <div class="spiral-ring-item"><span class="ring-hole"></span><span class="ring-wire"></span></div>
                  <div class="spiral-ring-item"><span class="ring-hole"></span><span class="ring-wire"></span></div>
                  <div class="spiral-ring-item"><span class="ring-hole"></span><span class="ring-wire"></span></div>
                </div>

                <!-- Flip Content (Cycles: UI/UX Designer <-> Frontend Developer <-> Creative Technologist) -->
                <div class="spiral-card-body">
                  <div class="spiral-card-content" id="spiral-card-content">
                    <span class="spiral-role-text active" data-index="0">UI/UX Designer</span>
                    <span class="spiral-role-text" data-index="1">Frontend Developer</span>
                    <span class="spiral-role-text" data-index="2">Creative Technologist</span>
                  </div>
                  <div class="spiral-card-corner-page" id="spiral-card-page">01 / 03</div>
                </div>

                <!-- Specular lighting sheen -->
                <div class="spiral-card-sheen" aria-hidden="true"></div>
              </div>
            </div>

            <!-- Professional title & description as requested in prompt -->
            <p class="hero-subtitle-zs">
              UI/UX DESIGNER &amp; FRONTEND DEVELOPER
            </p>

            <p class="hero-desc-zs">
              I craft beautiful digital experiences through thoughtful design, creative thinking, and modern frontend development.
            </p>

            <!-- Grey Pill Buttons (STRICTLY NO RED BUTTONS, EXACT FROM VIDEO) -->
            <div class="hero-actions-row">
              <a href="#selected-design-works" class="btn-pill-grey" id="btn-hero-work" aria-label="Explore My Work">
                <span>Explore My Work &#8594;</span>
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
                <span class="stat-lbl">&amp; Frontend</span>
              </div>
              <div class="hero-stat-sep" aria-hidden="true"></div>
              <div class="hero-stat-item">
                <span class="stat-num">Always</span>
                <span class="stat-lbl">Learning</span>
              </div>
            </div>

          </div>

          <!-- Right Column: Editorial Portrait with Floating Badge (Exact from reference video) -->
          <div class="hero-portrait-col hero-reference-portrait-col reveal-item">
            <div class="hero-reference-portrait-stage" id="hero-portrait-stage">
              <!-- Soft Atmospheric Crimson/Studio Lighting Behind Portrait -->
              <div class="hero-portrait-ambient-glow" aria-hidden="true"></div>

              <!-- Main Portrait Presentation (Grounded Cutout/Card matching reference) -->
              <div class="hero-reference-portrait-card">
                <img src="./NEW%20IMAGE%20FOR%20WEBSITE.jpeg" alt="Zeerak Siddiqui — UI/UX Designer &amp; Frontend Developer" class="hero-reference-portrait-img" width="480" height="620" loading="eager">
                
                <!-- Natural edge vignette & bottom fade -->
                <div class="hero-portrait-vignette" aria-hidden="true"></div>
                <div class="hero-portrait-fade-bottom" aria-hidden="true"></div>

                <!-- Floating Ability Badge on Chest/Jacket (Exact from reference video) -->
                <div class="hero-floating-ability-badge" aria-label="Designer Status">
                  <span class="badge-status-dot" aria-hidden="true"></span>
                  <span class="badge-ability-text">Designing Digital Experiences</span>
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

        </div>

        <!-- Reference Bottom Bar (Exact from reference video: AVAILABLE FOR WORK | REMOTE-FIRST | SCROLL) -->
        <div class="hero-reference-bottom-bar" aria-hidden="true">
          <div class="bottom-bar-item left">
            <span class="status-pulse-dot"></span>
            <span>AVAILABLE FOR WORK</span>
          </div>
          <div class="bottom-bar-item center">
            <span>REMOTE-FIRST, WORLDWIDE</span>
          </div>
          <div class="bottom-bar-item right">
            <span>SCROLL TO EXPLORE &#8595;</span>
          </div>
        </div>

      </div>
    </section>"""

# Replace hero section in index.html
pattern = re.compile(r'<!--\s*=+\s*00\.\s*HERO SECTION.*?<!--\s*=+\s*01\.\s*ABOUT SECTION', re.DOTALL)
replacement = hero_video_html + "\n\n    <!-- =========================================================================\n         01. ABOUT SECTION"

if pattern.search(html):
    html = pattern.sub(replacement, html)
    with open(r'c:\Users\siddi\Desktop\New folder\index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html successfully updated with video reference hero!")
else:
    print("Error: Could not match hero section in index.html")

