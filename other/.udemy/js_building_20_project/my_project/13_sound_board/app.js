const sounds = ["Effect1", "Effect2", "Effect3", "Effect4", "Effect5"]

sounds.forEach(sound=>{
    const btn = document.createElement("button")
    btn.classList.add("btn")
    btn.innerText = sound
    btn.addEventListener("click", ()=>{
        const song = document.getElementById(sound)
        song.volume = 0.025
        stopSounds()
        // console.log(sound)
        song.play()
    })
    document.getElementById("controller").appendChild(btn)
})

function stopSounds(){
    sounds.forEach(sound=>{
        const song = document.getElementById(sound)
        song.pause()
        song.currentTime = 0
    })
}