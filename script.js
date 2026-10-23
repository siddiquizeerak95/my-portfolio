/**
 * OBSIDIAN GOLD — THE DIGITAL ATELIER
 * Master Interactive Architecture & 3D Visual System
 * Specification: DESIGN.md (v3.0 Master Redesign)
 * Author: Zeerak Shafique Portfolio Engineering
 */

// -----------------------------------------------------------------------------
// 01. PRELOADER HUD CONTROLLER (WITH FAILSAFE)
// -----------------------------------------------------------------------------
function initPreloader() {
  const preloader = document.getElementById('preloader');
  const counter = document.getElementById('preloader-counter');
  const progressBar = document.getElementById('preloader-progress-bar');
  const statusText = document.getElementById('preloader-status-text');

  if (!preloader) {
    revealPageItems();
    return;
  }

  let progress = 0;
  let isDismissed = false;

  const dismiss = () => {
    if (isDismissed) return;
    isDismissed = true;
    preloader.classList.add('dismissed');
    document.body.classList.add('system-ready');
    revealPageItems();
  };

  const interval = setInterval(() => {
    progress += Math.floor(Math.random() * 18) + 10;
    if (progress >= 100) {
      progress = 100;
      clearInterval(interval);
      if (counter) counter.textContent = '100%';
      if (progressBar) progressBar.style.width = '100%';
      if (statusText) statusText.textContent = 'ATELIER INITIALIZED // ALL SYSTEMS ONLINE';
      setTimeout(dismiss, 180);
    } else {
      if (counter) counter.textContent = `${progress.toString().padStart(2, '0')}%`;
      if (progressBar) progressBar.style.width = `${progress}%`;
    }
  }, 35);

  // Hard Failsafe: Guarantees page access under 1.2s
  setTimeout(dismiss, 1200);
}

function revealPageItems() {
  const heroItems = document.querySelectorAll('.hero-section .reveal-item, .page-hero-banner .reveal-item');
  heroItems.forEach((item, index) => {
    setTimeout(() => {
      item.classList.add('revealed');
    }, index * 70);
  });
}

// -----------------------------------------------------------------------------
// 02. THREE.JS 3D KINETIC CENTERPIECE — THE GOLDEN GYROSCOPE & OBSIDIAN CORE
// -----------------------------------------------------------------------------
async function initThreeScene() {
  const container = document.getElementById('canvas-container');
  const fallback = document.getElementById('hero-fallback');
  const rotReadout = document.getElementById('hud-rotation-readout');

  if (!container) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    if (fallback) fallback.style.display = 'block';
    return;
  }

  let THREE;
  try {
    THREE = await import('three');
  } catch (err) {
    console.warn('Three.js CDN fallback active:', err);
    if (fallback) fallback.style.display = 'block';
    return;
  }

  try {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, (container.clientWidth || 190) / (container.clientHeight || 380), 0.1, 1000);
    camera.position.set(0, 0, 7.5);

    const renderer = new THREE.WebGLRenderer({
      alpha: true,
      antialias: true,
      powerPreference: 'high-performance'
    });
    renderer.setSize(container.clientWidth || 190, container.clientHeight || 380);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setClearColor(0x000000, 0);
    container.appendChild(renderer.domElement);

    const rootGroup = new THREE.Group();
    scene.add(rootGroup);

    // Central Obsidian Polyhedron Core (Scaled to sit comfortably in dedicated card)
    const coreGeo = new THREE.DodecahedronGeometry(1.0, 0);
    const coreMat = new THREE.MeshStandardMaterial({
      color: 0x121110,
      metalness: 0.92,
      roughness: 0.16
    });
    const coreMesh = new THREE.Mesh(coreGeo, coreMat);
    rootGroup.add(coreMesh);

    // Champagne Gold Architectural Edges
    const edgeGeo = new THREE.EdgesGeometry(coreGeo);
    const edgeMat = new THREE.LineBasicMaterial({
      color: 0xD6B46A,
      linewidth: 1.5,
      transparent: true,
      opacity: 0.88
    });
    const wireframeEdges = new THREE.LineSegments(edgeGeo, edgeMat);
    coreMesh.add(wireframeEdges);

    // Dual Concentric Golden Orbital Rings (Calibrated radii to avoid clipping)
    const ring1Geo = new THREE.TorusGeometry(1.55, 0.015, 16, 100);
    const ring1Mat = new THREE.MeshBasicMaterial({
      color: 0xD6B46A,
      wireframe: true,
      transparent: true,
      opacity: 0.75
    });
    const ring1 = new THREE.Mesh(ring1Geo, ring1Mat);
    ring1.rotation.x = Math.PI * 0.38;
    rootGroup.add(ring1);

    const ring2Geo = new THREE.TorusGeometry(2.05, 0.012, 16, 120);
    const ring2Mat = new THREE.MeshBasicMaterial({
      color: 0x9D7B3C,
      wireframe: true,
      transparent: true,
      opacity: 0.55
    });
    const ring2 = new THREE.Mesh(ring2Geo, ring2Mat);
    ring2.rotation.x = -Math.PI * 0.26;
    rootGroup.add(ring2);

    // Luxurious Studio Lighting
    const ambientLight = new THREE.AmbientLight(0x1a1610, 0.75);
    scene.add(ambientLight);

    const goldKeyLight = new THREE.PointLight(0xD6B46A, 4.2, 18);
    goldKeyLight.position.set(4, 3.5, 4);
    scene.add(goldKeyLight);

    const warmRimLight = new THREE.PointLight(0xF3EFE6, 2.2, 16);
    warmRimLight.position.set(-4, -3, 3);
    scene.add(warmRimLight);

    let targetRotX = 0;
    let targetRotY = 0;

    // Dynamic Camera Distance calculation ensuring 3D sculpture never clips
    function updateViewport() {
      if (!container || !renderer || !camera) return;
      const width = Math.max(container.clientWidth, 60);
      const height = Math.max(container.clientHeight, 60);
      const aspect = width / height;
      camera.aspect = aspect;

      // Outer ring geometry radius is 2.05 + tube. Margin target is 2.35.
      const targetRadius = 2.35;
      const vFovRad = (camera.fov * Math.PI) / 180;
      const distV = targetRadius / Math.sin(vFovRad / 2);
      const hFovRad = 2 * Math.atan(Math.tan(vFovRad / 2) * aspect);
      const distH = targetRadius / Math.sin(hFovRad / 2);
      camera.position.z = Math.max(distV, distH, 6.2);

      camera.updateProjectionMatrix();
      renderer.setSize(width, height);

      // On narrow mobile devices (< 480px), simplify orbit to save GPU cycles and maintain focus
      if (ring2) {
        ring2.visible = window.innerWidth >= 480;
      }
    }

    updateViewport();

    // Use ResizeObserver on container for exact responsiveness
    if (typeof ResizeObserver !== 'undefined') {
      const resizeObserver = new ResizeObserver(() => {
        updateViewport();
      });
      resizeObserver.observe(container);
    }
    window.addEventListener('resize', updateViewport, { passive: true });

    // Interactive Drag & Pointer Tracking
    let isDragging = false;
    let prevPointerX = 0;
    let prevPointerY = 0;
    const sculptureCard = container.closest('.hero-sculpture-card') || container;

    sculptureCard.addEventListener('pointerdown', (e) => {
      isDragging = true;
      prevPointerX = e.clientX;
      prevPointerY = e.clientY;
      try { sculptureCard.setPointerCapture(e.pointerId); } catch (_) {}
    });

    const endDrag = (e) => {
      if (isDragging) {
        isDragging = false;
        try { sculptureCard.releasePointerCapture(e.pointerId); } catch (_) {}
      }
    };
    window.addEventListener('pointerup', endDrag);
    window.addEventListener('pointercancel', endDrag);

    const onPointerMove = (e) => {
      const clientX = e.clientX !== undefined ? e.clientX : (e.touches && e.touches[0].clientX) || 0;
      const clientY = e.clientY !== undefined ? e.clientY : (e.touches && e.touches[0].clientY) || 0;

      if (isDragging) {
        const dx = clientX - prevPointerX;
        const dy = clientY - prevPointerY;
        prevPointerX = clientX;
        prevPointerY = clientY;
        targetRotY += dx * 0.016;
        targetRotX += dy * 0.016;
        return;
      }

      const rect = container.getBoundingClientRect();
      if (rect.width > 0 && rect.height > 0) {
        const mouseX = ((clientX - rect.left) / rect.width) * 2 - 1;
        const mouseY = -(((clientY - rect.top) / rect.height) * 2 - 1);
        targetRotY = Math.max(-1.4, Math.min(1.4, mouseX * 0.75));
        targetRotX = Math.max(-1.1, Math.min(1.1, -mouseY * 0.60));
      }
    };

    window.addEventListener('pointermove', onPointerMove, { passive: true });

    let isSceneVisible = true;
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        isSceneVisible = entry.isIntersecting;
      });
    }, { threshold: 0.1 });
    observer.observe(container);

    let clock = new THREE.Clock();
    const animate = () => {
      requestAnimationFrame(animate);
      if (!isSceneVisible) return;

      const elapsedTime = clock.getElapsedTime();
      coreMesh.rotation.y += (targetRotY - coreMesh.rotation.y) * 0.055;
      coreMesh.rotation.x += (targetRotX - coreMesh.rotation.x) * 0.055;

      rootGroup.rotation.y = elapsedTime * 0.11;
      ring1.rotation.z += 0.008;
      if (ring2 && ring2.visible) {
        ring2.rotation.z -= 0.005;
      }

      if (rotReadout) {
        const degX = (coreMesh.rotation.x * (180 / Math.PI)).toFixed(1);
        const degY = (coreMesh.rotation.y * (180 / Math.PI)).toFixed(1);
        rotReadout.textContent = `ROT_X: ${degX}° | ROT_Y: ${degY}°`;
      }

      renderer.render(scene, camera);
    };

    animate();
  } catch (sceneErr) {
    console.error('WebGL scene error:', sceneErr);
    if (fallback) fallback.style.display = 'block';
  }
}

// -----------------------------------------------------------------------------
// 03. SHARED MULTIPAGE NAVIGATION & MOBILE DRAWER
// -----------------------------------------------------------------------------
function initNavigation() {
  const currentPage = document.body.getAttribute('data-page') || 'home';
  const navItems = document.querySelectorAll('.nav-item');
  const mobileLinks = document.querySelectorAll('.mobile-link');
  const mobileToggle = document.getElementById('mobile-toggle');
  const mobileClose = document.getElementById('mobile-close');
  const mobileDrawer = document.getElementById('mobile-drawer');

  // Highlight active link matching current page
  navItems.forEach((link) => {
    const href = link.getAttribute('href') || '';
    if (
      (currentPage === 'home' && (href === 'index.html' || href === './' || href === '/')) ||
      href.includes(currentPage)
    ) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });

  mobileLinks.forEach((link) => {
    const href = link.getAttribute('href') || '';
    if (
      (currentPage === 'home' && (href === 'index.html' || href === './' || href === '/')) ||
      href.includes(currentPage)
    ) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });

  // Mobile Drawer Toggle
  if (mobileToggle && mobileDrawer) {
    const toggleDrawer = (open) => {
      const isOpen = open !== undefined ? open : !mobileDrawer.classList.contains('open');
      mobileDrawer.classList.toggle('open', isOpen);
      mobileToggle.setAttribute('aria-expanded', isOpen.toString());
      mobileDrawer.setAttribute('aria-hidden', (!isOpen).toString());
      document.body.style.overflow = isOpen ? 'hidden' : '';
    };

    mobileToggle.addEventListener('click', () => toggleDrawer());
    if (mobileClose) mobileClose.addEventListener('click', () => toggleDrawer(false));

    mobileLinks.forEach((link) => {
      link.addEventListener('click', () => toggleDrawer(false));
    });

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileDrawer.classList.contains('open')) {
        toggleDrawer(false);
      }
    });
  }
}

// -----------------------------------------------------------------------------
// 04. ONE-CLICK EMAIL / TRANSMISSION ADDRESS CAPSULE
// -----------------------------------------------------------------------------
function initEmailTransmission() {
  const emailCapsule = document.getElementById('email-capsule');
  const copyBtn = document.getElementById('btn-copy-email');
  const copyLabel = document.getElementById('copy-btn-label');
  const targetEmail = document.getElementById('target-email');

  const copyAddress = async () => {
    const emailToCopy = targetEmail ? targetEmail.textContent.trim() : 'siddiquizeerak@gmail.com';

    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(emailToCopy);
      } else {
        const textArea = document.createElement('textarea');
        textArea.value = emailToCopy;
        textArea.style.position = 'fixed';
        textArea.style.left = '-9999px';
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
      }

      if (copyLabel) copyLabel.textContent = 'COPIED TO CLIPBOARD // OK';
      if (copyBtn) copyBtn.classList.add('copied');

      setTimeout(() => {
        if (copyLabel) copyLabel.textContent = 'COPY ADDRESS';
        if (copyBtn) copyBtn.classList.remove('copied');
      }, 2500);
    } catch (err) {
      console.error('Failed to copy address:', err);
      if (copyLabel) copyLabel.textContent = 'COPY FAILED';
    }
  };

  if (copyBtn) {
    copyBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      copyAddress();
    });
  }

  if (emailCapsule) {
    emailCapsule.addEventListener('click', copyAddress);
  }
}

// -----------------------------------------------------------------------------
// 05. REAL-TIME INDIAN STANDARD TIME WORLD CLOCK (ASIA/KOLKATA)
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
// 06. 3D CARD PERSPECTIVE TILT (DATA-TILT)
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
// 07. CUSTOM DUAL-STATE PRECISION GOLD CURSOR
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
    const targets = document.querySelectorAll('a, button, [data-tilt], .skill-card, .email-capsule, input, textarea, select');
    targets.forEach((el) => {
      el.addEventListener('mouseenter', () => cursor.classList.add('hovering'));
      el.addEventListener('mouseleave', () => cursor.classList.remove('hovering'));
    });
  };
  updateHoverTargets();
}

// -----------------------------------------------------------------------------
// 08. SCROLL REVEAL (INTERSECTION OBSERVER)
// -----------------------------------------------------------------------------
function initScrollReveal() {
  const revealItems = document.querySelectorAll('.section:not(#hero) .reveal-item, .projects-dossier-list .reveal-item');

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
// 09. MAGNETIC BUTTON MICRO-INTERACTION
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
// 10. PROJECT CATEGORY FILTERING (FOR PROJECTS PAGE)
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
// 11. CONTACT TRANSMISSION FORM HANDLER
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

    const encodedSubject = encodeURIComponent(`[Portfolio Transmission] ${subject} - from ${name}`);
    const encodedBody = encodeURIComponent(
      `Name: ${name}\nEmail: ${email}\nClassification: ${subject}\n\nMessage Payload:\n${message}\n\n---\nSent via Zeerak Shafique Atelier Terminal`
    );

    setTimeout(() => {
      window.location.href = `mailto:siddiquizeerak@gmail.com?subject=${encodedSubject}&body=${encodedBody}`;
      statusMsg.innerHTML = `TRANSMISSION DISPATCHED // Mail client launched. If it didn't open, please send directly to <a href="mailto:siddiquizeerak@gmail.com" style="color: #D6B46A;">siddiquizeerak@gmail.com</a>.`;
    }, 700);
  });
}

// -----------------------------------------------------------------------------
// 12. MASTER DOM INITIALIZATION
// -----------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  initPreloader();
  initThreeScene();
  initNavigation();
  initEmailTransmission();
  initWorldClock();
  initCardTilt();
  initCustomCursor();
  initScrollReveal();
  initMagneticButtons();
  initProjectFilters();
  initContactForm();
});
