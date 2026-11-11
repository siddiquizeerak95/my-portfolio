/**
 * ZS STUDIO — Local Offline Decryption Utility
 * Decrypts incoming PGP-encrypted messages using your private key.
 *
 * Usage:
 *   1. Direct paste: node decrypt_message.js
 *   2. File input:   node decrypt_message.js path/to/encrypted_message.txt
 *   3. Custom key:   node decrypt_message.js --key path/to/key.asc path/to/encrypted_message.txt
 *   4. Help:         node decrypt_message.js --help
 */

import fs from 'fs';
import readline from 'readline';
import vm from 'vm';
import dotenv from 'dotenv';

dotenv.config();

const rawArgs = process.argv.slice(2);

// 1. Handle --help / -h
if (rawArgs.includes('--help') || rawArgs.includes('-h')) {
  console.log(`
ZS STUDIO — Local Offline Decryption Utility
Decrypts incoming PGP-encrypted messages using your private key.

Usage:
  node decrypt_message.js [options] [path/to/encrypted_message.txt]

Options:
  -k, --key <path>   Path to armored private key file
  -h, --help         Show this help message

Key Resolution Hierarchy:
  1. CLI flag: --key <path> or -k <path>
  2. Environment variable: PRIVATE_KEY_PATH (or via .env)
  3. Default fallback: keys/zeerak_private_KEY_KEEP_SAFE.asc

Modes:
  - File input:        node decrypt_message.js path/to/message.txt
  - Custom key + file: node decrypt_message.js -k path/to/key.asc path/to/message.txt
  - Interactive stdin: node decrypt_message.js [-k path/to/key.asc] (paste message and press Ctrl+D or Ctrl+Z)
  - Piped stdin:       cat message.txt | node decrypt_message.js [-k path/to/key.asc]
`);
  process.exit(0);
}

// 2. Parse arguments decoupling --key/-k from input file
let customKeyPath = null;
let messageFilePath = null;

for (let i = 0; i < rawArgs.length; i++) {
  const arg = rawArgs[i];
  if (arg === '--key' || arg === '-k') {
    if (i + 1 < rawArgs.length) {
      customKeyPath = rawArgs[++i];
    }
  } else if (arg.startsWith('--key=')) {
    customKeyPath = arg.slice('--key='.length);
  } else if (arg.startsWith('-k=')) {
    customKeyPath = arg.slice('-k='.length);
  } else if (!arg.startsWith('-')) {
    if (!messageFilePath) {
      messageFilePath = arg;
    }
  }
}

// 3. Resolve private key path using 3-tier hierarchy
const DEFAULT_KEY_PATH = 'keys/zeerak_private_KEY_KEEP_SAFE.asc';
const privateKeyPath = customKeyPath || process.env.PRIVATE_KEY_PATH || DEFAULT_KEY_PATH;

if (!fs.existsSync(privateKeyPath)) {
  console.error(`\n❌ ERROR: Private key file not found at: ${privateKeyPath}`);
  console.error('Troubleshooting:');
  console.error('  1. Specify your key with: node decrypt_message.js --key <path_to_key.asc>');
  console.error('  2. Or set PRIVATE_KEY_PATH in your environment or .env file.');
  console.error(`  3. Or place your private key at the default path: ${DEFAULT_KEY_PATH}\n`);
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

// 4. Execution Mode: File Input or Interactive/Piped Stdin
if (messageFilePath) {
  if (fs.existsSync(messageFilePath)) {
    const content = fs.readFileSync(messageFilePath, 'utf8');
    decryptText(content);
  } else {
    console.error(`\n❌ ERROR: Message file not found at: ${messageFilePath}\n`);
    process.exit(1);
  }
} else {
  // If stdin is interactive TTY, print welcoming guidance
  if (process.stdin.isTTY) {
    console.log('\n======================================================');
    console.log('ZS STUDIO — OFFLINE MESSAGE DECRYPTION TOOL');
    console.log('======================================================');
    console.log('Paste your encrypted PGP message below.');
    console.log('When finished, press ENTER and then CTRL+D (or CTRL+Z on Windows then Enter):\n');
  }

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
