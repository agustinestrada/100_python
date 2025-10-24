let data 

async function extraer_data() {
    let dati = await fetch('https://agustinestrada.github.io/100_python/golf/canchas.json')
    let datos = await dati.json()
    return datos
}

data = extraer_data()

async function main() {
    let data = await extraer_data()
    console.log(JSON.stringify(data,null,4))
}

main()