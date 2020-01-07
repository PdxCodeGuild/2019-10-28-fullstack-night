function weather(data, elArr) {
    // console.log(response)
    //get variables here
    // let data = response.data
    console.log(data)

    let name = data.main.name
    
    var timezone = data.timezone
    console.log(timezone)

    let temp = data.main.temp
    temp = Math.round(temp)
    
    let feelsLike = data.main.feels_like
    feelsLike = Math.round(feelsLike)
    if (feelsLike < temp - 5) {
        chillIndex = 'Wind Chill: '
    } else if (feelsLike > temp + 5) {
        chillIndex = 'Heat Index: '
    } else {
        chillIndex = 'Feels Like: '
    }
    
    let humidity = data.main.humidity
    
    let description = data.weather[0].description
    
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
    // console.log(data.weather[0].icon)
    let icon = data.weather[0].icon
    // console.log(icon)
    // update divs here
    for (item of elArr) {
        if (item.id === 'name') {
            item.innerText = `${name} Now`
        } else if (item.id === 'temp') {
            item.innerText = `${temp}°F`
        } else if (item.id === 'feels-like') {
            item.innerText = `${chillIndex}${feelsLike}°F`
        } else if (item.id === 'humidity') {
            item.innerText = `Humidity ${humidity}%`
        } else if (item.id === 'description') {
            item.innerText = description
        } else if (item.id === 'wind') {
            item.innerText = `Wind: ${windSpeed}mph ${windDir}`
        } else if (item.id === 'icon') {
            item.src = `http://openweathermap.org/img/wn/${icon}@2x.png`
        }
    }
    // nameDiv.innerText = `${name} Now`
    // tempDiv.innerText = `${temp}°F`
    // feelsLikeDiv.innerText = `${chillIndex}${feelsLike}°F`
    // humidityDiv.innerText = `Humidity: ${humidity}%`
    // descriptionDiv.innerText = description
    // windDiv.innerText = `Wind: ${windSpeed}mph ${windDir}`
    // iconImg.src = `http://openweathermap.org/img/wn/${icon}@2x.png`
}



// let url = "https://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=<api key goes here>"
let apiKey = '2a3b6c8a4967eb6fc1f41df5bbf6999b'
let input = document.querySelector('input')

let todayArr = document.querySelectorAll('.today')
let tomorrowArr = document.querySelectorAll('.tomorrow')

// for (item of todayArr) {
    
// }

// let iconImg = document.querySelector('#icon')
// let nameDiv = document.querySelector('#name')
// let tempDiv = document.querySelector('#temp')
// let feelsLikeDiv = document.querySelector('#feels-like')
// let humidityDiv = document.querySelector('#humidity')
// let descriptionDiv = document.querySelector('#description')
// let windDiv = document.querySelector('#wind')
// let inputText = input.value
input.addEventListener('keydown', function(e) {
    if (e.which === 13) {
        // curent forecast
        let url = `https://api.openweathermap.org/data/2.5/weather?q=${input.value}&units=imperial&APPID=${apiKey}`
        axios.get(url)
        .then(function(response) {
            console.log(response)
            let data = response.data
            weather(data. todayArr)
        })
        // .then(response => console.log(1, response, todayArr))

        //five day forecast
        let url2 = `https://api.openweathermap.org/data/2.5/forecast?q=${input.value}&mode=JSON&units=imperial&APPID=${apiKey}`
        axios.get(url2)
        .then(function(response) {
            console.log(2, response, tomorrowArr)
            let data = response.data
            let city = data.city
            let list = data.list
            let tomorrow = list[8]
            weather(tomorrow, tomorrowArr)
        })
    }
})//storing this here: 