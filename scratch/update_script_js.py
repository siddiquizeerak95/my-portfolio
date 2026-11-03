with open(r'c:\Users\siddi\Desktop\New folder\script.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_func = """function initHeroPerspective() {
  const isFinePointer = window.matchMedia('(pointer: fine) and (hover: hover)').matches;
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!isFinePointer || prefersReducedMotion) return;

  const heroSection = document.getElementById('hero');
  const stage = document.getElementById('hero-3d-stage');
  if (!heroSection || !stage) return;

  let targetRotX = 0;
  let targetRotY = 0;
  let currentRotX = 0;
  let currentRotY = 0;
  let isHovering = false;
  let animationFrameId = null;

  const renderLoop = () => {
    // Smooth damping (lerp)
    currentRotX += (targetRotX - currentRotX) * 0.08;
    currentRotY += (targetRotY - currentRotY) * 0.08;

    stage.style.transform = `perspective(1200px) rotateX(${currentRotX.toFixed(2)}deg) rotateY(${currentRotY.toFixed(2)}deg)`;

    const diff = Math.abs(targetRotX - currentRotX) + Math.abs(targetRotY - currentRotY);
    if (isHovering || diff > 0.01) {
      animationFrameId = requestAnimationFrame(renderLoop);
    } else {
      stage.style.transform = '';
      animationFrameId = null;
    }
  };

  heroSection.addEventListener('mousemove', (e) => {
    const rect = heroSection.getBoundingClientRect();
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    const relX = e.clientX - rect.left - centerX;
    const relY = e.clientY - rect.top - centerY;

    // Subtle 3D rotation (max ~±3.2 deg on X, ±4.2 deg on Y)
    targetRotX = (relY / centerY) * -3.2;
    targetRotY = (relX / centerX) * 4.2;

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
  }, { passive: true });
}"""

new_func = """function initHeroPerspective() {
  const isFinePointer = window.matchMedia('(pointer: fine) and (hover: hover)').matches;
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!isFinePointer || prefersReducedMotion) return;

  const heroSection = document.getElementById('hero');
  const stage = document.getElementById('hero-3d-stage');
  const rig = document.getElementById('hero-3d-rig');
  if (!heroSection || !stage || !rig) return;

  const panels = stage.querySelectorAll('.floating-panel');

  const BASE_ROTY = -15;
  const BASE_ROTX = 9;

  let targetRotX = BASE_ROTX;
  let targetRotY = BASE_ROTY;
  let currentRotX = BASE_ROTX;
  let currentRotY = BASE_ROTY;

  let targetNormX = 0;
  let targetNormY = 0;
  let currentNormX = 0;
  let currentNormY = 0;

  let isHovering = false;
  let animationFrameId = null;

  const renderLoop = () => {
    // Smooth damping (lerp factor 0.08)
    currentRotX += (targetRotX - currentRotX) * 0.08;
    currentRotY += (targetRotY - currentRotY) * 0.08;
    currentNormX += (targetNormX - currentNormX) * 0.08;
    currentNormY += (targetNormY - currentNormY) * 0.08;

    rig.style.transform = `rotateY(${currentRotY.toFixed(2)}deg) rotateX(${currentRotX.toFixed(2)}deg) rotateZ(-2deg)`;

    // Differential parallax on layered floating cards
    panels.forEach((p) => {
      const depth = parseFloat(p.getAttribute('data-depth')) || 60;
      const shiftX = (currentNormX * (depth * 0.16)).toFixed(1);
      const shiftY = (currentNormY * (depth * 0.16)).toFixed(1);
      p.style.transform = `translateZ(${depth}px) translate(${shiftX}px, ${shiftY}px)`;
    });

    const diff = Math.abs(targetRotX - currentRotX) + Math.abs(targetRotY - currentRotY);
    if (isHovering || diff > 0.02) {
      animationFrameId = requestAnimationFrame(renderLoop);
    } else {
      rig.style.transform = '';
      panels.forEach((p) => { p.style.transform = ''; });
      animationFrameId = null;
    }
  };

  heroSection.addEventListener('mousemove', (e) => {
    const rect = heroSection.getBoundingClientRect();
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    const relX = Math.max(-centerX, Math.min(centerX, e.clientX - rect.left - centerX));
    const relY = Math.max(-centerY, Math.min(centerY, e.clientY - rect.top - centerY));

    targetNormX = relX / centerX;
    targetNormY = relY / centerY;

    // Smooth tilt: ±8 deg on Y, ±6 deg on X
    targetRotY = BASE_ROTY + (targetNormX * 8.5);
    targetRotX = BASE_ROTX + (targetNormY * -6.5);

    if (!isHovering) {
      isHovering = true;
      if (!animationFrameId) {
        animationFrameId = requestAnimationFrame(renderLoop);
      }
    }
  }, { passive: true });

  heroSection.addEventListener('mouseleave', () => {
    isHovering = false;
    targetRotX = BASE_ROTX;
    targetRotY = BASE_ROTY;
    targetNormX = 0;
    targetNormY = 0;
  }, { passive: true });
}"""

if old_func in js:
    js = js.replace(old_func, new_func)
    with open(r'c:\Users\siddi\Desktop\New folder\script.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("script.js updated with advanced 3D perspective hero parallax tracker!")
else:
    print("Could not find exact old_func in script.js")

