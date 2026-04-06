// JavaScript for AI Disease Prediction System

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('symptom-form');
    const predictBtn = document.getElementById('predict-btn');
    
    if (form && predictBtn) {
        form.addEventListener('submit', function(e) {
            // Show loading animation
            predictBtn.disabled = true;
            predictBtn.textContent = 'Predicting...';
            
            // Add loading class to body or show spinner
            const loading = document.createElement('div');
            loading.className = 'loading show';
            loading.innerHTML = '<div class="spinner"></div>';
            document.body.appendChild(loading);
            
            // The form will submit normally, but we can add client-side validation here if needed
        });
    }
    
    // Smooth scrolling for anchor links
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add hover effects to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 10px 25px rgba(0, 0, 0, 0.1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        });
    });
});