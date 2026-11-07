/**
 * ZS STUDIO — Local Offline Decryption Utility
 * Decrypts incoming PGP-encrypted messages using your private key.
 *
 * Usage:
 *   1. Direct paste: node decrypt_message.js
 *   2. File input:   node decrypt_message.js path/to/encrypted_message.txt
 */

import fs from 'fs';
import readline from 'readline';
import vm from 'vm';

const privateKeyPath = 'keys/zeerak_private_KEY_KEEP_SAFE.asc';

if (!fs.existsSync(privateKeyPath)) {
  console.error(`\n❌ ERROR: Private key file not found at ${privateKeyPath}`);
  console.error('Please make sure your private key is located in the keys/ directory.\n');
  process.exit(1);
}

const privateKeyArmored = fs.readFileSync(privateKeyPath, 'utf8');

// Load OpenPGP in isolated sandbox
const openpgpCode = fs.readFileSync('vendor/openpgp.min.js', 'utf8');
const context = {
  global: {},
  window: {},
  console,
  crypto,
  TextEncoder,
  TextDecoder,
  Uint8Array,
  atob: (s) => Buffer.from(s, 'base64').toString('binary'),
  btoa: (s) => Buffer.from(s, 'binary').toString('base64'),
  setTimeout,
  clearTimeout
};
context.self = context;
context.window = context;
context.global = context;
vm.runInNewContext(openpgpCode, context);
const openpgp = context.openpgp || context.window.openpgp;

async function decryptText(armoredMessage) {
  try {
    const privKeyObj = await openpgp.readPrivateKey({ armoredKey: privateKeyArmored });
    const message = await openpgp.readMessage({ armoredMessage: armoredMessage.trim() });
    const { data: decrypted } = await openpgp.decrypt({
      message,
      decryptionKeys: privKeyObj
    });

    console.log('\n======================================================');
    console.log('🔓 DECRYPTED MESSAGE CONTENT:');
    console.log('======================================================\n');
    console.log(decrypted);
    console.log('\n======================================================\n');
  } catch (err) {
    console.error('\n❌ Decryption failed:', err.message);
    console.error('Verify that the entire PGP block was pasted (including -----BEGIN PGP MESSAGE----- and -----END PGP MESSAGE-----).\n');
  }
}

// Check if file argument provided
const args = process.argv.slice(2);
if (args.length > 0 && fs.existsSync(args[0])) {
  const content = fs.readFileSync(args[0], 'utf8');
  decryptText(content);
} else {
  console.log('\n======================================================');
  console.log('ZS STUDIO — OFFLINE MESSAGE DECRYPTION TOOL');
  console.log('======================================================');
  console.log('Paste your encrypted PGP message below.');
  console.log('When finished, press ENTER and then CTRL+D (or CTRL+Z on Windows then Enter):\n');

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
  });

  let lines = [];
  rl.on('line', (line) => {
    lines.push(line);
  });

  rl.on('close', () => {
    const text = lines.join('\n');
    if (text.trim()) {
      decryptText(text);
    } else {
      console.log('No text received.');
    }
  });
}

