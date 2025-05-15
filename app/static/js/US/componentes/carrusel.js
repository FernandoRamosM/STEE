const track = document.querySelector('.carousel-track');
const slides = Array.from(track.children);
const indicators = document.querySelectorAll('.carousel-indicator');
let currentIndex = 0;

function updateCarousel() {
    const slideWidth = slides[0].getBoundingClientRect().width;
    track.style.transform = `translateX(-${currentIndex * slideWidth}px)`;

    indicators.forEach((indicator, index) => {
        indicator.classList.toggle('active', index === currentIndex);
    });
}

function autoSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    updateCarousel();
}

indicators.forEach((indicator, index) => {
    indicator.addEventListener('click', () => {
        currentIndex = index;
        updateCarousel();
    });
});

setInterval(autoSlide, 3000); // Cambia de imagen cada 3 segundos