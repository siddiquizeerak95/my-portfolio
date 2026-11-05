import subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# Run with --dump-dom or evaluate javascript
script = """
setTimeout(() => {
  const c0 = document.getElementById('b3d-card-0');
  const c1 = document.getElementById('b3d-card-1');
  const c2 = document.getElementById('b3d-card-2');
  const sec = document.getElementById('blog-3d-experience');
  const view = document.querySelector('.blog-3d-sticky-viewport');
  const pin = document.querySelector('.pin-spacer');
  
  console.log('DEBUG_INFO:' + JSON.stringify({
    scrollY: window.scrollY,
    secRect: sec ? sec.getBoundingClientRect() : null,
    viewRect: view ? view.getBoundingClientRect() : null,
    pinRect: pin ? pin.getBoundingClientRect() : null,
    c0_style: c0 ? { transform: c0.style.transform, opacity: c0.style.opacity, rect: c0.getBoundingClientRect() } : null,
    c1_style: c1 ? { transform: c1.style.transform, opacity: c1.style.opacity, rect: c1.getBoundingClientRect() } : null,
    c2_style: c2 ? { transform: c2.style.transform, opacity: c2.style.opacity, rect: c2.getBoundingClientRect() } : null,
  }));
}, 300);
"""

# Let's write an html or inject this script into blog.html temporarily

