//vue component forecastDiv
let forecastDiv = {
    props: ['forecast'],
    template: `<div class="outer-container">
        <img :src="'http://openweathermap.org/img/wn/' + forecast.weather[0].icon + '@2x.png'">

        <div class="inner-container">
            <div class="datetime">{{forecast.dt}}</div>
            <div class="dt-text">{{forecast.dt_txt.toLocaleString()}}</div>
            <div class="temp">{{forecast.main.temp}}</div>
            <div class="feels-like">{{ forecast.main.feels_like}}</div>
            <div class="humidity">{{ forecast.main.humidity}}</div>
            <div class="description">{{ forecast.weather.description}}</div>
            <div class="wind">{{forecast.wind.speed}}</div>
        </div>
    </div>`,
    // data: () => ({
    //     forecast: getWeather(),
    // }),
    // data: {
    //     forecasts: []
    // }
}

//vue stuff
var vm = new Vue({
    el: '#vm',
    data: {
        search: '',
        city: '',
        forecasts: [],
        timeZone: '',
    },
    methods: {

    },
    components: {
        forecastDiv,
    }
})
let cityName = document.querySelector('#city-name')

let input = document.querySelector('input')
input.addEventListener('keydown', function(e) {
    if (e.which === 13) {
        console.log('were in!')
        //clear vm.forecasts
        vm.forecasts = []
        //axios stuff
        let apiKey = "2a3b6c8a4967eb6fc1f41df5bbf6999b"
        let url = `https://api.openweathermap.org/data/2.5/weather?q=${vm.search}&units=imperial&APPID=${apiKey}`
        let url2 = `https://api.openweathermap.org/data/2.5/forecast?q=${vm.search}&mode=JSON&units=imperial&APPID=${apiKey}`
        axios.get(url)
        .then(function(response) {
            console.log('current weather', response)
            let forecast = response.data
            vm.city = forecast.name
            cityName.innerText = `${vm.city} Current:`
            vm.timeZone = forecast.timezone
            forecast.id = 0
            vm.forecasts.push(forecast)
        
        })
        axios.get(url2)
        .then(function(response) {
            console.log('5 day', response)
            let list = response.data.list
            for (let i=0; i<list.length; i++) {
                let forecast = list[i]
                forecast.id = i + 1
                vm.forecasts.push(forecast)

            }
        })
    }
})
