const search = document.querySelector(".search")
const input = document.querySelector(".input")
const btn = document.querySelector(".btn")

btn.addEventListener("click", ()=>{
    // console.log("test");
    search.classList.toggle("active")
    // input.focus()
    if (search.classList.contains("active")) {
        input.removeAttribute("readonly");
        input.focus();
    } else {
        input.setAttribute("readonly", "readonly");
    }
})