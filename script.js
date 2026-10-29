/**
 * DIGITAL WORLD — CINEMATIC FUTURISTIC PORTFOLIO ARCHITECTURE
 * Awwwards-Inspired Creative Experience & 3D Spatial Systems
 * Specification: DESIGN.md (v5.0 Master Redesign)
 * Author: Zeerak Shafique Portfolio Engineering
 */

// -----------------------------------------------------------------------------
// 01. IMMEDIATE PAGE CONTENT REVEAL
// -----------------------------------------------------------------------------
function initPreloader() {
  const preloader = document.getElementById('preloader');
  if (preloader) {
    preloader.style.display = 'none';
  }
  document.body.classList.add('system-ready');
  revealPageItems();
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
// 05. 3D CARD PERSPECTIVE TILT (DATA-TILT)
// -----------------------------------------------------------------------------
function initCardTilt() {
  if (window.matchMedia('(hover: none)').matches) return;

  const tiltCards = document.querySelectorAll('[data-tilt]');

  tiltCards.forEach((card) => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -4;
      const rotateY = ((x - centerX) / centerX) * 4;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-3px)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0)';
    });
  });
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
  const revealItems = document.querySelectorAll('.section:not(#hero) .reveal-item, .projects-dossier-list .reveal-item, .blog-listing .reveal-item, .article-container .reveal-item, .article-section .reveal-item');

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
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectItems = document.querySelectorAll('.project-dossier-item');

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
          item.style.display = 'grid';
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

// -----------------------------------------------------------------------------
// 09.1 BLOG CATEGORY FILTERING (FOR BLOG PAGE)
// -----------------------------------------------------------------------------
function initBlogFilters() {
  const filterBtns = document.querySelectorAll('.blog-filter-btn');
  const blogItems = document.querySelectorAll('.blog-dossier-item');

  if (!filterBtns.length || !blogItems.length) return;

  filterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      filterBtns.forEach((b) => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      const filterValue = btn.getAttribute('data-filter');

      blogItems.forEach((item) => {
        const itemCategory = item.getAttribute('data-category');
        if (filterValue === 'all' || itemCategory === filterValue) {
          item.style.display = 'grid';
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
  const form = document.getElementById('contact-transmission-form');
  const statusMsg = document.getElementById('form-status-msg');

  if (!form || !statusMsg) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = form.querySelector('#contact-name').value.trim();
    const email = form.querySelector('#contact-email').value.trim();
    const subject = form.querySelector('#contact-subject').value;
    const message = form.querySelector('#contact-message').value.trim();

    if (!name || !email || !message) {
      statusMsg.className = 'form-status-msg error';
      statusMsg.textContent = 'ERROR: All required transmission fields must be filled before dispatch.';
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      statusMsg.className = 'form-status-msg error';
      statusMsg.textContent = 'ERROR: Return transmission address is invalid.';
      return;
    }

    statusMsg.className = 'form-status-msg success';
    statusMsg.innerHTML = `TRANSMISSION VALIDATED // PREPARING MAIL CLIENT FOR ${name.toUpperCase()}...`;

    const encodedSubject = encodeURIComponent(`[Digital World Transmission] ${subject} - from ${name}`);
    const encodedBody = encodeURIComponent(
      `Name: ${name}\nEmail: ${email}\nClassification: ${subject}\n\nMessage Payload:\n${message}\n\n---\nSent via Zeerak Shafique Digital World Terminal`
    );

    setTimeout(() => {
      window.location.href = `mailto:siddiquizeerak@gmail.com?subject=${encodedSubject}&body=${encodedBody}`;
      statusMsg.innerHTML = `Message validated. Mail client launched. You can also reach Zeerak directly at <a href="tel:+919580912686" style="color: #F5F5F5; text-decoration: underline;">+91 9580912686</a> or on Instagram <a href="https://www.instagram.com/_siddiqui_._zeerak_/" target="_blank" rel="noopener noreferrer" style="color: #F5F5F5; text-decoration: underline;">@_siddiqui_._zeerak_</a>.`;
    }, 600);
  });
}

// -----------------------------------------------------------------------------
// 11. BIDIRECTIONAL LIGHT / DARK THEME SYSTEM
// -----------------------------------------------------------------------------
function initThemeToggle() {
  const toggleBtn = document.getElementById('theme-toggle');
  const urlParams = new URLSearchParams(window.location.search);
  const paramTheme = urlParams.get('theme');
  const savedTheme = paramTheme || localStorage.getItem('zs_theme') || document.documentElement.getAttribute('data-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);

  if (!toggleBtn) return;

  const updateAria = (theme) => {
    const isDark = theme === 'dark';
    toggleBtn.setAttribute('aria-label', isDark ? 'Switch to light theme' : 'Switch to dark theme');
    toggleBtn.setAttribute('title', isDark ? 'Switch to light theme' : 'Switch to dark theme');
  };

  updateAria(savedTheme);

  toggleBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', nextTheme);
    localStorage.setItem('zs_theme', nextTheme);
    updateAria(nextTheme);
  });
}

// -----------------------------------------------------------------------------
// 12. MASTER DOM INITIALIZATION
// -----------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initPreloader();
  initThreeScene();
  initHeaderScroll();
  initNavigation();
  initWorldClock();
  initCardTilt();
  initCustomCursor();
  initParticleCursor();
  initScrollReveal();
  initMagneticButtons();
  initProjectFilters();
  initBlogFilters();
  initContactForm();
});
