function resizeHeaderOnScroll() {
    const distanceY = window.pageYOffset || document.documentElement.scrollTop,
    shrinkOn = 50,
    header = document.getElementById('js-header');
    title = document.getElementById('js-title');
    
    if (distanceY > shrinkOn) {
        header.classList.add("reduced");
        title.innerHTML = "";
    } else {
        header.classList.remove("reduced");
        title.innerHTML = blog_title;
    }        
}

var blog_title = document.getElementById("js-title").innerText;
window.addEventListener('scroll', resizeHeaderOnScroll);