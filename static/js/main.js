// Main JS file for Legal Bridge
document.addEventListener('DOMContentLoaded', () => {
    console.log('Legal Bridge Loaded');
    
    // Header scroll effect
    const nav = document.querySelector('.glass-nav');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            nav.style.background = 'rgba(78, 84, 200, 0.9)';
        } else {
            nav.style.background = 'rgba(255, 255, 255, 0.1)';
        }
    });
});
