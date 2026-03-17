const path = window.location.pathname;
const isHome = path === '/' || 
               path.endsWith('/learn-ai-fundamentals/') || 
               path.endsWith('/index.html');

if (!isHome) {
  localStorage.setItem('lastPage', window.location.href);
}

document.addEventListener("DOMContentLoaded", function () {
  const lastPage = localStorage.getItem('lastPage');
  const btn = document.querySelector('.ai-btn--primary');
  if (!btn) return;

  if (lastPage) {
    btn.href = lastPage;
    btn.textContent = 'Continue Learning →';
  }

  // Show button only after text is set
  btn.style.visibility = 'visible';
});