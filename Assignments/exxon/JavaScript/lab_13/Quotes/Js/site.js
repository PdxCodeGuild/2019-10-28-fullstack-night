



let app = new Vue({

    el: '#app',
    data: {

        search_input:null,
        type_input:null,
        quote_results:[],


    },

    methods: {
        
        getQuotes:function(){
            axios({
                
                method: 'get',
                baseURL: "https://favqs.com/api/quotes/",
                params:{
                    page:1,
                    type:this.type_input,
                    filter:this.search_input
                },
                headers:{
                    Authorization: 'Token token="e2fbc2fdb71d5e22f40b638b8d9568cb"'
                }
                


            })
            .then((response) => {this.quote_results = response.data.quotes
                console.log(response.data)
            })
            .catch(function(error){
                console.log(error)
            });

        },


    },

    mounted: function(){
     this.getQuotes();
    },




});
