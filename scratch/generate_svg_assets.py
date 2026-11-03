import os

assets_dir = r"c:\Users\siddi\Desktop\New folder\assets"
os.makedirs(assets_dir, exist_ok=True)

# 1. E-commerce App Preview SVG
ecommerce_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141720"/>
      <stop offset="100%" stop-color="#0B0D13"/>
    </linearGradient>
    <radialGradient id="phoneGlow" cx="50%" cy="40%" r="55%">
      <stop offset="0%" stop-color="rgba(229, 9, 43, 0.15)"/>
      <stop offset="100%" stop-color="transparent"/>
    </radialGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#242834"/>
      <stop offset="100%" stop-color="#181B24"/>
    </linearGradient>
    <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="500" fill="url(#bgGrad)"/>
  <circle cx="400" cy="250" r="320" fill="url(#phoneGlow)"/>

  <!-- Subtle Perspective Grid -->
  <g stroke="rgba(255,255,255,0.04)" stroke-width="1">
    <line x1="0" y1="420" x2="800" y2="420"/>
    <line x1="0" y1="450" x2="800" y2="450"/>
    <line x1="0" y1="480" x2="800" y2="480"/>
    <line x1="100" y1="500" x2="250" y2="400"/>
    <line x1="300" y1="500" x2="350" y2="400"/>
    <line x1="500" y1="500" x2="450" y2="400"/>
    <line x1="700" y1="500" x2="550" y2="400"/>
  </g>

  <!-- Tag Pill Top Left -->
  <g transform="translate(36, 36)">
    <rect width="170" height="28" rx="14" fill="#1C202C" stroke="#333A4D" stroke-width="1"/>
    <circle cx="14" cy="14" r="4" fill="#E5092B"/>
    <text x="26" y="18" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="11" font-weight="600" letter-spacing="1">CONCEPT DESIGN</text>
  </g>

  <!-- Floating Mobile Mockup Center Left -->
  <g transform="translate(250, 45)" filter="url(#softShadow)">
    <!-- Device Frame -->
    <rect width="300" height="420" rx="36" fill="#0E1015" stroke="#363C4E" stroke-width="2.5"/>
    <rect x="8" y="8" width="284" height="404" rx="28" fill="#13161F"/>

    <!-- Dynamic Island / Speaker -->
    <rect x="105" y="16" width="90" height="18" rx="9" fill="#08090C"/>
    <circle cx="178" cy="25" r="3.5" fill="#1B1E28"/>

    <!-- App Top Bar -->
    <text x="24" y="60" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="15" font-weight="700">AURA STORE</text>
    <rect x="236" y="47" width="28" height="28" rx="8" fill="#202430"/>
    <path d="M246 56 h8 v10 h-8 z" fill="none" stroke="#F5F5F5" stroke-width="1.5"/>

    <!-- Search Bar -->
    <rect x="20" y="80" width="244" height="32" rx="10" fill="#1B1F2B" stroke="#2D3344" stroke-width="1"/>
    <text x="36" y="101" fill="#7C849B" font-family="'Inter', sans-serif" font-size="11">Search luxury essentials...</text>

    <!-- Categories -->
    <rect x="20" y="122" width="60" height="22" rx="11" fill="#E5092B"/>
    <text x="35" y="137" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="10" font-weight="600">All</text>
    <rect x="86" y="122" width="76" height="22" rx="11" fill="#1B1F2B" stroke="#2D3344" stroke-width="1"/>
    <text x="98" y="137" fill="#A0A8C0" font-family="'Inter', sans-serif" font-size="10">Apparel</text>
    <rect x="168" y="122" width="76" height="22" rx="11" fill="#1B1F2B" stroke="#2D3344" stroke-width="1"/>
    <text x="180" y="137" fill="#A0A8C0" font-family="'Inter', sans-serif" font-size="10">Footwear</text>

    <!-- Featured Product Card -->
    <rect x="20" y="156" width="244" height="154" rx="18" fill="url(#cardGrad)" stroke="#32384A" stroke-width="1"/>
    <!-- Mockup Sneaker Geometry -->
    <path d="M50 230 C80 200, 140 190, 180 220 L230 220 C235 220, 240 225, 240 235 L240 245 C230 252, 170 255, 50 248 Z" fill="#E5092B" opacity="0.9"/>
    <path d="M120 205 L170 200 L165 220 Z" fill="#FFFFFF" opacity="0.8"/>
    <text x="36" y="186" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="700">Chronos Kinetic 01</text>
    <text x="36" y="202" fill="#8F98B2" font-family="'Inter', sans-serif" font-size="10">Minimalist Performance Footwear</text>
    <text x="36" y="292" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="700">$280</text>
    <rect x="184" y="272" width="68" height="28" rx="8" fill="#1E222D" stroke="#3D4559" stroke-width="1"/>
    <text x="198" y="290" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="10" font-weight="600">ADD +</text>

    <!-- Bottom Navigation Bar -->
    <rect x="20" y="360" width="244" height="40" rx="20" fill="#10121A" stroke="#2B3040" stroke-width="1"/>
    <circle cx="56" cy="380" r="5" fill="#E5092B"/>
    <circle cx="106" cy="380" r="4" fill="#586177"/>
    <circle cx="156" cy="380" r="4" fill="#586177"/>
    <circle cx="206" cy="380" r="4" fill="#586177"/>
  </g>

  <!-- Side Floating Card (Detail Sheet) -->
  <g transform="translate(580, 110)" filter="url(#softShadow)">
    <rect width="180" height="230" rx="18" fill="#171A24" stroke="#343B4E" stroke-width="1.5"/>
    <text x="20" y="34" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Checkout Flow</text>
    <rect x="20" y="48" width="140" height="2" fill="#E5092B"/>
    
    <text x="20" y="76" fill="#8E97B0" font-family="'Inter', sans-serif" font-size="10">Subtotal</text>
    <text x="135" y="76" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="10" font-weight="600">$280.00</text>
    <text x="20" y="98" fill="#8E97B0" font-family="'Inter', sans-serif" font-size="10">Express Shipping</text>
    <text x="145" y="98" fill="#00E676" font-family="'Inter', sans-serif" font-size="10">FREE</text>
    <line x1="20" y1="116" x2="160" y2="116" stroke="#2B3040" stroke-width="1"/>
    
    <text x="20" y="138" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="11" font-weight="700">Total</text>
    <text x="120" y="138" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="700">$280.00</text>
    
    <rect x="20" y="160" width="140" height="34" rx="8" fill="#202430" stroke="#3F465C" stroke-width="1"/>
    <text x="45" y="181" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="10" font-weight="600">1-CLICK PAY ↗</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "project-ecommerce-preview.svg"), "w", encoding="utf-8") as f:
    f.write(ecommerce_svg)

# 2. Personal Finance Dashboard Preview SVG
finance_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#12151F"/>
      <stop offset="100%" stop-color="#0A0C12"/>
    </linearGradient>
    <linearGradient id="chartGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="rgba(229, 9, 43, 0.45)"/>
      <stop offset="100%" stop-color="rgba(229, 9, 43, 0.0)"/>
    </linearGradient>
    <filter id="softShadow2" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#000000" flood-opacity="0.65"/>
    </filter>
  </defs>

  <rect width="800" height="500" fill="url(#bgGrad2)"/>

  <!-- Tag Pill Top Left -->
  <g transform="translate(36, 36)">
    <rect width="170" height="28" rx="14" fill="#1C202C" stroke="#333A4D" stroke-width="1"/>
    <circle cx="14" cy="14" r="4" fill="#E5092B"/>
    <text x="26" y="18" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="11" font-weight="600" letter-spacing="1">CONCEPT DESIGN</text>
  </g>

  <!-- Large Desktop Dashboard Mockup -->
  <g transform="translate(100, 60)" filter="url(#softShadow2)">
    <!-- Browser Window Frame -->
    <rect width="600" height="380" rx="16" fill="#161822" stroke="#303546" stroke-width="1.8"/>
    <!-- Titlebar -->
    <rect width="600" height="36" rx="16" fill="#10121A"/>
    <rect x="0" y="24" width="600" height="12" fill="#10121A"/>
    <circle cx="24" cy="18" r="4.5" fill="#FF5F56"/>
    <circle cx="40" cy="18" r="4.5" fill="#FFBD2E"/>
    <circle cx="56" cy="18" r="4.5" fill="#27C93F"/>
    <text x="230" y="22" fill="#757D94" font-family="'Inter', sans-serif" font-size="11" font-weight="500">zenith.finance/dashboard</text>

    <!-- Sidebar Mini -->
    <rect x="0" y="36" width="60" height="344" fill="#12141D"/>
    <circle cx="30" cy="65" r="10" fill="#E5092B"/>
    <rect x="20" y="100" width="20" height="3" rx="1.5" fill="#6A738A"/>
    <rect x="20" y="125" width="20" height="3" rx="1.5" fill="#6A738A"/>
    <rect x="20" y="150" width="20" height="3" rx="1.5" fill="#6A738A"/>
    <rect x="20" y="175" width="20" height="3" rx="1.5" fill="#6A738A"/>

    <!-- Dashboard Content Area -->
    <g transform="translate(80, 52)">
      <text x="0" y="20" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="16" font-weight="700">Financial Overview</text>
      <text x="0" y="36" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">Real-time liquidity, cashflow &amp; asset allocations</text>

      <!-- 3 Summary Metric Cards -->
      <g transform="translate(0, 50)">
        <!-- Card 1 -->
        <rect width="150" height="74" rx="10" fill="#1C1F2B" stroke="#2D3242" stroke-width="1"/>
        <text x="14" y="24" fill="#8A93AA" font-family="'Inter', sans-serif" font-size="10">TOTAL NET WORTH</text>
        <text x="14" y="50" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="18" font-weight="700">$142,850</text>
        <text x="96" y="50" fill="#00E676" font-family="'Inter', sans-serif" font-size="10" font-weight="600">+12.4%</text>

        <!-- Card 2 -->
        <rect x="165" width="150" height="74" rx="10" fill="#1C1F2B" stroke="#2D3242" stroke-width="1"/>
        <text x="179" y="24" fill="#8A93AA" font-family="'Inter', sans-serif" font-size="10">MONTHLY CASHFLOW</text>
        <text x="179" y="50" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="18" font-weight="700">+$8,420</text>
        <text x="270" y="50" fill="#00E676" font-family="'Inter', sans-serif" font-size="10" font-weight="600">+4.8%</text>

        <!-- Card 3 -->
        <rect x="330" width="150" height="74" rx="10" fill="#1C1F2B" stroke="#2D3242" stroke-width="1"/>
        <text x="344" y="24" fill="#8A93AA" font-family="'Inter', sans-serif" font-size="10">INVESTMENTS</text>
        <text x="344" y="50" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="18" font-weight="700">$94,200</text>
        <text x="430" y="50" fill="#E5092B" font-family="'Inter', sans-serif" font-size="10" font-weight="600">8 Assets</text>
      </g>

      <!-- Main Chart Card -->
      <g transform="translate(0, 140)">
        <rect width="480" height="170" rx="12" fill="#1A1D27" stroke="#2C3140" stroke-width="1"/>
        <text x="18" y="26" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Cashflow Trajectory (12 Months)</text>
        
        <!-- Grid lines -->
        <line x1="20" y1="50" x2="460" y2="50" stroke="#242836" stroke-width="1"/>
        <line x1="20" y1="90" x2="460" y2="90" stroke="#242836" stroke-width="1"/>
        <line x1="20" y1="130" x2="460" y2="130" stroke="#242836" stroke-width="1"/>

        <!-- Area Curve -->
        <path d="M 30 130 Q 80 110, 130 95 T 230 70 T 330 85 T 430 40 L 430 145 L 30 145 Z" fill="url(#chartGrad)"/>
        <path d="M 30 130 Q 80 110, 130 95 T 230 70 T 330 85 T 430 40" fill="none" stroke="#E5092B" stroke-width="2.5"/>
        
        <!-- Peak Dot -->
        <circle cx="430" cy="40" r="5" fill="#E5092B"/>
        <circle cx="430" cy="40" r="2.5" fill="#FFFFFF"/>
      </g>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "project-finance-preview.svg"), "w", encoding="utf-8") as f:
    f.write(finance_svg)

# 3. Mobile Banking App Preview SVG
banking_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141620"/>
      <stop offset="100%" stop-color="#090A0E"/>
    </linearGradient>
    <linearGradient id="metalCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#343949"/>
      <stop offset="50%" stop-color="#1F232D"/>
      <stop offset="100%" stop-color="#111319"/>
    </linearGradient>
    <filter id="softShadow3" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#000000" flood-opacity="0.65"/>
    </filter>
  </defs>

  <rect width="800" height="500" fill="url(#bgGrad3)"/>

  <!-- Tag Pill Top Left -->
  <g transform="translate(36, 36)">
    <rect width="170" height="28" rx="14" fill="#1C202C" stroke="#333A4D" stroke-width="1"/>
    <circle cx="14" cy="14" r="4" fill="#E5092B"/>
    <text x="26" y="18" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="11" font-weight="600" letter-spacing="1">CONCEPT DESIGN</text>
  </g>

  <!-- Mobile Device Left -->
  <g transform="translate(240, 45)" filter="url(#softShadow3)">
    <rect width="300" height="420" rx="36" fill="#0E1015" stroke="#363C4E" stroke-width="2.5"/>
    <rect x="8" y="8" width="284" height="404" rx="28" fill="#13161F"/>

    <!-- Island -->
    <rect x="105" y="16" width="90" height="18" rx="9" fill="#08090C"/>

    <text x="24" y="60" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11">TOTAL BALANCE</text>
    <text x="24" y="88" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="24" font-weight="800">$48,290.40</text>

    <!-- Virtual Metal Card Mockup -->
    <g transform="translate(20, 108)">
      <rect width="244" height="136" rx="16" fill="url(#metalCard)" stroke="#4A5268" stroke-width="1.2"/>
      <!-- Chip -->
      <rect x="20" y="24" width="30" height="22" rx="4" fill="#C5A059" opacity="0.85"/>
      <text x="20" y="90" fill="#9DA7C0" font-family="'JetBrains Mono', monospace" font-size="12" letter-spacing="2">&bull;&bull;&bull;&bull; 8842</text>
      <text x="20" y="115" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="11" font-weight="600">ZEERAK SIDDIQUI</text>
      <circle cx="210" cy="108" r="10" fill="#E5092B" opacity="0.8"/>
      <circle cx="222" cy="108" r="10" fill="#FFA000" opacity="0.8"/>
    </g>

    <!-- Action Pills (Send, Receive, Analytics) -->
    <g transform="translate(20, 260)">
      <rect width="76" height="34" rx="10" fill="#1E222D" stroke="#363C4E" stroke-width="1"/>
      <text x="22" y="21" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="10" font-weight="600">Send ↗</text>

      <rect x="84" width="76" height="34" rx="10" fill="#1E222D" stroke="#363C4E" stroke-width="1"/>
      <text x="98" y="21" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="10" font-weight="600">Request ↙</text>

      <rect x="168" width="76" height="34" rx="10" fill="#1E222D" stroke="#363C4E" stroke-width="1"/>
      <text x="185" y="21" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="10" font-weight="600">Cards ≡</text>
    </g>

    <!-- Recent Transactions -->
    <g transform="translate(20, 310)">
      <text x="0" y="16" fill="#8891A8" font-family="'Inter', sans-serif" font-size="11" font-weight="600">RECENT ACTIVITY</text>
      <rect y="26" width="244" height="34" rx="8" fill="#181B24" stroke="#292E3C" stroke-width="1"/>
      <circle cx="16" cy="43" r="7" fill="#E5092B" opacity="0.3"/>
      <text x="32" y="46" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="10" font-weight="500">Apple Store Regent</text>
      <text x="195" y="46" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="10" font-weight="600">-$1,299</text>
    </g>
  </g>

  <!-- Right Floating Metric Box -->
  <g transform="translate(570, 130)" filter="url(#softShadow3)">
    <rect width="190" height="210" rx="16" fill="#181B26" stroke="#32384A" stroke-width="1.5"/>
    <text x="20" y="32" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Biometric Security</text>
    <rect x="20" y="46" width="150" height="2" fill="#E5092B"/>
    <text x="20" y="74" fill="#8891A8" font-family="'Inter', sans-serif" font-size="10">FaceID / TouchID Flow</text>
    <circle cx="95" cy="120" r="28" fill="#202432" stroke="#3D4559" stroke-width="1.5"/>
    <path d="M85 115 C85 105, 105 105, 105 115 C105 125, 95 125, 95 132" fill="none" stroke="#E5092B" stroke-width="2"/>
    <circle cx="95" cy="138" r="1.5" fill="#E5092B"/>
    <text x="30" y="180" fill="#00E676" font-family="'Inter', sans-serif" font-size="10" font-weight="600">&bull; End-to-End Encrypted</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "project-banking-preview.svg"), "w", encoding="utf-8") as f:
    f.write(banking_svg)

# 4. Creative Portfolio Website Preview SVG
portfolio_design_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141622"/>
      <stop offset="100%" stop-color="#08090D"/>
    </linearGradient>
    <filter id="softShadow4" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#000000" flood-opacity="0.65"/>
    </filter>
  </defs>

  <rect width="800" height="500" fill="url(#bgGrad4)"/>

  <!-- Tag Pill Top Left -->
  <g transform="translate(36, 36)">
    <rect width="170" height="28" rx="14" fill="#1C202C" stroke="#333A4D" stroke-width="1"/>
    <circle cx="14" cy="14" r="4" fill="#E5092B"/>
    <text x="26" y="18" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="11" font-weight="600" letter-spacing="1">CONCEPT DESIGN</text>
  </g>

  <!-- Editorial Desktop Viewport Mockup -->
  <g transform="translate(110, 60)" filter="url(#softShadow4)">
    <rect width="580" height="375" rx="14" fill="#12141C" stroke="#323748" stroke-width="1.8"/>
    
    <!-- Top Nav -->
    <rect width="580" height="34" rx="14" fill="#0C0D12"/>
    <circle cx="20" cy="17" r="4" fill="#FF5F56"/>
    <circle cx="34" cy="17" r="4" fill="#FFBD2E"/>
    <circle cx="48" cy="17" r="4" fill="#27C93F"/>
    <text x="225" y="21" fill="#757D94" font-family="'Inter', sans-serif" font-size="11">atelier-concept.studio</text>

    <!-- Content Stage -->
    <g transform="translate(40, 50)">
      <text x="0" y="24" fill="#FFFFFF" font-family="'Space Grotesk', sans-serif" font-size="28" font-weight="700" letter-spacing="-0.02em">ARCHITECTURAL</text>
      <text x="0" y="56" fill="#E5092B" font-family="'Space Grotesk', sans-serif" font-size="28" font-weight="700" letter-spacing="-0.02em">EXPRESSIONS.</text>
      <text x="0" y="80" fill="#8891A8" font-family="'Inter', sans-serif" font-size="12">Spatial design, luxury editorial layouts &amp; 3D perspective depth.</text>

      <!-- 3 Project Panels Side by Side -->
      <g transform="translate(0, 105)">
        <rect width="155" height="170" rx="10" fill="#1B1E29" stroke="#303546" stroke-width="1"/>
        <rect x="12" y="12" width="131" height="85" rx="6" fill="#252A38"/>
        <text x="14" y="120" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600">01. Monolith</text>
        <text x="14" y="138" fill="#8891A8" font-family="'Inter', sans-serif" font-size="10">Spatial Web Exhibition</text>
        <text x="14" y="160" fill="#E5092B" font-family="'Inter', sans-serif" font-size="10" font-weight="600">VIEW &rarr;</text>

        <rect x="175" width="155" height="170" rx="10" fill="#1B1E29" stroke="#303546" stroke-width="1"/>
        <rect x="187" y="12" width="131" height="85" rx="6" fill="#252A38"/>
        <text x="189" y="120" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600">02. Kinetic Void</text>
        <text x="189" y="138" fill="#8891A8" font-family="'Inter', sans-serif" font-size="10">Generative Typography</text>
        <text x="189" y="160" fill="#E5092B" font-family="'Inter', sans-serif" font-size="10" font-weight="600">VIEW &rarr;</text>

        <rect x="350" width="155" height="170" rx="10" fill="#1B1E29" stroke="#303546" stroke-width="1"/>
        <rect x="362" y="12" width="131" height="85" rx="6" fill="#252A38"/>
        <text x="364" y="120" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600">03. Swiss Grid</text>
        <text x="364" y="138" fill="#8891A8" font-family="'Inter', sans-serif" font-size="10">Minimal Design Tokens</text>
        <text x="364" y="160" fill="#E5092B" font-family="'Inter', sans-serif" font-size="10" font-weight="600">VIEW &rarr;</text>
      </g>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "project-designportfolio-preview.svg"), "w", encoding="utf-8") as f:
    f.write(portfolio_design_svg)

print("Generated project SVGs successfully!")
