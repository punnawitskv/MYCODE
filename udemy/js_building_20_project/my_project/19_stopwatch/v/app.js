const timeEl = document.querySelector(".time")
const buttonsGroup = document.querySelector(".buttons-group")

let [milliseconds, seconds, minutes, hours] = [0, 0, 0, 0]
let timer = null

buttonsGroup.addEventListener("click", (e) => {
    if (e.target.closest("button").classList.contains("start")) {
        startTimer()
        updateButtons("pause")
    } else if (e.target.closest("button").classList.contains("pause")) {
        pauseTimer()
        updateButtons("continue", "reset")
    } else if (e.target.closest("button").classList.contains("continue")) {
        startTimer()
        updateButtons("pause")
    } else if (e.target.closest("button").classList.contains("reset")) {
        resetTimer()
        updateButtons("start")
    }
})

function updateButtons(...buttons) {
    const oldButtons = Array.from(buttonsGroup.querySelectorAll("button"))
    oldButtons.forEach(button => {
        button.classList.add("hidden")
    })

    setTimeout(() => {
        buttonsGroup.innerHTML = ""
        buttons.forEach(button => {
            const buttonElement = document.createElement("button")
            buttonElement.classList.add(button)
            buttonElement.classList.add("hidden")
            buttonElement.innerHTML = getButtonContent(button)
            buttonsGroup.appendChild(buttonElement)
            setTimeout(() => {
                buttonElement.classList.remove("hidden")
                buttonElement.classList.add("show")
            }, 50)
        })
    }, 300)
}

function getButtonContent(button) {
    switch (button) {
        case "start":
            return '<i class="fa-solid fa-play"></i>&nbsp;Start'
        case "pause":
            return '<i class="fa-solid fa-pause"></i>&nbsp;Pause'
        case "continue":
            return '<i class="fa-solid fa-play"></i>&nbsp;Continue'
        case "reset":
            return '<i class="fa-solid fa-rotate"></i>&nbsp;Reset'
    }
}

function startTimer(){
    if (timer == null){
        clearInterval(timer)
    }
    timer = setInterval(displayTime, 10)
}

function pauseTimer(){
    clearInterval(timer)
}

function resetTimer(){
    clearInterval(timer)
    hours = 0 
    minutes = 0
    seconds = 0 
    milliseconds = 0
    timeEl.innerHTML = `00:00:00:000`
}

function displayTime(){
    milliseconds += 10
    if (milliseconds >= 1000){
        milliseconds = 0
        seconds++
    }
    if (seconds >= 60){
        seconds = 0
        minutes++
    }
    if (minutes >= 60){
        minutes = 0
        hours++
    }
    let h = hours < 10 ? "0" + hours : hours
    let m = minutes < 10 ? "0" + minutes : minutes
    let s = seconds < 10 ? "0" + seconds : seconds
    let ms = milliseconds < 10 ? "00" + milliseconds : milliseconds < 100 ? "0" + milliseconds : milliseconds
    timeEl.innerHTML = `${h}:${m}:${s}:${ms}`
}
