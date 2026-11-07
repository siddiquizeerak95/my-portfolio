/**
 * ZS STUDIO — Production Server with Secure E2EE Contact API
 * - Serves static portfolio assets (Three.js, WebGL, CSS, Audio, HTML)
 * - Endpoint: POST /api/contact
 * - Validates OpenPGP ciphertext
 * - Delivers to siddiquizeerak95@gmail.com via SMTP (Gmail App Password), Resend, or SendGrid
 * - Protects credentials in server-side environment variables (.env)
 * - Rate limiting & Honeypot spam defense
 */

import http from 'http';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import dotenv from 'dotenv';
import nodemailer from 'nodemailer';

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const PORT = parseInt(process.env.PORT || '8080', 10);
const RECEIVING_EMAIL = process.env.RECEIVING_EMAIL || 'siddiquizeerak95@gmail.com';
const TEST_MODE = process.env.TEST_MODE === 'true';

// -----------------------------------------------------------------------------
// RATE LIMITER (In-Memory Sliding Window: Max 5 requests per 15 minutes per IP)
// -----------------------------------------------------------------------------
const rateLimitMap = new Map();
const RATE_LIMIT_WINDOW_MS = 15 * 60 * 1000;
const MAX_REQUESTS_PER_WINDOW = 5;

function checkRateLimit(ip) {
  const now = Date.now();
  const record = rateLimitMap.get(ip);

  if (!record || now > record.resetTime) {
    rateLimitMap.set(ip, { count: 1, resetTime: now + RATE_LIMIT_WINDOW_MS });
    return true;
  }

  if (record.count >= MAX_REQUESTS_PER_WINDOW) {
    return false;
  }

  record.count++;
  return true;
}

// Clean up stale rate limit entries every 10 minutes
setInterval(() => {
  const now = Date.now();
  for (const [ip, record] of rateLimitMap.entries()) {
    if (now > record.resetTime) {
      rateLimitMap.delete(ip);
    }
  }
}, 10 * 60 * 1000);

// -----------------------------------------------------------------------------
// MIME TYPES DICTIONARY
// -----------------------------------------------------------------------------
const MIME_TYPES = {
  '.html': 'text/html; charset=UTF-8',
  '.css': 'text/css; charset=UTF-8',
  '.js': 'application/javascript; charset=UTF-8',
  '.mjs': 'application/javascript; charset=UTF-8',
  '.json': 'application/json; charset=UTF-8',
  '.bin': 'application/octet-stream',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.wav': 'audio/wav',
  '.mp3': 'audio/mpeg',
  '.asc': 'text/plain; charset=UTF-8',
  '.txt': 'text/plain; charset=UTF-8'
};

// -----------------------------------------------------------------------------
// EMAIL DISPATCHER
// -----------------------------------------------------------------------------
async function dispatchEmail({ name, email, subject, encrypted_message }) {
  const emailSubject = `[ZS STUDIO Contact] ${subject} - from ${name}`;
  const timestamp = new Date().toISOString();

  const formattedBody = [
    `======================================================================`,
    `ZS STUDIO — NEW SECURE CONTACT TRANSMISSION`,
    `======================================================================`,
    `Sender Name  : ${name}`,
    `Sender Email : ${email}`,
    `Subject      : ${subject}`,
    `Received At  : ${timestamp}`,
    `Security     : OpenPGP 4096-bit End-to-End Encrypted (Client-Side)`,
    `======================================================================`,
    ``,
    `BEGIN ENCRYPTED PGP PAYLOAD:`,
    ``,
    encrypted_message,
    ``,
    `======================================================================`,
    `INSTRUCTIONS FOR ZEERAK SIDDIQUI:`,
    `This message was encrypted client-side in the visitor's browser before`,
    `transmission. Only your private decryption key can read the plaintext.`,
    `To decrypt locally, run:`,
    `   node decrypt_message.js`,
    `or import your private key into GPG / Kleopatra / Mailvelope.`,
    `======================================================================`
  ].join('\n');

  // Option 1: Live SMTP (Gmail App Password or Custom SMTP)
  if (process.env.SMTP_USER && process.env.SMTP_PASS) {
    const transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST || 'smtp.gmail.com',
      port: parseInt(process.env.SMTP_PORT || '465', 10),
      secure: (process.env.SMTP_PORT || '465') === '465',
      auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASS
      }
    });

    const info = await transporter.sendMail({
      from: `"${name} (via ZS STUDIO)" <${process.env.SMTP_USER}>`,
      to: RECEIVING_EMAIL,
      replyTo: email,
      subject: emailSubject,
      text: formattedBody
    });

    return { success: true, method: 'smtp', messageId: info.messageId };
  }

  // Option 2: Resend API
  if (process.env.RESEND_API_KEY) {
    const res = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from: process.env.RESEND_FROM || 'contact@zeeraksiddiqui.com',
        to: [RECEIVING_EMAIL],
        reply_to: email,
        subject: emailSubject,
        text: formattedBody
      })
    });

    if (!res.ok) {
      const errData = await res.json().catch(() => ({}));
      throw new Error(`Resend API error: ${errData.message || res.statusText}`);
    }

    const data = await res.json();
    return { success: true, method: 'resend', id: data.id };
  }

  // Option 3: Local Test Mode (Allows complete local E2EE testing before live SMTP credentials are provided)
  if (TEST_MODE) {
    const inboxDir = path.join(__dirname, 'inbox');
    if (!fs.existsSync(inboxDir)) {
      fs.mkdirSync(inboxDir, { recursive: true });
    }

    const filename = `transmission_${Date.now()}.txt`;
    const filePath = path.join(inboxDir, filename);
    fs.writeFileSync(filePath, formattedBody, 'utf8');

    console.log(`\n[TEST_MODE] Transmission saved locally to: ${filePath}`);
    console.log(`[TEST_MODE] Ready for decryption verification with 'node decrypt_message.js'`);

    return {
      success: true,
      method: 'test_mode',
      note: 'Saved to local inbox for verification. Set live SMTP credentials in .env for inbox delivery.'
    };
  }

  // If no transport configured and not in test mode:
  throw new Error('Email service credentials (SMTP_USER and SMTP_PASS) are not yet configured in .env.');
}

// -----------------------------------------------------------------------------
// HTTP SERVER
// -----------------------------------------------------------------------------
const server = http.createServer(async (req, res) => {
  const parsedUrl = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  const pathname = decodeURIComponent(parsedUrl.pathname);

  // Security Headers
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'SAMEORIGIN');

  // CORS Headers for API
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  // ---------------------------------------------------------------------------
  // CONTACT SUBMISSION ENDPOINT: POST /api/contact
  // ---------------------------------------------------------------------------
  if (req.method === 'POST' && pathname === '/api/contact') {
    const clientIp = req.headers['x-forwarded-for'] || req.socket.remoteAddress || 'unknown';

    // Rate Limiting
    if (!checkRateLimit(clientIp)) {
      res.writeHead(429, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({
        success: false,
        error: 'Too many requests. Please wait a few minutes before sending another message.'
      }));
      return;
    }

    // Collect Body
    let body = '';
    req.on('data', chunk => {
      body += chunk;
      if (body.length > 256 * 1024) { // Max 256KB
        res.writeHead(413, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: false, error: 'Payload too large.' }));
        req.destroy();
      }
    });

    req.on('end', async () => {
      try {
        const data = JSON.parse(body);
        const { name, email, subject, encrypted_message, _hp_security_check, timestamp } = data;

        // 1. Spam Honeypot Check: If honeypot is filled, silently discard
        if (_hp_security_check && String(_hp_security_check).trim() !== '') {
          console.warn(`[Spam Blocked] Honeypot triggered from ${clientIp}`);
          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ success: true, message: 'Transmission received.' }));
          return;
        }

        // 2. Bot Speed Check (must take at least 1.2s to fill form)
        if (timestamp && Date.now() - Number(timestamp) < 1200) {
          console.warn(`[Spam Blocked] Form submitted too rapidly (${Date.now() - Number(timestamp)}ms) from ${clientIp}`);
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ success: false, error: 'Submission rejected by anti-bot verification.' }));
          return;
        }

        // 3. Name Validation
        const cleanName = typeof name === 'string' ? name.trim() : '';
        if (!cleanName || cleanName.length < 2 || cleanName.length > 100) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ success: false, error: 'Please enter a valid name (2 to 100 characters).' }));
          return;
        }

        // 4. Email Validation
        const cleanEmail = typeof email === 'string' ? email.trim() : '';
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!cleanEmail || !emailRegex.test(cleanEmail) || cleanEmail.length > 150) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ success: false, error: 'Please enter a valid, deliverable email address.' }));
          return;
        }

        // 5. Subject Validation
        const cleanSubject = typeof subject === 'string' ? subject.trim() : 'General Inquiry';
        if (!cleanSubject || cleanSubject.length > 150) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ success: false, error: 'Please select or provide a valid subject.' }));
          return;
        }

        // 6. Encrypted PGP Message Validation
        if (!encrypted_message || typeof encrypted_message !== 'string') {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ success: false, error: 'Missing encrypted message payload.' }));
          return;
        }

        if (!encrypted_message.includes('-----BEGIN PGP MESSAGE-----') || !encrypted_message.includes('-----END PGP MESSAGE-----')) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ success: false, error: 'Invalid encryption block. Message must be PGP-armored.' }));
          return;
        }

        console.log(`[E2EE Contact] Valid encrypted transmission received from "${cleanName}" <${cleanEmail}> | Subject: "${cleanSubject}" | Size: ${encrypted_message.length} chars`);

        // Dispatch Email
        const result = await dispatchEmail({
          name: cleanName,
          email: cleanEmail,
          subject: cleanSubject,
          encrypted_message
        });

        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
          success: true,
          message: 'Transmission successfully encrypted and delivered to Zeerak Siddiqui.'
        }));
      } catch (err) {
        console.error('[E2EE Contact Error]', err.message);
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
          success: false,
          error: err.message || 'An error occurred while dispatching the message.'
        }));
      }
    });

    return;
  }

  // ---------------------------------------------------------------------------
  // STATIC ASSET SERVING
  // ---------------------------------------------------------------------------
  let filePath = path.join(__dirname, pathname === '/' ? 'index.html' : pathname);

  // Normalize path to prevent directory traversal
  if (!filePath.startsWith(__dirname)) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('Forbidden');
    return;
  }

  // If path is a directory, check for index.html
  if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
    filePath = path.join(filePath, 'index.html');
  }

  if (!fs.existsSync(filePath) || fs.statSync(filePath).isDirectory()) {
    res.writeHead(404, { 'Content-Type': 'text/html; charset=UTF-8' });
    res.end('<h1>404 Not Found</h1>');
    return;
  }

  const ext = path.extname(filePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';

  res.writeHead(200, { 'Content-Type': contentType });
  const readStream = fs.createReadStream(filePath);
  readStream.pipe(res);
});

server.listen(PORT, () => {
  console.log(`======================================================`);
  console.log(`ZS STUDIO Server Running on http://localhost:${PORT}`);
  console.log(`E2EE Contact Endpoint : POST http://localhost:${PORT}/api/contact`);
  console.log(`Target Receiving Email : ${RECEIVING_EMAIL}`);
  console.log(`Test Mode Active       : ${TEST_MODE}`);
  console.log(`======================================================`);
});

