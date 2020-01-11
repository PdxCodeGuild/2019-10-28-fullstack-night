let qotdUrl = "https://favqs.com/api/qotd"
let favqUrl = "https://favqs.com/api/quotes"
var app = new Vue({
    el: '#app',
    data: {
        quotes: [],
        filterInput: '',
        inputField: '',
    },
    methods: {
        getQuotes: function() {
            axios({
                method: 'get',
                url: favqUrl,
                params: {
                    filter: this.inputField,
                    type: this.filterInput,
                },
                headers: {
                    Authorization: 'Token token=a14f624b5fa91cf62f66a419f66a3503'
                }
            })
            .then((results) => {
                console.log('this:', this)
                console.log('results', results)
                console.log('this.quotes', this.quotes)
                this.quotes = results.data.quotes
            })
            
        },
        getRandomQuotes: function() {
            axios({
                method: 'get',
                url: qotdUrl,
            })
            .then((results) => {
                console.log('this:', this)
                console.log('results', results)
                console.log('this.quotes', this.quotes)
                this.quotes= [results.data.quote]
            })
            
        }
    }
})