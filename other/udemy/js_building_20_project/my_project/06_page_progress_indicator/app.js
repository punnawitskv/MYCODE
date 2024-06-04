const progressElement = document.querySelector(".progress")
window.onscroll=()=>scrollProgress()

function scrollProgress(){
    // console.log("test")
    const pageHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight
    const scrollTop = document.documentElement.scrollTop
    const scrollPercentage = (scrollTop/pageHeight)*100
    // console.log(scrollPercentage+"%")
    progressElement.style.visibility="visible"
    progressElement.style.width=scrollPercentage+"%"
}