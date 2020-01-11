function getWeather() {
    return [{main: 'hey'},'b','c']
}
let forecastDiv = {
    props: ['forecast'],
    template: `<div class="outer-container-div">
        <img src='http://openweathermap.org/img/wn/{{forecast.icon}@2x.png'>

        <div class="inner-container-div">
            <div class="temp">{{forecast.main.temp}}</div>
            <div class="feels-like">{{ forecast.main.feels_like}}</div>
            <div class="humidity">{{ forecast.main.humidity}}</div>
            <div class="description">{{ forecast.weather.description}}</div>
            <div class="wind">{{forecast.wind.speed}}</div>
        </div>
    </div>`,
    data: () => ({
        forecast: getWeather(),
    }),
    // data: {
    //     forecasts: ['1','2','3']
    // }
}

//vue stuff
var vm = new Vue({
    el: '#vm',
    data: {
        city: 'seattle',
        forecasts: [{
            main: 'main',

        }],
    },
    methods: {

    },
    components: {
        forecastDiv,
    }
})

//axios stuff
let apiKey = "2a3b6c8a4967eb6fc1f41df5bbf6999b"
let url = `https://api.openweathermap.org/data/2.5/weather?q=${vm.city}&units=imperial&APPID=${apiKey}`
axios.get(url)
.then(function(response) {
    console.log('current weather', response)
    let data = response.data
    let name = data.name
    // nameDiv.innerText = `${name} Now:`
    // weather(data, todayArr)
})
let url2 = `https://api.openweathermap.org/data/2.5/forecast?q=${vm.city}&mode=JSON&units=imperial&APPID=${apiKey}`
axios.get(url2)
.then(function(response) {
    console.log('5 day', response)
    // console.log(2, response, tomorrowArr)
    let data = response.data
    let city = data.city
    let list = data.list
    let tomorrow = list[8]
    // weather(tomorrow, tomorrowArr)
})