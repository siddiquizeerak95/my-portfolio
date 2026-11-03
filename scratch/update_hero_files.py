import re

# 1. Update index.html
with open(r'c:\Users\siddi\Desktop\New folder\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

hero_new_html = """    <!-- =========================================================================
         00. HERO SECTION — 3D PERSPECTIVE PORTFOLIO SHOWCASE (ZS STUDIO)
         ========================================================================= -->
    <section id="hero" class="section hero-section hero-3d-perspective-section" aria-label="Hero Introduction">
      <!-- Far Left Accent Line with Node 01 -->
      <div class="hero-left-accent-line" aria-hidden="true">
        <span class="hero-left-node">01</span>
      </div>

      <div class="container hero-container">
        <div class="hero-split-grid hero-3d-split-grid">
          <!-- Left Column: Typography & Actions (Editorial Composition) -->
          <div class="hero-editorial-col hero-3d-text-col reveal-item">
            <div class="section-tag-row">
              <span class="section-red-dot" aria-hidden="true"></span>
              <span class="section-tag-text">AVAILABLE FOR CREATIVE PROJECTS</span>
            </div>

            <h1 class="hero-headline-zs">
              Hi, I'm Zeerak<br><span class="text-accent-red">Siddiqui.</span>
            </h1>

            <p class="hero-subtitle-zs">
              UI/UX DESIGNER &amp; FRONTEND DEVELOPER
            </p>

            <p class="hero-desc-zs">
              I craft beautiful digital experiences through thoughtful design, creative thinking, and modern frontend development.
            </p>

            <!-- Grey Pill Buttons (STRICTLY NO RED BUTTONS) -->
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

          <!-- Right Column: 3D Perspective Floating Website Mockup with Layered Glass Panels -->
          <div class="hero-portrait-col hero-3d-viewport-col reveal-item">
            <div class="hero-3d-stage" id="hero-3d-stage">
              <!-- Soft Atmospheric Studio Glow & Ambient Crimson Diffusion Behind Mockup -->
              <div class="hero-3d-ambient-glow" aria-hidden="true"></div>
              <div class="hero-3d-radial-crimson" aria-hidden="true"></div>

              <!-- 3D Perspective Rig (Tilted & Floating with Mouse Parallax) -->
              <div class="hero-3d-rig" id="hero-3d-rig">
                
                <!-- Master Floating 3D Browser Window Mockup -->
                <div class="mockup-window" id="mockup-window">
                  <!-- Browser Window Chrome Header with Traffic Lights -->
                  <div class="mockup-window-header">
                    <div class="mockup-traffic-lights" aria-hidden="true">
                      <span class="light-dot light-red"></span>
                      <span class="light-dot light-dim"></span>
                      <span class="light-dot light-dim"></span>
                    </div>
                    <div class="mockup-url-pill">
                      <svg class="url-lock-icon" viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
                        <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                        <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                      </svg>
                      <span>zs-studio.design/portfolio</span>
                    </div>
                    <div class="mockup-header-actions" aria-hidden="true">
                      <span class="action-dash"></span>
                      <span class="action-square"></span>
                    </div>
                  </div>

                  <!-- Mockup Screen Viewport Content -->
                  <div class="mockup-screen-body">
                    <div class="mockup-screen-grid">
                      <!-- Left Inside Column: Featured UI/UX Design System Showcase -->
                      <div class="mockup-design-panel">
                        <div class="mockup-eyebrow">
                          <span class="mockup-red-dot" aria-hidden="true"></span>
                          <span>FEATURED CASE STUDY</span>
                        </div>
                        <h3 class="mockup-project-title">Fintech Banking OS</h3>
                        <p class="mockup-project-meta">End-to-end UX Architecture, Wireframes &amp; Design System</p>
                        
                        <!-- UI Metrics & Micro Interactive Graph Visual -->
                        <div class="mockup-preview-graph">
                          <div class="graph-bars-group" aria-hidden="true">
                            <span class="preview-graph-bar bar-1"></span>
                            <span class="preview-graph-bar bar-2"></span>
                            <span class="preview-graph-bar bar-3"></span>
                            <span class="preview-graph-bar bar-4"></span>
                          </div>
                          <div class="preview-metric-card">
                            <span class="metric-val">+340%</span>
                            <span class="metric-lbl">User Engagement</span>
                          </div>
                        </div>

                        <div class="mockup-tag-chips">
                          <span class="mockup-chip">Figma</span>
                          <span class="mockup-chip">Design System</span>
                          <span class="mockup-chip">React</span>
                        </div>
                      </div>

                      <!-- Right Inside Column: Zeerak Siddiqui High-Res Editorial Portrait -->
                      <div class="mockup-portrait-panel">
                        <div class="mockup-portrait-frame">
                          <img src="./NEW%20IMAGE%20FOR%20WEBSITE.jpeg" alt="Zeerak Siddiqui — UI/UX Designer &amp; Frontend Developer" class="mockup-portrait-photo" width="360" height="460" loading="eager">
                          <div class="mockup-portrait-vignette" aria-hidden="true"></div>
                          <div class="mockup-portrait-gradient" aria-hidden="true"></div>
                          <div class="mockup-portrait-meta">
                            <span class="portrait-name">Zeerak Siddiqui</span>
                            <span class="portrait-role">Lead UI/UX &amp; Frontend</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Specular Glass Sheen Overlay -->
                  <div class="mockup-specular-glare" aria-hidden="true"></div>
                </div>

                <!-- LAYERED FLOATING GLASS UI PANELS (True 3D translateZ Depth) -->
                
                <!-- Floating Panel 1: Top-Left Elevated Glass Card (Design System) -->
                <div class="floating-panel floating-panel-topleft" data-depth="75">
                  <div class="glass-panel-content">
                    <div class="panel-icon-wrap" aria-hidden="true">
                      <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                      </svg>
                    </div>
                    <div class="panel-text-wrap">
                      <span class="panel-title">Design System</span>
                      <span class="panel-subtitle">100% Componentized</span>
                    </div>
                    <span class="panel-status-dot" aria-hidden="true"></span>
                  </div>
                </div>

                <!-- Floating Panel 2: Bottom-Right Elevated Glass Card (Live Availability) -->
                <div class="floating-panel floating-panel-bottomright" data-depth="95">
                  <div class="glass-panel-content">
                    <div class="panel-avatar-wrap">
                      <img src="./NEW%20IMAGE%20FOR%20WEBSITE.jpeg" alt="Zeerak Siddiqui Profile Avatar" class="panel-avatar-thumb" width="40" height="40">
                    </div>
                    <div class="panel-text-wrap">
                      <div class="panel-badge-row">
                        <span class="panel-status-pulse" aria-hidden="true"></span>
                        <span class="panel-live-text">AVAILABLE NOW</span>
                      </div>
                      <span class="panel-desc-highlight">Designing Intuitive Systems</span>
                    </div>
                  </div>
                </div>

                <!-- Floating Panel 3: Top-Right Minimalist Code Tag -->
                <div class="floating-panel floating-panel-topright" data-depth="50">
                  <div class="glass-panel-content chip-compact">
                    <span class="chip-code-symbol" aria-hidden="true">&lt;/&gt;</span>
                    <span class="chip-label">Interactive 3D &amp; Code</span>
                  </div>
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
      </div>
    </section>"""

# Replace hero section in index.html
pattern = re.compile(r'<!--\s*=+\s*00\.\s*HERO SECTION.*?<!--\s*=+\s*01\.\s*ABOUT SECTION', re.DOTALL)
replacement = hero_new_html + "\n\n    <!-- =========================================================================\n         01. ABOUT SECTION"

if pattern.search(html):
    html = pattern.sub(replacement, html)
    with open(r'c:\Users\siddi\Desktop\New folder\index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html updated with 3D perspective hero successfully!")
else:
    print("Could not match hero section in index.html")

# 2. Update style.css
with open(r'c:\Users\siddi\Desktop\New folder\scratch\hero_3d_perspective.css', 'r', encoding='utf-8') as f:
    new_css = f.read()

with open(r'c:\Users\siddi\Desktop\New folder\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace from /* ========================================================================== 12. EDITORIAL RECTANGULAR HERO PORTRAIT REDESIGN
sec12_pattern = re.compile(r'/\*\s*=+\s*12\.\s*EDITORIAL RECTANGULAR HERO PORTRAIT REDESIGN.*', re.DOTALL)
if sec12_pattern.search(css):
    css = sec12_pattern.sub(new_css, css)
    with open(r'c:\Users\siddi\Desktop\New folder\style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("style.css updated with 3D perspective hero CSS successfully!")
else:
    print("Could not find section 12 in style.css")

