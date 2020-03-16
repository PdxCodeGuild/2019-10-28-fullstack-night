



let app = new Vue({

    el: '#app',
    data: {

        search_input:null,
        type_input:null,
        joke_results:[],


    },

    methods: {
        
        getJokes:function(){
            axios({
                
                method: 'get',
                baseURL: "https://sv443.net/jokeapi/category/Any",
                params:{
                    
                    // type:this.type_input,
                    // filter:this.search_input
                },
                headers:{
                    
                }
                


            })
            .then((response) => {this.joke_results = response.data
                console.log(response.data)
            })
            .catch(function(error){
                console.log(error)
            });

        },


    },

    mounted: function(){
     this.getJokes();
    },




});