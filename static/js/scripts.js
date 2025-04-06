// Simple JavaScript for interactions

document.addEventListener('DOMContentLoaded', function() {
    console.log('Website loaded successfully!');
    
    // You can add more JavaScript functionality here
    // For example, a simple mobile menu toggle
    
    // This is just a placeholder for future functionality
});

function toggleLanguage() {
    const body = document.body;
    const button = document.getElementById('langToggle');
    
    if (body.classList.contains('lang-en')) {
        // Switch to Tagalog
        body.classList.remove('lang-en');
        button.textContent = 'English';
        localStorage.setItem('lang', 'tl');
    } else {
        // Switch to English
        body.classList.add('lang-en');
        button.textContent = 'Tagalog';
        localStorage.setItem('lang', 'en');
    }
}

// Check if language preference is saved
document.addEventListener('DOMContentLoaded', function() {
    const savedLang = localStorage.getItem('lang');
    if (savedLang === 'en') {
        document.body.classList.add('lang-en');
        document.getElementById('langToggle').textContent = 'Tagalog';
    }
});
