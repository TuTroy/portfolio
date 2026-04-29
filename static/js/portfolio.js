/* ────────────────────────────────────────────────────────────────
   Troy Portfolio · portfolio.js
   Vanilla JS · No dependencies
──────────────────────────────────────────────────────────────── */

(function () {
  'use strict';

  /* ── Scroll reveal ─────────────────────────────────────────── */
  const revealEls = document.querySelectorAll('.reveal');
  if (revealEls.length) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (!e.isIntersecting) return;
          e.target.classList.add('visible');
          // Animate skill bars
          const bar = e.target.querySelector('.skill-fill');
          if (bar) bar.style.width = bar.dataset.width + '%';
          io.unobserve(e.target);
        });
      },
      { threshold: 0.05 }
    );
    revealEls.forEach((el) => io.observe(el));
  }

  /* ── Nav scroll behavior ──────────────────────────────────── */
  const navbar = document.getElementById('navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 30);
    }, { passive: true });
  }

  /* ── Mobile nav toggle ────────────────────────────────────── */
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      mobileMenu.classList.toggle('open');
    });
    // Close on link click
    mobileMenu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        mobileMenu.classList.remove('open');
      });
    });
  }

  /* ── Project filter ───────────────────────────────────────── */
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');
  if (filterBtns.length) {
    filterBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        filterBtns.forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.dataset.filter;
        projectCards.forEach((card) => {
          card.style.display =
            filter === 'all' || card.dataset.type === filter ? '' : 'none';
        });
      });
    });
  }

  /* ── Contact form ─────────────────────────────────────────── */
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    const emailInput = document.getElementById('form-email');
    const messageInput = document.getElementById('form-message');
    const submitBtn = document.getElementById('form-submit');
    const successEl = document.getElementById('form-success');
    const formspreeId = contactForm.dataset.formspree || 'YOUR_FORM_ID';

    function showError(input, msg) {
      const field = input.closest('.form-field') || input.parentElement;
      if (!field) return;
      field.classList.add('has-error');
      let err = field.querySelector('.form-error');
      if (!err) {
        err = document.createElement('div');
        err.className = 'form-error';
        field.appendChild(err);
      }
      err.textContent = msg;
    }

    function clearError(input) {
      const field = input.closest('.form-field') || input.parentElement;
      if (!field) return;
      field.classList.remove('has-error');
    }

    function validateEmail(v) {
      return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v);
    }

    emailInput.addEventListener('input', () => clearError(emailInput));
    messageInput.addEventListener('input', () => clearError(messageInput));

    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      clearError(emailInput);
      clearError(messageInput);

      const email = emailInput.value.trim();
      const message = messageInput.value.trim();
      let valid = true;

      if (!email) {
        showError(emailInput, '请输入邮箱');
        valid = false;
      } else if (!validateEmail(email)) {
        showError(emailInput, '请输入有效邮箱');
        valid = false;
      }

      if (!message) {
        showError(messageInput, '请输入想说的话');
        valid = false;
      } else if (message.length < 5) {
        showError(messageInput, '至少5个字符');
        valid = false;
      }

      if (!valid) return;

      submitBtn.disabled = true;
      submitBtn.textContent = '发送中…';

      try {
        const fd = new FormData();
        fd.append('email', email);
        fd.append('message', message);
        const res = await fetch(`https://formspree.io/f/${formspreeId}`, {
          method: 'POST',
          body: fd,
        });
        if (res.ok) {
          contactForm.style.display = 'none';
          successEl.classList.add('show');
        } else {
          showError(messageInput, '发送失败，请重试');
          submitBtn.disabled = false;
          submitBtn.textContent = '发送 →';
        }
      } catch {
        showError(messageInput, '网络错误，请重试');
        submitBtn.disabled = false;
        submitBtn.textContent = '发送 →';
      }
    });
  }

  /* ── Success reset ─────────────────────────────────────────── */
  const successResetBtn = document.getElementById('form-success-reset');
  if (successResetBtn) {
    successResetBtn.addEventListener('click', () => {
      const contactForm = document.getElementById('contact-form');
      const successEl = document.getElementById('form-success');
      if (contactForm) contactForm.style.display = '';
      if (successEl) successEl.classList.remove('show');
      const submitBtn = document.getElementById('form-submit');
      const emailInput = document.getElementById('form-email');
      const messageInput = document.getElementById('form-message');
      if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = '发送 →'; }
      if (emailInput) emailInput.value = '';
      if (messageInput) messageInput.value = '';
    });
  }

})();