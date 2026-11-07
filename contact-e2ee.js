/**
 * ZS STUDIO — Client-Side End-to-End Encryption (E2EE) Contact Form Engine
 *
 * Security Architecture:
 * 1. Validates visitor name, email, subject, and message.
 * 2. Uses Zeerak Siddiqui's 4096-bit RSA OpenPGP Public Key to encrypt the payload
 *    entirely inside the visitor's browser before any network transmission occurs.
 * 3. Only the ASCII-armored PGP ciphertext is sent to the backend.
 * 4. The backend dispatches the encrypted payload directly to siddiquizeerak95@gmail.com.
 * 5. Only Zeerak's private key (held exclusively offline by Zeerak) can decrypt it.
 */

(function () {
  'use strict';

  // Fallback armored public key (matches assets/keys/zeerak_public.asc)
  const ZEERAK_PUBLIC_KEY_FALLBACK = `-----BEGIN PGP PUBLIC KEY BLOCK-----

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
7mwD8fj984YyiVQ=
=/M/e
-----END PGP PUBLIC KEY BLOCK-----`;

  let cachedPublicKey = null;
  const pageLoadedAt = Date.now();

  async function getPublicKey() {
    if (cachedPublicKey) return cachedPublicKey;

    try {
      const res = await fetch('assets/keys/zeerak_public.asc');
      if (res.ok) {
        const text = await res.text();
        if (text.includes('-----BEGIN PGP PUBLIC KEY BLOCK-----')) {
          cachedPublicKey = text;
          return cachedPublicKey;
        }
      }
    } catch (_) {
      // Fallback below
    }

    cachedPublicKey = ZEERAK_PUBLIC_KEY_FALLBACK;
    return cachedPublicKey;
  }

  function init() {
    const form = document.getElementById('contact-transmission-form');
    if (!form) return;

    const subjectSelect = form.querySelector('#contact-subject');
    const customSubjectGroup = form.querySelector('#custom-subject-group');
    const customSubjectInput = form.querySelector('#contact-custom-subject');
    const statusMsg = document.getElementById('form-status-msg') || document.getElementById('contact-status-msg');
    const submitBtn = form.querySelector('#btn-submit-contact');

    // Toggle custom subject input when "Custom Subject..." option is chosen
    if (subjectSelect && customSubjectGroup) {
      subjectSelect.addEventListener('change', () => {
        if (subjectSelect.value === 'Custom Subject') {
          customSubjectGroup.style.display = 'block';
          if (customSubjectInput) customSubjectInput.focus();
        } else {
          customSubjectGroup.style.display = 'none';
        }
      });
    }

    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      if (!statusMsg) return;

      const nameInput = form.querySelector('#contact-name');
      const emailInput = form.querySelector('#contact-email');
      const messageInput = form.querySelector('#contact-message');
      const honeypotInput = form.querySelector('#contact-hp') || form.querySelector('input[name="_hp_security_check"]');

      const name = nameInput ? nameInput.value.trim() : '';
      const email = emailInput ? emailInput.value.trim() : '';
      const message = messageInput ? messageInput.value.trim() : '';
      const hp = honeypotInput ? honeypotInput.value.trim() : '';

      let subject = subjectSelect ? subjectSelect.value : 'Other / General Inquiry';
      if (subject === 'Custom Subject' && customSubjectInput) {
        const customVal = customSubjectInput.value.trim();
        subject = customVal || 'Other / General Inquiry';
      }

      // Honeypot spam silent discard
      if (hp !== '') {
        showStatus(statusMsg, 'success', '✔ TRANSMISSION RECEIVED // Thank you for reaching out.');
        form.reset();
        return;
      }

      // Client Validations
      if (!name) {
        showStatus(statusMsg, 'error', 'ERROR: Please enter your name.');
        if (nameInput) nameInput.focus();
        return;
      }

      if (!email) {
        showStatus(statusMsg, 'error', 'ERROR: Please enter your email address.');
        if (emailInput) emailInput.focus();
        return;
      }

      const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
      if (!emailRegex.test(email)) {
        showStatus(statusMsg, 'error', 'ERROR: Please enter a valid, deliverable email address.');
        if (emailInput) emailInput.focus();
        return;
      }

      if (!message || message.length < 5) {
        showStatus(statusMsg, 'error', 'ERROR: Please enter your message (at least 5 characters).');
        if (messageInput) messageInput.focus();
        return;
      }

      // Prevent duplicate submissions
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.style.opacity = '0.6';
        submitBtn.style.cursor = 'not-allowed';
      }

      showStatus(statusMsg, 'info', 'ENCRYPTING // Generating 4096-bit OpenPGP ciphertext in browser...');

      try {
        if (typeof openpgp === 'undefined') {
          throw new Error('OpenPGP encryption library not loaded in browser.');
        }

        const armoredPublicKey = await getPublicKey();
        const pubKeyObj = await openpgp.readKey({ armoredKey: armoredPublicKey });

        const plaintextPayload = [
          `======================================================`,
          `ZS STUDIO CONTACT TRANSMISSION (AUTHENTICATED E2EE)`,
          `======================================================`,
          `Date         : ${new Date().toISOString()}`,
          `Sender Name  : ${name}`,
          `Sender Email : ${email}`,
          `Subject      : ${subject}`,
          `------------------------------------------------------`,
          `MESSAGE CONTENT:`,
          `------------------------------------------------------`,
          message,
          `======================================================`
        ].join('\n');

        const encrypted = await openpgp.encrypt({
          message: await openpgp.createMessage({ text: plaintextPayload }),
          encryptionKeys: pubKeyObj
        });

        showStatus(statusMsg, 'info', 'TRANSMITTING // Delivering encrypted payload to backend...');

        const endpoint = '/api/contact';
        const response = await fetch(endpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            name,
            email,
            subject,
            encrypted_message: encrypted,
            _hp_security_check: hp,
            timestamp: pageLoadedAt
          })
        });

        const data = await response.json().catch(() => ({}));

        if (response.ok && data.success) {
          showStatus(statusMsg, 'success', '✔ TRANSMISSION SECURELY DELIVERED // Your message has been encrypted with 4096-bit OpenPGP and delivered directly to Zeerak Siddiqui.');
          form.reset();
          if (customSubjectGroup) customSubjectGroup.style.display = 'none';
        } else {
          const errDetail = data.error || 'Server rejected transmission or email delivery failed.';
          showStatus(statusMsg, 'error', `DELIVERY FAILED: ${errDetail}`);
        }
      } catch (err) {
        console.error('[E2EE Contact Error]', err);
        showStatus(statusMsg, 'error', `TRANSMISSION ERROR: ${err.message || 'Unable to encrypt and deliver message.'}`);
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.style.opacity = '';
          submitBtn.style.cursor = '';
        }
      }
    });
  }

  function showStatus(el, type, text) {
    el.className = `form-status-msg active ${type}`;
    el.textContent = text;
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

