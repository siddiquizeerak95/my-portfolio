import os

assets_dir = r"c:\Users\siddi\Desktop\New folder\assets"
os.makedirs(assets_dir, exist_ok=True)

# 1. Case Study Hero Mockup SVG
hero_mockup_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" height="100%">
  <defs>
    <linearGradient id="csHeroGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#161822"/>
      <stop offset="100%" stop-color="#0A0B10"/>
    </linearGradient>
    <radialGradient id="csHeroGlow" cx="50%" cy="40%" r="55%">
      <stop offset="0%" stop-color="rgba(229, 9, 43, 0.22)"/>
      <stop offset="100%" stop-color="transparent"/>
    </radialGradient>
    <filter id="csShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="24" stdDeviation="32" flood-color="#000000" flood-opacity="0.75"/>
    </filter>
  </defs>

  <rect width="1200" height="680" rx="20" fill="url(#csHeroGrad)"/>
  <circle cx="600" cy="340" r="420" fill="url(#csHeroGlow)"/>

  <!-- Figma Replacement Notice Banner -->
  <g transform="translate(40, 36)">
    <rect width="360" height="34" rx="17" fill="#1C202C" stroke="#333A4D" stroke-width="1"/>
    <circle cx="17" cy="17" r="5" fill="#E5092B"/>
    <text x="32" y="22" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600">FIGMA PLACEHOLDER &bull; 1200 &times; 680</text>
  </g>

  <!-- Left Phone: Product Detail Sheet -->
  <g transform="translate(220, 90)" filter="url(#csShadow)">
    <rect width="320" height="520" rx="38" fill="#0E1015" stroke="#363C4E" stroke-width="2.5"/>
    <rect x="8" y="8" width="304" height="504" rx="30" fill="#13161F"/>
    <!-- Island -->
    <rect x="110" y="16" width="100" height="20" rx="10" fill="#08090C"/>
    
    <text x="24" y="65" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">COLLECTION 2026</text>
    <text x="24" y="90" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="18" font-weight="700">Chronos Kinetic 01</text>
    
    <!-- Hero Product Visual Box -->
    <rect x="20" y="110" width="264" height="200" rx="16" fill="#1A1E29" stroke="#2B3040" stroke-width="1"/>
    <path d="M50 210 C90 170, 160 160, 200 200 L250 200 C255 200, 260 205, 260 215 L260 225 C250 235, 180 240, 50 230 Z" fill="#E5092B"/>
    
    <!-- Size Selector -->
    <text x="24" y="340" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600">SELECT SIZE (EU)</text>
    <g transform="translate(24, 355)">
      <rect width="40" height="34" rx="8" fill="#E5092B"/>
      <text x="13" y="22" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="700">41</text>
      <rect x="50" width="40" height="34" rx="8" fill="#1C202C" stroke="#2D3344" stroke-width="1"/>
      <text x="63" y="22" fill="#8E97B0" font-family="'Inter', sans-serif" font-size="12">42</text>
      <rect x="100" width="40" height="34" rx="8" fill="#1C202C" stroke="#2D3344" stroke-width="1"/>
      <text x="113" y="22" fill="#8E97B0" font-family="'Inter', sans-serif" font-size="12">43</text>
      <rect x="150" width="40" height="34" rx="8" fill="#1C202C" stroke="#2D3344" stroke-width="1"/>
      <text x="163" y="22" fill="#8E97B0" font-family="'Inter', sans-serif" font-size="12">44</text>
    </g>

    <!-- Buy Button -->
    <rect x="24" y="420" width="256" height="46" rx="12" fill="#202430" stroke="#3E465B" stroke-width="1.2"/>
    <text x="80" y="448" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="700">ADD TO CART &bull; $280</text>
  </g>

  <!-- Right Phone: Checkout & One-Click Auth -->
  <g transform="translate(620, 90)" filter="url(#csShadow)">
    <rect width="320" height="520" rx="38" fill="#0E1015" stroke="#363C4E" stroke-width="2.5"/>
    <rect x="8" y="8" width="304" height="504" rx="30" fill="#13161F"/>
    <!-- Island -->
    <rect x="110" y="16" width="100" height="20" rx="10" fill="#08090C"/>

    <text x="24" y="65" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">EXPRESS CHECKOUT</text>
    <text x="24" y="90" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="18" font-weight="700">Order Summary</text>

    <!-- Item in cart -->
    <rect x="20" y="110" width="264" height="90" rx="14" fill="#1A1E29" stroke="#2B3040" stroke-width="1"/>
    <rect x="34" y="125" width="60" height="60" rx="10" fill="#242938"/>
    <text x="106" y="146" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Chronos 01</text>
    <text x="106" y="164" fill="#8E97B0" font-family="'Inter', sans-serif" font-size="11">Size 41 &bull; Stealth Black</text>
    <text x="106" y="184" fill="#E5092B" font-family="'Inter', sans-serif" font-size="13" font-weight="700">$280.00</text>

    <!-- Shipping Method -->
    <rect x="20" y="215" width="264" height="60" rx="12" fill="#161822" stroke="#2B3040" stroke-width="1"/>
    <circle cx="44" cy="245" r="8" fill="#E5092B"/>
    <circle cx="44" cy="245" r="3" fill="#FFFFFF"/>
    <text x="64" y="242" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600">DHL Express Next-Day</text>
    <text x="64" y="258" fill="#00E676" font-family="'Inter', sans-serif" font-size="11">Complimentary</text>

    <!-- Payment Auth Badge -->
    <rect x="20" y="290" width="264" height="100" rx="14" fill="#1C202C" stroke="#333A4D" stroke-width="1"/>
    <text x="36" y="320" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">BIOMETRIC AUTHENTICATION</text>
    <circle cx="60" cy="355" r="16" fill="#252B3C"/>
    <path d="M55 352 C55 347, 65 347, 65 352 C65 358, 55 358, 55 363" fill="none" stroke="#E5092B" stroke-width="1.8"/>
    <text x="90" y="360" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Double Click to Pay</text>

    <!-- Pay Button -->
    <rect x="24" y="420" width="256" height="46" rx="12" fill="#202430" stroke="#3E465B" stroke-width="1.2"/>
    <text x="80" y="448" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="700">CONFIRM &amp; PAY &bull; $280</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "case-study-hero-mockup.svg"), "w", encoding="utf-8") as f:
    f.write(hero_mockup_svg)

# 2. Case Study Persona Graphic SVG
persona_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 500" width="100%" height="100%">
  <defs>
    <linearGradient id="pGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#161822"/>
      <stop offset="100%" stop-color="#0E1015"/>
    </linearGradient>
  </defs>

  <rect width="1000" height="500" rx="16" fill="url(#pGrad)" stroke="#2B3040" stroke-width="1.5"/>

  <!-- Left Column: Avatar & Profile -->
  <g transform="translate(48, 48)">
    <!-- Avatar Box -->
    <rect width="180" height="200" rx="18" fill="#202534" stroke="#363C4E" stroke-width="1.5"/>
    <circle cx="90" cy="80" r="40" fill="#2F364C"/>
    <path d="M40 180 C40 135, 140 135, 140 180 Z" fill="#2F364C"/>
    <circle cx="90" cy="80" r="14" fill="#E5092B" opacity="0.8"/>

    <text x="0" y="235" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="20" font-weight="700">Elena Rostova</text>
    <text x="0" y="258" fill="#E5092B" font-family="'Inter', sans-serif" font-size="12" font-weight="600">MINIMALIST TECH PROFESSIONAL</text>
    
    <g transform="translate(0, 280)">
      <text y="16" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">Age: <tspan fill="#FFFFFF">28</tspan></text>
      <text y="36" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">Role: <tspan fill="#FFFFFF">Senior UX Researcher</tspan></text>
      <text y="56" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">Device: <tspan fill="#FFFFFF">iPhone 15 Pro, Mac</tspan></text>
      <text y="76" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">Location: <tspan fill="#FFFFFF">Berlin, Germany</tspan></text>
    </g>
  </g>

  <!-- Right Column: Goals, Frustrations, Behaviors -->
  <g transform="translate(290, 48)">
    <!-- Bio Quote -->
    <rect width="660" height="64" rx="12" fill="#1C202C" stroke="#2E3446" stroke-width="1"/>
    <text x="24" y="32" fill="#F5F5F5" font-family="'Inter', sans-serif" font-size="13" font-style="italic">"I value speed, zero clutter, and transparent pricing. If a checkout takes more than 2 steps, I leave."</text>
    <text x="24" y="50" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">&bull; Elena's shopping criteria &amp; mindset</text>

    <!-- 3 Cards: Goals, Frustrations, Tech Habits -->
    <g transform="translate(0, 84)">
      <!-- Goals -->
      <rect width="210" height="270" rx="14" fill="#161822" stroke="#2B3040" stroke-width="1"/>
      <rect x="20" y="20" width="28" height="28" rx="8" fill="#1E2332"/>
      <path d="M28 34 L33 39 L41 29" fill="none" stroke="#00E676" stroke-width="2"/>
      <text x="56" y="38" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="700">Core Goals</text>
      
      <text x="20" y="74" fill="#C5CBE0" font-family="'Inter', sans-serif" font-size="11" line-height="1.6">
        &bull; Find premium curated goods fast.<br/><br/>
        &bull; Verify materials and sizing accurately.<br/><br/>
        &bull; One-tap biometric checkout with zero account hurdles.<br/><br/>
        &bull; Real-time order dispatch notifications.
      </text>

      <!-- Frustrations -->
      <rect x="225" width="210" height="270" rx="14" fill="#161822" stroke="#2B3040" stroke-width="1"/>
      <rect x="245" y="20" width="28" height="28" rx="8" fill="#1E2332"/>
      <path d="M253 28 L265 40 M265 28 L253 40" fill="none" stroke="#E5092B" stroke-width="2"/>
      <text x="281" y="38" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="700">Frustrations</text>
      
      <text x="245" y="74" fill="#C5CBE0" font-family="'Inter', sans-serif" font-size="11">
        &bull; Popups and aggressive discount banners.<br/><br/>
        &bull; Hidden shipping fees revealed only at final step.<br/><br/>
        &bull; Complex registration forms before purchasing.<br/><br/>
        &bull; Slow visual loading of product galleries.
      </text>

      <!-- Behaviors -->
      <rect x="450" width="210" height="270" rx="14" fill="#161822" stroke="#2B3040" stroke-width="1"/>
      <rect x="470" y="20" width="28" height="28" rx="8" fill="#1E2332"/>
      <circle cx="484" cy="34" r="7" fill="none" stroke="#61DAFB" stroke-width="2"/>
      <text x="506" y="38" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="700">Behaviors</text>
      
      <text x="470" y="74" fill="#C5CBE0" font-family="'Inter', sans-serif" font-size="11">
        &bull; Shops primarily during evening commute on mobile.<br/><br/>
        &bull; Prefers Apple Pay or Google Pay over entering card details.<br/><br/>
        &bull; Bookmark items in wishlist for weekend consideration.
      </text>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "case-study-persona.svg"), "w", encoding="utf-8") as f:
    f.write(persona_svg)

# 3. Case Study Wireframes SVG
wireframes_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 520" width="100%" height="100%">
  <defs>
    <linearGradient id="wfGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141620"/>
      <stop offset="100%" stop-color="#0C0D12"/>
    </linearGradient>
  </defs>

  <rect width="1000" height="520" rx="16" fill="url(#wfGrad)" stroke="#2B3040" stroke-width="1.5"/>

  <!-- Wireframe Blueprint Grid Header -->
  <g transform="translate(40, 36)">
    <rect width="250" height="28" rx="14" fill="#1A1E29" stroke="#31384A" stroke-width="1"/>
    <text x="20" y="18" fill="#8E97B0" font-family="'Inter', sans-serif" font-size="11" font-weight="600">LOW-FIDELITY ARCHITECTURE</text>
    <text x="300" y="18" fill="#F5F5F5" font-family="'Inter', sans-serif" font-size="14" font-weight="600">User Flow: Discovery &rarr; Product Dossier &rarr; Instant Bag &rarr; Biometric Authorization</text>
  </g>

  <!-- 4 Wireframe Phone Frames Flow -->
  <!-- Screen 1: Discovery -->
  <g transform="translate(50, 90)">
    <rect width="190" height="380" rx="18" fill="#0E1016" stroke="#40475B" stroke-width="1.5" stroke-dasharray="4 2"/>
    <rect x="20" y="24" width="150" height="24" rx="6" fill="#1C202C"/>
    <rect x="20" y="60" width="40" height="14" rx="7" fill="#E5092B" opacity="0.6"/>
    <rect x="66" y="60" width="40" height="14" rx="7" fill="#1C202C"/>
    <rect x="112" y="60" width="40" height="14" rx="7" fill="#1C202C"/>
    
    <!-- Wireframe card 1 -->
    <rect x="20" y="86" width="150" height="110" rx="8" fill="#161922" stroke="#2B3040" stroke-width="1"/>
    <line x1="20" y1="86" x2="170" y2="196" stroke="#2B3040" stroke-width="1"/>
    <line x1="170" y1="86" x2="20" y2="196" stroke="#2B3040" stroke-width="1"/>

    <!-- Wireframe card 2 -->
    <rect x="20" y="210" width="150" height="110" rx="8" fill="#161922" stroke="#2B3040" stroke-width="1"/>
    <line x1="20" y1="210" x2="170" y2="320" stroke="#2B3040" stroke-width="1"/>
    <line x1="170" y1="210" x2="20" y2="320" stroke="#2B3040" stroke-width="1"/>

    <text x="20" y="355" fill="#8891A8" font-family="'Inter', sans-serif" font-size="10">01. Discovery Grid</text>
  </g>

  <!-- Arrow 1-2 -->
  <path d="M 260 270 L 290 270 M 285 265 L 292 270 L 285 275" fill="none" stroke="#E5092B" stroke-width="2"/>

  <!-- Screen 2: Product Detail -->
  <g transform="translate(305, 90)">
    <rect width="190" height="380" rx="18" fill="#0E1016" stroke="#40475B" stroke-width="1.5" stroke-dasharray="4 2"/>
    <rect x="20" y="24" width="150" height="140" rx="10" fill="#161922" stroke="#2B3040" stroke-width="1"/>
    <line x1="20" y1="24" x2="170" y2="164" stroke="#2B3040" stroke-width="1"/>
    <line x1="170" y1="24" x2="20" y2="164" stroke="#2B3040" stroke-width="1"/>

    <rect x="20" y="180" width="110" height="14" rx="4" fill="#242938"/>
    <rect x="20" y="202" width="150" height="8" rx="4" fill="#1C202C"/>
    <rect x="20" y="216" width="130" height="8" rx="4" fill="#1C202C"/>
    
    <!-- Pills -->
    <rect x="20" y="238" width="28" height="24" rx="6" fill="#1C202C"/>
    <rect x="54" y="238" width="28" height="24" rx="6" fill="#E5092B" opacity="0.6"/>
    <rect x="88" y="238" width="28" height="24" rx="6" fill="#1C202C"/>

    <rect x="20" y="280" width="150" height="36" rx="8" fill="#242938"/>
    <text x="20" y="355" fill="#8891A8" font-family="'Inter', sans-serif" font-size="10">02. Detail Dossier</text>
  </g>

  <!-- Arrow 2-3 -->
  <path d="M 515 270 L 545 270 M 540 265 L 547 270 L 540 275" fill="none" stroke="#E5092B" stroke-width="2"/>

  <!-- Screen 3: Cart Sheet -->
  <g transform="translate(560, 90)">
    <rect width="190" height="380" rx="18" fill="#0E1016" stroke="#40475B" stroke-width="1.5" stroke-dasharray="4 2"/>
    <rect x="20" y="24" width="90" height="14" rx="4" fill="#242938"/>

    <rect x="20" y="54" width="150" height="60" rx="8" fill="#161922" stroke="#2B3040" stroke-width="1"/>
    <rect x="28" y="62" width="44" height="44" rx="6" fill="#242938"/>

    <rect x="20" y="124" width="150" height="60" rx="8" fill="#161922" stroke="#2B3040" stroke-width="1"/>
    <rect x="28" y="132" width="44" height="44" rx="6" fill="#242938"/>

    <line x1="20" y1="210" x2="170" y2="210" stroke="#2B3040" stroke-width="1"/>
    <rect x="20" y="226" width="150" height="12" rx="4" fill="#1C202C"/>
    <rect x="20" y="280" width="150" height="36" rx="8" fill="#242938"/>
    <text x="20" y="355" fill="#8891A8" font-family="'Inter', sans-serif" font-size="10">03. Slide Cart</text>
  </g>

  <!-- Arrow 3-4 -->
  <path d="M 770 270 L 800 270 M 795 265 L 802 270 L 795 275" fill="none" stroke="#E5092B" stroke-width="2"/>

  <!-- Screen 4: Confirmation -->
  <g transform="translate(815, 90)">
    <rect width="150" height="380" rx="18" fill="#0E1016" stroke="#40475B" stroke-width="1.5" stroke-dasharray="4 2"/>
    <circle cx="75" cy="110" r="28" fill="#161922" stroke="#00E676" stroke-width="2"/>
    <path d="M65 110 L72 117 L85 104" fill="none" stroke="#00E676" stroke-width="2"/>

    <rect x="20" y="160" width="110" height="14" rx="4" fill="#242938"/>
    <rect x="20" y="184" width="110" height="8" rx="4" fill="#1C202C"/>
    <rect x="20" y="198" width="80" height="8" rx="4" fill="#1C202C"/>

    <rect x="20" y="240" width="110" height="60" rx="8" fill="#161922" stroke="#2B3040" stroke-width="1"/>
    <text x="20" y="355" fill="#8891A8" font-family="'Inter', sans-serif" font-size="10">04. Confirmation</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "case-study-wireframes.svg"), "w", encoding="utf-8") as f:
    f.write(wireframes_svg)

# 4. Case Study Design System SVG
design_system_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 500" width="100%" height="100%">
  <defs>
    <linearGradient id="dsGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141722"/>
      <stop offset="100%" stop-color="#0A0B10"/>
    </linearGradient>
  </defs>

  <rect width="1000" height="500" rx="16" fill="url(#dsGrad)" stroke="#2B3040" stroke-width="1.5"/>

  <!-- Left Column: Color Palette Tokens -->
  <g transform="translate(48, 48)">
    <text x="0" y="20" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="16" font-weight="700">01. Color Palette Tokens</text>
    <text x="0" y="38" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">High-contrast monochrome core with crimson focus accents</text>

    <!-- Color Swatches Row -->
    <g transform="translate(0, 56)">
      <!-- Swatch 1: Obsidian -->
      <rect width="80" height="80" rx="12" fill="#080808" stroke="#333A4D" stroke-width="1"/>
      <text x="0" y="104" fill="#FFFFFF" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600">#080808</text>
      <text x="0" y="120" fill="#8891A8" font-family="'Inter', sans-serif" font-size="10">Main Void</text>

      <!-- Swatch 2: Charcoal Surface -->
      <rect x="100" width="80" height="80" rx="12" fill="#1A1D27" stroke="#333A4D" stroke-width="1"/>
      <text x="100" y="104" fill="#FFFFFF" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600">#1A1D27</text>
      <text x="100" y="120" fill="#8891A8" font-family="'Inter', sans-serif" font-size="10">Elevated Card</text>

      <!-- Swatch 3: Pure Crimson Accent -->
      <rect x="200" width="80" height="80" rx="12" fill="#E5092B" stroke="#FF4D6A" stroke-width="1"/>
      <text x="200" y="104" fill="#FFFFFF" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600">#E5092B</text>
      <text x="200" y="120" fill="#E5092B" font-family="'Inter', sans-serif" font-size="10" font-weight="600">Accent Focus</text>

      <!-- Swatch 4: Primary Text -->
      <rect x="300" width="80" height="80" rx="12" fill="#F5F5F5" stroke="#FFFFFF" stroke-width="1"/>
      <text x="300" y="104" fill="#FFFFFF" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600">#F5F5F5</text>
      <text x="300" y="120" fill="#8891A8" font-family="'Inter', sans-serif" font-size="10">Primary Text</text>
    </g>

    <!-- Typography Scale Preview -->
    <g transform="translate(0, 210)">
      <text x="0" y="20" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="16" font-weight="700">02. Typographic Scale</text>
      <text x="0" y="44" fill="#FFFFFF" font-family="'Space Grotesk', sans-serif" font-size="28" font-weight="700">Display 28px Space Grotesk</text>
      <text x="0" y="76" fill="#F5F5F5" font-family="'Inter', sans-serif" font-size="18" font-weight="600">H1 Headline 18px SemiBold Inter</text>
      <text x="0" y="104" fill="#B5BED6" font-family="'Inter', sans-serif" font-size="13">Body Regular 13px / 1.6 Line-Height Inter System</text>
      <text x="0" y="130" fill="#8891A8" font-family="'JetBrains Mono', monospace" font-size="11">CODE &amp; TELEMETRY 11PX JETBRAINS MONO</text>
    </g>
  </g>

  <!-- Right Column: Atomic UI Components -->
  <g transform="translate(540, 48)">
    <text x="0" y="20" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="16" font-weight="700">03. Component Library</text>
    <text x="0" y="38" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">Interactive states, button tokens, inputs &amp; pills</text>

    <!-- Component Row 1: Buttons -->
    <g transform="translate(0, 60)">
      <rect width="180" height="42" rx="10" fill="#1E222D" stroke="#3D4559" stroke-width="1.2"/>
      <text x="35" y="26" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Default Button &rarr;</text>

      <rect x="200" width="180" height="42" rx="10" fill="#2E3446" stroke="#525C77" stroke-width="1.2"/>
      <text x="240" y="26" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Hover State &rarr;</text>
    </g>

    <!-- Component Row 2: Pills -->
    <g transform="translate(0, 120)">
      <rect width="80" height="28" rx="14" fill="#E5092B"/>
      <text x="22" y="18" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="11" font-weight="600">Active</text>

      <rect x="95" width="90" height="28" rx="14" fill="#1C202C" stroke="#333A4D" stroke-width="1"/>
      <text x="110" y="18" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">Inactive</text>

      <rect x="200" width="110" height="28" rx="14" fill="#182A22" stroke="#22543D" stroke-width="1"/>
      <circle cx="214" cy="14" r="3.5" fill="#00E676"/>
      <text x="226" y="18" fill="#00E676" font-family="'Inter', sans-serif" font-size="11" font-weight="600">Verified</text>
    </g>

    <!-- Component Row 3: Input Field -->
    <g transform="translate(0, 170)">
      <rect width="380" height="44" rx="10" fill="#141720" stroke="#3A4257" stroke-width="1.2"/>
      <text x="16" y="27" fill="#F5F5F5" font-family="'Inter', sans-serif" font-size="12">elena.rostova@design.com</text>
      <circle cx="355" cy="22" r="5" fill="#00E676"/>
    </g>

    <!-- Component Row 4: Card Component -->
    <g transform="translate(0, 235)">
      <rect width="380" height="135" rx="14" fill="#161822" stroke="#2B3040" stroke-width="1"/>
      <rect x="16" y="16" width="65" height="65" rx="10" fill="#202432"/>
      <text x="96" y="38" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="700">Chronos Kinetic 01</text>
      <text x="96" y="58" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">EU 41 &bull; Stealth Matte Edition</text>
      <text x="96" y="80" fill="#E5092B" font-family="'Inter', sans-serif" font-size="13" font-weight="700">$280.00</text>
      <line x1="16" y1="96" x2="364" y2="96" stroke="#262B3A" stroke-width="1"/>
      <text x="16" y="118" fill="#00E676" font-family="'Inter', sans-serif" font-size="10" font-weight="600">&bull; IN STOCK &bull; DISPATCHES IN 24H</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "case-study-design-system.svg"), "w", encoding="utf-8") as f:
    f.write(design_system_svg)

# 5. Case Study Metrics SVG
metrics_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 450" width="100%" height="100%">
  <defs>
    <linearGradient id="mGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141622"/>
      <stop offset="100%" stop-color="#0A0B10"/>
    </linearGradient>
  </defs>

  <rect width="1000" height="450" rx="16" fill="url(#mGrad)" stroke="#2B3040" stroke-width="1.5"/>

  <!-- Top Header -->
  <g transform="translate(48, 40)">
    <text x="0" y="20" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="18" font-weight="700">Usability Testing Outcomes &amp; Performance Metrics</text>
    <text x="0" y="38" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">Empirical testing conducted across 16 target users navigating product discovery to checkout</text>
  </g>

  <!-- 3 Big Metric Cards -->
  <g transform="translate(48, 110)">
    <!-- Metric 1 -->
    <rect width="280" height="150" rx="14" fill="#181B26" stroke="#2E3446" stroke-width="1"/>
    <text x="24" y="36" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11" font-weight="600">CHECKOUT SPEEDUP</text>
    <text x="24" y="85" fill="#FFFFFF" font-family="'Space Grotesk', sans-serif" font-size="44" font-weight="700">3.2&times;</text>
    <text x="140" y="80" fill="#00E676" font-family="'Inter', sans-serif" font-size="14" font-weight="700">&uarr; Faster</text>
    <text x="24" y="124" fill="#C5CBE0" font-family="'Inter', sans-serif" font-size="11">Reduced time to purchase from 115s to 36s</text>

    <!-- Metric 2 -->
    <rect x="310" width="280" height="150" rx="14" fill="#181B26" stroke="#2E3446" stroke-width="1"/>
    <text x="334" y="36" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11" font-weight="600">TASK COMPLETION</text>
    <text x="334" y="85" fill="#FFFFFF" font-family="'Space Grotesk', sans-serif" font-size="44" font-weight="700">96.8%</text>
    <text x="495" y="80" fill="#00E676" font-family="'Inter', sans-serif" font-size="14" font-weight="700">&uarr; +24%</text>
    <text x="334" y="124" fill="#C5CBE0" font-family="'Inter', sans-serif" font-size="11">Zero users abandoned during payment flow</text>

    <!-- Metric 3 -->
    <rect x="620" width="280" height="150" rx="14" fill="#181B26" stroke="#2E3446" stroke-width="1"/>
    <text x="644" y="36" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11" font-weight="600">SUS USABILITY SCORE</text>
    <text x="644" y="85" fill="#E5092B" font-family="'Space Grotesk', sans-serif" font-size="44" font-weight="700">92/100</text>
    <text x="795" y="80" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="700">Grade A+</text>
    <text x="644" y="124" fill="#C5CBE0" font-family="'Inter', sans-serif" font-size="11">Industry benchmark average is 68</text>
  </g>

  <!-- Key Takeaway Banner -->
  <g transform="translate(48, 290)">
    <rect width="904" height="110" rx="14" fill="#1A1E2B" stroke="#333A4D" stroke-width="1"/>
    <text x="28" y="34" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="700">Key Design Takeaway &amp; Insight</text>
    <text x="28" y="62" fill="#B5BED6" font-family="'Inter', sans-serif" font-size="12" line-height="1.6">
      Eliminating multi-screen transitions in favor of an expandable drawer checkout significantly reduced user hesitation. 
      Clear shipping fee transparency from the initial product card eliminated cart abandonment spikes.
    </text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "case-study-metrics.svg"), "w", encoding="utf-8") as f:
    f.write(metrics_svg)

print("Generated case study SVG assets successfully!")
