const celciusInput = document.getElementById("celcius")
const fahrenheitInput = document.getElementById("fahrenheit")
const kelvinInput = document.getElementById("kelvin")
const temperatureInputs = document.querySelectorAll("input")

temperatureInputs.forEach(input=>{
    input.addEventListener("input",(e)=>{
        let temperatureValue = parseInt(e.target.value)
        let inputName = e.target.name
        console.log("Input = ", temperatureValue, " Unit = ", inputName)

        if(e.target.value === ""){
            celciusInput = null
            fahrenheitInput = null
            kelvinInput = null
            return
        }

        if(inputName === "celcius"){
            let fahrenheit = temperatureValue * 1.8 + 32
            fahrenheitInput.value = fahrenheit.toFixed(2)

            let kelvin = temperatureValue + 273
            kelvinInput.value = kelvin.toFixed(2)
        }else if(inputName === "fahrenheit"){
            let kelvin = (temperatureValue - 32) / 1.8 + 273
            kelvinInput.value = kelvin.toFixed(2)

            let celcius = (temperatureValue - 32) / 1.8
            celciusInput.value = celcius.toFixed(2)
        }else if(inputName === "kelvin"){
            let celcius = temperatureValue - 273
            celciusInput.value = celcius.toFixed(2)

            let fahrenheit = (temperatureValue - 273) * 1.8 + 32
            fahrenheitInput.value = fahrenheit.toFixed(2)
        }
    })
})