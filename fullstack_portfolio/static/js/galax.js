let stars = document.getElementById('stars')
let moon = document.getElementById('moon')
let mountains_behind = document.getElementById('mountains_behind')
let text = document.getElementById('text')
let moontext = document.getElementById('moontext')
let btn = document.getElementById('btn')
let mountains_front = document.getElementById('mountains_front')
let header = document.getElementById('header')
let lake = document.getElementById('lake')
let star = document.getElementById('star')
let button = document.getElementById('button')
let nt_txt = document.getElementById('nt_txt')

window.addEventListener('scroll', function(){
    let value = window.scrollY;
    stars.style.left = value * 0.25 + 'px'
    moon.style.top = value * 1.05 + 'px'
    mountains_behind.style.top = value * 0.5 + 'px'
    mountains_front.style.top = value * 0 + 'px'
    text.style.marginRight = value * 4 + 'px'
    text.style.marginTop = value * 1.5 + 'px'
    moontext.style.marginLeft = value * 2 + 'px'
    moontext.style.marginTop = value * 1.5 + 'px'
    btn.style.marginTop = value * 1.5 + 'px'
    header.style.marginTop = value * 1.5 + 'px'
    nt_txt.style.top = value * 4 + 'px'
    button.style.top = value * 3 + 'px'
    star.style.left = value * 0.25 + 'px'
    lake.style.top = value * 0 + 'px'
})