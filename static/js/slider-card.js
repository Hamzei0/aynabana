$(document).ready(function() {
    class ScaleSlider {
        constructor() {
            this.slides = $('.slide');
            this.currentSlide = 0;
            this.isAnimating = false;
            this.autoPlayInterval = null;
            
            this.init();
        }
        
        init() {
            this.updateSlidesPosition();
            this.createDots();
            this.bindEvents();
            this.startAutoPlay();
            this.applyParallax();
        }
        
        updateSlidesPosition() {
            this.slides.removeClass('active prev next far-prev far-next');
            
            const totalSlides = this.slides.length;
            
            // اسلاید اصلی
            $(this.slides[this.currentSlide]).addClass('active');
            
            // اسلاید قبلی
            const prevIndex = (this.currentSlide - 1 + totalSlides) % totalSlides;
            $(this.slides[prevIndex]).addClass('prev');
            
            // اسلاید بعدی
            const nextIndex = (this.currentSlide + 1) % totalSlides;
            $(this.slides[nextIndex]).addClass('next');
            
            // اسلایدهای دورتر
            const farPrevIndex = (this.currentSlide - 2 + totalSlides) % totalSlides;
            $(this.slides[farPrevIndex]).addClass('far-prev');
            
            const farNextIndex = (this.currentSlide + 2) % totalSlides;
            $(this.slides[farNextIndex]).addClass('far-next');
        }
        
        createDots() {
            const dotsContainer = $('.slider-dots');
            dotsContainer.empty();
            
            this.slides.each((index) => {
                const dot = $('<div class="dot"></div>');
                if (index === this.currentSlide) dot.addClass('active');
                dot.on('click', () => this.goToSlide(index));
                dotsContainer.append(dot);
            });
        }
        
        bindEvents() {
            $('.prev-btn').on('click', () => this.prevSlide());
            $('.next-btn').on('click', () => this.nextSlide());
            
            // Parallax effect on mouse move
            $('.slider-container').on('mousemove', (e) => {
                if (this.isAnimating) return;
                this.handleParallax(e);
            });
            
            // Pause auto-play on hover
            $('.slider-container')
                .on('mouseenter', () => this.stopAutoPlay())
                .on('mouseleave', () => this.startAutoPlay());
            
            // Touch events for mobile
            this.handleTouchEvents();
            
            // Keyboard navigation
            $(document).on('keydown', (e) => {
                if (e.key === 'ArrowLeft') this.prevSlide();
                if (e.key === 'ArrowRight') this.nextSlide();
            });
        }
        
        handleParallax(e) {
            const $activeSlide = $(this.slides[this.currentSlide]);
            const $image = $activeSlide.find('.slide-image');
            
            const mouseX = e.clientX / window.innerWidth;
            const mouseY = e.clientY / window.innerHeight;
            
            const moveX = (mouseX - 0.5) * 30;
            const moveY = (mouseY - 0.5) * 20;
            
            $image.css({
                transform: `translate(${moveX}px, ${moveY}px) scale(1.05)`
            });
        }
        
        applyParallax() {
            // Reset parallax on slide change
            this.slides.on('transitionend', (e) => {
                if (e.originalEvent.propertyName === 'transform') {
                    const $activeImage = $(this.slides[this.currentSlide]).find('.slide-image');
                    $activeImage.css('transform', 'translate(0, 0) scale(1.05)');
                }
            });
        }
        
        handleTouchEvents() {
            let startX = 0;
            let endX = 0;
            
            $('.slider-container').on('touchstart', (e) => {
                startX = e.originalEvent.touches[0].clientX;
                this.stopAutoPlay();
            });
            
            $('.slider-container').on('touchmove', (e) => {
                endX = e.originalEvent.touches[0].clientX;
            });
            
            $('.slider-container').on('touchend', () => {
                const diff = startX - endX;
                if (Math.abs(diff) > 50) {
                    if (diff > 0) {
                        this.nextSlide();
                    } else {
                        this.prevSlide();
                    }
                }
                this.startAutoPlay();
            });
        }
        
        goToSlide(index) {
            if (this.isAnimating || index === this.currentSlide) return;
            
            this.isAnimating = true;
            this.currentSlide = index;
            
            this.updateSlidesPosition();
            this.createDots();
            
            setTimeout(() => {
                this.isAnimating = false;
            }, 800);
        }
        
        nextSlide() {
            const nextIndex = (this.currentSlide + 1) % this.slides.length;
            this.goToSlide(nextIndex);
        }
        
        prevSlide() {
            const prevIndex = (this.currentSlide - 1 + this.slides.length) % this.slides.length;
            this.goToSlide(prevIndex);
        }
        
        startAutoPlay() {
            this.stopAutoPlay();
            this.autoPlayInterval = setInterval(() => {
                this.nextSlide();
            }, 4000);
        }
        
        stopAutoPlay() {
            if (this.autoPlayInterval) {
                clearInterval(this.autoPlayInterval);
                this.autoPlayInterval = null;
            }
        }
    }
    
    // راه‌اندازی اسلایدر
    new ScaleSlider();
});