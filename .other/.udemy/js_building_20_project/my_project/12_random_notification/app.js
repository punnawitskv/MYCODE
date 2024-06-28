const btn = document.querySelector(".btn")
const container = document.querySelector(".container")
const message = [
    "Hello World",
    "Good Morning",
    "Good Night",
    "test",
    "Brrrrr",
    "Va",
    "Love",
    "What!!!!!"
]
btn.addEventListener("click", ()=>createNotification())

function createNotification(){
    const notificationEl = document.createElement("div")
    notificationEl.classList.add("notification")
    notificationEl.innerText = randomMessage()
    container.appendChild(notificationEl)
    setTimeout(()=>{
        notificationEl.remove()
    }, 3000)
}

function randomMessage(){
    return message[Math.floor(Math.random()*message.length)]
}