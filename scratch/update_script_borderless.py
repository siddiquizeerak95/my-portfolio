with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

target_start = '// 05.1 HERO CINEMATIC 3D PERSPECTIVE MOUSE-FOLLOW TILT'
target_end = '// 06. CUSTOM DUAL-STATE PRECISION CYAN CURSOR'

idx1 = text.find(target_start)
idx2 = text.find(target_end)

if idx1 != -1 and idx2 != -1:
    new_code = """// 05.1 HERO BORDERLESS CINEMATIC PARALLAX DEPTH
// -----------------------------------------------------------------------------
function initHeroPerspective() {
  const isFinePointer = window.matchMedia('(pointer: fine) and (hover: hover)').matches;
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!isFinePointer || prefersReducedMotion) return;

  const heroSection = document.getElementById('hero');
  const portraitWrap = document.getElementById('hero-portrait-card') || document.querySelector('.hero-borderless-portrait-wrap');
  const glow = document.querySelector('.hero-borderless-ambient-glow') || document.querySelector('.hero-cinematic-ambient-glow');
  if (!heroSection || !portraitWrap) return;

  let targetShiftX = 0;
  let targetShiftY = 0;
  let currentShiftX = 0;
  let currentShiftY = 0;

  let targetRotY = 0;
  let targetRotX = 0;
  let currentRotY = 0;
  let currentRotX = 0;

  let isHovering = false;
  let animationFrameId = null;

  const renderLoop = () => {
    // Silk-smooth lerp damping for organic photographic depth
    currentShiftX += (targetShiftX - currentShiftX) * 0.06;
    currentShiftY += (targetShiftY - currentShiftY) * 0.06;
    currentRotY += (targetRotY - currentRotY) * 0.06;
    currentRotX += (targetRotX - currentRotX) * 0.06;

    portraitWrap.style.transform = `translate3d(${currentShiftX.toFixed(1)}px, ${currentShiftY.toFixed(1)}px, 0) rotateY(${currentRotY.toFixed(2)}deg) rotateX(${currentRotX.toFixed(2)}deg)`;
    if (glow) {
      glow.style.transform = `translate(calc(-50% + ${(-currentShiftX * 1.4).toFixed(1)}px), calc(-50% + ${(-currentShiftY * 1.4).toFixed(1)}px))`;
    }

    const diff = Math.abs(targetShiftX - currentShiftX) + Math.abs(targetShiftY - currentShiftY);
    if (isHovering || diff > 0.1) {
      animationFrameId = requestAnimationFrame(renderLoop);
    } else {
      portraitWrap.style.transform = '';
      if (glow) glow.style.transform = '';
      animationFrameId = null;
    }
  };

  heroSection.addEventListener('mousemove', (e) => {
    const rect = heroSection.getBoundingClientRect();
    const centerX = rect.left + rect.width * 0.5;
    const centerY = rect.top + rect.height * 0.5;
    const normX = Math.max(-1, Math.min(1, (e.clientX - centerX) / (rect.width * 0.5)));
    const normY = Math.max(-1, Math.min(1, (e.clientY - centerY) / (rect.height * 0.5)));

    // Restrained, subtle cinematic depth (±7px translation, ±1.5 deg tilt)
    targetShiftX = normX * 7.5;
    targetShiftY = normY * 5.5;
    targetRotY = normX * 1.5;
    targetRotX = normY * -1.2;

    if (!isHovering) {
      isHovering = true;
      if (!animationFrameId) {
        animationFrameId = requestAnimationFrame(renderLoop);
      }
    }
  }, { passive: true });

  heroSection.addEventListener('mouseleave', () => {
    isHovering = false;
    targetShiftX = 0;
    targetShiftY = 0;
    targetRotY = 0;
    targetRotX = 0;
  }, { passive: true });
}

// -----------------------------------------------------------------------------
"""
    text = text[:idx1] + new_code + text[idx2:]
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully updated script.js with borderless depth interaction!")
else:
    print(f"Could not find indices: {idx1}, {idx2}")

