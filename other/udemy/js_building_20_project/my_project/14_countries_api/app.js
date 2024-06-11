const container = document.getElementById("container")

const getCountry = async()=>{
    const url = 'https://restcountries.com/v3/all'
    const res = await fetch(url)
    const items = await res.json()
    console.log(items)
    items.forEach(element => {
        // console.log("Country Name =", element.name.common, element.capital)
        createCard(element)
    });
}

const createCard=(data)=>{
    const cardEl = document.createElement("div")
    cardEl.classList.add("country")
    const contentHTML = `
        <div class="img-container">
            <img src="${data.flags[1]}"/>
        </div>
        
        <div class="info">
            <h3 class="name">${data.name.common}</h3>
            <small>Capital : <span>${data.capital}</span></small>
        </div>
    `
    cardEl.innerHTML = contentHTML
    container.appendChild(cardEl)
}

getCountry()