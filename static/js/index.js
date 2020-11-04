window.addEventListener('DOMContentLoaded', () => {
    const menu = document.querySelector('.header-nav'),
    menuExit = document.querySelector('.menu-exit'),
    hamburger = document.querySelector('.gamburger');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('d-none');
        menu.classList.toggle('activ-menu');
        menuExit.classList.toggle('d-block');
    });
    menuExit.addEventListener('click', () => {
        hamburger.classList.toggle('d-none');
        menu.classList.toggle('activ-menu');
        menuExit.classList.toggle('d-block');
    });
    
})