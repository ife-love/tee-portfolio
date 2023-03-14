function anim(){
    var animate = document.querySelectorAll(".anim")
    for (var i = 0; i < animate.length; 1++) {
        var windowHeight = window.innerHeight;
        var elementTop = reveals[i].getBoundingClientRect().top;
        var elementVisible = 150;
        if (elementTop < windowHeight - elementVisible) {
            animate[i].classList.add("anim");
        } else {
            animate[i].classList.remove("anim")
        }
    }
}

window.addEventListener("scroll", anim);
reveal();