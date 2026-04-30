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
      { threshold: 0.05, rootMargin: '0px 0px -40px 0px' }
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

  /* ── Active nav link on scroll ────────────────────────────── */
  const navLinks = document.querySelectorAll('.nav-links a');
  const sections = ['about', 'skills', 'projects', 'blogs', 'contact'];
  if (navLinks.length) {
    const sectionEls = sections
      .map((id) => document.getElementById(id))
      .filter(Boolean);

    const sectionObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const id = entry.target.id;
          navLinks.forEach((link) => {
            link.classList.toggle('active', link.getAttribute('href') === '#' + id);
          });
        });
      },
      { threshold: 0.3, rootMargin: '-20% 0px -60% 0px' }
    );

    sectionEls.forEach((el) => sectionObserver.observe(el));
  }

  /* ── Mobile nav toggle ────────────────────────────────────── */
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      mobileMenu.classList.toggle('open');
    });
    mobileMenu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        mobileMenu.classList.remove('open');
      });
    });
  }

  /* ── Project filter with smooth transition ─────────────────── */
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');
  if (filterBtns.length && projectCards.length) {
    filterBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        filterBtns.forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.dataset.filter;

        // First: fade out non-matching cards
        projectCards.forEach((card) => {
          const show = filter === 'all' || card.dataset.type === filter;
          if (!show) {
            card.classList.add('hidden-card');
            card.classList.remove('visible-card');
          }
        });

        // Then: fade in matching cards with stagger
        const matching = Array.from(projectCards).filter(
          (card) => filter === 'all' || card.dataset.type === filter
        );
        matching.forEach((card, i) => {
          card.classList.remove('hidden-card');
          setTimeout(() => {
            card.classList.add('visible-card');
          }, i * 60);
        });
      });
    });
  }

  /* ── Full card click zone ──────────────────────────────────── */
  document.querySelectorAll('.project-card[data-url]').forEach((card) => {
    card.addEventListener('click', (e) => {
      const url = card.dataset.url;
      if (url) window.location.href = url;
    });
    card.style.cursor = 'pointer';
  });

  /* ── Blog card click zone ───────────────────────────────────── */
  document.querySelectorAll('.blog-item[data-url]').forEach((card) => {
    card.addEventListener('click', (e) => {
      const url = card.dataset.url;
      if (url) window.location.href = url;
    });
  });

  /* ── Thumb carousel ─────────────────────────────────────────── */
  document.querySelectorAll('.thumb-carousel').forEach((carousel) => {
    const imagesAttr = carousel.dataset.images;
    if (!imagesAttr) return;
    const images = imagesAttr.split('');
    let current = 0;

    function showNext() {
      const items = carousel.querySelectorAll('.carousel-item');
      items.forEach((item, idx) => {
        item.style.display = (idx === current) ? 'flex' : 'none';
        item.style.alignItems = 'center';
        item.style.justifyContent = 'center';
      });
    }

    // Create carousel items
    carousel.innerHTML = '';
    images.forEach((img, idx) => {
      const span = document.createElement('span');
      span.className = 'carousel-item';
      span.textContent = img;
      span.style.display = 'none';
      carousel.appendChild(span);
    });
    showNext();

    let interval;
    const card = carousel.closest('.project-card');
    if (card) {
      card.addEventListener('mouseenter', () => {
        interval = setInterval(() => {
          current = (current + 1) % images.length;
          showNext();
        }, 1200);
      });
      card.addEventListener('mouseleave', () => {
        clearInterval(interval);
        current = 0;
        showNext();
      });
    }
  });

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
