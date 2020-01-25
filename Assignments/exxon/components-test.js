



Vue.component('change-red',{

    props:['items'],
    template: '<button v-on:click="changeThings"> change to red </button>',
    methods:{
        changeThings:function(){
            three.style.color = "red";
            two.style.color = "red";
            one.style.color = "red";
            
        }
    
    }

})



Vue.component('change-green',{

    props:['items'],
    template: '<button v-on:click="changeThings"> change to green </button>',
    methods:{
        changeThings:function(){
            three.style.color = "green";
            two.style.color = 'green'
            one.style.color = 'green'
            
        }
    
    }

})




// Vue.component("all-information",{
//     props: ['infoProp'],
//     template: `<div><ul> <li v-for="(item, key, index) in infoProp">{{key + ", " + item }}</li></ul></div>`,

//     computed: {
//         countItems: function(){
//             console.log("it worked bro!");
//             return ( 'i love this thing bro')
//         }
//     }
  

// })


Vue.component('items-all', {

    props: ['items'],
    template: `<h3>{{items}}</h3>`,

})


Vue.component('dark-weatherinfo', {
    props:['locationCondTemp','LocationInfo','locationIcon'],
    template:`<div>  <h3 id="CityState">{{LocationInfo}}</h3> <h3 id="CondTemp">{{locationCondTemp}}</h3> <i id="weatherIcon" v-bind:class="[{'wi': true}, locationIcon ? 'wi-' + locationIcon : '']"></i></div> `,
    // trying to filter data dictionary look up filtering dictionary of object this is wrong i searched array instead on
})



let app = new Vue({

 el: "#app",
 data: {
    items: ['one', 'two', 'three'],
    darkWeatherinfo:'',
    locationCondTemp: '',
    Locationinfo:'',
    locationIcon:'',




  },



  methods: {






    // finally got the geolocating api to send lat/long to darksky api 

    getLocationWeather:function(){

        axios.get("https://ipapi.co/json")             
            .then((response)=>{ this.Locationinfo = response.data.city + " " + response.data.region
                console.log(this.Locationinfo)     // <---- response that has state and city
            })
            axios.get("https://ipapi.co/latlong")      
                .then((response)=>{ this.locationLatLong = response.data
                    console.log(this.locationLatLong)                                   // <------ response that has lat/long for current ip address
                    axios.get(`https://api.darksky.net/forecast/ee2b9f44555aefe31a9a72cae4f5999b/${this.locationLatLong}?units=us&exclude=minutely,hourly,daily,alerts,flags`)  
                        .then((response)=>{ this.locationCondTemp = response.data.currently.summary + ' ' + ' ' + (Math.floor(response.data.currently.temperature)) + "°F"
                            console.log(this.locationCondTemp)  // <-- response that has  weather for vancouver  and icon and temp
                        })
                })
            

        },


    getWeatherIcon:function(){

        axios.get("https://ipapi.co/json")             
        .then((response)=>{ this.Locationinfo = response.data.city + " " + response.data.region
   // <---- response that has state and city
        })
        axios.get("https://ipapi.co/latlong")      
            .then((response)=>{ this.locationLatLong = response.data
                                  // <------ response that has lat/long for current ip address
                axios.get(`https://api.darksky.net/forecast/ee2b9f44555aefe31a9a72cae4f5999b/${this.locationLatLong}?units=us&exclude=minutely,hourly,daily,alerts,flags`)  
                    .then((response)=>{ this.locationIcon = response.data.currently.icon 
                        console.log(this.locationIcon)  // <-- response that has  weather for vancouver  and icon and temp
                    })
            })








    }






        // .then((response)=>{ this.locationLat = response.data.latitude
        //     console.log(this.locationLat)
        // })
    

    },


    // getLocationLong:function(){
    //     axios({
    //         method:'get',
    //         url:"https://ipapi.co/json/"
    //     })

    //     .then((response)=>{ this.locationLong = response.data.longitude
    //         console.log(this.locationLong)
    //     })


    // },



    


    // getLocationIp:function(){
    //     axios({
    //         method:'get',
    //         url:"https://ipapi.co/json/"
    //     })

    //     .then((response)=>{ this.locationIp = response.data.city
    //         console.log(this.locationIp)
    //     })


    // },




    getWeatherDescription:function(){

        axios({
            method: 'get',
            url:"https://www.metaweather.com/api/location/2475687",
            
        })

        
        .then((response) => { this.weatherLocationDesc = response.data.consolidated_weather[0].weather_state_name
            console.log(this.weatherLocationDesc)
         })




    },





    DarkskyWeather:function(){

        axios({
            method: 'get',
            url:'https://api.darksky.net/forecast/ee2b9f44555aefe31a9a72cae4f5999b/18.681305,-99.101349?units=us&exclude=minutely,hourly,daily,alerts,flags',
            
        })

        .then((response)=>{
            this.darkWeatherinfo = response.data.currently.summary;
            console.log(this.darkWeatherinfo)
        })

    },






  

  mounted: function(){
      this.getLocationWeather();
      this.getWeatherIcon();
  },




});