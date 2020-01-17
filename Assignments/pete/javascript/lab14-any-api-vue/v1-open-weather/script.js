//vue component forecastDiv
let forecastDiv = {
    props: ['forecast', 'moment', 'timeZone'],
    template: `<div class="outer-container">
        <img :src="'http://openweathermap.org/img/wn/' + forecast.weather[0].icon + '@2x.png'">

        <div class="inner-container">
            <div class="dt-text">{{localTime}}</div>
            <div class="temp">Temperature: {{Math.round(forecast.main.temp)}}°F</div>
            <div class="feels-like">Feels Like: {{Math.round(forecast.main.feels_like)}}°F</div>
            <div class="humidity">Humidity: {{forecast.main.humidity}}%</div>
            <div class="description">Description: {{forecast.weather[0].description}}</div>
            <div class="wind">{{windInfo}}</div>
        </div>
        </div>`,
    computed: {
        localTime: function() {
            return moment(this.forecast.dt_txt.toLocaleString()).add(vm.timeZone, 'seconds').calendar()
        },
        windInfo: function() {
            let windSpeed = this.forecast.wind.speed
            windSpeed = Math.round(windSpeed)
            let windDirDeg = this.forecast.wind.deg
            let windDir
            if (windDirDeg <= 22.5 || windDirDeg > 337.5) {windDir = 'N'}
            else if (windDirDeg > 22.5 && windDirDeg <= 67.5) {windDir = 'NE'}
            else if (windDirDeg > 67.5 && windDirDeg <= 112.5) {windDir = 'E'}
            else if (windDirDeg > 112.5 && windDirDeg <= 157.5) {windDir = 'SE'}
            else if (windDirDeg > 157.5 && windDirDeg <= 202.5) {windDir = 'S'}
            else if (windDirDeg > 202.5 && windDirDeg <= 147.5) {windDir = 'SW'}
            else if (windDirDeg > 147.5 && windDirDeg <= 292.5) {windDir = 'W'}
            else if (windDirDeg > 292.5 && windDirDeg <= 337.5) {windDir = 'NW'}
            return `Wind: ${windSpeed}mph ${windDir}`
        },
    }
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
    template: `<div class="big outer-container">
        <img :src="'http://openweathermap.org/img/wn/' + forecast.weather[0].icon + '@2x.png'">
    
        <div class="inner-container">
            <div class="dt-text">{{forecast.name}} Current:</div>
            <div class="temp">Temperature: {{Math.round(forecast.main.temp)}}°F</div>
            <div class="feels-like">Feels Like: {{ Math.round(forecast.main.feels_like)}}°F</div>
            <div class="humidity">Humidity: {{ forecast.main.humidity}}%</div>
            <div class="description">Description: {{ forecast.weather[0].description}}</div>
            <div class="wind">{{windInfo}}</div>
        </div>
        </div>`,
    computed: {
        windInfo: function() {
            let windSpeed = this.forecast.wind.speed
            windSpeed = Math.round(windSpeed)
            let windDirDeg = this.forecast.wind.deg
            let windDir
            if (windDirDeg <= 22.5 || windDirDeg > 337.5) {windDir = 'N'}
            else if (windDirDeg > 22.5 && windDirDeg <= 67.5) {windDir = 'NE'}
            else if (windDirDeg > 67.5 && windDirDeg <= 112.5) {windDir = 'E'}
            else if (windDirDeg > 112.5 && windDirDeg <= 157.5) {windDir = 'SE'}
            else if (windDirDeg > 157.5 && windDirDeg <= 202.5) {windDir = 'S'}
            else if (windDirDeg > 202.5 && windDirDeg <= 147.5) {windDir = 'SW'}
            else if (windDirDeg > 147.5 && windDirDeg <= 292.5) {windDir = 'W'}
            else if (windDirDeg > 292.5 && windDirDeg <= 337.5) {windDir = 'NW'}
            return `Wind: ${windSpeed}mph ${windDir}`
        },
    }
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
