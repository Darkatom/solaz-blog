function resizeHeaderOnScroll() {
    const distanceY = window.pageYOffset || document.documentElement.scrollTop,
    shrinkOn = 200,
    header = document.getElementById('js-header');
    title = document.getElementById('js-title');
    
    if (distanceY > shrinkOn) {
        header.classList.add("reduced");
        title.innerHTML = "";
    } else {
        header.classList.remove("reduced");
        title.innerHTML = "La bruja moderna";
    }        
}

window.addEventListener('scroll', resizeHeaderOnScroll);