/**
 * =============================================================================
 * ZS STUDIO — CINEMATIC 3D MONOCHROME STIPPLE PORTRAIT INTRODUCTION
 * Three.js WebGL Engine with Particle Assembly, Dual-Axis Parallax & Dissolution
 * 
 * Recreates the exact stippled point-cloud sculpture style from the user reference:
 * - Genuine 3D volumetric point cloud reconstructed from Zeerak's photograph
 * - 125,000+ tiny, sharply defined monochrome particles (black, grey, and white)
 * - Recognizable facial identity: eyebrows, eyes/pupils, nose, lips, goatee, hair, coat
 * - Continuous anatomical relief (nose bump, eye socket recess, brow, chin, lapels)
 * - Initial assembly animation: scattered particle cloud gathers smoothly over ~1.4s
 * - Idle state: gentle living breathing oscillation & floating ambient dust
 * - Dual-axis cursor parallax: controlled rotation (up to 12° yaw, 8° pitch)
 * - Dissolution: smooth particle dispersal on scroll or "ENTER WEBSITE →" click
 * =============================================================================
 */

class ParticleSculptureIntro {
  constructor(options = {}) {
    this.stage = document.getElementById('sculpture-intro-stage');
    this.canvas = document.getElementById('sculpture-canvas');
    this.welcomeBlock = document.getElementById('sculpture-welcome-block');
    this.brandTop = document.querySelector('.intro-brand-top-left');
    this.exploreHint = document.querySelector('.intro-explore-hint');
    this.scrollIndicator = document.getElementById('intro-scroll-indicator');
    this.scrollThumb = document.getElementById('intro-scroll-thumb');
    this.enterWrap = document.querySelector('.sculpture-enter-wrap');
    this.enterBtn = document.getElementById('btn-enter-website');
    this.onEnterCallback = options.onEnter || (() => {});

    this.scene = null;
    this.camera = null;
    this.renderer = null;
    this.portraitMesh = null;
    this.ambientMesh = null;
    this.pointMesh = null; // compatibility alias
    this.sculptureGroup = null;

    this.vertexCount = 0;
    this.portraitCount = 0;
    this.ambientCount = 0;

    this.originPositions = null;
    this.currentPositions = null;
    this.baseColors = null;
    this.currentColors = null;
    this.deltas = null;
    this.tStarts = null;
    this.phases = null;
    this.scatterOffsets = null;

    // Formation (Assembly) State
    this.isForming = false;
    this.formationDuration = 1400; // ms
    this.formationStartTime = null;
    this.formationProgress = 1.0; // 0.0 -> scattered, 1.0 -> fully formed

    // Dissolution & Interactive State
    this.dissolveProgress = 0.0;
    this.targetDissolveProgress = 0.0;
    this.isEnteringWebsite = false;
    this.hasFinishedIntro = false;
    this.isSnapshotMode = false;
    this.isReady = false;
    this.pendingFormation = false;
    this.phase = 'loading'; // 'loading', 'active', 'dissolving', 'dismissed'

    // Subtle, elegant cursor tracking (Capped at ±5 deg yaw, ±3 deg pitch)
    this.mouse = { x: 0, y: 0 };
    this.targetMouse = { x: 0, y: 0 };
    this.animationFrameId = null;

    this.boundAnimate = this.animate.bind(this);
    this.boundResize = this.onResize.bind(this);
    this.boundMouseMove = this.onMouseMove.bind(this);
    this.boundMouseLeave = this.onMouseLeave.bind(this);
    this.boundTouchMove = this.onTouchMove.bind(this);
    this.boundTouchEnd = this.onTouchEnd.bind(this);
    this.boundWheel = this.onWheel.bind(this);
    this.boundKeyDown = this.onKeyDown.bind(this);

    this.init();
  }

  async init() {
    if (!this.stage || !this.canvas) return;

    // Accessibility check: prefers-reduced-motion
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      this.dismissImmediately();
      return;
    }

    // URL override: ?skip_intro=1
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('skip_intro') === '1') {
      this.dismissImmediately();
      return;
    }

    // Three.js availability check
    if (typeof THREE === 'undefined') {
      console.warn('Three.js unavailable, falling back to static presentation.');
      this.stage.classList.add('no-webgl');
      this.setupFallbackEvents();
      return;
    }

    try {
      this.initThree();
      await this.loadSculptureData();
      this.createHologramMesh();
      this.bindEvents();

      this.isReady = true;
      this.stage.classList.add('ready');

      // Check test overrides
      const introState = urlParams.get('intro_state');
      const testScroll = urlParams.get('scroll_progress');
      const cursorX = parseFloat(urlParams.get('cursor_x') || '0');
      const cursorY = parseFloat(urlParams.get('cursor_y') || '0');

      if (cursorX || cursorY) {
        this.targetMouse.x = cursorX;
        this.mouse.x = cursorX;
        this.targetMouse.y = cursorY;
        this.mouse.y = cursorY;
      }

      if (urlParams.get('snap') === '1') {
        this.isSnapshotMode = true;
        this.stage.classList.add('snap-no-transition');
      }

      if (testScroll !== null) {
        const p = parseFloat(testScroll);
        this.phase = 'active';
        this.stage.classList.add('active');
        if (this.welcomeBlock && p < 0.2) this.welcomeBlock.classList.add('visible');
        this.targetDissolveProgress = p;
        this.dissolveProgress = p;
        this.isForming = false;
        this.formationProgress = 1.0;
        this.setDissolveProgress(p);
      } else if (introState === 'assembled') {
        this.phase = 'active';
        this.stage.classList.add('active');
        if (this.welcomeBlock) this.welcomeBlock.classList.add('visible');
        this.targetDissolveProgress = 0.0;
        this.dissolveProgress = 0.0;
        this.isForming = false;
        this.formationProgress = 1.0;
        this.setDissolveProgress(0.0);
      }

      // If preloader finished while loading, launch formation immediately
      if (this.pendingFormation) {
        this.pendingFormation = false;
        this.startFormation();
      }

      if (this.isSnapshotMode && this.sculptureGroup) {
        const rotAttenuation = Math.max(0.0, 1.0 - this.dissolveProgress * 2.2);
        // Reduced rotation: max ±5 deg (0.0872 rad) yaw, ±3 deg (0.0523 rad) pitch
        this.sculptureGroup.rotation.y = this.mouse.x * 0.0872 * rotAttenuation;
        this.sculptureGroup.rotation.x = -this.mouse.y * 0.0523 * rotAttenuation;
        this.sculptureGroup.position.z = Math.abs(this.mouse.x) * 2.5 * rotAttenuation;
        this.sculptureGroup.position.x = this.mouse.x * 1.8 * rotAttenuation;
        if (this.renderer && this.scene && this.camera) {
          this.renderer.render(this.scene, this.camera);
        }
      }

      if (!this.animationFrameId) {
        this.animate();
      }
    } catch (err) {
      console.error('3D Holographic sculpture initialization error:', err);
      this.stage.classList.add('no-webgl');
      this.setupFallbackEvents();
    }
  }

  initThree() {
    const width = window.innerWidth;
    const height = window.innerHeight;

    // Scene with transparent background so CSS studio ambient glow shines through
    this.scene = new THREE.Scene();

    // Perspective Camera framing sculpture comfortably centered
    this.camera = new THREE.PerspectiveCamera(45, width / height, 1, 2000);
    const cameraZ = width <= 768 ? 580 : (width <= 1024 ? 510 : 475);
    this.camera.position.set(0, 0, cameraZ);
    this.camera.lookAt(0, 0, 0);

    // High Precision WebGL Renderer with alpha transparency
    this.renderer = new THREE.WebGLRenderer({
      canvas: this.canvas,
      antialias: true,
      powerPreference: 'high-performance',
      alpha: true
    });
    this.renderer.setSize(width, height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    this.renderer.outputEncoding = THREE.sRGBEncoding;

    // Sculpture Group centered in 3D space
    this.sculptureGroup = new THREE.Group();
    const baseY = (width <= 768 ? -22 : (width <= 1024 ? -6 : 2));
    this.sculptureGroup.position.set(0, baseY, 0);
    this.scene.add(this.sculptureGroup);
  }

  async loadSculptureData() {
    // Attempt high-speed binary stream first
    try {
      const res = await fetch('assets/scrolldriven-portrait.bin?v=75');
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const buf = await res.arrayBuffer();

      const header = new Uint32Array(buf, 0, 4);
      this.vertexCount = header[0];
      this.portraitCount = header[1] || this.vertexCount;
      this.ambientCount = header[2] || 0;

      let byteOffset = 16;
      this.originPositions = new Float32Array(buf, byteOffset, this.vertexCount * 3);
      byteOffset += this.vertexCount * 3 * 4;

      this.baseColors = new Float32Array(buf, byteOffset, this.vertexCount * 3);
      byteOffset += this.vertexCount * 3 * 4;

      this.deltas = new Float32Array(buf, byteOffset, this.vertexCount * 3);
      byteOffset += this.vertexCount * 3 * 4;

      this.tStarts = new Float32Array(buf, byteOffset, this.vertexCount);
      byteOffset += this.vertexCount * 4;

      this.phases = new Float32Array(buf, byteOffset, this.vertexCount);

      // Initialize working buffers
      this.currentPositions = new Float32Array(this.originPositions);
      this.currentColors = new Float32Array(this.baseColors);

      // Precalculate spherical scatter offsets for smooth assembly formation
      this.generateScatterOffsets();
      return;
    } catch (binErr) {
      console.warn('Binary fetch failed, attempting JSON fallback...', binErr);
    }

    // JSON fallback
    const res = await fetch('assets/scrolldriven-portrait.json?v=75');
    const data = await res.json();
    this.vertexCount = data.vertexCount;
    this.portraitCount = data.portraitCount || this.vertexCount;
    this.ambientCount = data.ambientCount || 0;
    this.originPositions = new Float32Array(data.vertices);
    this.baseColors = new Float32Array(data.colors);
    this.deltas = new Float32Array(data.deltas);
    this.tStarts = new Float32Array(data.tStarts);
    this.phases = new Float32Array(data.phases || this.vertexCount);

    this.currentPositions = new Float32Array(this.originPositions);
    this.currentColors = new Float32Array(this.baseColors);
    this.generateScatterOffsets();
  }

  generateScatterOffsets() {
    this.scatterOffsets = new Float32Array(this.vertexCount * 3);
    for (let i = 0; i < this.vertexCount; i++) {
      const i3 = i * 3;
      // Spherical shell explosion offset (radius 180 to 320)
      const theta = Math.random() * Math.PI * 2.0;
      const phi = (Math.random() - 0.5) * Math.PI * 0.9;
      const r = 180.0 + Math.random() * 140.0;

      this.scatterOffsets[i3] = Math.cos(phi) * Math.cos(theta) * r;
      this.scatterOffsets[i3 + 1] = Math.sin(phi) * r * 1.1 + (Math.random() - 0.5) * 50.0;
      this.scatterOffsets[i3 + 2] = Math.cos(phi) * Math.sin(theta) * (r * 0.8) + (Math.random() - 0.5) * 60.0;
    }
  }

  createDotTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 64;
    canvas.height = 64;
    const ctx = canvas.getContext('2d');

    // Crisp circular micro-dot texture with high central luminosity
    const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 30);
    grad.addColorStop(0.0, 'rgba(255, 255, 255, 1.0)');
    grad.addColorStop(0.68, 'rgba(255, 255, 255, 0.98)');
    grad.addColorStop(0.88, 'rgba(255, 255, 255, 0.55)');
    grad.addColorStop(1.0, 'rgba(255, 255, 255, 0.0)');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 64, 64);

    return new THREE.CanvasTexture(canvas);
  }

  createHologramMesh() {
    const dotTex = this.createDotTexture();
    const pCount = this.portraitCount || this.vertexCount;
    const isMobile = window.innerWidth <= 768;

    // 1. High-Density Bust Stipple Mesh (crisp luminous micro-dots)
    const portraitGeo = new THREE.BufferGeometry();
    const portraitPosSub = this.currentPositions.subarray(0, pCount * 3);
    const portraitColSub = this.currentColors.subarray(0, pCount * 3);
    portraitGeo.setAttribute('position', new THREE.BufferAttribute(portraitPosSub, 3));
    portraitGeo.setAttribute('color', new THREE.BufferAttribute(portraitColSub, 3));

    const portraitMat = new THREE.PointsMaterial({
      size: isMobile ? 2.6 : 2.2,
      map: dotTex,
      vertexColors: true,
      transparent: true,
      opacity: 1.0,
      blending: THREE.NormalBlending,
      depthTest: true,
      depthWrite: false
    });

    this.portraitMesh = new THREE.Points(portraitGeo, portraitMat);
    this.pointMesh = this.portraitMesh; // compatibility alias
    this.sculptureGroup.add(this.portraitMesh);

    // 2. Ambient Floating Stardust (gentle drifting dust particles)
    if (this.ambientCount > 0) {
      const ambientGeo = new THREE.BufferGeometry();
      const ambPosSub = this.currentPositions.subarray(pCount * 3, this.vertexCount * 3);
      const ambColSub = this.currentColors.subarray(pCount * 3, this.vertexCount * 3);
      ambientGeo.setAttribute('position', new THREE.BufferAttribute(ambPosSub, 3));
      ambientGeo.setAttribute('color', new THREE.BufferAttribute(ambColSub, 3));

      const ambientMat = new THREE.PointsMaterial({
        size: isMobile ? 2.8 : 2.4,
        map: dotTex,
        vertexColors: true,
        transparent: true,
        opacity: 0.90,
        blending: THREE.AdditiveBlending,
        depthTest: true,
        depthWrite: false
      });

      this.ambientMesh = new THREE.Points(ambientGeo, ambientMat);
      this.sculptureGroup.add(this.ambientMesh);
    }
  }

  startFormation() {
    if (!this.isReady) {
      this.pendingFormation = true;
      return;
    }

    this.phase = 'active';
    this.stage.classList.add('active');

    // Prevent body scroll during full-screen intro
    document.body.style.overflow = 'hidden';

    // Ensure camera aspect and renderer dimensions are calibrated
    this.onResize();

    if (!this.isSnapshotMode) {
      // Begin smooth particle assembly over ~1.4s
      this.isForming = true;
      this.formationStartTime = performance.now();
      this.formationProgress = 0.0;
    } else {
      this.isForming = false;
      this.formationProgress = 1.0;
    }

    if (this.welcomeBlock) {
      setTimeout(() => {
        this.welcomeBlock.classList.add('visible');
      }, 350);
    }

    this.setDissolveProgress(0.0);
  }

  onWheel(e) {
    if (this.hasFinishedIntro || this.phase !== 'active') return;

    // Advance dissolution on scroll down, reassemble on scroll up
    const delta = e.deltaY;
    if (delta > 0) {
      this.targetDissolveProgress += delta * 0.0018;
    } else {
      this.targetDissolveProgress += delta * 0.0018;
    }

    this.targetDissolveProgress = Math.min(1.0, Math.max(0.0, this.targetDissolveProgress));
    e.preventDefault();
  }

  onTouchMove(e) {
    if (e.touches && e.touches[0]) {
      const halfW = window.innerWidth / 2;
      const halfH = window.innerHeight / 2;
      // Subtle touch tracking on mobile
      this.targetMouse.x = ((e.touches[0].clientX - halfW) / halfW) * 0.65;
      this.targetMouse.y = ((e.touches[0].clientY - halfH) / halfH) * 0.65;

      if (this.lastTouchY !== undefined && !this.hasFinishedIntro && this.phase === 'active') {
        const delta = this.lastTouchY - e.touches[0].clientY;
        if (delta > 0) {
          this.targetDissolveProgress += delta * 0.0035;
          this.targetDissolveProgress = Math.min(1.0, Math.max(0.0, this.targetDissolveProgress));
        }
      }
      this.lastTouchY = e.touches[0].clientY;
    }
  }

  onTouchEnd() {
    this.targetMouse.x = 0;
    this.targetMouse.y = 0;
    this.lastTouchY = undefined;
  }

  triggerEnterDissolution() {
    if (this.isEnteringWebsite || this.hasFinishedIntro) return;
    this.isEnteringWebsite = true;

    // Cinematic smooth transition into website over ~1.15s
    if (typeof gsap !== 'undefined') {
      gsap.to(this, {
        targetDissolveProgress: 1.0,
        dissolveProgress: 1.0,
        duration: 1.15,
        ease: 'power2.out',
        onUpdate: () => {
          this.setDissolveProgress(this.dissolveProgress);
        },
        onComplete: () => {
          this.finishIntro();
        }
      });
    } else {
      const startTime = performance.now();
      const startP = this.dissolveProgress;
      const duration = 1150;

      const step = (now) => {
        const elapsed = now - startTime;
        const t = Math.min(1.0, elapsed / duration);
        const ease = t * (2 - t);
        const p = startP + (1.0 - startP) * ease;
        this.setDissolveProgress(p);

        if (t < 1.0) {
          requestAnimationFrame(step);
        } else {
          this.finishIntro();
        }
      };
      requestAnimationFrame(step);
    }
  }

  setDissolveProgress(progress) {
    this.dissolveProgress = Math.min(1.0, Math.max(0.0, progress));

    // 1. Update Particle Positions & Colors in 3D Space
    if (this.currentPositions && this.currentColors) {
      const posArr = this.currentPositions;
      const colArr = this.currentColors;
      const origPos = this.originPositions;
      const baseCol = this.baseColors;
      const deltas = this.deltas;
      const tStarts = this.tStarts;
      const count = this.vertexCount;
      const p = this.dissolveProgress;

      for (let i = 0; i < count; i++) {
        const i3 = i * 3;
        const ts = tStarts[i];

        if (p <= ts) {
          posArr[i3] = origPos[i3];
          posArr[i3 + 1] = origPos[i3 + 1];
          posArr[i3 + 2] = origPos[i3 + 2];

          colArr[i3] = baseCol[i3];
          colArr[i3 + 1] = baseCol[i3 + 1];
          colArr[i3 + 2] = baseCol[i3 + 2];
        } else {
          const u = (p - ts) / (1.0 - ts);
          const uClamped = Math.min(1.0, Math.max(0.0, u));
          // Cubic acceleration for organic 3D drift
          const ease = uClamped * uClamped * (3.0 - 2.0 * uClamped);

          posArr[i3] = origPos[i3] + deltas[i3] * ease;
          posArr[i3 + 1] = origPos[i3 + 1] + deltas[i3 + 1] * ease;
          posArr[i3 + 2] = origPos[i3 + 2] + deltas[i3 + 2] * ease;

          // Fade particles outward
          const fade = Math.max(0.0, 1.0 - Math.pow(uClamped, 1.3));
          colArr[i3] = baseCol[i3] * fade;
          colArr[i3 + 1] = baseCol[i3 + 1] * fade;
          colArr[i3 + 2] = baseCol[i3 + 2] * fade;
        }
      }

      if (this.portraitMesh) {
        this.portraitMesh.geometry.attributes.position.needsUpdate = true;
        this.portraitMesh.geometry.attributes.color.needsUpdate = true;
      }
      if (this.ambientMesh) {
        this.ambientMesh.geometry.attributes.position.needsUpdate = true;
        this.ambientMesh.geometry.attributes.color.needsUpdate = true;
      }
    }

    // 2. Update UI Typography & Scroll Indicator
    const p = this.dissolveProgress;
    if (this.scrollThumb) {
      const trackHeight = 104; // px
      this.scrollThumb.style.transform = `translate(-50%, ${p * trackHeight}px)`;
    }

    const uiAlpha = Math.max(0.0, 1.0 - p / 0.18);
    if (this.welcomeBlock) this.welcomeBlock.style.opacity = uiAlpha;
    if (this.brandTop) this.brandTop.style.opacity = uiAlpha;
    if (this.exploreHint) this.exploreHint.style.opacity = uiAlpha;
    if (this.scrollIndicator) this.scrollIndicator.style.opacity = uiAlpha;
    if (this.enterWrap) this.enterWrap.style.opacity = Math.max(0.0, 1.0 - p / 0.40);

    // 3. Stage Background Fade to reveal homepage smoothly near end
    if (p >= 0.82) {
      const exitAlpha = Math.max(0.0, (1.0 - p) / 0.18);
      this.stage.style.opacity = exitAlpha;
      if (p >= 0.98 && !this.hasFinishedIntro) {
        this.finishIntro();
      }
    } else {
      this.stage.style.opacity = 1.0;
    }
  }

  finishIntro() {
    if (this.hasFinishedIntro) return;
    this.hasFinishedIntro = true;
    this.phase = 'dismissed';

    // Restore body scroll
    document.body.style.overflow = '';

    // Hide intro stage cleanly
    this.stage.classList.add('intro-dismissed');
    this.stage.style.opacity = '0';
    this.stage.style.pointerEvents = 'none';

    setTimeout(() => {
      this.stage.style.display = 'none';
    }, 600);

    // Reveal homepage
    this.onEnterCallback();
  }

  dismissImmediately() {
    this.hasFinishedIntro = true;
    this.phase = 'dismissed';
    document.body.style.overflow = '';

    if (this.stage) {
      this.stage.classList.add('intro-dismissed');
      this.stage.style.display = 'none';
      this.stage.style.pointerEvents = 'none';
    }
    this.onEnterCallback();
  }

  bindEvents() {
    window.addEventListener('resize', this.boundResize);
    window.addEventListener('mousemove', this.boundMouseMove);
    window.addEventListener('mouseleave', this.boundMouseLeave);
    window.addEventListener('touchmove', this.boundTouchMove, { passive: true });
    window.addEventListener('touchend', this.boundTouchEnd);
    window.addEventListener('keydown', this.boundKeyDown);
    window.addEventListener('wheel', this.boundWheel, { passive: false });

    if (this.enterBtn) {
      this.enterBtn.addEventListener('click', (e) => {
        e.preventDefault();
        this.triggerEnterDissolution();
      });
    }
  }

  setupFallbackEvents() {
    if (this.enterBtn) {
      this.enterBtn.addEventListener('click', (e) => {
        e.preventDefault();
        this.dismissImmediately();
      });
    }
  }

  onMouseMove(e) {
    const halfW = window.innerWidth / 2;
    const halfH = window.innerHeight / 2;
    this.targetMouse.x = (e.clientX - halfW) / halfW;
    this.targetMouse.y = (e.clientY - halfH) / halfH;
  }

  onMouseLeave() {
    this.targetMouse.x = 0;
    this.targetMouse.y = 0;
  }

  onKeyDown(e) {
    if ((e.key === 'Enter' || e.key === ' ') && !this.hasFinishedIntro && this.phase === 'active') {
      if (document.activeElement && (document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'TEXTAREA')) {
        return;
      }
      this.triggerEnterDissolution();
    }
  }

  onResize() {
    const width = window.innerWidth;
    const height = window.innerHeight;

    if (this.camera) {
      this.camera.aspect = width / height;
      const cameraZ = width <= 768 ? 580 : (width <= 1024 ? 510 : 475);
      this.camera.position.z = cameraZ;
      this.camera.updateProjectionMatrix();
    }

    if (this.renderer) {
      this.renderer.setSize(width, height);
      this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    }

    if (this.sculptureGroup) {
      const baseY = (width <= 768 ? -22 : (width <= 1024 ? -6 : 2));
      this.sculptureGroup.position.y = baseY;
    }
  }

  animate() {
    this.animationFrameId = requestAnimationFrame(this.boundAnimate);
    const now = performance.now();

    // 1. Formation Assembly Interpolation
    if (this.isForming && this.formationStartTime) {
      const elapsed = now - this.formationStartTime;
      const t = Math.min(1.0, elapsed / this.formationDuration);
      // Cubic ease out
      const ease = 1.0 - Math.pow(1.0 - t, 3.0);
      this.formationProgress = ease;

      const scatterFactor = 1.0 - ease;
      const posArr = this.currentPositions;
      const origPos = this.originPositions;
      const scatter = this.scatterOffsets;
      const count = this.vertexCount;

      for (let i = 0; i < count; i++) {
        const i3 = i * 3;
        posArr[i3] = origPos[i3] + scatter[i3] * scatterFactor;
        posArr[i3 + 1] = origPos[i3 + 1] + scatter[i3 + 1] * scatterFactor;
        posArr[i3 + 2] = origPos[i3 + 2] + scatter[i3 + 2] * scatterFactor;
      }

      if (this.portraitMesh) this.portraitMesh.geometry.attributes.position.needsUpdate = true;
      if (this.ambientMesh) this.ambientMesh.geometry.attributes.position.needsUpdate = true;

      if (t >= 1.0) {
        this.isForming = false;
        this.formationProgress = 1.0;
      }
    }
    // 2. Idle Living Breathing Oscillation (Active formed state)
    else if (!this.isForming && this.formationProgress >= 1.0 && this.dissolveProgress <= 0.001 && !this.isSnapshotMode) {
      const posArr = this.currentPositions;
      const origPos = this.originPositions;
      const phases = this.phases;
      const pCount = this.portraitCount;
      const total = this.vertexCount;
      const time = now * 0.0016;

      // Subtle breathing wave on bust particles (amplitude ~0.45 units)
      for (let i = 0; i < pCount; i++) {
        const i3 = i * 3;
        const ph = phases[i];
        const breathZ = Math.sin(time * 1.4 + ph) * 0.65;
        const breathY = Math.cos(time * 1.0 + ph) * 0.35;
        posArr[i3 + 1] = origPos[i3 + 1] + breathY;
        posArr[i3 + 2] = origPos[i3 + 2] + breathZ;
      }

      // Gentle drift for ambient stardust particles
      for (let i = pCount; i < total; i++) {
        const i3 = i * 3;
        const ph = phases[i];
        posArr[i3] = origPos[i3] + Math.sin(time * 0.8 + ph) * 3.5;
        posArr[i3 + 1] = origPos[i3 + 1] + Math.cos(time * 0.6 + ph) * 4.0;
        posArr[i3 + 2] = origPos[i3 + 2] + Math.sin(time * 1.0 + ph) * 2.5;
      }

      if (this.portraitMesh) this.portraitMesh.geometry.attributes.position.needsUpdate = true;
      if (this.ambientMesh) this.ambientMesh.geometry.attributes.position.needsUpdate = true;
    }

    // Smooth scroll dissolution interpolation
    if (!this.isEnteringWebsite && Math.abs(this.targetDissolveProgress - this.dissolveProgress) > 0.001) {
      const scrollLerp = this.isSnapshotMode ? 1.0 : 0.08;
      this.dissolveProgress += (this.targetDissolveProgress - this.dissolveProgress) * scrollLerp;
      this.setDissolveProgress(this.dissolveProgress);
    }

    // Slow, subtle, elegant cursor damping
    const lerpFactor = this.isSnapshotMode ? 1.0 : 0.040;
    this.mouse.x += (this.targetMouse.x - this.mouse.x) * lerpFactor;
    this.mouse.y += (this.targetMouse.y - this.mouse.y) * lerpFactor;

    // Attenuate cursor rotation as sculpture dissolves
    const rotAttenuation = Math.max(0.0, 1.0 - this.dissolveProgress * 2.2);

    if (this.sculptureGroup) {
      // Horizontal rotation: maximum approximately ±5 degrees (0.0872 rad)
      this.sculptureGroup.rotation.y = this.mouse.x * 0.0872 * rotAttenuation;
      // Vertical rotation: maximum approximately ±3 degrees (0.0523 rad)
      this.sculptureGroup.rotation.x = -this.mouse.y * 0.0523 * rotAttenuation;

      // Subtle parallax depth shift (strictly centered, no swinging)
      this.sculptureGroup.position.z = Math.abs(this.mouse.x) * 2.5 * rotAttenuation;
      this.sculptureGroup.position.x = this.mouse.x * 1.8 * rotAttenuation;
    }

    if (this.renderer && this.scene && this.camera) {
      this.renderer.render(this.scene, this.camera);
    }
  }

  destroy() {
    if (this.animationFrameId) {
      cancelAnimationFrame(this.animationFrameId);
    }
    window.removeEventListener('resize', this.boundResize);
    window.removeEventListener('mousemove', this.boundMouseMove);
    window.removeEventListener('mouseleave', this.boundMouseLeave);
    window.removeEventListener('touchmove', this.boundTouchMove);
    window.removeEventListener('touchend', this.boundTouchEnd);
    window.removeEventListener('wheel', this.boundWheel);
    window.removeEventListener('keydown', this.boundKeyDown);
  }
}

// Global initialization hook
window.ParticleSculptureIntro = ParticleSculptureIntro;
