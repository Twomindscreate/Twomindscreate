// jQuery is required before this script

//Teghnologies
document.addEventListener("DOMContentLoaded", function() {
    window.addEventListener('scroll', function() {
        const scrollTop = window.scrollY;
        const windowHeight = window.innerHeight;
        const sectionTop = document.getElementById('technologies').offsetTop;
        const sectionHeight = document.getElementById('technologies').offsetHeight;
        const progressBars = document.querySelectorAll('.progress-bartech');

        if (scrollTop >= sectionTop - windowHeight && scrollTop <= sectionTop + sectionHeight) {
            progressBars.forEach(function(bar) {
                const percentage = bar.getAttribute('aria-valuenow');
                bar.style.width = percentage + '%';
            });
        }
    });
});


$(document).ready(function () {
    // Nav Bar Code
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('.navbar').addClass('bg-scroll');
            $('.nav-link').addClass('scrolled');
        } else {
            $('.navbar').removeClass('bg-scroll');
            $('.nav-link').removeClass('scrolled');
        }
    });




});


// typing text animation script
var typed = new Typed(".typing", {
            strings: ["Fullstack Developer", "Freelancer", "Software Developer", "ML Developer"],
            typeSpeed: 100,
            backSpeed: 60,
            loop: true
    });


//Projects

$('.carousel').carousel({
    interval: 2000 // Change slide interval here (milliseconds)
});
