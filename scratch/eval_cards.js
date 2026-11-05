import subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# Evaluate in chrome
code = """
(() => {
  const c0 = document.getElementById('b3d-card-0');
  const c1 = document.getElementById('b3d-card-1');
  const c2 = document.getElementById('b3d-card-2');
  return {
    c0: { opacity: getComputedStyle(c0).opacity, display: getComputedStyle(c0).display, visibility: getComputedStyle(c0).visibility, transform: getComputedStyle(c0).transform },
    c1: { opacity: getComputedStyle(c1).opacity, display: getComputedStyle(c1).display, visibility: getComputedStyle(c1).visibility, transform: getComputedStyle(c1).transform },
    c2: { opacity: getComputedStyle(c2).opacity, display: getComputedStyle(c2).display, visibility: getComputedStyle(c2).visibility, transform: getComputedStyle(c2).transform },
    stage: document.getElementById('blog-3d-cards-stage').getBoundingClientRect(),
    viewport: document.querySelector('.blog-3d-sticky-viewport').getBoundingClientRect(),
    experience: document.getElementById('blog-3d-experience').getBoundingClientRect()
  };
})()
"""

