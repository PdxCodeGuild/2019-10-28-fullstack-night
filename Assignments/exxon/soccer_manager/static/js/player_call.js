

let csrf_token = document.querySelector("input[name=csrfmiddlewaretoken]").value;



Vue.component('dark-weatherinfo', {
    props:['locationCondTemp','LocationInfo','locationIcon'],
    template:`<div>  <h3 id="CityState">{{LocationInfo}}</h3> <h3 id="CondTemp">{{locationCondTemp}}</h3> <i id="weatherIcon" v-bind:class="[{'wi': true}, locationIcon ? 'wi-' + locationIcon : '']"></i></div> `,
    // trying to filter data dictionary look up filtering dictionary of object this is wrong i searched array instead on
})


let app = new Vue({

    el: '#app',
    delimiters: ['[[',']]'],
    data: {
        showNav: false,
        shiftX:null,
        shiftY:null,
        activeDiv:null,
        PlayerPics:[],
        locationCondTemp: '',
        Locationinfo:'',
        Newname:'',
        locationIcon:'',
        file: '',
        result: {
            position: '',
            starter: false
        },
        EditPlayer: -1,
        Positions:['Goalkeeper', 'Right-Fullback','Left-Fullback','Center-Back','Sweeper','Defending-Midfielder','Right-Midfielder','Center-Midfielder','Striker','Attacking-Midfielder','Left-Midfielder'],
    },


    methods: {


        editPlayer(newId){
            console.log('was', this.EditPlayer)
            if (this.EditPlayer == -1) this.EditPlayer = newId 
            else this.EditPlayer = -1 
            console.log('changed to', this.EditPlayer)
        },

        submitFile() {
            let formData = new FormData();
            console.log(this)
            formData.append('file', this.file );

            // option to add name of file to dataform and pass to server 
                // formData.append('name',this.file.name)

            // replace name field in file/image for the name that is typed in input field on html page 
            formData.append('name',this.Newname)
            formData.append('position', this.result.position)
            formData.append('starter', this.result.starter)
            console.log('>> formData >> ', formData);
            

            axios.post('/photos/',
                formData, 
                {
                    // had to add csrf_token to headers because it was missing and denying post request
                headers: {
                "X-CSRFToken": csrf_token, 
                }
                },
                
              ).then(function () {
                console.log('SUCCESS!!');
              })
              .catch(function () {
                console.log('FAILURE!!');
            
              })

            
              .then(response => this.getPlayersPhotos())

            

          },


          handleFileUpload() {
            this.file = this.$refs.file.files[0];
            console.log('>>>> 1st element in files array >>>> ', this.file);
          },

        // darksky api says to use proxy to send get request to avoid corse issues below i added cors-anywhere address before url for darksky and it fixed corse issues is this safe?


        getLocationWeather:function(){

            axios.get("https://ipapi.co/json")             
                .then((response)=>{ this.Locationinfo = response.data.city + " " + response.data.region
                    console.log(this.Locationinfo)     // <---- response that has state and city
                })
                axios.get("https://ipapi.co/latlong")      
                    .then((response)=>{ this.locationLatLong = response.data
                        console.log(this.locationLatLong)                                   // <------ response that has lat/long for current ip address
                        axios.get(`https://cors-anywhere.herokuapp.com/https://api.darksky.net/forecast/ee2b9f44555aefe31a9a72cae4f5999b/${this.locationLatLong}?units=us&exclude=minutely,hourly,daily,alerts,flags`)  
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
                    axios.get(`https://cors-anywhere.herokuapp.com/https://api.darksky.net/forecast/ee2b9f44555aefe31a9a72cae4f5999b/${this.locationLatLong}?units=us&exclude=minutely,hourly,daily,alerts,flags`)  
                        .then((response)=>{ this.locationIcon = response.data.currently.icon 
                            console.log(this.locationIcon)  // <-- response that has  weather for vancouver  and icon and temp
                        })
                })
    
    
    
    
    
    
    
    
        },







        // get players photo from server (images uploded by formdata)
        getPlayersPhotos:function(){
            axios({

                method: 'get',
                url: "/photos/",
                headers: {

                },


            })

            .then((response) => {this.PlayerPics = response.data
                console.log(response.data)
            })


            .catch(function(error){
                console.log(error)
            });

        },


        DeletePLayerPhoto:function(index,result){
        // console.log(index)
        // console.log(this.PlayerPics[index])
        var data = new 
            axios({
                
                
                method: 'delete',
// need to add id dynamically?? cant seem to ad ID and have it find the ID of the player it works if number is hard coded like below 
                baseURL: `/photos/${result.id}/`,
                headers: {
                    "X-CSRFToken": csrf_token,
                    'Content-Type': 'application/json'
                },

            })
            // .then((response) => {
            //     console.log(response.data)
            // })
            
            .then( res => this.PlayerPics.splice(index,1),
            console.log(this.PlayerPics))
            .catch(function(error){
                console.log(error)
            });

            // .then(res => this.getPlayersPhotos())
        },




// passing through my 
        UpdatePlayer:function(result,e){

            let formData = new FormData();

// grab the new file user is choosing for the edit and set it as var uploadedfile so i can pass it to form data as uploadedfile
            var uploadedFile = e.target.parentElement.parentElement.querySelector("#Newfile").files[0];
            formData.set('name', result.name)
            formData.append('position', result.position)
            formData.append('starter', result.starter)
//  conditional if there is a new image grab it and swap it out for old image but if no new image 'undefined' dont make a change, this is needed so it doesnt break when no new image is sent with out request
            if(uploadedFile !== undefined){
                formData.append('file', uploadedFile,);
            }

            
           


            
            axios({
                
                method: "put",
                baseURL:`/photos/${result.id}/`,formData,
                headers: {
                    "X-CSRFToken": csrf_token,
                    // "Content-Type": "application/json",
                },
                // data: {
                //     name: result.name,
                //     position: result.position,
                //     file: formData
                    
                // },

                data: formData, 


            })
            .then(res => this.getPlayersPhotos())
            // closes the edit employee input window
            .then( res => this.EditPlayer = null);
        },

        UpdatePlayerInfo(result,e){

                let formData = new FormData();

    // grab the new file user is choosing for the edit and set it as var uploadedfile so i can pass it to form data as uploadedfile
                var uploadedFile = e.target.parentElement.parentElement.querySelector("#Newfile").files[0];
                formData.set('name', result.name)
                formData.append('position', result.position)
                formData.append('number', result.number)
                formData.append('address', result.address)
                formData.set('starter', result.starter)
    //  conditional if there is a new image grab it and swap it out for old image but if no new image 'undefined' dont make a change, this is needed so it doesnt break when no new image is sent with out request
                if(uploadedFile !== undefined){
                    formData.append('file', uploadedFile,);
                }
    
                
               
    
    
                
                axios({
                    
                    method: "put",
                    baseURL:`/photos/${result.id}/`,formData,
                    headers: {
                        "X-CSRFToken": csrf_token,
                        // "Content-Type": "application/json",
                    },
                    // data: {
                    //     name: result.name,
                    //     position: result.position,
                    //     file: formData
                        
                    // },
    
                    data: formData, 
    
    
                })
                .then(res => this.getPlayersPhotos())
                // closes the edit employee input window
                .then( res => this.EditPlayer = null);

        },


        chooseDiv:function(e){

            
            if (e.type === "touchstart"){

                this.activeDiv = e.target;

                initialX = e.touches[0].clientX - this.activeDiv.getBoundingClientRect().left;
                initialY = e.touches[0].clientY - this.activeDiv.getBoundingClientRect().top;

                document.querySelector("#app").append(this.activeDiv);
                this.activeDiv.style.position = "absolute";

                this.activeDiv.style.top = `${e.touches[0].clientY - (this.activeDiv.offsetHeight/5)}px`;
                this.activeDiv.style.left = `${e.touches[0].clientX - (this.activeDiv.offsetWidth/2)}px`;
                
                console.log("where did it go?")
                }
                else{
            
                this.activeDiv = e.target;
                
                this.shiftX = e.clientX - this.activeDiv.getBoundingClientRect().left;
                this.shiftY = e.clientY - this.activeDiv.getBoundingClientRect().top;
                // appending it to body helps with getting position relative to whole page but also causes div to jump to bottom of body we fix this by doing the calculation pagY and pageX calculations in chooseDiv also 
                document.querySelector("#app").append(this.activeDiv);
                this.activeDiv.style.position = "absolute";
                    
                this.activeDiv.style.top = `${e.clientY - (this.activeDiv.offsetHeight/5)}px`;
                this.activeDiv.style.left = `${e.clientX - (this.activeDiv.offsetWidth/2)}px`;
                console.log('choose')
                }
            
        },

        releaseDiv:function(){
            this.activeDiv = null;
            console.log('release')
        },

        dragDiv:function(e){
        
            e.preventDefault();
            if (this.activeDiv !== null){
                // console.log(e.x, e.y)
                console.log(e)
                
                if (e.type === "touchmove"){
                    this.activeDiv.style.position = "absolute";
                    this.activeDiv.style.left = `${e.touches[0].clientX - (this.activeDiv.offsetWidth/2)}px`;
                    this.activeDiv.style.top = `${e.touches[0].clientY - (this.activeDiv.offsetHeight/5)}px`;
                    console.log('Touch');
                }
                else{
                this.activeDiv.style.position = "absolute";
                this.activeDiv.style.top = `${e.pageY - (this.activeDiv.offsetHeight/5)}px`;
                this.activeDiv.style.left = `${e.pageX - (this.activeDiv.offsetWidth/2)}px`;
                }
            }
        },

        UpdateStartingStatus:function(result){

            result.starter = !result.starter
            

            let formData = new FormData();

            // grab the new file user is choosing for the edit and set it as var uploadedfile so i can pass it to form data as uploadedfile


                formData.set('starter', result.starter)
            
    
    
                
                axios({
                    
                    method: "patch",
                    baseURL:`/photos/${result.id}/`,formData,
                    headers: {
                        "X-CSRFToken": csrf_token,
                        // "Content-Type": "application/json",
                    },
                    // data: {
                    //     name: result.name,
                    //     position: result.position,
                    //     file: formData
                        
                    // },
    
                    data: formData, 
    
    
                })
                .then(res => this.getPlayersPhotos())
            

                .then(function () {
                    console.log('SUCCESS!!');
                    })
                .catch(function(error){
                    console.log(error)
                });

        },

        // greet: function (event) {
        //     // `this` inside methods point to the Vue instance
        //     alert('Hello ' + this.name + '!')
        //     // `event` is the native DOM event
        //     alert(event.target.tagName)
        //   }

        



    },
//  starters function filters the PlayerPics results (all players) for only players with Truthy boolean 
    computed: {
        starters: function() {
            console.log('>>>', this.PlayerPics)
            return this.PlayerPics.filter((player) => (player.starter))
        
        },

    },

    

    mounted: function(){
        this.getPlayersPhotos();
        this.getLocationWeather();
        this.getWeatherIcon();
        
    }








})