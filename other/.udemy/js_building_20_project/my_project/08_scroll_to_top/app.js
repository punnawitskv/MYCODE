const scrollBtn = document.querySelector(".top")
const rootEl = document.documentElement

document.addEventListener("scroll", showBtn)
scrollBtn.addEventListener("click", scrollToTop)

function showBtn(){
    // console.log("test")
    const scrollTotaL = rootEl.scrollHeight - rootEl.clientHeight
    // console.log(scrollTotaL)
    if(rootEl.scrollTop/scrollTotaL > 0.3){
        scrollBtn.classList.add("show-btn")
    }else{
        scrollBtn.classList.remove("show-btn")
    }
}

function scrollToTop(){
    rootEl.scrollTo({
        top:0,
        behavior:"smooth"
    })
}