const smallImg = document.querySelectorAll(".gallery img")
// console.log(smallImg)
const fullImg = document.querySelector(".full-image")
const modal = document.querySelector(".modal")
smallImg.forEach(img=>{
    img.addEventListener("click", ()=>{
        const fullSize = img.getAttribute("alt")
        // alert(fullSize)
        const path = `foods-images/full/${fullSize}.jpg`
        // alert(path)
        fullImg.src = path
        modal.classList.add("open")
    })
})
modal.addEventListener("click", (e)=>{
    if(e.target.classList.contains("modal")){
        modal.classList.remove("open")
        fullImg.src = "#"
    }
})