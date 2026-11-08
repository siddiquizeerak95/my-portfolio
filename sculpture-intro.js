/**
 * =============================================================================
 * ZS STUDIO — DIGITAL UNIVERSE: SCENE 01 (THE AWAKENING)
 * Master Cinematic 3D Scroll-Driven WebGL Portfolio Opening Experience
 * 
 * Brand: ZS STUDIO | Name: ZEERAK SIDDIQUI | Website: zsstudio.netlify.app
 * Palette: #030305 (Deep Black Void), #E5092B (Pure Crimson Red),
 *          #790014 (Deep Red), #DCDCDC (Metallic Silver)
 * Strictly zero blue tints or gradients. Expansive monumental 3D architectural cosmos.
 * =============================================================================
 */

class DigitalUniverse {
  constructor(options = {}) {
    this.stage = document.getElementById('sculpture-intro-stage');
    this.canvas = document.getElementById('sculpture-canvas');
    this.welcomeBlock = document.getElementById('sculpture-welcome-block');
    this.topBar = document.querySelector('.universe-top-bar');
    this.brandTop = document.querySelector('.intro-brand-top-left');
    this.scrollIndicator = document.getElementById('intro-scroll-indicator');
    this.skipBtn = document.getElementById('btn-enter-website');
    this.onEnterCallback = options.onEnter || (() => {});

    this.scene = null;
    this.camera = null;
    this.renderer = null;

    // 3D Scene Components
    this.universeGroup = null;
    this.energySphereGroup = null;
    this.coreMesh = null;
    this.innerNuclearMesh = null;
    this.latticeMesh1 = null;
    this.latticeMesh2 = null;
    this.latticeMesh3 = null;
    this.haloSprite = null;
    this.swarmPoints = null;
    this.orbitalRings = [];
    this.architectureGroup = null;
    this.floatingStructures = [];
    this.starfieldPoints = null;
    this.stardustPoints = null;

    // Lighting
    this.crimsonLight = null;
    this.silverRimLight = null;
    this.deepRedFillLight = null;

    // Particle & Geometry Buffers
    this.stardustCount = 6000;
    this.stardustPositions = null;
    this.stardustOrigins = null;
    this.stardustScatter = null;

    this.starfieldCount = 4500;

    // Swarm particles around energy sphere
    this.swarmCount = 1200;
    this.swarmPositions = null;
    this.swarmAngles = null;
    this.swarmSpeeds = null;
    this.swarmRadii = null;
    this.swarmPhis = null;

    // Animation & Interactive State
    this.isReady = false;
    this.phase = 'loading'; // 'loading', 'active', 'transitioning', 'homepage'
    this.hasRevealedHomepage = false;
    this.awakeningProgress = 0.0;
    this.scrollProgress = 0.0;
    this.targetScrollProgress = 0.0;
    this.isSkipping = false;
    this.isSnapshotMode = false;

    // Camera Framing (Close, cinematic, majestic framing)
    this.baseCameraZ = 380;
    this.baseCameraY = 24;
    this.baseCameraX = -25;
    this.cameraFov = 46;

    // Dual-Axis Cursor Parallax
    this.mouse = { x: 0, y: 0 };
    this.targetMouse = { x: 0, y: 0 };
    this.animationFrameId = null;

    this.boundAnimate = this.animate.bind(this);
    this.boundResize = this.onResize.bind(this);
    this.boundMouseMove = this.onMouseMove.bind(this);
    this.boundMouseLeave = this.onMouseLeave.bind(this);
    this.boundTouchStart = this.onTouchStart.bind(this);
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

    // Three.js check
    if (typeof THREE === 'undefined') {
      console.warn('Three.js unavailable, falling back to static presentation.');
      this.stage.classList.add('no-webgl');
      this.setupFallbackEvents();
      return;
    }

    try {
      this.initThree();
      this.createDigitalUniverse();
      this.bindEvents();

      this.isReady = true;
      this.stage.classList.add('ready');

      // Test overrides
      if (urlParams.get('snap') === '1') {
        this.isSnapshotMode = true;
        this.stage.classList.add('snap-no-transition');
      }

      const testScroll = urlParams.get('scroll_progress');
      if (testScroll !== null) {
        const p = parseFloat(testScroll);
        this.phase = 'active';
        this.stage.classList.add('active');
        this.targetScrollProgress = p;
        this.scrollProgress = p;
        this.awakeningProgress = 1.0;
        this.updateScrollCinematics(p);
      } else {
        if (this.pendingFormation) {
          this.pendingFormation = false;
          this.startFormation();
        }
      }

      if (!this.animationFrameId) {
        this.animate();
      }
    } catch (err) {
      console.error('Digital Universe WebGL initialization error:', err);
      this.stage.classList.add('no-webgl');
      this.setupFallbackEvents();
    }
  }

  initThree() {
    const width = window.innerWidth;
    const height = window.innerHeight;

    // Pure deep black universe void (#030305, zero blue, calibrated atmospheric fog)
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0x030305);
    this.scene.fog = new THREE.FogExp2(0x030305, 0.00022);

    // Perspective Camera with dynamic depth of field
    this.camera = new THREE.PerspectiveCamera(this.cameraFov, width / height, 1, 4500);
    this.updateCameraFraming(width, height);

    // High Precision WebGL Renderer
    this.renderer = new THREE.WebGLRenderer({
      canvas: this.canvas,
      antialias: true,
      powerPreference: 'high-performance',
      alpha: false
    });
    this.renderer.setSize(width, height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    this.renderer.outputEncoding = THREE.LinearEncoding;

    // Root Master Universe Group
    this.universeGroup = new THREE.Group();
    this.scene.add(this.universeGroup);
  }

  /**
   * Delicate circular particle texture with soft anti-aliased edge
   */
  createDotTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 64;
    canvas.height = 64;
    const ctx = canvas.getContext('2d');

    const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 30);
    grad.addColorStop(0.0, 'rgba(255, 255, 255, 1.0)');
    grad.addColorStop(0.35, 'rgba(255, 255, 255, 0.85)');
    grad.addColorStop(0.70, 'rgba(255, 255, 255, 0.25)');
    grad.addColorStop(1.0, 'rgba(255, 255, 255, 0.0)');

    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 64, 64);
    return new THREE.CanvasTexture(canvas);
  }

  /**
   * Controlled Crimson Corona Halo Texture (Pure deep crimson #E5092B and #790014, zero pink/magenta)
   */
  createCrimsonHaloTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 128;
    canvas.height = 128;
    const ctx = canvas.getContext('2d');

    const grad = ctx.createRadialGradient(64, 64, 25, 64, 64, 63);
    grad.addColorStop(0.0, 'rgba(229, 9, 43, 0.28)');    // Primary Crimson Red #E5092B
    grad.addColorStop(0.48, 'rgba(121, 0, 20, 0.14)');   // Dark Red #790014
    grad.addColorStop(0.82, 'rgba(60, 0, 10, 0.03)');    // Deep Ruby Edge
    grad.addColorStop(1.0, 'rgba(3, 3, 5, 0.0)');        // Pure Black Void

    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 128, 128);
    return new THREE.CanvasTexture(canvas);
  }

  createDigitalUniverse() {
    const dotTex = this.createDotTexture();

    // -------------------------------------------------------------------------
    // 1. CINEMATIC DIRECTIONAL & PORTAL LIGHTING SYSTEM
    // -------------------------------------------------------------------------
    // Neutral deep space ambient revealing solid metallic architecture facets
    const ambientLight = new THREE.AmbientLight(0x18181A, 1.35);
    this.scene.add(ambientLight);

    // Primary Crimson Point Light at Center of Energy Singularity
    // Calibrated to 0xE50608 at intensity 1.8 to guarantee highlights stay strictly crimson-red without 8-bit clamping into magenta/pink
    this.crimsonLight = new THREE.PointLight(0xE50608, 1.8, 480, 1.35);
    this.crimsonLight.position.set(80, 36, -180);
    this.universeGroup.add(this.crimsonLight);

    // Deep Red Fill Light beneath the Grand Runway (Lowered well below deck to eliminate hotspot)
    this.deepRedFillLight = new THREE.PointLight(0x790008, 0.9, 600, 1.4);
    this.deepRedFillLight.position.set(0, -95, -160);
    this.universeGroup.add(this.deepRedFillLight);

    // Primary Crimson Directional Key Light (#E50608)
    this.crimsonKeyLight = new THREE.DirectionalLight(0xE50608, 1.0);
    this.crimsonKeyLight.position.set(160, 220, 260);
    this.scene.add(this.crimsonKeyLight);

    // Pure Metallic Silver Rim Light (#E0E4EC) picking up sharp specular architectural edges
    this.silverRimLight = new THREE.DirectionalLight(0xE0E4EC, 1.25);
    this.silverRimLight.position.set(-350, 500, 250);
    this.scene.add(this.silverRimLight);

    // Dimensional Gateway Portal Light (Deep Crimson #E50608 inside stargate arch)
    this.portalLight = new THREE.PointLight(0xE50608, 1.0, 420, 1.4);
    this.portalLight.position.set(0, 25, -380);
    this.universeGroup.add(this.portalLight);

    // -------------------------------------------------------------------------
    // 2. REALISTIC 3D MATERIALS (Physically Based Shading - Neutral Metallic Albedos)
    // -------------------------------------------------------------------------
    // Dark brushed obsidian titanium for megaliths, pylons and structural platforms
    const matTitanium = new THREE.MeshStandardMaterial({
      color: 0x222225,
      roughness: 0.46,
      metalness: 0.78
    });

    // Dark satin obsidian for promenade floor (soft diffuse sheen, no harsh bulb reflections)
    const matObsidian = new THREE.MeshStandardMaterial({
      color: 0x0A0A0C,
      roughness: 0.65,
      metalness: 0.25
    });

    // Heavy structural steel for mechanical gimbals
    const matDarkSteel = new THREE.MeshStandardMaterial({
      color: 0x1A1A1C,
      roughness: 0.48,
      metalness: 0.80
    });

    // Sleek metallic silver for architectural bevels, brackets and structural crowns
    const matChrome = new THREE.MeshStandardMaterial({
      color: 0xD4D4D8,
      roughness: 0.20,
      metalness: 0.95
    });

    // Recessed crimson illumination channels (#E50614)
    const matCrimsonGlow = new THREE.MeshBasicMaterial({
      color: 0xE50614
    });

    // Translucent celestial event horizon veil
    const matPortalVeil = new THREE.MeshBasicMaterial({
      color: 0x48000A,
      transparent: true,
      opacity: 0.18,
      side: THREE.DoubleSide
    });

    // -------------------------------------------------------------------------
    // 3. THE CRIMSON ENERGY CONSTRUCT (Integrated Energy Singularity Reactor)
    // -------------------------------------------------------------------------
    this.energySphereGroup = new THREE.Group();
    this.energySphereGroup.position.set(80, 36, -180);
    this.universeGroup.add(this.energySphereGroup);

    // 3a. Inner Incandescent Nuclear Core (Pure dark ruby #790014, zero white specular)
    const nuclearGeo = new THREE.SphereGeometry(18, 48, 48);
    const nuclearMat = new THREE.MeshBasicMaterial({ color: 0x790014 });
    this.innerNuclearMesh = new THREE.Mesh(nuclearGeo, nuclearMat);
    this.coreMesh = this.innerNuclearMesh;
    this.energySphereGroup.add(this.innerNuclearMesh);

    // 3b. Flowing Dynamic Plasma Mantle (Pure Crimson #E5092B, MeshLambertMaterial prevents specular blowout)
    const plasmaGeo = new THREE.IcosahedronGeometry(28, 4);
    this.plasmaOrigPositions = new Float32Array(plasmaGeo.attributes.position.array);
    const plasmaMat = new THREE.MeshLambertMaterial({
      color: 0xE50614,
      emissive: 0x440008,
      transparent: true,
      opacity: 0.94
    });
    this.plasmaMesh = new THREE.Mesh(plasmaGeo, plasmaMat);
    this.energySphereGroup.add(this.plasmaMesh);

    // 3c. Heavy Solid Metallic Armature Rings (Dimensional 3D Toruses with Armor Brackets)
    // Ring 1 (Equatorial): Heavy Titanium with 6 Armor Brackets and recessed crimson conduit
    const g1Group = new THREE.Group();
    const g1Torus = new THREE.Mesh(new THREE.TorusGeometry(38, 3.8, 16, 72), matTitanium);
    const g1Glow = new THREE.Mesh(new THREE.TorusGeometry(38, 1.2, 12, 72), matCrimsonGlow);
    g1Group.add(g1Torus, g1Glow);
    for (let b = 0; b < 6; b++) {
      const angle = (b / 6) * Math.PI * 2;
      const bracket = new THREE.Mesh(new THREE.BoxGeometry(8, 5, 11), matChrome);
      bracket.position.set(Math.cos(angle) * 38, Math.sin(angle) * 38, 0);
      bracket.rotation.z = angle;
      g1Group.add(bracket);
    }
    g1Group.rotation.x = Math.PI / 7;
    this.gimbal1 = g1Group;
    this.energySphereGroup.add(this.gimbal1);

    // Ring 2 (Polar Gyro, tilted 60°): Heavy Titanium with silver bevels & 4 counterweights
    const g2Group = new THREE.Group();
    const g2Torus = new THREE.Mesh(new THREE.TorusGeometry(48, 4.2, 16, 72), matTitanium);
    const g2Trim = new THREE.Mesh(new THREE.TorusGeometry(48, 1.2, 12, 72), matChrome);
    g2Group.add(g2Torus, g2Trim);
    for (let b = 0; b < 4; b++) {
      const angle = (b / 4) * Math.PI * 2;
      const weight = new THREE.Mesh(new THREE.BoxGeometry(11, 11, 13), matDarkSteel);
      weight.position.set(Math.cos(angle) * 48, Math.sin(angle) * 48, 0);
      weight.rotation.z = angle;
      g2Group.add(weight);
    }
    g2Group.rotation.z = Math.PI / 2.8;
    this.gimbal2 = g2Group;
    this.energySphereGroup.add(this.gimbal2);

    // Ring 3 (Oblique Outer Stator, tilted -38°): Heavy Structural Steel with 8 armor brackets & crimson emitters
    const g3Group = new THREE.Group();
    const g3Torus = new THREE.Mesh(new THREE.TorusGeometry(60, 3.5, 16, 72), matDarkSteel);
    g3Group.add(g3Torus);
    for (let b = 0; b < 8; b++) {
      const angle = (b / 8) * Math.PI * 2;
      const bracket = new THREE.Mesh(new THREE.BoxGeometry(8, 5, 10), matTitanium);
      bracket.position.set(Math.cos(angle) * 60, Math.sin(angle) * 60, 0);
      bracket.rotation.z = angle;
      const node = new THREE.Mesh(new THREE.BoxGeometry(4.5, 3.2, 11), matCrimsonGlow);
      node.position.set(Math.cos(angle) * 60, Math.sin(angle) * 60, 0);
      node.rotation.z = angle;
      g3Group.add(bracket, node);
    }
    g3Group.rotation.y = -Math.PI / 4.5;
    this.gimbal3 = g3Group;
    this.energySphereGroup.add(this.gimbal3);

    // 3d. Micro-Particle Accretion Belts (Thin, Crisp Planetary Rings)
    this.orbitalRings = [];
    this.orbitalRings.push(this.createOrbitalRing({
      radiusMin: 68, radiusMax: 80,
      count: 650,
      tiltX: 0.35, tiltZ: -0.20,
      speed: 0.0016,
      color: 0xE50614, size: 0.90,
      opacity: 0.75,
      dotTex
    }));

    this.orbitalRings.push(this.createOrbitalRing({
      radiusMin: 92, radiusMax: 108,
      count: 500,
      tiltX: -0.45, tiltZ: 0.38,
      speed: -0.0012,
      color: 0x790010, size: 0.80,
      opacity: 0.60,
      dotTex
    }));
    this.orbitalRings.forEach(ring => this.energySphereGroup.add(ring.group));

    // 3e. Fine Plasma Swarm Sparks (1,200 Micro-Particles hugging core)
    this.createEnergySwarm(dotTex);

    // -------------------------------------------------------------------------
    // 4. MONUMENTAL FUTURISTIC ARCHITECTURE (Solid 3D Geometry)
    // -------------------------------------------------------------------------
    this.architectureGroup = new THREE.Group();
    this.universeGroup.add(this.architectureGroup);
    this.floatingStructures = [];

    // 4a. Left Citadel Bastion (Foreground Monolith Tower, X: -130, Y: 10, Z: +20)
    const leftBastion = new THREE.Group();
    leftBastion.position.set(-130, 10, 20);
    const lbPylon = new THREE.Mesh(new THREE.BoxGeometry(45, 520, 65), matTitanium);
    const lbButtress = new THREE.Mesh(new THREE.BoxGeometry(65, 20, 55), matObsidian);
    lbButtress.position.set(12, 45, -5);
    const lbCrown = new THREE.Mesh(new THREE.BoxGeometry(49, 16, 69), matChrome);
    lbCrown.position.y = 268;
    const lbSlot = new THREE.Mesh(new THREE.BoxGeometry(2.5, 480, 2), matCrimsonGlow);
    lbSlot.position.set(0, 0, 33);
    leftBastion.add(lbPylon, lbButtress, lbCrown, lbSlot);
    leftBastion.rotation.y = 0.24;
    this.architectureGroup.add(leftBastion);
    this.floatingStructures.push({ group: leftBastion, basePos: { x: -130, y: 10, z: 20 }, speed: 0.0006, amp: 4.5 });

    // 4b. Right Sentinel Bastion (Foreground Obelisk Tower, X: 140, Y: -10, Z: 0)
    const rightBastion = new THREE.Group();
    rightBastion.position.set(140, -10, 0);
    const rbPylon = new THREE.Mesh(new THREE.BoxGeometry(40, 480, 60), matTitanium);
    const rbCantilever = new THREE.Mesh(new THREE.BoxGeometry(70, 22, 60), matObsidian);
    rbCantilever.position.set(-15, -80, 0);
    const rbCrown = new THREE.Mesh(new THREE.BoxGeometry(44, 16, 64), matChrome);
    rbCrown.position.y = 248;
    const rbSlot = new THREE.Mesh(new THREE.BoxGeometry(2.5, 440, 2), matCrimsonGlow);
    rbSlot.position.set(0, 0, 31);
    rightBastion.add(rbPylon, rbCantilever, rbCrown, rbSlot);
    rightBastion.rotation.y = -0.22;
    this.architectureGroup.add(rightBastion);
    this.floatingStructures.push({ group: rightBastion, basePos: { x: 140, y: -10, z: 0 }, speed: 0.0007, amp: 5.0 });

    // 4c. Grand Celestial Promenade (Runway extending into deep space, Y: -82, Z: -130)
    const runwayGroup = new THREE.Group();
    runwayGroup.position.set(0, -82, -130);
    const runwayDeck = new THREE.Mesh(new THREE.BoxGeometry(130, 16, 540), matObsidian);
    const runwayBase = new THREE.Mesh(new THREE.BoxGeometry(154, 12, 560), matTitanium);
    runwayBase.position.y = -14;
    const stripL = new THREE.Mesh(new THREE.BoxGeometry(2, 1.2, 530), matCrimsonGlow);
    stripL.position.set(-58, 8.5, 0);
    const stripR = new THREE.Mesh(new THREE.BoxGeometry(2, 1.2, 530), matCrimsonGlow);
    stripR.position.set(58, 8.5, 0);

    // Lateral cross terraces
    const terrace1 = new THREE.Mesh(new THREE.BoxGeometry(250, 12, 75), matTitanium);
    terrace1.position.set(0, -4, 50);
    const terrace2 = new THREE.Mesh(new THREE.BoxGeometry(230, 12, 65), matTitanium);
    terrace2.position.set(0, -4, -140);
    runwayGroup.add(runwayDeck, runwayBase, stripL, stripR, terrace1, terrace2);
    this.architectureGroup.add(runwayGroup);
    this.floatingStructures.push({ group: runwayGroup, basePos: { x: 0, y: -82, z: -130 }, speed: 0.0004, amp: 3.5 });

    // 4d. Overhead Framing Cantilever Sky-Bridge (X: 0, Y: 145, Z: -150)
    const overpassGroup = new THREE.Group();
    overpassGroup.position.set(0, 145, -150);
    const overpassDeck = new THREE.Mesh(new THREE.BoxGeometry(320, 18, 50), matTitanium);
    const overpassTrim = new THREE.Mesh(new THREE.BoxGeometry(322, 2.5, 4), matChrome);
    overpassTrim.position.set(0, -8.5, 25);
    const overpassSlot = new THREE.Mesh(new THREE.BoxGeometry(280, 1.5, 2), matCrimsonGlow);
    overpassSlot.position.set(0, 0, 26);
    overpassGroup.add(overpassDeck, overpassTrim, overpassSlot);
    this.architectureGroup.add(overpassGroup);
    this.floatingStructures.push({ group: overpassGroup, basePos: { x: 0, y: 145, z: -150 }, speed: 0.00055, amp: 4.5 });

    // 4e. Right Reactor Support Terrace (Beneath Energy Singularity, X: 80, Y: -44, Z: -180)
    const rightDeck = new THREE.Group();
    rightDeck.position.set(80, -44, -180);
    const rdMesh = new THREE.Mesh(new THREE.BoxGeometry(130, 16, 120), matTitanium);
    const rdFascia = new THREE.Mesh(new THREE.BoxGeometry(132, 2.5, 4), matChrome);
    rdFascia.position.set(0, 7.5, 59);
    const rdGlow = new THREE.Mesh(new THREE.BoxGeometry(120, 1.2, 2), matCrimsonGlow);
    rdGlow.position.set(0, 0, 60.5);
    rightDeck.add(rdMesh, rdFascia, rdGlow);
    rightDeck.rotation.y = -0.15;
    this.architectureGroup.add(rightDeck);
    this.floatingStructures.push({ group: rightDeck, basePos: { x: 80, y: -44, z: -180 }, speed: 0.0007, amp: 5.0 });

    // 4f. Floating Metallic Geometric Objects & Polyhedra (Rotating at various depths)
    const poly1 = new THREE.Mesh(new THREE.OctahedronGeometry(13, 0), matChrome);
    poly1.position.set(-150, 45, -80);
    this.architectureGroup.add(poly1);
    this.floatingStructures.push({ group: poly1, basePos: { x: -150, y: 45, z: -80 }, speed: 0.0008, amp: 5.0, rotSpeedY: 0.012, rotSpeedZ: 0.008 });

    const poly2 = new THREE.Mesh(new THREE.IcosahedronGeometry(12, 0), matTitanium);
    poly2.position.set(165, 15, -110);
    this.architectureGroup.add(poly2);
    this.floatingStructures.push({ group: poly2, basePos: { x: 165, y: 15, z: -110 }, speed: 0.0009, amp: 4.5, rotSpeedY: -0.010, rotSpeedZ: 0.014 });

    const poly3 = new THREE.Mesh(new THREE.DodecahedronGeometry(10, 0), matChrome);
    poly3.position.set(-100, -20, -240);
    this.architectureGroup.add(poly3);
    this.floatingStructures.push({ group: poly3, basePos: { x: -100, y: -20, z: -240 }, speed: 0.0007, amp: 6.0, rotSpeedY: 0.015, rotSpeedZ: -0.010 });

    // 4g. Midground Floating Bastions & Sentinel Spires
    const midBastionL = new THREE.Mesh(new THREE.BoxGeometry(110, 14, 90), matTitanium);
    midBastionL.position.set(-220, 65, -460);
    this.architectureGroup.add(midBastionL);
    this.floatingStructures.push({ group: midBastionL, basePos: { x: -220, y: 65, z: -460 }, speed: 0.0005, amp: 4.0 });

    const midBastionR = new THREE.Mesh(new THREE.BoxGeometry(120, 14, 100), matTitanium);
    midBastionR.position.set(230, -45, -540);
    this.architectureGroup.add(midBastionR);
    this.floatingStructures.push({ group: midBastionR, basePos: { x: 230, y: -45, z: -540 }, speed: 0.0006, amp: 4.5 });

    const spireL = new THREE.Mesh(new THREE.BoxGeometry(22, 280, 22), matTitanium);
    spireL.position.set(-190, -10, -360);
    this.architectureGroup.add(spireL);
    this.floatingStructures.push({ group: spireL, basePos: { x: -190, y: -10, z: -360 }, speed: 0.0004, amp: 3.5 });

    const spireR = new THREE.Mesh(new THREE.BoxGeometry(20, 260, 20), matTitanium);
    spireR.position.set(210, 85, -420);
    this.architectureGroup.add(spireR);
    this.floatingStructures.push({ group: spireR, basePos: { x: 210, y: 85, z: -420 }, speed: 0.00045, amp: 3.5 });

    // 4h. Massive Dimensional Stargate Portal (Substantial 3D Volume & Thickness, Z: -380)
    const stargateGroup = new THREE.Group();
    stargateGroup.position.set(0, 25, -380);
    const gateW = 340, gateH = 360, colW = 50, colD = 70;

    const colLeft = new THREE.Mesh(new THREE.BoxGeometry(colW, gateH, colD), matTitanium);
    colLeft.position.set(-gateW / 2 + colW / 2, 0, 0);
    const colLeftTrim = new THREE.Mesh(new THREE.BoxGeometry(6, gateH - 40, colD + 4), matChrome);
    colLeftTrim.position.set(-gateW / 2 + colW + 3, 0, 0);

    const colRight = new THREE.Mesh(new THREE.BoxGeometry(colW, gateH, colD), matTitanium);
    colRight.position.set(gateW / 2 - colW / 2, 0, 0);
    const colRightTrim = new THREE.Mesh(new THREE.BoxGeometry(6, gateH - 40, colD + 4), matChrome);
    colRightTrim.position.set(gateW / 2 - colW - 3, 0, 0);

    const topLintel = new THREE.Mesh(new THREE.BoxGeometry(gateW + 60, 56, colD + 12), matTitanium);
    topLintel.position.set(0, gateH / 2, 0);
    const topTrim = new THREE.Mesh(new THREE.BoxGeometry(gateW + 64, 6, colD + 14), matChrome);
    topTrim.position.set(0, gateH / 2 + 30, 0);

    const basePedestal = new THREE.Mesh(new THREE.BoxGeometry(gateW + 80, 40, colD + 25), matTitanium);
    basePedestal.position.set(0, -gateH / 2, 0);

    // Embedded Heavy Circular Stargate Ring (Thickness 11 units!)
    const stargateRing = new THREE.Mesh(new THREE.TorusGeometry(140, 11, 16, 96), matTitanium);
    const stargateRingGlow = new THREE.Mesh(new THREE.TorusGeometry(138, 2.2, 12, 96), matCrimsonGlow);
    const portalVeil = new THREE.Mesh(new THREE.PlaneGeometry(260, 290), matPortalVeil);

    // 3D ZS Monogram Insignia Crest mounted on Stargate Lintel
    const zsMonogram = new THREE.Group();
    zsMonogram.position.set(0, gateH / 2, colD / 2 + 5);

    // Letter 'Z' (Top bar, diagonal bar, bottom bar)
    const zGroup = new THREE.Group();
    zGroup.position.set(-16, 0, 0);
    const zTop = new THREE.Mesh(new THREE.BoxGeometry(22, 3.5, 3), matChrome);
    zTop.position.set(0, 11, 0);
    const zDiag = new THREE.Mesh(new THREE.BoxGeometry(25, 3.5, 3), matChrome);
    zDiag.rotation.z = -0.785;
    const zBot = new THREE.Mesh(new THREE.BoxGeometry(22, 3.5, 3), matChrome);
    zBot.position.set(0, -11, 0);
    zGroup.add(zTop, zDiag, zBot);

    // Letter 'S' (Top bar, upper stem, mid bar, lower stem, bot bar)
    const sGroup = new THREE.Group();
    sGroup.position.set(16, 0, 0);
    const sTop = new THREE.Mesh(new THREE.BoxGeometry(20, 3.5, 3), matChrome);
    sTop.position.set(0, 11, 0);
    const sStemU = new THREE.Mesh(new THREE.BoxGeometry(3.5, 9, 3), matChrome);
    sStemU.position.set(-8.25, 6, 0);
    const sMid = new THREE.Mesh(new THREE.BoxGeometry(18, 3.5, 3), matChrome);
    sMid.position.set(0, 0, 0);
    const sStemL = new THREE.Mesh(new THREE.BoxGeometry(3.5, 9, 3), matChrome);
    sStemL.position.set(8.25, -6, 0);
    const sBot = new THREE.Mesh(new THREE.BoxGeometry(20, 3.5, 3), matChrome);
    sBot.position.set(0, -11, 0);
    sGroup.add(sTop, sStemU, sMid, sStemL, sBot);

    // Monogram Titanium Backing Crest with Crimson Edge Trim
    const crestPlate = new THREE.Mesh(new THREE.BoxGeometry(70, 36, 1.5), matTitanium);
    crestPlate.position.set(0, 0, -1.5);
    const crestTrim = new THREE.Mesh(new THREE.BoxGeometry(72, 1.5, 2), matCrimsonGlow);
    crestTrim.position.set(0, -18, 0);
    zsMonogram.add(zGroup, sGroup, crestPlate, crestTrim);

    stargateGroup.add(colLeft, colLeftTrim, colRight, colRightTrim, topLintel, topTrim, basePedestal, stargateRing, stargateRingGlow, portalVeil, zsMonogram);
    this.architectureGroup.add(stargateGroup);
    this.floatingStructures.push({ group: stargateGroup, basePos: { x: 0, y: 25, z: -380 }, speed: 0.0003, amp: 3.5 });

    // 4i. Secondary Distant Portal Arch (Z = -750)
    const distGateGroup = new THREE.Group();
    distGateGroup.position.set(0, 35, -750);
    const dgRing = new THREE.Mesh(new THREE.TorusGeometry(200, 8, 16, 72), matTitanium);
    distGateGroup.add(dgRing);
    this.architectureGroup.add(distGateGroup);
    this.floatingStructures.push({ group: distGateGroup, basePos: { x: 0, y: 35, z: -750 }, speed: 0.0002, amp: 4.0 });

    // 4j. Colossal Deep Space Orbital Megastructure Ring (Z = -1100)
    const ringGeo = new THREE.TorusGeometry(500, 14, 16, 120);
    const celestialRing = new THREE.Mesh(ringGeo, matTitanium);
    celestialRing.position.set(0, 60, -1100);
    celestialRing.rotation.x = Math.PI / 4.2;
    this.architectureGroup.add(celestialRing);
    this.floatingStructures.push({
      group: celestialRing,
      basePos: { x: 0, y: 60, z: -1100 },
      speed: 0.00015,
      amp: 5.0,
      rotSpeedZ: 0.0003
    });

    // 4k. Deep Space Cosmic Sentinel Monoliths (Z = -1350)
    const sentinelGeo = new THREE.BoxGeometry(60, 1000, 60);
    const sentinelL = new THREE.Mesh(sentinelGeo, matTitanium);
    sentinelL.position.set(-520, 0, -1350);
    sentinelL.rotation.y = 0.40;
    const sentinelR = new THREE.Mesh(sentinelGeo, matTitanium);
    sentinelR.position.set(520, 0, -1350);
    sentinelR.rotation.y = -0.40;
    this.architectureGroup.add(sentinelL, sentinelR);
    this.floatingStructures.push(
      { group: sentinelL, basePos: { x: -520, y: 0, z: -1350 }, speed: 0.00015, amp: 3.5 },
      { group: sentinelR, basePos: { x: 520, y: 0, z: -1350 }, speed: 0.00015, amp: 3.5 }
    );

    // -------------------------------------------------------------------------
    // 5. DISTANT PINPOINT COSMIC STARFIELD (6,000 Stars)
    // -------------------------------------------------------------------------
    this.createDistantStarfield(dotTex);

    // -------------------------------------------------------------------------
    // 6. MIDGROUND STARDUST PARTICLE FIELD (4,000 Fine Particles)
    // -------------------------------------------------------------------------
    this.createStardustField(dotTex);
  }

  /**
   * Surface plasma swarm particles orbiting around the sphere (1,200 sparks)
   */
  createEnergySwarm(dotTex) {
    const count = this.swarmCount;
    const geo = new THREE.BufferGeometry();
    const pos = new Float32Array(count * 3);
    const col = new Float32Array(count * 3);

    this.swarmPositions = pos;
    this.swarmAngles = new Float32Array(count);
    this.swarmSpeeds = new Float32Array(count);
    this.swarmRadii = new Float32Array(count);
    this.swarmPhis = new Float32Array(count);

    const cCrimson = new THREE.Color(0xE5092B);   // Primary Deep Crimson #E5092B
    const cDarkRed = new THREE.Color(0x790014);   // Dark Red #790014
    const cWhite = new THREE.Color(0xF5F5F7);     // Subtle White Highlights #F5F5F7

    for (let i = 0; i < count; i++) {
      const i3 = i * 3;
      const r = 34 + Math.random() * 16;
      const theta = Math.random() * Math.PI * 2;
      const phi = (Math.random() - 0.5) * Math.PI;

      this.swarmRadii[i] = r;
      this.swarmAngles[i] = theta;
      this.swarmPhis[i] = phi;
      this.swarmSpeeds[i] = 0.012 + Math.random() * 0.020;

      pos[i3] = Math.cos(phi) * Math.cos(theta) * r;
      pos[i3 + 1] = Math.sin(phi) * r;
      pos[i3 + 2] = Math.cos(phi) * Math.sin(theta) * r;

      const rand = Math.random();
      const color = rand > 0.35 ? cCrimson : (rand > 0.08 ? cDarkRed : cWhite);
      col[i3] = color.r;
      col[i3 + 1] = color.g;
      col[i3 + 2] = color.b;
    }

    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    geo.setAttribute('color', new THREE.BufferAttribute(col, 3));

    const mat = new THREE.PointsMaterial({
      size: 1.05,
      map: dotTex,
      vertexColors: true,
      transparent: true,
      opacity: 0.85,
      blending: THREE.NormalBlending,
      depthWrite: false
    });

    this.swarmPoints = new THREE.Points(geo, mat);
    this.energySphereGroup.add(this.swarmPoints);
  }

  /**
   * Distant 3D starry backdrop: 4,500 subtle, sharp stars
   */
  createDistantStarfield(dotTex) {
    const count = this.starfieldCount;
    const geo = new THREE.BufferGeometry();
    const pos = new Float32Array(count * 3);
    const col = new Float32Array(count * 3);

    const cWhite = new THREE.Color(0xDCDCDC);
    const cRuby = new THREE.Color(0x790014);

    for (let i = 0; i < count; i++) {
      const i3 = i * 3;
      pos[i3] = (Math.random() - 0.5) * 4200;
      pos[i3 + 1] = (Math.random() - 0.5) * 3200;
      pos[i3 + 2] = -320 - Math.random() * 2400; // Z from -320 to -2720

      const rand = Math.random();
      const starCol = rand > 0.88 ? cRuby : cWhite;
      const brightness = 0.32 + Math.random() * 0.60;
      col[i3] = starCol.r * brightness;
      col[i3 + 1] = starCol.g * brightness;
      col[i3 + 2] = starCol.b * brightness;
    }

    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    geo.setAttribute('color', new THREE.BufferAttribute(col, 3));

    const mat = new THREE.PointsMaterial({
      size: 1.35,
      map: dotTex,
      vertexColors: true,
      transparent: true,
      opacity: 0.82,
      depthWrite: false
    });

    this.starfieldPoints = new THREE.Points(geo, mat);
    this.universeGroup.add(this.starfieldPoints);
  }

  /**
   * Midground Stardust with initial Awakening assembly animation (6,000 particles)
   */
  createStardustField(dotTex) {
    const count = this.stardustCount;
    const positions = new Float32Array(count * 3);
    const origins = new Float32Array(count * 3);
    const scatter = new Float32Array(count * 3);
    const colors = new Float32Array(count * 3);

    const colSilver = new THREE.Color(0xDCDCDC);
    const colCrimson = new THREE.Color(0xE5092B);
    const colDeepRed = new THREE.Color(0x790014);

    for (let i = 0; i < count; i++) {
      const i3 = i * 3;
      const ox = (Math.random() - 0.5) * 1800;
      const oy = (Math.random() - 0.5) * 1300;
      const oz = (Math.random() - 0.5) * 1500 - 80;

      origins[i3] = ox;
      origins[i3 + 1] = oy;
      origins[i3 + 2] = oz;

      // Dispersed void scatter offsets for Scene 01 "The Awakening"
      const theta = Math.random() * Math.PI * 2;
      const phi = (Math.random() - 0.5) * Math.PI;
      const r = 280 + Math.random() * 550;
      scatter[i3] = Math.cos(phi) * Math.cos(theta) * r;
      scatter[i3 + 1] = Math.sin(phi) * r * 1.1;
      scatter[i3 + 2] = Math.cos(phi) * Math.sin(theta) * r;

      positions[i3] = ox;
      positions[i3 + 1] = oy;
      positions[i3 + 2] = oz;

      const rand = Math.random();
      const col = rand > 0.35 ? colCrimson : (rand > 0.08 ? colDeepRed : colSilver);
      colors[i3] = col.r;
      colors[i3 + 1] = col.g;
      colors[i3 + 2] = col.b;
    }

    this.stardustPositions = positions;
    this.stardustOrigins = origins;
    this.stardustScatter = scatter;

    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geo.setAttribute('color', new THREE.BufferAttribute(colors, 3));

    const mat = new THREE.PointsMaterial({
      size: 1.15,
      map: dotTex,
      vertexColors: true,
      transparent: true,
      opacity: 0.75,
      blending: THREE.NormalBlending,
      depthWrite: false
    });

    this.stardustPoints = new THREE.Points(geo, mat);
    this.universeGroup.add(this.stardustPoints);
  }

  createOrbitalRing({ radiusMin, radiusMax, count, tiltX, tiltZ, speed, color, size, opacity = 0.85, dotTex }) {
    const group = new THREE.Group();
    group.rotation.x = tiltX;
    group.rotation.z = tiltZ;

    const geo = new THREE.BufferGeometry();
    const pos = new Float32Array(count * 3);
    const angles = new Float32Array(count);
    const radii = new Float32Array(count);
    const heights = new Float32Array(count);

    for (let i = 0; i < count; i++) {
      const a = Math.random() * Math.PI * 2;
      const r = radiusMin + Math.random() * (radiusMax - radiusMin);
      const h = (Math.random() - 0.5) * 4.5;

      angles[i] = a;
      radii[i] = r;
      heights[i] = h;

      pos[i * 3] = Math.cos(a) * r;
      pos[i * 3 + 1] = h;
      pos[i * 3 + 2] = Math.sin(a) * r;
    }

    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));

    const mat = new THREE.PointsMaterial({
      size,
      map: dotTex,
      color,
      transparent: true,
      opacity,
      blending: THREE.NormalBlending,
      depthWrite: false
    });

    const points = new THREE.Points(geo, mat);
    group.add(points);

    return { group, points, angles, radii, heights, speed, count };
  }

  updateCameraFraming(width, height) {
    if (!this.camera) return;
    const aspect = width / height;
    this.camera.aspect = aspect;

    // Establishing vantage point: wide, epic cinematic framing down the promenade runway
    let baseZ = 320;
    let baseY = 24;
    let baseX = 0;
    if (width <= 480 || aspect < 0.6) {
      baseZ = 420;
      baseY = 28;
      baseX = 0;
    } else if (width <= 768) {
      baseZ = 380;
      baseY = 26;
      baseX = 0;
    } else if (width <= 1280) {
      baseZ = 340;
      baseY = 24;
      baseX = 0;
    }

    this.baseCameraZ = baseZ;
    this.baseCameraY = baseY;
    this.baseCameraX = baseX;
    this.camera.position.set(baseX, baseY, baseZ);
    this.camera.lookAt(0, 5, -180);
    this.camera.updateProjectionMatrix();
  }

  startFormation() {
    if (!this.isReady) {
      this.pendingFormation = true;
      return;
    }

    this.phase = 'active';
    this.stage.classList.add('active');
    document.body.style.overflow = 'hidden';
    this.onResize();

    // SCENE 01: THE AWAKENING ANIMATION
    if (!this.isSnapshotMode && typeof gsap !== 'undefined') {
      this.awakeningProgress = 0.0;
      gsap.to(this, {
        awakeningProgress: 1.0,
        duration: 2.2,
        ease: 'power2.out',
        onComplete: () => {
          this.awakeningProgress = 1.0;
        }
      });

      if (this.welcomeBlock) {
        this.welcomeBlock.classList.add('visible');
        gsap.fromTo(this.welcomeBlock,
          { opacity: 0, y: 16 },
          { opacity: 1, y: 0, duration: 0.85, ease: 'power2.out', delay: 0.25 }
        );
      }
    } else {
      this.awakeningProgress = 1.0;
      if (this.welcomeBlock) this.welcomeBlock.classList.add('visible');
    }

    this.setScrollProgress(0.0);
  }

  setScrollProgress(progress) {
    this.scrollProgress = Math.min(1.0, Math.max(0.0, progress));
    const p = this.scrollProgress;
    this.updateScrollCinematics(p);
  }

  updateScrollCinematics(p) {
    // 1. Cinematic 3D Camera Flight through the environment (NOT zooming into the sphere!)
    if (this.camera && this.baseCameraZ !== undefined) {
      let targetX, targetY;
      if (p < 0.35) {
        // Drift gently along the promenade, viewing the singularity on the right
        const t = p / 0.35;
        targetX = (this.baseCameraX || 0.0) + t * 18.0;
        targetY = (this.baseCameraY || 24.0) - t * 6.0;
      } else if (p < 0.70) {
        // Bank back under the cantilever sky-bridge
        const t = (p - 0.35) / 0.35;
        targetX = 18.0 - t * 32.0;
        targetY = 18.0 - t * 6.0;
      } else {
        // Align centered directly through the Stargate Portal Arch (Z = -350)
        const t = (p - 0.70) / 0.30;
        targetX = -14.0 + t * 14.0;
        targetY = 12.0 - t * 4.0;
      }
      // Camera travels from baseCameraZ down straight through Stargate Portal (Z = -380)
      const targetZ = this.baseCameraZ - p * 710.0;

      this.currentCamZ = targetZ;
      this.currentCamY = targetY;
      this.currentCamX = targetX;
    }

    // 2. Controlled energy sphere radiance (Zero artificial zooming - real 3D perspective!)
    if (this.energySphereGroup) {
      this.energySphereGroup.scale.set(1.0, 1.0, 1.0);
      if (this.crimsonLight) {
        this.crimsonLight.intensity = 1.8 + p * 0.35;
      }
    }

    // 3. UI Typography Opacity Falloff (fades out smoothly between p = 0.0 and 0.28)
    const uiAlpha = Math.max(0.0, 1.0 - p / 0.28);
    if (this.welcomeBlock) this.welcomeBlock.style.opacity = uiAlpha;
    if (this.scrollIndicator) this.scrollIndicator.style.opacity = uiAlpha;

    // Top Bar & Skip Button Falloff as entering the portal (p: 0.70 -> 0.85)
    const topBarAlpha = Math.max(0.0, 1.0 - Math.max(0, p - 0.70) / 0.15);
    if (this.topBar) this.topBar.style.opacity = topBarAlpha;

    // 4. Smooth Transition into Homepage as camera passes event horizon (p >= 0.85)
    if (p >= 0.85) {
      const exitProgress = (p - 0.85) / 0.11; // 0.0 -> 1.0
      const exitAlpha = Math.max(0.0, 1.0 - exitProgress);
      this.stage.style.opacity = exitAlpha.toFixed(3);

      if (p >= 0.96) {
        this.completeHomepageReveal();
      } else {
        this.stage.style.display = 'block';
        this.stage.style.pointerEvents = 'auto';
        document.body.style.overflow = 'hidden';
      }
    } else {
      this.stage.style.opacity = '1.0';
      this.stage.style.display = 'block';
      this.stage.style.pointerEvents = 'auto';
      document.body.style.overflow = 'hidden';
    }
  }

  completeHomepageReveal() {
    this.stage.style.opacity = '0';
    this.stage.style.pointerEvents = 'none';
    this.stage.style.visibility = 'hidden';
    this.stage.classList.add('intro-dismissed');
    document.body.style.overflow = '';

    if (!this.hasRevealedHomepage) {
      this.hasRevealedHomepage = true;
      this.phase = 'homepage';
      this.onEnterCallback();
    }
  }

  /**
   * Smooth reverse transition: restores the Digital Universe from homepage
   */
  reactivateIntro() {
    this.stage.style.display = 'block';
    this.stage.style.visibility = 'visible';
    this.stage.style.pointerEvents = 'auto';
    this.stage.classList.remove('intro-dismissed');
    document.body.style.overflow = 'hidden';
    this.phase = 'active';
    if (this.topBar) this.topBar.style.opacity = '1';
  }

  triggerEnterDissolution() {
    if (this.isSkipping) return;
    this.isSkipping = true;

    this.stage.classList.add('smooth-fade');

    // Seamless camera fly-through directly into website
    if (typeof gsap !== 'undefined' && !this.isSnapshotMode) {
      gsap.to(this, {
        targetScrollProgress: 1.0,
        scrollProgress: 1.0,
        duration: 0.85,
        ease: 'power2.inOut',
        onUpdate: () => {
          this.setScrollProgress(this.scrollProgress);
        },
        onComplete: () => {
          this.completeHomepageReveal();
          this.stage.classList.remove('smooth-fade');
          this.isSkipping = false;
        }
      });
    } else {
      this.setScrollProgress(1.0);
      this.completeHomepageReveal();
      this.stage.classList.remove('smooth-fade');
      this.isSkipping = false;
    }
  }

  dismissImmediately() {
    this.hasRevealedHomepage = true;
    this.phase = 'homepage';
    document.body.style.overflow = '';

    if (this.stage) {
      this.stage.classList.add('intro-dismissed');
      this.stage.style.display = 'none';
      this.stage.style.opacity = '0';
      this.stage.style.pointerEvents = 'none';
    }
    this.onEnterCallback();
  }

  bindEvents() {
    window.addEventListener('resize', this.boundResize);
    window.addEventListener('mousemove', this.boundMouseMove);
    window.addEventListener('mouseleave', this.boundMouseLeave);
    window.addEventListener('touchstart', this.boundTouchStart, { passive: true });
    window.addEventListener('touchmove', this.boundTouchMove, { passive: false });
    window.addEventListener('touchend', this.boundTouchEnd);
    window.addEventListener('keydown', this.boundKeyDown);
    window.addEventListener('wheel', this.boundWheel, { passive: false });

    if (this.skipBtn) {
      this.skipBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        this.triggerEnterDissolution();
      });
    }
  }

  setupFallbackEvents() {
    if (this.skipBtn) {
      this.skipBtn.addEventListener('click', (e) => {
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

  onTouchStart(e) {
    if (e.target && e.target.closest('#site-header, #mobile-drawer')) return;
    if (e.touches && e.touches[0]) {
      this.lastTouchY = e.touches[0].clientY;
    }
  }

  onTouchMove(e) {
    if (e.target && e.target.closest('#site-header, #mobile-drawer')) return;
    if (!e.touches || !e.touches[0]) return;
    const currentY = e.touches[0].clientY;

    const halfW = window.innerWidth / 2;
    const halfH = window.innerHeight / 2;
    this.targetMouse.x = ((e.touches[0].clientX - halfW) / halfW) * 0.65;
    this.targetMouse.y = ((e.touches[0].clientY - halfH) / halfH) * 0.65;

    if (this.lastTouchY !== undefined) {
      const deltaY = this.lastTouchY - currentY;

      // Inside 3D Digital Universe
      if (this.scrollProgress < 0.96) {
        e.preventDefault();
        this.targetScrollProgress += deltaY * 0.0012;
        this.targetScrollProgress = Math.min(1.0, Math.max(0.0, this.targetScrollProgress));
      } else {
        // On Homepage: if at very top and pulling down, reactivate Digital Universe
        if (window.scrollY <= 2 && deltaY < 0) {
          e.preventDefault();
          this.reactivateIntro();
          this.targetScrollProgress = Math.max(0.0, this.targetScrollProgress + deltaY * 0.0012);
        }
      }
    }
    this.lastTouchY = currentY;
  }

  onTouchEnd(e) {
    if (e && e.target && e.target.closest('#site-header, #mobile-drawer')) return;
    this.targetMouse.x = 0;
    this.targetMouse.y = 0;
    this.lastTouchY = undefined;
  }

  onWheel(e) {
    // Case 1: In the Digital Universe (scrollProgress < 0.96)
    if (this.scrollProgress < 0.96) {
      e.preventDefault();
      const delta = e.deltaY;
      this.targetScrollProgress += delta * 0.00045;
      this.targetScrollProgress = Math.min(1.0, Math.max(0.0, this.targetScrollProgress));
      return;
    }

    // Case 2: On the Homepage (scrollProgress >= 0.96)
    if (window.scrollY > 2) {
      return;
    }

    // If at top of homepage (scrollY <= 2) and scrolling UP, smoothly reverse into Digital Universe!
    if (e.deltaY < 0) {
      e.preventDefault();
      this.reactivateIntro();
      this.targetScrollProgress = Math.max(0.0, this.targetScrollProgress + e.deltaY * 0.00045);
    }
  }

  onKeyDown(e) {
    if ((e.key === 'Enter' || e.key === ' ' || e.key === 'Escape') && this.scrollProgress < 0.96) {
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
      this.updateCameraFraming(width, height);
    }

    if (this.renderer) {
      this.renderer.setSize(width, height);
      this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    }
  }

  animate() {
    this.animationFrameId = requestAnimationFrame(this.boundAnimate);
    const now = performance.now();
    const time = now * 0.001;

    // 1. Smooth Scroll Interpolation (Lerp)
    if (!this.isSkipping && Math.abs(this.targetScrollProgress - this.scrollProgress) > 0.0005) {
      const scrollLerp = this.isSnapshotMode ? 1.0 : 0.07;
      this.scrollProgress += (this.targetScrollProgress - this.scrollProgress) * scrollLerp;
      this.setScrollProgress(this.scrollProgress);
    }

    // 2. Smooth Cursor Damping (Parallax)
    const mouseLerp = this.isSnapshotMode ? 1.0 : 0.045;
    this.mouse.x += (this.targetMouse.x - this.mouse.x) * mouseLerp;
    this.mouse.y += (this.targetMouse.y - this.mouse.y) * mouseLerp;

    // 3. Stardust "Awakening" Assembly & Continuous Cosmic Drift (6,000 particles)
    if (this.stardustPoints && this.stardustPositions) {
      const pos = this.stardustPositions;
      const orig = this.stardustOrigins;
      const scat = this.stardustScatter;
      const count = this.stardustCount;
      const scatterFactor = 1.0 - this.awakeningProgress;

      for (let i = 0; i < count; i++) {
        const i3 = i * 3;
        const driftY = Math.sin(time * 0.35 + i * 0.05) * 2.5;
        const driftX = Math.cos(time * 0.28 + i * 0.04) * 2.0;

        pos[i3] = orig[i3] + driftX + scat[i3] * scatterFactor;
        pos[i3 + 1] = orig[i3 + 1] + driftY + scat[i3 + 1] * scatterFactor;
        pos[i3 + 2] = orig[i3 + 2] + scat[i3 + 2] * scatterFactor;
      }
      this.stardustPoints.geometry.attributes.position.needsUpdate = true;
    }

    // 4. Subtle Distant Starfield Shimmer (4,500 stars)
    if (this.starfieldPoints) {
      this.starfieldPoints.rotation.y = time * 0.00015;
    }

    // 5. Flowing Dynamic Plasma Shell Surface Wave Displacement
    if (this.plasmaMesh && this.plasmaOrigPositions) {
      const plasPos = this.plasmaMesh.geometry.attributes.position.array;
      const origPos = this.plasmaOrigPositions;
      const vCount = origPos.length / 3;

      for (let i = 0; i < vCount; i++) {
        const i3 = i * 3;
        const ox = origPos[i3];
        const oy = origPos[i3 + 1];
        const oz = origPos[i3 + 2];

        const dist = Math.sqrt(ox * ox + oy * oy + oz * oz);
        const wave = Math.sin(time * 3.0 + oy * 0.16 + ox * 0.12) * Math.cos(time * 2.2 + oz * 0.14) * 3.5;
        const scale = (dist + wave) / dist;

        plasPos[i3] = ox * scale;
        plasPos[i3 + 1] = oy * scale;
        plasPos[i3 + 2] = oz * scale;
      }
      this.plasmaMesh.geometry.attributes.position.needsUpdate = true;
      this.plasmaMesh.rotation.y = time * 0.18;
      this.plasmaMesh.rotation.x = time * 0.12;
    }

    // 6. Solid Metallic Armature Rings Independent Multi-Axis Rotations
    if (this.gimbal1) {
      this.gimbal1.rotation.z = time * 0.22;
      this.gimbal1.rotation.y = time * 0.14;
    }
    if (this.gimbal2) {
      this.gimbal2.rotation.x = -time * 0.20;
      this.gimbal2.rotation.y = time * 0.26;
    }
    if (this.gimbal3) {
      this.gimbal3.rotation.z = -time * 0.16;
      this.gimbal3.rotation.x = time * 0.18;
    }

    // 7. Inner Nuclear Core Breathing Pulse & Slow Rotation
    if (this.coreMesh) {
      this.coreMesh.rotation.y = -time * 0.30;
      const corePulse = 1.0 + Math.sin(time * 2.2) * 0.03;
      this.coreMesh.scale.set(corePulse, corePulse, corePulse);
    }

    // 8. Surface Plasma Swarm Particles Orbiting Core (1,200 sparks)
    if (this.swarmPoints && this.swarmPositions) {
      const pos = this.swarmPositions;
      const angles = this.swarmAngles;
      const phis = this.swarmPhis;
      const radii = this.swarmRadii;
      const speeds = this.swarmSpeeds;
      const count = this.swarmCount;

      for (let i = 0; i < count; i++) {
        const i3 = i * 3;
        angles[i] += speeds[i];
        const r = radii[i] + Math.sin(time * 2.6 + i) * 1.8;
        const phi = phis[i] + Math.cos(time * 1.3 + i * 0.5) * 0.14;

        pos[i3] = Math.cos(phi) * Math.cos(angles[i]) * r;
        pos[i3 + 1] = Math.sin(phi) * r;
        pos[i3 + 2] = Math.cos(phi) * Math.sin(angles[i]) * r;
      }
      this.swarmPoints.geometry.attributes.position.needsUpdate = true;
    }

    // 9. Accretion Belt Particle Rings Rotation
    if (this.orbitalRings && this.orbitalRings.length > 0) {
      this.orbitalRings.forEach(ring => {
        ring.points.rotation.y += ring.speed * 2.0;
      });
    }

    // 10. Floating 3D Architectural Monoliths & Platforms (Harmonic Zero-Gravity Levitation)
    if (this.floatingStructures && this.floatingStructures.length > 0) {
      this.floatingStructures.forEach(struct => {
        const bp = struct.basePos;
        struct.group.position.y = bp.y + Math.sin(time * struct.speed * 1000) * struct.amp;
        if (struct.rotSpeedY) {
          struct.group.rotation.y += struct.rotSpeedY;
        }
        if (struct.rotSpeedZ) {
          struct.group.rotation.z += struct.rotSpeedZ;
        }
      });
    }

    // 11. Camera Cinematic 3D Flight & Dual-Axis Cursor Parallax
    if (this.camera) {
      const targetZ = this.currentCamZ !== undefined ? this.currentCamZ : this.baseCameraZ;
      const targetY = this.currentCamY !== undefined ? this.currentCamY : this.baseCameraY;
      const targetX = this.currentCamX !== undefined ? this.currentCamX : (this.baseCameraX || 0);

      this.camera.position.x = targetX + this.mouse.x * 16.0;
      this.camera.position.y = targetY - this.mouse.y * 9.0;
      this.camera.position.z = targetZ;

      // Dynamic look target: smooth flight gaze tracking down the runway into the Stargate
      const p = this.scrollProgress || 0.0;
      let lookTargetX, lookTargetY, lookTargetZ;
      if (p < 0.40) {
        lookTargetX = 14.0 - p * 20.0;
        lookTargetY = 8.0 - p * 4.0;
        lookTargetZ = -140.0 - p * 160.0;
      } else {
        const t = (p - 0.40) / 0.60;
        lookTargetX = 6.0 * (1.0 - t);
        lookTargetY = 6.4 + t * 18.6;
        lookTargetZ = -204.0 - t * 296.0;
      }
      this.camera.lookAt(lookTargetX - this.mouse.x * 8.0, lookTargetY + this.mouse.y * 6.0, lookTargetZ);
    }

    // Render WebGL frame
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
    window.removeEventListener('touchstart', this.boundTouchStart);
    window.removeEventListener('touchmove', this.boundTouchMove);
    window.removeEventListener('touchend', this.boundTouchEnd);
    window.removeEventListener('wheel', this.boundWheel);
    window.removeEventListener('keydown', this.boundKeyDown);

    if (this.renderer) {
      this.renderer.dispose();
    }
  }
}

// Global initialization hook maintaining 100% backward compatibility with script.js
window.ParticleSculptureIntro = DigitalUniverse;
window.DigitalUniverse = DigitalUniverse;
