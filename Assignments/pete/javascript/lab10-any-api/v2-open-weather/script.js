// let url = "https://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=<api key goes here>"

let input = document.querySelector('input')
let inputText = input.value
input.addEventListener('keydown', function(e) {
    if (e.which === 13) {
        console.log('pressed it')
        let url = `https://api.openweathermap.org/data/2.5/weather?q=${inputText}`
        axios.get(url)
        .then(function(response) {
            console.log(response)
            
        })
    }
})