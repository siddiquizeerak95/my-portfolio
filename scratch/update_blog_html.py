with open('blog.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add blog-3d.css to <head> if not present
if 'blog-3d.css' not in text:
    target_css = '<link rel="stylesheet" href="style.css">'
    replacement_css = '<link rel="stylesheet" href="style.css">\n  <!-- Dedicated 3D Blog Showcase Stylesheet (Scoped to blog.html) -->\n  <link rel="stylesheet" href="blog-3d.css">'
    text = text.replace(target_css, replacement_css)

# 2. Add the 3D Experience section after <section class="page-hero-banner" ...> </section>
if 'blog-3d-experience' not in text:
    target_sec = '</section>\n\n    <!-- SECTION 05 MASTER SHOWCASE: 3-COLUMN MAGAZINE GRID -->'
    section_3d = '''</section>

    <!-- ======================================================================
         CINEMATIC 3D SCROLL-DRIVEN BLOG SHOWCASE (Exclusively on blog.html)
         ====================================================================== -->
    <section class="blog-3d-experience-section" id="blog-3d-experience" aria-label="Cinematic 3D Article Showcase">
      <div class="blog-3d-sticky-viewport">
        <!-- Atmospheric Red Studio Lighting Behind 3D Stage -->
        <div class="blog-3d-ambient-glow" aria-hidden="true"></div>

        <!-- Telemetry Controller Bar -->
        <div class="blog-3d-telemetry-bar">
          <div class="b3d-tag-badge">
            <span class="b3d-pulse-dot" aria-hidden="true"></span>
            <span>3D EDITORIAL SHOWCASE</span>
          </div>
          <div class="b3d-article-counter" aria-live="polite">
            <span class="b3d-counter-num" id="b3d-active-num">01</span>
            <span class="b3d-counter-sep">/</span>
            <span class="b3d-counter-total">03</span>
            <span class="b3d-topic-ticker" id="b3d-topic-ticker">Web Architecture</span>
          </div>
          <div class="b3d-pills-nav" role="tablist" aria-label="3D Article Selection">
            <button class="b3d-pill-btn active" data-index="0" role="tab" aria-selected="true" title="Jump to Article 01">01</button>
            <button class="b3d-pill-btn" data-index="1" role="tab" aria-selected="false" title="Jump to Article 02">02</button>
            <button class="b3d-pill-btn" data-index="2" role="tab" aria-selected="false" title="Jump to Article 03">03</button>
          </div>
        </div>

        <!-- 3D Spatial Perspective Stage -->
        <div class="blog-3d-stage-wrap">
          <div class="blog-3d-stage" id="blog-3d-cards-stage">

            <!-- Card 01: How I Built My Portfolio Website -->
            <article class="blog-3d-card" data-card-index="0" id="b3d-card-0">
              <div class="b3d-card-inner">
                <div class="b3d-visual-pane">
                  <img src="assets/blog-architecture.svg" alt="How I Built My Portfolio Website Architecture" class="b3d-card-img" width="460" height="380" loading="eager">
                  <span class="b3d-date-badge">OCT 2026</span>
                  <div class="b3d-visual-overlay" aria-hidden="true"></div>
                </div>
                <div class="b3d-content-pane">
                  <div class="b3d-meta-header">
                    <span class="b3d-category-tag">Web Architecture</span>
                    <span class="b3d-read-time">
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                      6 min read
                    </span>
                  </div>
                  <h2 class="b3d-card-title">How I Built My Portfolio Website</h2>
                  <p class="b3d-card-excerpt">
                    A complete breakdown of my portfolio, design process and key takeaways. Why I chose vanilla HTML5, CSS3 clamp math, and zero framework overhead.
                  </p>
                  <div class="b3d-card-actions">
                    <a href="blog-how-i-built-my-portfolio.html" class="b3d-cta-btn" aria-label="Read full article: How I Built My Portfolio Website">
                      <span>Read Article</span>
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </a>
                    <span class="b3d-card-index-ghost" aria-hidden="true">01</span>
                  </div>
                </div>
              </div>
              <div class="b3d-card-glare" aria-hidden="true"></div>
            </article>

            <!-- Card 02: My Learning Journey in BCA -->
            <article class="blog-3d-card" data-card-index="1" id="b3d-card-1">
              <div class="b3d-card-inner">
                <div class="b3d-visual-pane">
                  <img src="assets/blog-forest.svg" alt="My Learning Journey in BCA Path" class="b3d-card-img" width="460" height="380" loading="eager">
                  <span class="b3d-date-badge">SEP 2026</span>
                  <div class="b3d-visual-overlay" aria-hidden="true"></div>
                </div>
                <div class="b3d-content-pane">
                  <div class="b3d-meta-header">
                    <span class="b3d-category-tag">Developer Journey</span>
                    <span class="b3d-read-time">
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                      5 min read
                    </span>
                  </div>
                  <h2 class="b3d-card-title">My Learning Journey in BCA</h2>
                  <p class="b3d-card-excerpt">
                    Experiences, challenges and lessons from my academic journey. How low-level systems programming in C anchored my engineering discipline.
                  </p>
                  <div class="b3d-card-actions">
                    <a href="blog-my-journey-as-a-developer.html" class="b3d-cta-btn" aria-label="Read full article: My Learning Journey in BCA">
                      <span>Read Article</span>
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </a>
                    <span class="b3d-card-index-ghost" aria-hidden="true">02</span>
                  </div>
                </div>
              </div>
              <div class="b3d-card-glare" aria-hidden="true"></div>
            </article>

            <!-- Card 03: Why I Prefer Minimalist Web Design -->
            <article class="blog-3d-card" data-card-index="2" id="b3d-card-2">
              <div class="b3d-card-inner">
                <div class="b3d-visual-pane">
                  <img src="assets/blog-peaks.svg" alt="Why I Prefer Minimalist Web Design" class="b3d-card-img" width="460" height="380" loading="eager">
                  <span class="b3d-date-badge">AUG 2026</span>
                  <div class="b3d-visual-overlay" aria-hidden="true"></div>
                </div>
                <div class="b3d-content-pane">
                  <div class="b3d-meta-header">
                    <span class="b3d-category-tag">Design Philosophy</span>
                    <span class="b3d-read-time">
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                      4 min read
                    </span>
                  </div>
                  <h2 class="b3d-card-title">Why I Prefer Minimalist Web Design</h2>
                  <p class="b3d-card-excerpt">
                    Essential tools for developers, productivity workflows, and why minimalist monochromatic aesthetics elevate real-world user experiences.
                  </p>
                  <div class="b3d-card-actions">
                    <a href="blog-why-i-prefer-minimalist-web-design.html" class="b3d-cta-btn" aria-label="Read full article: Why I Prefer Minimalist Web Design">
                      <span>Read Article</span>
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </a>
                    <span class="b3d-card-index-ghost" aria-hidden="true">03</span>
                  </div>
                </div>
              </div>
              <div class="b3d-card-glare" aria-hidden="true"></div>
            </article>

          </div>
        </div>

        <!-- Bottom Guidance / Scroll Indicator -->
        <div class="blog-3d-footer-hint" aria-hidden="true">
          <span class="b3d-hint-text">SCROLL TO ADVANCE 3D SHOWCASE</span>
          <div class="b3d-scroll-line">
            <div class="b3d-scroll-pip"></div>
          </div>
          <span class="b3d-hint-sub">TRANSITIONS INTO COMPLETE ARTICLE GRID BELOW</span>
        </div>
      </div>
    </section>

    <!-- SECTION 05 MASTER SHOWCASE: 3-COLUMN MAGAZINE GRID -->'''
    text = text.replace(target_sec, section_3d)

# 3. Add vendor scripts & blog-3d.js right before <script type="module" src="script.js"></script>
if 'blog-3d.js' not in text:
    target_script = '<script type="module" src="script.js"></script>'
    replacement_script = '''<!-- GSAP & ScrollTrigger Engine for Blog 3D Experience (Scoped strictly to blog.html) -->
  <script src="vendor/gsap.min.js"></script>
  <script src="vendor/ScrollTrigger.min.js"></script>
  <script src="blog-3d.js"></script>

  <!-- Main JavaScript Orchestrator (ES Module) -->
  <script type="module" src="script.js"></script>'''
    text = text.replace(target_script, replacement_script)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully integrated 3D scroll showcase into blog.html!")

