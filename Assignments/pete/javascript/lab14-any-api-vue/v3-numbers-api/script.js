let goButton = document.querySelector('button')

let radioDiv = {
    props: ['radioButton', 'type'],
    template: `<span><input type="radio" name="type-option" :value="radioButton" v-on:click="$emit('typeclick', radioButton)">{{radioButton}}</span>`
}

let numFactsDiv = {
    props: ['numFacts'],
    template: `<span>{{numFacts.data}}</span>`
}

var app = new Vue({
    el: "#app",
    data: {
        number: '',
        type: '',
        radioButtons: ['trivia', 'math', 'date', 'year'],
        numFactsArr: [],
    },
    components: {
        radioDiv,
        numFactsDiv,
    },
    computed: {
        reversedNumFactsArr: function() {
            return this.numFactsArr.reverse()
        }
    },
    methods: {
        updateType(e) {
            this.type = e;
        },
        getInfo() {
            let url = `http://numbersapi.com/${app.number}/${app.type}`
            
            axios.get(url)
            .then(function(response) {
                console.log(response)
                app.numFactsArr.push(response);
            })

        }
    }

})


// let number = '1'
// let type = 'trivia'
goButton.addEventListener('onclick', function() {
    console.log('we clickin')
    
})