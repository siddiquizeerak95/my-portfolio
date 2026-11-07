/**
 * DIGITAL WORLD — CINEMATIC FUTURISTIC PORTFOLIO ARCHITECTURE
 * Awwwards-Inspired Creative Experience & 3D Spatial Systems
 * Specification: DESIGN.md (v5.0 Master Redesign)
 * Author: Zeerak Siddiqui Portfolio Engineering
 */

// -----------------------------------------------------------------------------
// 01. CINEMATIC PARTICLE LOADING SCREEN (5–7 SECOND MASTER EXPERIENCE)
// -----------------------------------------------------------------------------

/**
 * Lightweight 2D Canvas Particle Engine
 * Creates gentle orbital drift, soft sinusoidal fading, and orbital wave harmonics.
 */
class PreloaderParticleSystem {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.particles = [];
    this.animationFrameId = null;
    this.isRunning = false;
    this.isFadingOut = false;
    this.globalOpacity = 0.0; // Emerges gradually in 0–1s
    this.waveMotion = false;
    this.waveIntensity = 0.0;
    this.wavePhase = 0.0;
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.dpr = Math.min(window.devicePixelRatio || 1, 2);
    this.isReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.isMobile = window.innerWidth < 768;
    this.particleCount = this.isMobile ? 24 : 52;
    this.startTime = performance.now();

    this.handleResize = this.handleResize.bind(this);
    this.handleVisibility = this.handleVisibility.bind(this);
    this.loop = this.loop.bind(this);

    this.init();
  }

  init() {
    this.resize();
    window.addEventListener('resize', this.handleResize, { passive: true });
    document.addEventListener('visibilitychange', this.handleVisibility);

    // Seed particles in polar orbital distribution around center logo
    for (let i = 0; i < this.particleCount; i++) {
      this.particles.push(this.createParticle(true));
    }

    this.isRunning = true;
    if (!this.isReducedMotion) {
      this.animationFrameId = requestAnimationFrame(this.loop);
    } else {
      this.globalOpacity = 1.0;
      this.render();
    }
  }

  resize() {
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.canvas.width = Math.floor(this.width * this.dpr);
    this.canvas.height = Math.floor(this.height * this.dpr);
    this.canvas.style.width = `${this.width}px`;
    this.canvas.style.height = `${this.height}px`;
    this.ctx.scale(this.dpr, this.dpr);
  }

  handleResize() {
    this.resize();
  }

  handleVisibility() {
    if (document.hidden) {
      if (this.animationFrameId) {
        cancelAnimationFrame(this.animationFrameId);
        this.animationFrameId = null;
      }
    } else if (this.isRunning && !this.isReducedMotion) {
      if (!this.animationFrameId) {
        this.animationFrameId = requestAnimationFrame(this.loop);
      }
    }
  }

  createParticle(initial = false) {
    const minR = this.isMobile ? 35 : 45;
    const maxR = this.isMobile ? 180 : 270;
    const radius = initial ? minR + Math.random() * (maxR - minR) : minR + Math.random() * 25;
    const angle = Math.random() * Math.PI * 2;

    // Slow, elegant orbital movement (rad/frame)
    const direction = Math.random() > 0.5 ? 1 : -1;
    const speedAngle = direction * (0.0018 + Math.random() * 0.0038);

    // Gentle outward radial drift (px/frame)
    const speedRadius = 0.06 + Math.random() * 0.14;

    // Small white and gray particles for natural depth (0.75px to 2.0px)
    const size = 0.75 + Math.random() * 1.25;

    // Soft fading and breathing opacity
    const baseOpacity = 0.25 + Math.random() * 0.65;
    const pulseSpeed = 0.012 + Math.random() * 0.024;
    const pulsePhase = Math.random() * Math.PI * 2;

    // Subtle glow highlight for larger particles
    const isGlow = size > 1.5 && Math.random() > 0.55;

    return {
      radius,
      baseRadius: radius,
      angle,
      speedAngle,
      speedRadius,
      size,
      baseOpacity,
      pulseSpeed,
      pulsePhase,
      isGlow,
      maxRadius: maxR + Math.random() * 40
    };
  }

  setWaveMotion(active) {
    this.waveMotion = active;
  }

  fadeOut() {
    this.isFadingOut = true;
  }

  loop(now) {
    if (!this.isRunning) return;

    // 0–1 sec: Tiny particles gradually emerge
    const elapsed = now - this.startTime;
    if (elapsed < 1100 && !this.isFadingOut) {
      this.globalOpacity = Math.min(1.0, elapsed / 1000);
    } else if (!this.isFadingOut) {
      this.globalOpacity = 1.0;
    }

    // 3–5 sec: Orbital wave harmonics
    if (this.waveMotion && this.waveIntensity < 1.0) {
      this.waveIntensity = Math.min(1.0, this.waveIntensity + 0.015);
    }

    // 6–7 sec: Slowly dissolve
    if (this.isFadingOut) {
      this.globalOpacity *= 0.88;
      if (this.globalOpacity < 0.008) {
        this.destroy();
        return;
      }
    }

    this.render();
    this.animationFrameId = requestAnimationFrame(this.loop);
  }

  render() {
    const { ctx, width, height } = this;
    ctx.clearRect(0, 0, width, height);

    const cx = width / 2;
    const cy = height / 2;
    const isLight = document.documentElement.getAttribute('data-theme') === 'light';

    if (this.waveMotion) {
      this.wavePhase += 0.016;
    }

    for (let i = 0; i < this.particles.length; i++) {
      const p = this.particles[i];

      // Update orbital angle and radius
      p.angle += p.speedAngle;
      p.radius += p.speedRadius;
      p.pulsePhase += p.pulseSpeed;

      // Gentle flowing orbital waves around the logo
      let effectiveRadius = p.radius;
      if (this.waveMotion) {
        const waveOffset = Math.sin(p.angle * 2.8 + this.wavePhase) * (14 * this.waveIntensity);
        effectiveRadius += waveOffset;
      }

      // Soft sinusoidal fading in and out
      const pulseFactor = 0.65 + 0.35 * Math.sin(p.pulsePhase);
      const alpha = Math.max(0, Math.min(1, p.baseOpacity * pulseFactor * this.globalOpacity));

      // Re-seed particle if it drifts past outer threshold
      if (p.radius > p.maxRadius) {
        Object.assign(p, this.createParticle(false));
      }

      const x = cx + Math.cos(p.angle) * effectiveRadius;
      const y = cy + Math.sin(p.angle) * effectiveRadius;

      ctx.save();
      ctx.beginPath();
      ctx.arc(x, y, p.size, 0, Math.PI * 2);

      if (isLight) {
        ctx.fillStyle = p.isGlow ? `rgba(20, 20, 20, ${alpha})` : `rgba(90, 90, 90, ${alpha * 0.85})`;
        if (p.isGlow && !this.isMobile) {
          ctx.shadowBlur = 5;
          ctx.shadowColor = `rgba(0, 0, 0, ${alpha * 0.35})`;
        }
      } else {
        ctx.fillStyle = p.isGlow ? `rgba(255, 255, 255, ${alpha})` : `rgba(200, 200, 200, ${alpha * 0.85})`;
        if (p.isGlow && !this.isMobile) {
          ctx.shadowBlur = 6;
          ctx.shadowColor = `rgba(255, 255, 255, ${alpha * 0.55})`;
        }
      }

      ctx.fill();
      ctx.restore();
    }
  }

  destroy() {
    this.isRunning = false;
    if (this.animationFrameId) {
      cancelAnimationFrame(this.animationFrameId);
      this.animationFrameId = null;
    }
    window.removeEventListener('resize', this.handleResize);
    document.removeEventListener('visibilitychange', this.handleVisibility);
    this.ctx.clearRect(0, 0, this.width, this.height);
  }
}

/**
 * Real Asset Tracker
 * Measures DOM parsing, document.fonts, and essential imagery without blocking.
 */
function trackEssentialAssets(onAssetsReady) {
  let isReady = false;
  const finish = () => {
    if (isReady) return;
    isReady = true;
    onAssetsReady();
  };

  if (document.readyState === 'complete') {
    finish();
    return;
  }

  window.addEventListener('load', finish, { once: true });

  const essentialImgs = Array.from(document.querySelectorAll('.preloader-logo, .hero-borderless-portrait-img, .header-brand-logo'));
  let loadedCount = 0;
  const checkImgs = () => {
    loadedCount++;
    if (loadedCount >= essentialImgs.length) {
      finish();
    }
  };

  essentialImgs.forEach((img) => {
    if (img.complete && img.naturalWidth > 0) {
      checkImgs();
    } else {
      img.addEventListener('load', checkImgs, { once: true });
      img.addEventListener('error', checkImgs, { once: true });
    }
  });

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(finish).catch(finish);
  }

  // Safety fallback: guarantees completion within 3s without stalling
  setTimeout(finish, 3000);
}

/**
 * Master Choreographed Loading Experience (5–7 Seconds)
 */
function initPreloader() {
  const preloader = document.getElementById('site-preloader') || document.getElementById('preloader');
  const canvas = document.getElementById('preloader-particle-canvas');
  const preloaderContent = document.getElementById('preloader-content');
  const logoWrap = document.getElementById('preloader-logo-wrap');
  const chars = document.querySelectorAll('.preloader-char');
  const experienceTag = document.getElementById('preloader-experience-tag');
  const gauge = document.getElementById('preloader-gauge');
  const progressBar = document.getElementById('preloader-progress-bar');
  const counter = document.getElementById('preloader-counter');
  const status = document.getElementById('preloader-status');

  if (!preloader) {
    document.body.classList.add('system-ready');
    revealPageItems();
    return;
  }

  const isReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const urlParams = new URLSearchParams(window.location.search);
  const skipPreloader = urlParams.get('skip_preloader') === '1';
  const skipIntro = urlParams.get('skip_intro') === '1';

  if (isReducedMotion || skipPreloader) {
    preloader.style.display = 'none';
    if (isReducedMotion || skipIntro) {
      document.body.classList.add('system-ready');
      revealPageItems();
      if (window.sculptureIntroInstance) window.sculptureIntroInstance.dismissImmediately();
    } else if (window.sculptureIntroInstance) {
      window.sculptureIntroInstance.startFormation();
    } else {
      document.body.classList.add('system-ready');
      revealPageItems();
    }
    return;
  }

  // Initialize Particle Canvas Engine
  let particleSystem = null;
  if (canvas) {
    try {
      particleSystem = new PreloaderParticleSystem(canvas);
    } catch (e) {
      console.warn('Particle canvas bypass:', e);
    }
  }

  // Track essential assets in parallel
  let assetsConfirmed = false;
  trackEssentialAssets(() => {
    assetsConfirmed = true;
  });

  // UI Progress Updater
  const updateProgressUI = (val, statusText) => {
    const clamped = Math.min(100, Math.max(0, val));
    if (progressBar) progressBar.style.width = `${clamped}%`;
    if (counter) counter.textContent = `${Math.floor(clamped)}%`;
    if (status && statusText) status.innerHTML = statusText;
  };

  // ---------------------------------------------------------------------------
  // 5–7 SECOND CHOREOGRAPHED TIMELINE
  // ---------------------------------------------------------------------------

  // Phase 1 (0–1s): Particles emerge (handled inside PreloaderParticleSystem)
  updateProgressUI(0, 'INITIALIZING SYSTEM');

  // Phase 2 (1–2s): ZS logo smoothly fades into centre
  setTimeout(() => {
    if (logoWrap) logoWrap.classList.add('logo-revealed');
    updateProgressUI(18, 'SYSTEM INITIALIZED');
  }, 1050);

  // Phase 3 (2–3s): ZEERAK wordmark reveals letter by letter
  const letterDelays = [2050, 2200, 2350, 2500, 2650, 2800];
  chars.forEach((char, idx) => {
    const delay = letterDelays[idx] || (2050 + idx * 150);
    setTimeout(() => {
      char.classList.add('char-revealed');
    }, delay);
  });

  // Subtitle & progress line reveal
  setTimeout(() => {
    if (experienceTag) experienceTag.classList.add('tag-revealed');
    if (gauge) gauge.classList.add('gauge-revealed');
    updateProgressUI(32, 'LOADING EXPERIENCE');
  }, 2950);

  // Phase 4 (3–5s): Flowing orbital waves around logo & steady progress
  setTimeout(() => {
    if (particleSystem) particleSystem.setWaveMotion(true);
    updateProgressUI(48, 'CALIBRATING ORBITAL FLOW');
  }, 3400);

  setTimeout(() => {
    updateProgressUI(68, 'SYNCHRONIZING MATRICES');
  }, 4100);

  setTimeout(() => {
    updateProgressUI(88, 'COMPUTING TELEMETRY');
  }, 4800);

  // Phase 5 (5–6s): Progress completion
  const checkCompletion = () => {
    if (assetsConfirmed) {
      updateProgressUI(100, 'EXPERIENCE READY');

      // Phase 6 (6–7s): Particles dissolve & transition into homepage
      setTimeout(() => {
        // Step 1: Particles slowly dissolve
        if (particleSystem) particleSystem.fadeOut();

        // Step 2: Content fades out
        if (preloaderContent) preloaderContent.classList.add('preloader-content-fade');

        // Step 3: Seamless cinematic curtain transition
        setTimeout(() => {
          preloader.classList.add('preloader-dismissed');

          if (window.sculptureIntroInstance && !skipIntro && !isReducedMotion) {
            window.sculptureIntroInstance.startFormation();
          } else {
            document.body.classList.add('system-ready');
            revealPageItems();
          }

          // Step 4: Cleanup
          setTimeout(() => {
            if (particleSystem) particleSystem.destroy();
            preloader.style.display = 'none';
          }, 850);
        }, 350);
      }, 550);
    } else {
      updateProgressUI(95, 'SYNCHRONIZING ASSETS');
      setTimeout(checkCompletion, 120);
    }
  };

  // Launch Phase 5 at 5.2 seconds
  setTimeout(checkCompletion, 5200);
}

function revealPageItems() {
  const heroItems = document.querySelectorAll('.hero-section .reveal-item, .page-hero-banner .reveal-item');
  heroItems.forEach((item) => {
    item.classList.add('revealed');
  });
}

// -----------------------------------------------------------------------------
// 02. EDITORIAL MINIMALIST ARCHITECTURE (THREE.JS RETIRED)
// -----------------------------------------------------------------------------
function initThreeScene() {
  // 3D canvas replaced with clean monochrome portrait frame
}

// -----------------------------------------------------------------------------
// 03. SHARED MULTIPAGE NAVIGATION & STICKY SCROLL
// -----------------------------------------------------------------------------
function initHeaderScroll() {
  const header = document.getElementById('site-header') || document.querySelector('.site-header');
  if (!header) return;

  let ticking = false;
  const handleScroll = () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        if (window.scrollY > 20) {
          header.classList.add('scrolled');
        } else {
          header.classList.remove('scrolled');
        }
        ticking = false;
      });
      ticking = true;
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

function initNavigation() {
  const currentPage = document.body.getAttribute('data-page') || 'home';
  const navItems = document.querySelectorAll('.nav-item');
  const mobileLinks = document.querySelectorAll('.mobile-link');
  const mobileToggle = document.getElementById('mobile-toggle');
  const mobileClose = document.getElementById('mobile-close');
  const mobileDrawer = document.getElementById('mobile-drawer');
  const mobileBackdrop = document.getElementById('mobile-drawer-backdrop');
  const drawerCta = document.querySelectorAll('.btn-drawer-cta, .drawer-link-btn');

  // Highlight active link matching current page across all 5 routes
  const setActiveState = (links) => {
    links.forEach((link) => {
      const href = link.getAttribute('href') || '';
      let isCurrent = false;

      if (currentPage === 'home' && (href === 'index.html' || href === './' || href === '/' || href === '')) {
        isCurrent = true;
      } else if (currentPage !== 'home' && href.includes(currentPage)) {
        isCurrent = true;
      }

      if (isCurrent) {
        link.classList.add('active');
        link.setAttribute('aria-current', 'page');
      } else {
        link.classList.remove('active');
        link.removeAttribute('aria-current');
      }
    });
  };

  setActiveState(navItems);
  setActiveState(mobileLinks);

  // Mobile Drawer Toggle
  if (mobileToggle && mobileDrawer) {
    const toggleDrawer = (open) => {
      const isOpen = open !== undefined ? open : !mobileDrawer.classList.contains('open');
      mobileDrawer.classList.toggle('open', isOpen);
      mobileToggle.setAttribute('aria-expanded', isOpen.toString());
      mobileDrawer.setAttribute('aria-hidden', (!isOpen).toString());
      document.body.style.overflow = isOpen ? 'hidden' : '';

      if (isOpen) {
        const firstLink = mobileDrawer.querySelector('.mobile-close, .mobile-link');
        if (firstLink) setTimeout(() => firstLink.focus(), 100);
      } else {
        mobileToggle.focus();
      }
    };

    mobileToggle.addEventListener('click', () => toggleDrawer());
    if (mobileClose) mobileClose.addEventListener('click', () => toggleDrawer(false));
    if (mobileBackdrop) mobileBackdrop.addEventListener('click', () => toggleDrawer(false));

    mobileDrawer.addEventListener('click', (e) => {
      if (e.target === mobileDrawer) {
        toggleDrawer(false);
      }
    });

    mobileLinks.forEach((link) => {
      link.addEventListener('click', () => toggleDrawer(false));
    });

    drawerCta.forEach((btn) => {
      btn.addEventListener('click', () => toggleDrawer(false));
    });

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileDrawer.classList.contains('open')) {
        toggleDrawer(false);
      }
    });
  }
}

// -----------------------------------------------------------------------------
// 04. REAL-TIME INDIAN STANDARD TIME WORLD CLOCK (ASIA/KOLKATA)
// -----------------------------------------------------------------------------
const indiaTimeFormatter = new Intl.DateTimeFormat('en-IN', {
  timeZone: 'Asia/Kolkata',
  hour: '2-digit',
  minute: '2-digit',
  second: '2-digit',
  hour12: false
});

const indiaYearFormatter = new Intl.DateTimeFormat('en-IN', {
  timeZone: 'Asia/Kolkata',
  year: 'numeric'
});

function getIndianTime(date = new Date()) {
  return indiaTimeFormatter.format(date);
}

let clockIntervalId = null;

function initWorldClock() {
  const clockEl = document.getElementById('live-clock');
  const yearEl = document.getElementById('current-year');

  if (yearEl) {
    try {
      yearEl.textContent = indiaYearFormatter.format(new Date());
    } catch (e) {
      yearEl.textContent = new Date().getFullYear().toString();
    }
  }

  const updateClock = () => {
    if (!clockEl) return;
    try {
      clockEl.textContent = `${getIndianTime()} IST`;
    } catch (err) {
      const now = new Date();
      clockEl.textContent = `${now.toTimeString().split(' ')[0]} IST`;
    }
  };

  if (clockIntervalId) {
    clearInterval(clockIntervalId);
  }

  updateClock();
  clockIntervalId = setInterval(updateClock, 1000);
}

// -----------------------------------------------------------------------------
// 05. 3D CARD PERSPECTIVE TILT WITH DYNAMIC SPECULAR GLARE
// -----------------------------------------------------------------------------
function initCardTilt() {
  const isFinePointer = window.matchMedia('(pointer: fine) and (hover: hover)').matches;
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!isFinePointer || prefersReducedMotion) return;

  const tiltCards = document.querySelectorAll('[data-tilt]');

  tiltCards.forEach((card) => {
    let ticking = false;
    let mouseX = 0;
    let mouseY = 0;

    const updateTilt = () => {
      const rect = card.getBoundingClientRect();
      const x = mouseX - rect.left;
      const y = mouseY - rect.top;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      // Restrained, elegant Swiss angles (max ±4.5 degrees)
      const rotateX = ((y - centerY) / centerY) * -4.2;
      const rotateY = ((x - centerX) / centerX) * 4.6;

      card.style.transform = `perspective(1100px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateY(-4px)`;
      card.style.setProperty('--glare-x', `${x}px`);
      card.style.setProperty('--glare-y', `${y}px`);
      card.style.setProperty('--glare-opacity', '1');
      ticking = false;
    };

    card.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      if (!ticking) {
        requestAnimationFrame(updateTilt);
        ticking = true;
      }
    }, { passive: true });

    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
      card.style.setProperty('--glare-opacity', '0');
      ticking = false;
    });
  });
}

// -----------------------------------------------------------------------------
// 05.1 HERO BORDERLESS CINEMATIC PARALLAX DEPTH
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
// 06. CUSTOM DUAL-STATE PRECISION CYAN CURSOR
// -----------------------------------------------------------------------------
function initCustomCursor() {
  if (window.matchMedia('(hover: none)').matches) return;

  const cursor = document.getElementById('custom-cursor');
  const dot = document.getElementById('cursor-dot');
  const ring = document.getElementById('cursor-ring');

  if (!cursor || !dot || !ring) return;

  let mouseX = -100;
  let mouseY = -100;
  let ringX = -100;
  let ringY = -100;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    dot.style.transform = `translate(${mouseX}px, ${mouseY}px)`;
  });

  const updateRing = () => {
    ringX += (mouseX - ringX) * 0.18;
    ringY += (mouseY - ringY) * 0.18;
    ring.style.transform = `translate(${ringX}px, ${ringY}px)`;
    requestAnimationFrame(updateRing);
  };
  requestAnimationFrame(updateRing);

  const updateHoverTargets = () => {
    const targets = document.querySelectorAll('a, button, [data-tilt], .skill-card, input, textarea, select');
    targets.forEach((el) => {
      el.addEventListener('mouseenter', () => cursor.classList.add('hovering'));
      el.addEventListener('mouseleave', () => cursor.classList.remove('hovering'));
    });
  };
  updateHoverTargets();
}

// -----------------------------------------------------------------------------
// 06.1 MINIMALIST MONOCHROME PARTICLE CURSOR TRAIL (DIGITAL DUST)
// -----------------------------------------------------------------------------
function initParticleCursor() {
  // Device & accessibility checks: desktop fine pointer only; respect reduced motion
  const isFinePointer = window.matchMedia('(pointer: fine) and (hover: hover)').matches;
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!isFinePointer || prefersReducedMotion) return;

  // Retrieve or dynamically mount the canvas element
  let canvas = document.getElementById('particle-cursor-canvas');
  if (!canvas) {
    canvas = document.createElement('canvas');
    canvas.id = 'particle-cursor-canvas';
    canvas.setAttribute('aria-hidden', 'true');
    document.body.appendChild(canvas);
  }

  const ctx = canvas.getContext('2d', { alpha: true });
  if (!ctx) return;

  let width = 0;
  let height = 0;
  let dpr = 1;

  function resizeCanvas() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = Math.floor(width * dpr);
    canvas.height = Math.floor(height * dpr);
    canvas.style.width = `${width}px`;
    canvas.style.height = `${height}px`;
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.scale(dpr, dpr);
  }

  resizeCanvas();

  let resizeTimeout;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(resizeCanvas, 120);
  }, { passive: true });

  // State & object pool for zero GC pressure
  const particles = [];
  const pool = [];
  const MAX_PARTICLES = 45; // Restrained cap to maintain elegant minimalism
  let lastX = null;
  let lastY = null;
  let animating = false;
  let animationFrameId = null;

  class Particle {
    constructor(x, y, isLight) {
      this.reset(x, y, isLight);
    }

    reset(x, y, isLight) {
      // Natural subtle dispersion around pointer
      const angle = Math.random() * Math.PI * 2;
      const dist = Math.random() * 3.5;
      this.x = x + Math.cos(angle) * dist;
      this.y = y + Math.sin(angle) * dist;

      // Gentle drift velocity with slight upward buoyancy
      const speed = 0.2 + Math.random() * 0.45;
      const driftAngle = Math.random() * Math.PI * 2;
      this.vx = Math.cos(driftAngle) * speed;
      this.vy = Math.sin(driftAngle) * speed - 0.12;

      // Variable sizing for natural atmospheric depth (0.75px to 2.2px)
      this.size = 0.75 + Math.random() * 1.45;

      // Opacity and smooth fade decay (lifetime: ~0.45s to 0.75s)
      this.alpha = 0.72 + Math.random() * 0.24;
      this.decay = 0.024 + Math.random() * 0.022;

      // Strictly monochromatic palette depending on current theme
      if (isLight) {
        // Light Mode: deep charcoal to medium gray
        const shade = Math.floor(20 + Math.random() * 65);
        this.r = shade;
        this.g = shade;
        this.b = shade;
      } else {
        // Dark Mode: pure crisp white to soft silver gray
        const shade = Math.floor(215 + Math.random() * 40);
        this.r = shade;
        this.g = shade;
        this.b = shade;
      }
    }

    update() {
      this.x += this.vx;
      this.y += this.vy;
      this.vx *= 0.96;
      this.vy *= 0.96;
      this.alpha -= this.decay;
      this.size = Math.max(0.35, this.size * 0.985);
      return this.alpha > 0.01;
    }

    draw(context) {
      context.beginPath();
      context.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      context.fillStyle = `rgba(${this.r}, ${this.g}, ${this.b}, ${this.alpha.toFixed(3)})`;
      context.fill();
    }
  }

  function getParticle(x, y, isLight) {
    if (pool.length > 0) {
      const p = pool.pop();
      p.reset(x, y, isLight);
      return p;
    }
    return new Particle(x, y, isLight);
  }

  function releaseParticle(p) {
    if (pool.length < MAX_PARTICLES) {
      pool.push(p);
    }
  }

  function emitParticles(x, y) {
    const isLight = document.documentElement.getAttribute('data-theme') === 'light';
    const count = Math.random() < 0.35 ? 2 : 1;

    for (let i = 0; i < count; i++) {
      if (particles.length < MAX_PARTICLES) {
        particles.push(getParticle(x, y, isLight));
      }
    }

    // Wake up animation loop if currently idle
    if (!animating) {
      animating = true;
      animationFrameId = requestAnimationFrame(render);
    }
  }

  function render() {
    ctx.clearRect(0, 0, width, height);

    for (let i = particles.length - 1; i >= 0; i--) {
      const p = particles[i];
      if (p.update()) {
        p.draw(ctx);
      } else {
        particles.splice(i, 1);
        releaseParticle(p);
      }
    }

    // Continue loop if active particles exist; otherwise pause to eliminate idle CPU drain
    if (particles.length > 0) {
      animationFrameId = requestAnimationFrame(render);
    } else {
      animating = false;
      ctx.clearRect(0, 0, width, height);
    }
  }

  // Distance-based particle emission (only on active mouse movement)
  window.addEventListener('mousemove', (e) => {
    const curX = e.clientX;
    const curY = e.clientY;

    if (lastX === null || lastY === null) {
      lastX = curX;
      lastY = curY;
      emitParticles(curX, curY);
      return;
    }

    const dx = curX - lastX;
    const dy = curY - lastY;
    const dist = Math.hypot(dx, dy);

    // Only emit when pointer moves at least 5 pixels
    if (dist >= 5) {
      // Interpolate along fast sweeps so trail remains continuous without clustering
      const steps = Math.min(Math.floor(dist / 9), 3);
      if (steps > 1) {
        for (let s = 1; s <= steps; s++) {
          const ix = lastX + (dx * s) / steps;
          const iy = lastY + (dy * s) / steps;
          emitParticles(ix, iy);
        }
      } else {
        emitParticles(curX, curY);
      }
      lastX = curX;
      lastY = curY;
    }
  }, { passive: true });

  window.addEventListener('mouseleave', () => {
    lastX = null;
    lastY = null;
  }, { passive: true });

  // Pause rendering when document is hidden (tab switch or minimization)
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      particles.forEach(p => releaseParticle(p));
      particles.length = 0;
      if (animating) {
        cancelAnimationFrame(animationFrameId);
        animating = false;
      }
      ctx.clearRect(0, 0, width, height);
    }
  });
}

// -----------------------------------------------------------------------------
// 07. SCROLL REVEAL (INTERSECTION OBSERVER)
// -----------------------------------------------------------------------------
function initScrollReveal() {
  const urlParams = new URLSearchParams(window.location.search);
  const revealAll = urlParams.get('reveal_all') === '1';
  const focusSecId = urlParams.get('focus_section');

  if (focusSecId) {
    const allSections = document.querySelectorAll('main > section, footer.site-footer');
    allSections.forEach((sec) => {
      if (sec.id !== focusSecId && !sec.classList.contains(focusSecId)) {
        sec.style.display = 'none';
      } else {
        sec.style.display = 'block';
        sec.querySelectorAll('.reveal-item').forEach(el => el.classList.add('revealed'));
      }
    });
  }

  if (revealAll || focusSecId || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('.reveal-item').forEach(el => el.classList.add('revealed'));
    return;
  }

  const revealItems = document.querySelectorAll('.reveal-item:not(.revealed)');

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    revealItems.forEach((item) => item.classList.add('revealed'));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -40px 0px'
  });

  revealItems.forEach((item) => observer.observe(item));
}

// -----------------------------------------------------------------------------
// 08. MAGNETIC BUTTON MICRO-INTERACTION
// -----------------------------------------------------------------------------
function initMagneticButtons() {
  if (window.matchMedia('(hover: none)').matches) return;

  const magneticBtns = document.querySelectorAll('.magnetic-btn');

  magneticBtns.forEach((btn) => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const deltaX = (e.clientX - rect.left - rect.width / 2) * 0.22;
      const deltaY = (e.clientY - rect.top - rect.height / 2) * 0.22;
      btn.style.transform = `translate(${deltaX}px, ${deltaY}px)`;
    });

    btn.addEventListener('mouseleave', () => {
      btn.style.transform = 'translate(0px, 0px)';
    });
  });
}

// -----------------------------------------------------------------------------
// 09. PROJECT CATEGORY FILTERING (FOR PROJECTS PAGE)
// -----------------------------------------------------------------------------
function initProjectFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn, .skills-filter-pill[data-filter]');
  const projectItems = document.querySelectorAll('.project-dossier-item, .projects-showcase-grid .project-card-glass-body');

  if (!filterBtns.length || !projectItems.length) return;

  filterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      filterBtns.forEach((b) => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      const filterValue = btn.getAttribute('data-filter');

      projectItems.forEach((item) => {
        const itemCategory = item.getAttribute('data-category');
        if (filterValue === 'all' || itemCategory === filterValue) {
          item.style.display = '';
          setTimeout(() => {
            item.classList.add('revealed');
          }, 40);
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}

// -----------------------------------------------------------------------------
// 09.1 BLOG CATEGORY FILTERING (FOR BLOG PAGE)
// -----------------------------------------------------------------------------
function initBlogFilters() {
  const filterBtns = document.querySelectorAll('.blog-filter-btn, .skills-filter-pill[data-blog-filter]');
  const blogItems = document.querySelectorAll('.blog-dossier-item, .magazine-article-card');

  if (!filterBtns.length || !blogItems.length) return;

  filterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      filterBtns.forEach((b) => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      const filterValue = btn.getAttribute('data-blog-filter') || btn.getAttribute('data-filter');

      blogItems.forEach((item) => {
        const itemCategory = item.getAttribute('data-category');
        if (filterValue === 'all' || itemCategory === filterValue) {
          item.style.display = '';
          setTimeout(() => {
            item.classList.add('revealed');
          }, 40);
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}

// 10. CONTACT TRANSMISSION FORM HANDLER
// -----------------------------------------------------------------------------
function initContactForm() {
  // Handled securely by contact-e2ee.js with genuine OpenPGP client-side encryption
}

// -----------------------------------------------------------------------------
// 10.1 SKILLS 3D PEDESTAL & CATEGORY FILTERING
// -----------------------------------------------------------------------------
function initSkillsPedestal() {
  const filterPills = document.querySelectorAll('.skills-filter-pill');
  const cards = document.querySelectorAll('.skill-card-3d');
  if (!filterPills.length || !cards.length) return;

  filterPills.forEach((pill) => {
    pill.addEventListener('click', () => {
      filterPills.forEach((p) => {
        p.classList.remove('active');
        p.setAttribute('aria-selected', 'false');
      });
      pill.classList.add('active');
      pill.setAttribute('aria-selected', 'true');

      const selectedCategory = pill.getAttribute('data-category');

      cards.forEach((card) => {
        const cardCat = card.getAttribute('data-category');
        if (selectedCategory === 'all' || cardCat === selectedCategory) {
          card.style.opacity = '1';
          card.style.transform = 'translateY(0) scale(1)';
          card.style.pointerEvents = 'auto';
        } else {
          card.style.opacity = '0.15';
          card.style.transform = 'translateY(6px) scale(0.96)';
          card.style.pointerEvents = 'none';
        }
      });
    });
  });
}

// -----------------------------------------------------------------------------
// 10.2 PROJECTS 3D PERSPECTIVE CAROUSEL & SLIDER
// -----------------------------------------------------------------------------
function initProjects3DCarousel() {
  const stage = document.getElementById('projects-3d-stage') || document.getElementById('projects-3d-carousel');
  if (!stage) return;

  const slides = stage.querySelectorAll('.project-slide-item, .project-slide-card');
  const dots = document.querySelectorAll('#projects-pagination-dots .slider-dot, #projects-pagination-dots .pagination-dot');
  const btnPrev = document.getElementById('projects-slider-prev') || document.getElementById('proj-slider-prev');
  const btnNext = document.getElementById('projects-slider-next') || document.getElementById('proj-slider-next');

  if (!slides.length) return;

  let activeIndex = 0;
  const total = slides.length;

  const updateSlideClasses = () => {
    slides.forEach((slide, idx) => {
      slide.classList.remove('active', 'prev-1', 'next-1');
      if (idx === activeIndex) {
        slide.classList.add('active');
        slide.setAttribute('aria-hidden', 'false');
      } else if (idx === (activeIndex - 1 + total) % total) {
        slide.classList.add('prev-1');
        slide.setAttribute('aria-hidden', 'true');
      } else if (idx === (activeIndex + 1) % total) {
        slide.classList.add('next-1');
        slide.setAttribute('aria-hidden', 'true');
      } else {
        slide.setAttribute('aria-hidden', 'true');
      }
    });

    dots.forEach((dot, idx) => {
      const isActive = idx === activeIndex;
      dot.classList.toggle('active', isActive);
      dot.setAttribute('aria-selected', isActive ? 'true' : 'false');
    });

    stage.setAttribute('data-active-index', activeIndex);
  };

  if (btnPrev) {
    btnPrev.addEventListener('click', () => {
      activeIndex = (activeIndex - 1 + total) % total;
      updateSlideClasses();
    });
  }

  if (btnNext) {
    btnNext.addEventListener('click', () => {
      activeIndex = (activeIndex + 1) % total;
      updateSlideClasses();
    });
  }

  dots.forEach((dot, idx) => {
    dot.addEventListener('click', () => {
      activeIndex = idx;
      updateSlideClasses();
    });
  });

  slides.forEach((slide, idx) => {
    slide.addEventListener('click', (e) => {
      if (e.target.closest('a') || e.target.closest('button')) return;
      if (idx !== activeIndex) {
        activeIndex = idx;
        updateSlideClasses();
      }
    });
  });

  // Touch swipe support for mobile/tablets
  let touchStartX = 0;
  let touchEndX = 0;

  stage.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  stage.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    const diff = touchStartX - touchEndX;
    if (Math.abs(diff) > 40) {
      if (diff > 0) {
        activeIndex = (activeIndex + 1) % total;
      } else {
        activeIndex = (activeIndex - 1 + total) % total;
      }
      updateSlideClasses();
    }
  }, { passive: true });

  updateSlideClasses();
}

// -----------------------------------------------------------------------------

// -----------------------------------------------------------------------------
// 10.3 PARALLAX BACKGROUND DEPTH CONTROLLER (SWISS LUXURY MOTION)
// -----------------------------------------------------------------------------
function initParallaxBackground() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  let layer = document.getElementById('cinematic-parallax-layer');
  if (!layer) {
    layer = document.createElement('div');
    layer.id = 'cinematic-parallax-layer';
    layer.className = 'cinematic-parallax-layer';
    layer.setAttribute('aria-hidden', 'true');
    layer.innerHTML = `
      <div class="parallax-orbital-ring ring-1" data-speed="0.05"></div>
      <div class="parallax-orbital-ring ring-2" data-speed="-0.07"></div>
      <div class="parallax-ambient-spot spot-1" data-speed="0.03"></div>
      <div class="parallax-dust-particle p-1" data-speed="0.08"></div>
      <div class="parallax-dust-particle p-2" data-speed="-0.06"></div>
      <div class="parallax-dust-particle p-3" data-speed="0.04"></div>
    `;
    document.body.prepend(layer);
  }

  const elements = layer.querySelectorAll('[data-speed]');
  if (!elements.length) return;

  let ticking = false;

  const updateParallax = () => {
    const scrollY = window.pageYOffset || document.documentElement.scrollTop;
    elements.forEach((el) => {
      const speed = parseFloat(el.getAttribute('data-speed')) || 0.05;
      const yPos = Math.round(scrollY * speed);
      el.style.transform = `translate3d(0, ${yPos}px, 0)`;
    });
    ticking = false;
  };

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(updateParallax);
      ticking = true;
    }
  }, { passive: true });

  updateParallax();
}

// -----------------------------------------------------------------------------
// 10.4 TIMELINE SCROLL & PROGRESSIVE MILESTONE ILLUMINATION
// -----------------------------------------------------------------------------
function initTimelineScrollAnimation() {
  const track = document.querySelector('.journey-vertical-track');
  if (!track) return;

  let fillLine = document.getElementById('timeline-line-fill');
  if (!fillLine) {
    const parentLine = document.getElementById('timeline-glowing-line') || track.querySelector('.timeline-glowing-line');
    if (parentLine) {
      fillLine = document.createElement('div');
      fillLine.id = 'timeline-line-fill';
      fillLine.className = 'timeline-line-fill';
      parentLine.appendChild(fillLine);
    }
  }

  const milestones = track.querySelectorAll('.timeline-milestone-item');
  if (!milestones.length) return;

  let ticking = false;

  const updateTimeline = () => {
    const trackRect = track.getBoundingClientRect();
    const windowH = window.innerHeight;
    const triggerPoint = windowH * 0.65;
    const trackTop = trackRect.top;
    const trackHeight = trackRect.height;

    let progress = 0;
    if (trackTop < triggerPoint) {
      progress = (triggerPoint - trackTop) / (trackHeight * 0.9);
      progress = Math.min(1, Math.max(0, progress));
    }

    if (fillLine) {
      fillLine.style.height = `${(progress * 100).toFixed(1)}%`;
    }

    milestones.forEach((item) => {
      const itemRect = item.getBoundingClientRect();
      if (itemRect.top < triggerPoint + 40) {
        item.classList.add('milestone-active');
      } else {
        item.classList.remove('milestone-active');
      }
    });

    ticking = false;
  };

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(updateTimeline);
      ticking = true;
    }
  }, { passive: true });

  updateTimeline();
}

// -----------------------------------------------------------------------------
// 10.5 EDITORIAL TEXT REVEAL TYPOGRAPHY
// -----------------------------------------------------------------------------
function initTextReveal() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const headings = document.querySelectorAll('.section-heading-zs');
  headings.forEach((heading) => {
    if (heading.dataset.textRevealInit) return;
    heading.dataset.textRevealInit = 'true';

    if (!heading.querySelector('.text-reveal-inner')) {
      const lines = heading.innerHTML.split(/<br\s*\/?>/i);
      if (lines.length > 1) {
        heading.innerHTML = lines.map((l, i) => `
          <span class="text-reveal-line">
            <span class="text-reveal-inner" style="transition-delay: ${i * 80}ms;">${l.trim()}</span>
          </span>
        `).join('');
      } else {
        heading.innerHTML = `
          <span class="text-reveal-line">
            <span class="text-reveal-inner">${heading.innerHTML.trim()}</span>
          </span>
        `;
      }
    }
  });
}

// -----------------------------------------------------------------------------
// 10.6 SUBTLE IMAGE SCROLL PARALLAX
// -----------------------------------------------------------------------------
function initImageScrollParallax() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (window.matchMedia('(max-width: 768px)').matches) return;

  const parallaxImgs = document.querySelectorAll('.project-preview-box img, .blog-card-thumb-wrap img, .journey-landscape-img');
  if (!parallaxImgs.length) return;

  let ticking = false;

  const updateImgParallax = () => {
    const windowH = window.innerHeight;
    parallaxImgs.forEach((img) => {
      const rect = img.getBoundingClientRect();
      if (rect.bottom > 0 && rect.top < windowH) {
        const centerOffset = (rect.top + rect.height / 2) - (windowH / 2);
        const yOffset = Math.round(centerOffset * -0.03);
        img.style.transform = `translate3d(0, ${yOffset}px, 0)`;
      }
    });
    ticking = false;
  };

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(updateImgParallax);
      ticking = true;
    }
  }, { passive: true });
}

// 11. BIDIRECTIONAL LIGHT / DARK THEME SYSTEM
// -----------------------------------------------------------------------------
function initThemeToggle() {
  const toggleBtn = document.getElementById('theme-toggle');
  const urlParams = new URLSearchParams(window.location.search);
  const paramTheme = urlParams.get('theme');
  const localTheme = localStorage.getItem('zs_theme');
  // First-time visitors unconditionally default to dark mode (#080808)
  const activeTheme = paramTheme || localTheme || document.documentElement.getAttribute('data-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', activeTheme);

  if (!toggleBtn) return;

  const updateAria = (theme) => {
    const isDark = theme === 'dark';
    toggleBtn.setAttribute('aria-label', isDark ? 'Switch to light theme' : 'Switch to dark theme');
    toggleBtn.setAttribute('title', isDark ? 'Switch to light theme' : 'Switch to dark theme');
  };

  updateAria(activeTheme);

  toggleBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', nextTheme);
    localStorage.setItem('zs_theme', nextTheme);
    updateAria(nextTheme);
  });
}

// -----------------------------------------------------------------------------
// 11.2 GLOBAL SOUND SYSTEM (MIXKIT SCI-FI INTERFACE ROBOT CLICK)
// -----------------------------------------------------------------------------
function initSoundSystem() {
  const toggleBtn = document.getElementById('sound-toggle');
  const AUDIO_SRC = 'assets/audio/mixkit-sci-fi-interface-robot-click-901.wav';

  class PortfolioSoundSystem {
    constructor() {
      this.src = AUDIO_SRC;
      this.audio = new Audio(this.src);
      this.audio.preload = 'auto';

      this.audioCtx = null;
      this.audioBuffer = null;
      this.currentSource = null;
      this.lastPlayTime = 0;
      this.minInterval = 50; // ms: prevent overlapping sounds during rapid clicks

      // Default is strictly OFF unless explicitly saved as 'on'
      this.enabled = localStorage.getItem('zs_sound') === 'on';

      this.initAudioContext();
      this.bindUserGestureUnlock();
      this.bindGlobalListeners();
      this.syncUI();
    }

    async initAudioContext() {
      try {
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        if (!AudioContextClass) return;
        this.audioCtx = new AudioContextClass();

        // Preload and decode audio data for zero-latency responsive playback
        const res = await fetch(this.src);
        if (!res.ok) return;
        const arrayBuffer = await res.arrayBuffer();
        this.audioBuffer = await this.audioCtx.decodeAudioData(arrayBuffer);
      } catch (err) {
        // Fallback to HTML5 audio element
        this.audioBuffer = null;
      }
    }

    bindUserGestureUnlock() {
      const unlockAudio = () => {
        if (this.audioCtx && this.audioCtx.state === 'suspended') {
          this.audioCtx.resume().catch(() => {});
        }
      };
      ['click', 'pointerdown', 'touchstart', 'keydown'].forEach(evt => {
        window.addEventListener(evt, unlockAudio, { capture: true, once: true, passive: true });
      });
    }

    unlock() {
      if (this.audioCtx && this.audioCtx.state === 'suspended') {
        this.audioCtx.resume().catch(() => {});
      }
    }

    syncUI() {
      const state = this.enabled ? 'on' : 'off';
      document.documentElement.setAttribute('data-sound', state);
      if (toggleBtn) {
        toggleBtn.setAttribute('data-sound', state);
        const label = this.enabled ? 'Sound effects enabled (Click to mute)' : 'Sound effects muted (Click to unmute)';
        toggleBtn.setAttribute('aria-label', label);
        toggleBtn.setAttribute('title', label);
      }
    }

    toggle() {
      this.unlock();
      this.enabled = !this.enabled;
      localStorage.setItem('zs_sound', this.enabled ? 'on' : 'off');
      this.syncUI();

      // Play sound upon enabling as audible confirmation
      if (this.enabled) {
        this.play();
      }
    }

    play() {
      if (!this.enabled) return;

      const now = performance.now();
      if (now - this.lastPlayTime < this.minInterval) return;
      this.lastPlayTime = now;

      this.unlock();

      // 1. Web Audio API playback (Zero-latency & prevents overlapping)
      if (this.audioCtx && this.audioBuffer) {
        try {
          if (this.currentSource) {
            try {
              this.currentSource.stop();
              this.currentSource.disconnect();
            } catch (e) {}
            this.currentSource = null;
          }

          const source = this.audioCtx.createBufferSource();
          source.buffer = this.audioBuffer;
          source.connect(this.audioCtx.destination);
          source.start(0);
          this.currentSource = source;
          return;
        } catch (e) {
          // Fall back to HTML5 Audio if Web Audio source fails
        }
      }

      // 2. HTML5 Audio Fallback (Reset to 0 to prevent overlap)
      try {
        this.audio.pause();
        this.audio.currentTime = 0;
        const p = this.audio.play();
        if (p && p.catch) p.catch(() => {});
      } catch (e) {}
    }

    bindGlobalListeners() {
      // Touch-scroll detection: prevent sound while dragging/scrolling on mobile
      let touchStartX = 0;
      let touchStartY = 0;
      let isTouchScrolling = false;

      document.addEventListener('touchstart', (e) => {
        if (e.touches && e.touches[0]) {
          touchStartX = e.touches[0].clientX;
          touchStartY = e.touches[0].clientY;
          isTouchScrolling = false;
        }
      }, { passive: true });

      document.addEventListener('touchmove', (e) => {
        if (e.touches && e.touches[0]) {
          const dx = Math.abs(e.touches[0].clientX - touchStartX);
          const dy = Math.abs(e.touches[0].clientY - touchStartY);
          if (dx > 10 || dy > 10) {
            isTouchScrolling = true;
          }
        }
      }, { passive: true });

      document.addEventListener('touchend', () => {
        setTimeout(() => { isTouchScrolling = false; }, 60);
      }, { passive: true });

      // Interactive element selector: covers all navigation links, buttons, cards, filter pills, toggles
      const interactiveSelector = [
        'a[href]',
        'button',
        '[role="button"]',
        '[role="tab"]',
        '[role="link"]',
        '[role="switch"]',
        'input[type="submit"]',
        'input[type="button"]',
        'input[type="reset"]',
        'summary',
        '[data-filter]',
        '[data-tab]',
        '[data-tilt]',
        '[data-category]',
        '.nav-item',
        '.mobile-link',
        '.mobile-nav-item',
        '.header-brand',
        '.header-social-btn',
        '.theme-toggle-btn',
        '.sound-toggle-btn',
        '.mobile-toggle',
        '.mobile-close',
        '.btn-sculpture-enter',
        '.project-card-glass-body',
        '.project-slide-item',
        '.skill-squircle-card',
        '.skill-card-glass',
        '.skills-filter-pill',
        '.blog-3d-card',
        '.b3d-pill-btn',
        '.b3d-cta-btn',
        '.contact-channel-item-zs',
        '.contact-3d-glass-card',
        '.about-feature-card-zs',
        '.hero-spiral-card',
        '.slider-nav-btn',
        '.slider-dot',
        '.accordion-trigger',
        '.scroll-to-top'
      ].join(', ');

      document.addEventListener('click', (e) => {
        if (isTouchScrolling) return;
        if (!this.enabled) return;

        // Sound toggle button handles its own state and sound
        if (e.target.closest('#sound-toggle')) return;

        const target = e.target.closest(interactiveSelector);
        if (!target) return;
        if (target.disabled || target.getAttribute('aria-disabled') === 'true') return;

        // Check if target is an internal navigation link requiring delay for audio delivery
        const anchor = target.closest('a[href]');
        if (anchor && this.enabled) {
          const href = anchor.getAttribute('href');
          const isSpecial = !href || href.startsWith('#') || href.startsWith('javascript:') || href.startsWith('mailto:') || href.startsWith('tel:');
          const isNewTab = anchor.target === '_blank' || e.ctrlKey || e.metaKey || e.shiftKey || e.altKey;
          const isDownload = anchor.hasAttribute('download');

          if (!isSpecial && !isNewTab && !isDownload) {
            // Internal page transition: play click sound and navigate after brief 140ms delay
            e.preventDefault();
            this.play();
            const targetUrl = anchor.href;
            setTimeout(() => {
              window.location.href = targetUrl;
            }, 140);
            return;
          }
        }

        // Standard interactive element click (buttons, cards, toggles, filter pills)
        this.play();
      }, { capture: true });
    }
  }

  const soundSystem = new PortfolioSoundSystem();
  window.zsSoundSystem = soundSystem;

  if (toggleBtn) {
    toggleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      soundSystem.toggle();
    });
  }
}

// -----------------------------------------------------------------------------
// 12. MASTER DOM INITIALIZATION (MODULE-SAFE BOOTSTRAP)
// -----------------------------------------------------------------------------
// -----------------------------------------------------------------------------
// 05.2 SPIRAL NOTEBOOK 3D FLIP CARD ANIMATION (EXACT REFERENCE VIDEO)
// -----------------------------------------------------------------------------
function initSpiralFlipCard() {
  const items = document.querySelectorAll('.spiral-role-text');
  const pageIndicator = document.getElementById('spiral-card-page');
  if (!items || items.length === 0) return;

  let currentIndex = 0;
  const total = items.length;

  setInterval(() => {
    const prev = items[currentIndex];
    prev.classList.remove('active');
    prev.classList.add('exit-up');

    setTimeout(() => {
      prev.classList.remove('exit-up');
    }, 550);

    currentIndex = (currentIndex + 1) % total;
    const next = items[currentIndex];
    next.classList.add('active');

    if (pageIndicator) {
      pageIndicator.textContent = `0${currentIndex + 1} / 0${total}`;
    }
  }, 2800);
}

function initSculptureIntro() {
  const stage = document.getElementById('sculpture-intro-stage');
  if (!stage) return;
  if (typeof ParticleSculptureIntro !== 'undefined') {
    window.sculptureIntroInstance = new ParticleSculptureIntro({
      onEnter: () => {
        document.body.classList.add('system-ready');
        revealPageItems();
      }
    });
  }
}

function bootPortfolio() {
  initThemeToggle();
  initSoundSystem();
  initSculptureIntro();
  initPreloader();
  initThreeScene();
  initHeaderScroll();
  initNavigation();
  initWorldClock();
  initCardTilt();
  initHeroPerspective();
  initSpiralFlipCard();
  initCustomCursor();
  initParticleCursor();
  initScrollReveal();
  initMagneticButtons();
  initProjectFilters();
  initBlogFilters();
  initContactForm();
  initSkillsPedestal();
  initProjects3DCarousel();
  initParallaxBackground();
  initTimelineScrollAnimation();
  initTextReveal();
  initImageScrollParallax();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', bootPortfolio);
} else {
  bootPortfolio();
}
