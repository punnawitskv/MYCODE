const result = document.getElementById("result")
const filter = document.getElementById("filter")
const listItem = []

filter.addEventListener("input", (e)=>{
    const searchInput = e.target.value.toLowerCase()
    listItem.forEach(item=>{
        if(item.innerText.toLowerCase().includes(searchInput)){
            item.classList.remove("hide")
        }else{
            item.classList.add("hide")
        }
    })

    console.log(searchInput)
})

async function getData(){
    const url = "https://restcountries.com/v3.1/all"
    const response = await fetch(url)
    const items = await response.json()
    result.innerHTML = ""
    items.forEach(data => {
        const li = document.createElement("li")
        listItem.push(li)
        li.innerHTML = `
            <img src="${data.flags.png}">
            <div class="info">
                <h4>${data.name.common}</h4>
                <p>${formatNumber(data.population)}</p>
            </div>
        `
        result.appendChild(li)
    });
console.log(items)
}

function formatNumber(num){
    return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
}
    
getData()