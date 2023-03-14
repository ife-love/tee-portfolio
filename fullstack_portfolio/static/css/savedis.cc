@import url(fonts.css);

/* css variables */
@import url("./partials/variables.css");

/* _global variables */
@import url("./partials/global.css");


/* @media(min-width:320px){
    .site-main .about-area{
    
        padding-top: 0 !important;
    }
 } */

 

.header-area .main-menu .navbar .navbar-brand img{
    height: 80px;
    width: 100px;

}

/* START NAVIGATION */

 .header-area .main-menu .navbar .navbar-brand{
    padding: 1.5rem 2rem 0 1rem;
}


.header-area .main-menu .navbar{
    padding: 0 2rem;
}

.header-area .main-menu .nav-item .nav-link{
    font-family:var(--font-roboto);
    text-transform: uppercase;
    font-weight: bold;
    padding: 1.5rem;
    margin-left: 1rem;
    color: var(--title-color);

}

.header-area .main-menu .navbar-nav .active{
    background:  var(--gradient-color);
    
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
    background-clip: text;
}

.header-area .main-menu .navbar-nav a:hover{
    background: var(--bg-gradient1);
    -webkit-text-fill-color:transparent;
    -webkit-background-clip: text;
    background-clip: text;
}

/* / END NAVIGATION */






/*################################ Banner Area ###############################*/

.site-main .site-banner{
    background: url('../img/clothes/cloth2.jpg');
    background-position:auto;
    background-repeat: no-repeat;
    padding-left: 8rem;
    padding-top: 10rem;
    padding-right: 8rem;
}

/* .site-main .site-banner .site-title h3{
    padding-top: 40px;
    font-weight: 500;
    margin-bottom: 5%;

} */
/* .site-main .site-banner .first-row{

} */
.site-main .site-banner .site-title h3{
    padding-top: 25%;
    font-weight: 500;
    margin-bottom: 5%;

}

/* .site-main .site-banner .site-title{
    padding-top: 0;
} */

.site-main .site-banner .site-title h3:after{
    content: '';
    height: 2px;
    width:18vw;
    background: black;
    display: inline-block;
    margin-left: 5%;
    transform: translateY(-10px);

}

.site-main .site-banner .site-title h1{
    font-size: 6rem;
    margin-bottom: 2%;  

}

.site-main .site-banner .site-title h4{
    font-size: 1.7rem;
}

.site-main .site-banner .banner-image img{
    margin-top: 0;
    width: 50rem;
    margin-top: 5rem;
}


/*################################ End Banner Area ###############################*/


/*################################ start about Area ###############################*/

.site-main .about-area{
    padding-top: 20rem;
}

.site-main .about-area .about-image{
    margin-top: 0;
    padding-bottom: 3rem;
    padding-left: 8rem;
    padding-right: 8rem;
}

.site-main .about-area .about-image .aboutimage{
    margin-top: 5rem;

}

/* @media(min-width:320px){
    .site-main .about-area{
    
        padding-top: 0;
    }
} */

 .site-main .about-area .about-title h2 span {
    display: block;
    font: normal bold 30px/50px var(--font-robot);
    letter-spacing: 10px;
}

.site-main .about-area .about-title{
    padding-left: 8rem;
    padding-right: 8rem;
    /* padding-top: 4rem; */
}




/*################################ end about Area ###############################*/


/*################################ start brand Area ###############################*/

.site-main .brand-area{
    padding-top: 4rem;
    padding-bottom: 10rem;
}

.site-main .brand-area .first-row .col-lg-4{
    display: flex;
    justify-content:center;
    margin-top: 2rem;
    margin-bottom: 3rem;
    padding-top: 1.5rem;
}

.site-main .brand-area .first-row .col-lg-4 .single-brand{
    border: none;
    text-align:center;
    width: 200px;
    height: 100px;
    cursor: pointer;
    transition: transform .4s ease;
}

.site-main .brand-area .first-row .col-lg-4 .single-brand img{
    width: 80%;
}

.site-main .brand-area .first-row .col-lg-4 .single-brand img:hover{
    /* box-shadow: var(--gradient-color); */
    transform: scale(2);
}

.site-main .brand-area .experience-area{
    padding-left: 3rem;
    margin-top: 5rem;
}
.site-main .brand-area .experience-area span{
    display: block;

}

.site-main .brand-area .experience-area .spans{
    padding-top: 1rem;
    font-family: var(--font-roboto);
    font-weight: bold;
}

.site-main .brand-area .experience-area .years-area{
    background: url("../img/blanks/blank2.jpg");
    background-repeat: no-repeat;
    background-position: auto;
    position: relative;
    width: 700px;
    height: 400px;
    z-index: -1;
}

.site-main .brand-area .experience-area .years-area .years{
    font: normal bold 100px/60px var(--font-roboto);
    color: rgb(8, 94, 94);
    /* color: rgb(17, 131, 131); */
    /* color: rgb(92, 92, 179); */
    /* color: tomato; */
    z-index: 2;
}

.site-main .brand-area .experience-area .years-area .years h2 span{
    font: normal 600 22px/30px var(--font-roboto);
}

.site-main .brand-area .experience-area .call-area{
    padding-top: 2rem;
    padding-left: 1rem;
    /* color: rgb(8, 94, 94); */
}
/* .site-main .brand-area .experience-area .call-area .call-now{ */
    /* font-family: var(--font-robot); */
/* } */
/* .site-main .brand-area .first-row .col-lg-4 .single-brand:hover img{
    filter: brightness(.15); */
/* } */
/*################################ end Brand Area ###############################*/


/*################################ start Services Area ###############################*/

.site-main .services-area{
    padding: 2rem 0rem;
}


/*################################ end services Area ###############################*/