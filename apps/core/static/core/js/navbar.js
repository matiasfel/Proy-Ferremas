/* Script para el menu burger con transición */
const burger = document.querySelector('.responsive');
const navbarOpen = document.querySelector('.navbar-open');
const close = document.querySelector('.close');

navbarOpen.style.transition = 'transform 0.3s ease-in-out';

burger.addEventListener('click', () => {
    navbarOpen.style.transform = navbarOpen.style.transform === 'translateX(0)' ? '' : 'translateX(0)';
});

close.addEventListener('click', () => {
    navbarOpen.style.transform = '';
});