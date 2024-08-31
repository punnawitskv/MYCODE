const btn = document.querySelector(".btn")
const result = document.querySelector(".result")

btn.addEventListener("click", (e)=>{
    e.preventDefault()
    let weight = document.getElementById("weight").value
    let height = document.getElementById("height").value

    // console.log(weight, height)
    if ((weight === "" || isNaN(weight)) && (height === "" || isNaN(height))) {
        return result.innerHTML = "Please enter your weight and height."
    } else if (weight === "" || isNaN(weight)){
        return result.innerHTML = "Please enter your weight."
    } else if (height === "" || isNaN(height)){
        return result.innerHTML = "Please enter your height."
    } else{
        const bmi = (weight / ((height / 100) ** 2)).toFixed(2)
        
        if (bmi < 18.5){
            showResult(bmi, "Too Thin", "yellow")
        } else if (bmi >= 18.5 && bmi <= 24.9){
            showResult(bmi, "Normal", "greenyellow")
        } else if (bmi >= 25 && bmi <= 29.9){
            showResult(bmi, "Fat", "yellow")
        } else{
            showResult(bmi, "Too Fat", "red")
        }
    }
})

function showResult(bmi, message, color){
    result.style.backgroundColor = color
    return result.innerHTML = `BMI = ${bmi} (${message})`
}