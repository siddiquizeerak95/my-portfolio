with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

target_start = '// 05.1 HERO 3D PERSPECTIVE SPATIAL TRACKER'
target_end = '// 06. CUSTOM DUAL-STATE PRECISION CYAN CURSOR'

idx1 = text.find(target_start)
idx2 = text.find(target_end)

if idx1 != -1 and idx2 != -1:
    new_code = """// 05.1 HERO CINEMATIC 3D PERSPECTIVE MOUSE-FOLLOW TILT
// -----------------------------------------------------------------------------
function initHeroPerspective() {
  const isFinePointer = window.matchMedia('(pointer: fine) and (hover: hover)').matches;
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!isFinePointer || prefersReducedMotion) return;

  const heroSection = document.getElementById('hero');
  const card = document.getElementById('hero-portrait-card') || document.querySelector('.hero-cinematic-portrait-card');
  const glow = document.querySelector('.hero-cinematic-ambient-glow') || document.querySelector('.hero-portrait-ambient-glow');
  if (!heroSection || !card) return;

  let targetRotX = 0;
  let targetRotY = 0;
  let currentRotX = 0;
  let currentRotY = 0;

  let targetShiftX = 0;
  let targetShiftY = 0;
  let currentShiftX = 0;
  let currentShiftY = 0;

  let isHovering = false;
  let animationFrameId = null;

  const renderLoop = () => {
    // Smooth damping (lerp factor 0.08) for silky luxury editorial feel
    currentRotX += (targetRotX - currentRotX) * 0.08;
    currentRotY += (targetRotY - currentRotY) * 0.08;
    currentShiftX += (targetShiftX - currentShiftX) * 0.08;
    currentShiftY += (targetShiftY - currentShiftY) * 0.08;

    card.style.transform = `perspective(1200px) rotateX(${currentRotX.toFixed(2)}deg) rotateY(${currentRotY.toFixed(2)}deg) translateY(-2px)`;
    if (glow) {
      glow.style.transform = `translate(calc(-50% + ${currentShiftX.toFixed(1)}px), calc(-50% + ${currentShiftY.toFixed(1)}px))`;
    }

    const diff = Math.abs(targetRotX - currentRotX) + Math.abs(targetRotY - currentRotY);
    if (isHovering || diff > 0.02) {
      animationFrameId = requestAnimationFrame(renderLoop);
    } else {
      card.style.transform = '';
      if (glow) glow.style.transform = '';
      animationFrameId = null;
    }
  };

  heroSection.addEventListener('mousemove', (e) => {
    const cardRect = card.getBoundingClientRect();
    const cardCenterX = cardRect.left + cardRect.width / 2;
    const cardCenterY = cardRect.top + cardRect.height / 2;

    // Gentle normalized distance relative to card center
    const maxDistX = window.innerWidth * 0.45;
    const maxDistY = window.innerHeight * 0.45;
    const normX = Math.max(-1, Math.min(1, (e.clientX - cardCenterX) / maxDistX));
    const normY = Math.max(-1, Math.min(1, (e.clientY - cardCenterY) / maxDistY));

    // Subtle, elegant rotation (max ±4.0 deg on Y, ±3.2 deg on X)
    targetRotY = normX * 4.2;
    targetRotX = normY * -3.4;
    targetShiftX = normX * -12;
    targetShiftY = normY * -12;

    if (!isHovering) {
      isHovering = true;
      if (!animationFrameId) {
        animationFrameId = requestAnimationFrame(renderLoop);
      }
    }
  }, { passive: true });

  heroSection.addEventListener('mouseleave', () => {
    isHovering = false;
    targetRotX = 0;
    targetRotY = 0;
    targetShiftX = 0;
    targetShiftY = 0;
  }, { passive: true });
}

// -----------------------------------------------------------------------------
"""
    new_text = text[:idx1] + new_code + text[idx2:]
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully replaced initHeroPerspective in script.js")
else:
    print(f"Could not find indices in script.js: {idx1}, {idx2}")

