//vue component forecastDiv
let forecastDiv = {
    props: ['forecast', 'moment'],
    template: `<div class="outer-container">
        <img :src="'http://openweathermap.org/img/wn/' + forecast.weather[0].icon + '@2x.png'">

        <div class="inner-container">
            <div class="datetime">datetime: {{forecast.dt}}</div>
            <div class="dt-text">dt-text: {{moment(forecast.dt_txt.toLocaleString()).calendar()}}</div>
            <div class="temp">temp: {{Math.round(forecast.main.temp)}}°F</div>
            <div class="feels-like">feels-like: {{ Math.round(forecast.main.feels_like)}}°F</div>
            <div class="humidity">humidity: {{ forecast.main.humidity}}%</div>
            <div class="description">description: {{ forecast.weather[0].description}}</div>
            <div class="wind">wind speed: {{Math.round(forecast.wind.speed)}}</div>
        </div>
        </div>`,
    // methods: {
    //     firstOneIsDifferent: function() {

    //     }
    // }
    // data: () => ({
    //     forecast: getWeather(),
    // }),
    // data: {
    //     forecasts: []
    // }
}
let currentDiv = {
    props: ['forecast', 'moment', 'city'],
    template: `<div class="outer-container">
        <div class="dt-text">{{forecast.name}} Current:</div>
        <img :src="'http://openweathermap.org/img/wn/' + forecast.weather[0].icon + '@2x.png'">

        <div class="inner-container">
            <div class="datetime">datetime: {{forecast.dt}}</div>
            <div class="temp">temp: {{Math.round(forecast.main.temp)}}°F</div>
            <div class="feels-like">feels-like: {{ Math.round(forecast.main.feels_like)}}°F</div>
            <div class="humidity">humidity: {{ forecast.main.humidity}}%</div>
            <div class="description">description: {{ forecast.weather[0].description}}</div>
            <div class="wind">wind speed: {{Math.round(forecast.wind.speed)}}</div>
        </div>
        </div>`,
}
//vue stuff
var vm = new Vue({
    el: '#vm',
    data: {
        search: '',
        city: '',
        forecasts: [],
        timeZone: '',
        moment: moment,
    },
    methods: {

    },
    components: {
        forecastDiv,
        currentDiv,
    }
    // computed
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
            // cityName.innerText = `${vm.city} Current:`
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
