const http = require('http');
const { spawn } = require('child_process');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function main() {
  const chromeProc = spawn(CHROME, [
    '--headless=new',
    '--remote-debugging-port=9223',
    '--disable-gpu',
    '--window-size=1440,900',
    'http://127.0.0.1:5500/blog.html'
  ]);

  // wait 1.5s
  await new Promise(r => setTimeout(r, 1500));

  try {
    const list = await new Promise((resolve, reject) => {
      http.get('http://127.0.0.1:9223/json', res => {
        let d = '';
        res.on('data', c => d += c);
        res.on('end', () => resolve(JSON.parse(d)));
      }).on('error', reject);
    });

    const page = list.find(t => t.type === 'page');
    console.log('Page found:', page.url, page.webSocketDebuggerUrl);

    const ws = new WebSocket(page.webSocketDebuggerUrl);
    await new Promise(r => ws.onopen = r);

    let id = 1;
    function send(method, params = {}) {
      return new Promise((resolve) => {
        const msgId = id++;
        const handler = (event) => {
          const res = JSON.parse(event.data);
          if (res.id === msgId) {
            ws.removeEventListener('message', handler);
            resolve(res.result);
          }
        };
        ws.addEventListener('message', handler);
        ws.send(JSON.stringify({ id: msgId, method, params }));
      });
    }

    await send('Runtime.enable');
    await send('Page.enable');

    // Wait for GSAP and load
    await new Promise(r => setTimeout(r, 1000));

    // Test different scroll positions
    const scrollPositions = [0, 200, 500, 800, 1100, 1400, 1700, 2000, 2500];
    const fs = require('fs');

    for (const y of scrollPositions) {
      await send('Runtime.evaluate', {
        expression: `window.scrollTo(0, ${y}); window.ScrollTrigger && window.ScrollTrigger.update();`
      });
      await new Promise(r => setTimeout(r, 200));

      const evalRes = await send('Runtime.evaluate', {
        expression: `(() => {
          const c0 = document.getElementById('b3d-card-0');
          const c1 = document.getElementById('b3d-card-1');
          const c2 = document.getElementById('b3d-card-2');
          const sec = document.getElementById('blog-3d-experience');
          const st = window.ScrollTrigger ? window.ScrollTrigger.getAll()[0] : null;
          return {
            scrollY: window.scrollY,
            st_prog: st ? st.progress : null,
            sec_top: sec ? sec.getBoundingClientRect().top : null,
            c0_op: c0 ? getComputedStyle(c0).opacity : null,
            c1_op: c1 ? getComputedStyle(c1).opacity : null,
            c2_op: c2 ? getComputedStyle(c2).opacity : null,
            c0_rect: c0 ? c0.getBoundingClientRect() : null,
            c1_rect: c1 ? c1.getBoundingClientRect() : null,
            c2_rect: c2 ? c2.getBoundingClientRect() : null
          };
        })()`,
        returnByValue: true
      });

      console.log(`SCROLL ${y}:`, JSON.stringify(evalRes.value));

      const screenshot = await send('Page.captureScreenshot', { format: 'png' });
      fs.writeFileSync(`C:\\Users\\siddi\\.gemini\\antigravity\\brain\\4dd10c7b-bb97-46d2-a619-344ea8415c35\\cdp_scroll_${y}.png`, Buffer.from(screenshot.data, 'base64'));
    }

    ws.close();
  } finally {
    chromeProc.kill();
  }
}

main().catch(console.error);

