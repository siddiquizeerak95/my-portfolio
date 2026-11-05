/**
 * ZS STUDIO — 3D SCROLL-DRIVEN BLOG ENGINE
 * Exclusively for blog.html
 * Powered by GSAP ScrollTrigger with visible 3D card deck depth.
 */

(function () {
  'use strict';

  const topics = [
    'Web Architecture',
    'Developer Journey',
    'Design Philosophy'
  ];

  function initBlog3D() {
    const experienceSec = document.getElementById('blog-3d-experience');
    const cards = [
      document.getElementById('b3d-card-0'),
      document.getElementById('b3d-card-1'),
      document.getElementById('b3d-card-2')
    ].filter(Boolean);

    if (!experienceSec || cards.length === 0) return;

    const counterNum = document.getElementById('b3d-active-num');
    const topicTicker = document.getElementById('b3d-topic-ticker');
    const pills = document.querySelectorAll('.b3d-pill-btn');
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Helper: update header telemetry
    let currentActiveIndex = 0;
    function updateTelemetry(index) {
      if (index === currentActiveIndex) return;
      currentActiveIndex = index;
      if (counterNum) counterNum.textContent = String(index + 1).padStart(2, '0');
      if (topicTicker) {
        topicTicker.style.opacity = '0';
        setTimeout(() => {
          topicTicker.textContent = topics[index] || '';
          topicTicker.style.opacity = '1';
        }, 120);
      }
      pills.forEach((p, idx) => {
        p.classList.toggle('active', idx === index);
        p.setAttribute('aria-selected', idx === index ? 'true' : 'false');
      });
    }

    // Interactive Card Specular Glare on Mouse Movement
    if (window.matchMedia('(pointer: fine)').matches && !prefersReducedMotion) {
      cards.forEach((card) => {
        card.addEventListener('mousemove', (e) => {
          if (parseInt(card.getAttribute('data-card-index'), 10) !== currentActiveIndex) return;
          const rect = card.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          card.style.setProperty('--glare-x', `${x}px`);
          card.style.setProperty('--glare-y', `${y}px`);
          card.style.setProperty('--glare-opacity', '1');
        }, { passive: true });

        card.addEventListener('mouseleave', () => {
          card.style.setProperty('--glare-opacity', '0');
        });
      });
    }

    // Helper: click queued cards to advance
    cards.forEach((card, idx) => {
      card.addEventListener('click', (e) => {
        if (e.target.closest('.b3d-cta-btn')) return;
        if (idx !== currentActiveIndex && pills[idx]) {
          pills[idx].click();
        }
      });
    });

    // Check for ?scroll=URL query parameter for headless testing
    const urlParams = new URLSearchParams(window.location.search);
    const scrollTarget = urlParams.get('scroll');
    if (scrollTarget) {
      const targetY = parseInt(scrollTarget, 10);
      window.scrollTo(0, targetY);
      setTimeout(() => {
        window.scrollTo(0, targetY);
        if (window.ScrollTrigger) window.ScrollTrigger.update();
        const st = window.ScrollTrigger ? window.ScrollTrigger.getById('b3d-trigger') || window.ScrollTrigger.getAll()[0] : null;
        const sec = document.getElementById('blog-3d-experience');
        const view = document.querySelector('.blog-3d-sticky-viewport');
        const pin = document.querySelector('.pin-spacer');
        const c0 = document.getElementById('b3d-card-0');
        const c1 = document.getElementById('b3d-card-1');
        const c2 = document.getElementById('b3d-card-2');
        console.log('ST_DIAGNOSTIC:', JSON.stringify({
          scrollY: window.scrollY,
          st_start: st ? st.start : null,
          st_end: st ? st.end : null,
          st_progress: st ? st.progress : null,
          sec_top: sec ? sec.getBoundingClientRect().top : null,
          view_top: view ? view.getBoundingClientRect().top : null,
          pin_top: pin ? pin.getBoundingClientRect().top : null,
          c0_op: c0 ? c0.style.opacity : null,
          c1_op: c1 ? c1.style.opacity : null,
          c2_op: c2 ? c2.style.opacity : null,
          c0_trans: c0 ? c0.style.transform : null,
          c1_trans: c1 ? c1.style.transform : null,
          c2_trans: c2 ? c2.style.transform : null,
        }));
      }, 250);
    }

    // =========================================================================
    // GSAP + ScrollTrigger Timeline Implementation
    // =========================================================================
    if (typeof window.gsap !== 'undefined' && typeof window.ScrollTrigger !== 'undefined') {
      window.gsap.registerPlugin(window.ScrollTrigger);

      // Initial card stack in 3D perspective
      window.gsap.set(cards[0], { z: 0, y: 0, scale: 1, opacity: 1, rotateX: 0, zIndex: 3, pointerEvents: 'auto' });
      window.gsap.set(cards[1], { z: -80, y: -30, scale: 0.95, opacity: 0.75, rotateX: 3, zIndex: 2, pointerEvents: 'auto' });
      window.gsap.set(cards[2], { z: -160, y: -60, scale: 0.90, opacity: 0.5, rotateX: 6, zIndex: 1, pointerEvents: 'auto' });

      // Correctly configure Timeline with embedded ScrollTrigger
      const tl = window.gsap.timeline({
        scrollTrigger: {
          trigger: experienceSec,
          start: 'top top',
          end: '+=160%',
          pin: true,
          pinSpacing: true,
          scrub: 0.6,
          anticipatePin: 1,
          onUpdate: (self) => {
            const p = self.progress;
            if (p < 0.4) {
              updateTelemetry(0);
            } else if (p < 0.75) {
              updateTelemetry(1);
            } else {
              updateTelemetry(2);
            }
          }
        }
      });

      // Transition 1: Card 0 moves forward & up, Card 1 takes center stage
      tl.to(cards[0], {
        z: 200,
        y: -80,
        opacity: 0,
        rotateX: -7,
        ease: 'power1.inOut',
        duration: 1
      }, 0.1);

      tl.to(cards[1], {
        z: 0,
        y: 0,
        scale: 1,
        opacity: 1,
        rotateX: 0,
        zIndex: 3,
        ease: 'power1.inOut',
        duration: 1
      }, 0.1);

      tl.to(cards[2], {
        z: -80,
        y: -30,
        scale: 0.95,
        opacity: 0.75,
        rotateX: 3,
        zIndex: 2,
        ease: 'power1.inOut',
        duration: 1
      }, 0.1);

      // Settle pause on Card 1
      tl.to({}, { duration: 0.4 });

      // Transition 2: Card 1 moves forward & up, Card 2 takes center stage
      tl.to(cards[1], {
        z: 200,
        y: -80,
        opacity: 0,
        rotateX: -7,
        ease: 'power1.inOut',
        duration: 1
      }, 1.5);

      tl.to(cards[2], {
        z: 0,
        y: 0,
        scale: 1,
        opacity: 1,
        rotateX: 0,
        zIndex: 3,
        ease: 'power1.inOut',
        duration: 1
      }, 1.5);

      // Settle pause on Card 2 before smooth unpin into articles grid
      tl.to({}, { duration: 0.4 });

      // Pill click navigation
      pills.forEach((pill) => {
        pill.addEventListener('click', (e) => {
          e.preventDefault();
          const targetIdx = parseInt(pill.getAttribute('data-index'), 10);
          if (isNaN(targetIdx)) return;
          const stInstance = tl.scrollTrigger;
          if (!stInstance) return;
          const progressTargets = [0.0, 0.52, 0.95];
          const targetProgress = progressTargets[targetIdx];
          const targetScroll = stInstance.start + (stInstance.end - stInstance.start) * targetProgress;
          window.scrollTo({ top: targetScroll, behavior: 'smooth' });
        });
      });

      // Recalculate ScrollTrigger on load
      window.addEventListener('load', () => {
        window.ScrollTrigger.refresh();
      });

    } else {
      // Native scroll fallback
      let ticking = false;
      function renderNativeScroll() {
        const rect = experienceSec.getBoundingClientRect();
        const totalTravel = experienceSec.offsetHeight - window.innerHeight;
        if (totalTravel <= 0) return;

        const currentOffset = -rect.top;
        const progress = Math.max(0, Math.min(1, currentOffset / totalTravel));

        if (progress < 0.4) updateTelemetry(0);
        else if (progress < 0.75) updateTelemetry(1);
        else updateTelemetry(2);

        const seg1 = Math.max(0, Math.min(1, (progress - 0.1) / 0.35));
        const seg2 = Math.max(0, Math.min(1, (progress - 0.55) / 0.35));

        // Card 0
        cards[0].style.transform = `translate3d(0, ${seg1 * -80}px, ${seg1 * 200}px) rotateX(${seg1 * -7}deg)`;
        cards[0].style.opacity = 1 - seg1;

        // Card 1
        const c1_z = -80 + (seg1 * 80) + (seg2 * 200);
        const c1_y = -30 + (seg1 * 30) - (seg2 * 80);
        const c1_scale = 0.95 + (seg1 * 0.05);
        const c1_rotX = 3 - (seg1 * 3) - (seg2 * 7);
        const c1_op = 0.75 + (seg1 * 0.25) - seg2;
        cards[1].style.transform = `translate3d(0, ${c1_y}px, ${c1_z}px) scale(${c1_scale}) rotateX(${c1_rotX}deg)`;
        cards[1].style.opacity = Math.max(0, c1_op);

        // Card 2
        const c2_z = -160 + (seg1 * 80) + (seg2 * 80);
        const c2_y = -60 + (seg1 * 30) + (seg2 * 30);
        const c2_scale = 0.90 + (seg1 * 0.05) + (seg2 * 0.05);
        const c2_rotX = 6 - (seg1 * 3) - (seg2 * 3);
        const c2_op = 0.5 + (seg1 * 0.25) + (seg2 * 0.25);
        cards[2].style.transform = `translate3d(0, ${c2_y}px, ${c2_z}px) scale(${c2_scale}) rotateX(${c2_rotX}deg)`;
        cards[2].style.opacity = Math.max(0, c2_op);

        ticking = false;
      }

      window.addEventListener('scroll', () => {
        if (!ticking) {
          requestAnimationFrame(renderNativeScroll);
          ticking = true;
        }
      }, { passive: true });

      renderNativeScroll();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBlog3D);
  } else {
    initBlog3D();
  }
})();
