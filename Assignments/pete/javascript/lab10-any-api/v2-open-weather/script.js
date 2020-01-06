// let url = "https://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=<api key goes here>"
let apiKey = '<api key goes here>'
let input = document.querySelector('input')

let iconImg = document.querySelector('#icon')
let nameDiv = document.querySelector('#name')
let tempDiv = document.querySelector('#temp')
let feelsLikeDiv = document.querySelector('#feels-like')
let humidityDiv = document.querySelector('#humidity')
let descriptionDiv = document.querySelector('#description')
let windDiv = document.querySelector('#wind')
let inputText = input.value
input.addEventListener('keydown', function(e) {
    if (e.which === 13) {
        // curent forecast
        let url = `https://api.openweathermap.org/data/2.5/weather?q=${input.value}&units=imperial&APPID=${apiKey}`
        axios.get(url)
        .then(function(response) {
            // console.log(response)

            let data = response.data
            console.log(data)

            let name = data.name
            nameDiv.innerText = name

            let temp = data.main.temp
            temp = Math.round(temp)
            tempDiv.innerText = `${temp}°F`

            let feelsLike = data.main.feels_like
            feelsLike = Math.round(feelsLike)
            if (feelsLike < temp - 5) {
                chillIndex = 'Wind Chill: '
            } else if (feelsLike > temp + 5) {
                chillIndex = 'Heat Index: '
            } else {
                chillIndex = 'Feels Like: '
            }
            feelsLikeDiv.innerText = `${chillIndex}${feelsLike}°F`

            let humidity = data.main.humidity
            humidityDiv.innerText = `Humidity: ${humidity}%`

            let description = data.weather[0].description
            descriptionDiv.innerText = description

            let windSpeed = data.wind.speed
            windSpeed = Math.round(windSpeed)
            let windDirDeg = data.wind.deg
            let windDir
            if (windDirDeg <= 22.5 || windDirDeg > 337.5) {windDir = 'N'}
            else if (windDirDeg > 22.5 && windDirDeg <= 67.5) {windDir = 'NE'}
            else if (windDirDeg > 67.5 && windDirDeg <= 112.5) {windDir = 'E'}
            else if (windDirDeg > 112.5 && windDirDeg <= 157.5) {windDir = 'SE'}
            else if (windDirDeg > 157.5 && windDirDeg <= 202.5) {windDir = 'S'}
            else if (windDirDeg > 202.5 && windDirDeg <= 147.5) {windDir = 'SW'}
            else if (windDirDeg > 147.5 && windDirDeg <= 292.5) {windDir = 'W'}
            else if (windDirDeg > 292.5 && windDirDeg <= 337.5) {windDir = 'NW'}
            windDiv.innerText = `Wind: ${windSpeed}mph ${windDir}`
            // console.log(data.weather[0].icon)
            let icon = data.weather[0].icon
            console.log(icon)
            iconImg.src = `http://openweathermap.org/img/wn/${icon}@2x.png`

        })
        //five day forecast
        let url2 = `https://api.openweathermap.org/data/2.5/forecast?q=${input.value}&mode=JSON&units=imperial&APPID=${apiKey}`
        axios.get(url2)
        .then(function(response) {
            console.log(response)
        })
    }
})//storing this here: 