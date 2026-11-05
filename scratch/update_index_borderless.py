with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target_start = '<!-- Right Column: Cinematic Editorial Portrait'
target_end = '<!-- Reference Bottom Bar'

idx1 = text.find(target_start)
idx2 = text.find(target_end)

if idx1 != -1 and idx2 != -1:
    new_html = """<!-- Right Column: Borderless Seamless Cinematic Editorial Portrait (Exact Match to User Reference) -->
          <div class="hero-portrait-col hero-borderless-portrait-col reveal-item">
            <div class="hero-borderless-portrait-stage" id="hero-portrait-stage">
              <!-- Soft Atmospheric Red Glow Concentrated Behind Window & Portrait -->
              <div class="hero-borderless-ambient-glow" aria-hidden="true"></div>

              <!-- Seamless Borderless Portrait Container (NO BORDER, NO CARD, NO BOX) -->
              <div class="hero-borderless-portrait-wrap" id="hero-portrait-card">
                <img src="NEW IMAGE FOR WEBSITE.jpeg" alt="Zeerak Siddiqui — UI/UX Designer &amp; Frontend Developer" class="hero-borderless-portrait-img" width="580" height="720" loading="eager">
                
                <!-- Directional Cinematic Red Window Illumination on Left -->
                <div class="hero-borderless-window-light" aria-hidden="true"></div>

                <!-- Soft Vignette Blending Subject & Coat Seamlessly into #080808 -->
                <div class="hero-borderless-vignette" aria-hidden="true"></div>
              </div>
            </div>
          </div>

        </div>

        """
    text = text[:idx1] + new_html + text[idx2:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully updated index.html with borderless portrait markup!")
else:
    print(f"Could not find markers: {idx1}, {idx2}")

