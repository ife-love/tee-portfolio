$(document).ready(function(){
    $nav = $('.nav');
    $toggleCollapse = $('.toggle-collapse');

    // Click event on toggle menu

    $toggleCollapse.click(function(){
    $nav.toggleClass('collapse');
    })

    // const hamburger = document.querySelector(".harmburger");
    // const navMenu = document.querySelector(".nav-items");

    // hamburger.addEventListener("click", () => {
    //     hamburger.classList.toggle("collapse");
    //     navMenu.classList.toggle("collapse");

    // })





// $(document).ready(function(){

//     $('#icon').click(function(){
//     $('ul').toggleClass('collapse');

//     })





    // Owl-Carousel foe blog

    //   owl-carousel

    $('.owl-carousel').owlCarousel({
        loop:true,
        autoplay:true,
        autoplayTimeout:4000,
        dots:false,
        nav:true,
        navText:[$('.owl-navigation .owl-nav-prev'), $('.owl-navigation .owl-nav-next')],
        responsive: {

            0: {
                items:1
            },
            360: {
                items:1
            },
            560: {
                items: 2
            },
            960: {
                items: 3
            }
        }

    })

// click to scroll Top

$('.move-up span').click(function(){
    $('html, body').animate({
        scrollTop: 0
    }, 2000);
})


// AOS instance

AOS.init({
    // offset: 120,
    // delay:0,
    // duration:400,
    // easing:'ease-in-out',
    // once:false,

});

// AOS.refresh();

const body = document.body;
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = (window.pageYOffset)

        if (currentScroll <= 0) {
            body.classList.remove("scroll-up")
            body.classList.remove("scroll-down")
        }

        if (currentScroll > lastScroll && !body.classList.contains("scroll-down")){
            body.classList.remove("scroll-up")
            body.classList.add("scroll-down")
        }

        if (currentScroll < lastScroll && body.classList.contains("scroll-down")){
            body.classList.add("scroll-up")
            body.classList.remove("scroll-down")
        }

        lastScroll = currentScroll;
    })

    
});