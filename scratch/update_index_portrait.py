with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target_start = '<!-- Right Column: Editorial Portrait with Floating Badge'
target_end = '<!-- Minimalist Discipline Spine on Far Right -->'

idx1 = text.find(target_start)
idx2 = text.find(target_end)

if idx1 != -1 and idx2 != -1:
    old_block = text[idx1:idx2]
    new_block = """<!-- Right Column: Cinematic Editorial Portrait (Cinematic Red & Black direction) -->
          <div class="hero-portrait-col hero-reference-portrait-col hero-cinematic-portrait-col reveal-item">
            <div class="hero-reference-portrait-stage hero-cinematic-portrait-stage" id="hero-portrait-stage">
              <!-- Atmospheric Red Ambient Lighting Behind Portrait -->
              <div class="hero-portrait-ambient-glow hero-cinematic-ambient-glow" aria-hidden="true"></div>

              <!-- Main Cinematic Rectangular Portrait Frame -->
              <div class="hero-reference-portrait-card hero-cinematic-portrait-card" id="hero-portrait-card">
                <img src="NEW IMAGE FOR WEBSITE.jpeg" alt="Zeerak Siddiqui — UI/UX Designer &amp; Frontend Developer" class="hero-reference-portrait-img hero-cinematic-portrait-img" width="480" height="620" loading="eager">
                
                <!-- Directional Cinematic Red Rim Lighting Layer -->
                <div class="hero-cinematic-rim-light" aria-hidden="true"></div>

                <!-- Atmospheric Vignette & Soft Grounding Fade -->
                <div class="hero-portrait-vignette hero-cinematic-vignette" aria-hidden="true"></div>
                <div class="hero-portrait-fade-bottom hero-cinematic-fade-bottom" aria-hidden="true"></div>

                <!-- Precision Luxury Inner Accent Rim -->
                <div class="hero-cinematic-inner-rim" aria-hidden="true"></div>
              </div>

              """
    new_text = text[:idx1] + new_block + text[idx2:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully replaced portrait block in index.html")
else:
    print(f"Could not find indices: idx1={idx1}, idx2={idx2}")

