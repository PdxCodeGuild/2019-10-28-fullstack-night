let buttonDiv = {
    props: ['button'],
    template: `<button>{{button.value}}</button>`,
}

let displayDiv = {
    template: `<div><slot></slot></div>`
}

var app = new Vue({
    el: '#app',
    data: {
        buttons: [
            {value: '0', cat: 'digit'},
            {value: '1', cat: 'digit'},
            {value: '2', cat: 'digit'},
            {value: '3', cat: 'digit'},
            {value: '4', cat: 'digit'},
            {value: '5', cat: 'digit'},
            {value: '6', cat: 'digit'},
            {value: '7', cat: 'digit'},
            {value: '8', cat: 'digit'},
            {value: '9', cat: 'digit'},
            {value: '.', cat: 'dot'},
            {value: '=', cat: 'equals'},
            {value: '+/-', cat: 'plusMinus'},
            {value: '%', cat: 'percent'},
            {value: '+', cat: 'operand'},
            {value: '-', cat: 'operand'},
            {value: '*', cat: 'operand'},
            {value: '/', cat: 'operand'},
        ],
        buttonFlags: {
            digit: true,
            operand: false,
            dot: true,
            plusMinus: false,
            percent: false,
            equals: true,
        },
        val1: '',
        val2: '',
        operand: '',
        equals: '',
        val3: '',
        // expression: [this.val1 + this.operand + this.val3 + this.equals + this.val3],
    },
    components: {
        buttonDiv,
        displayDiv,
    },
    methods: {
        updateExpression: function(button) {
            if (button.cat === 'digit') {
                this.digitMethod(button)
            } else if (button.cat === 'operand') {
                this.operandMethod(button)
            } else if (button.cat === 'equals') {
                this.equalsMethod()
            }
        },
        digitMethod: function(button) {
            if (this.operand) {
                this.val2 += button.value
            } else {
                this.val1 += button.value
            }
        },
        operandMethod: function(button) {
            if (this.val1 && !(this.val2)) {
                this.operand += button.value
            }
        },
        equalsMethod: function() {
            this.equals = '=';
            if (this.operand === '+') {
                this.val3 = parseInt(this.val1) + parseInt(this.val2)
            } else if (this.operand === '-') {
                this.val3 = parseInt(this.val1) - parseInt(this.val2)
            } else if (this.operand === '*') {
                this.val3 = parseInt(this.val1) * parseInt(this.val2)
            } else if (this.operand === '/') {
                this.val3 = parseInt(this.val1) / parseInt(this.val2)
            }
        }
    },
    computed: {
        expression: function() {
            return this.val1 + this.operand + this.val2 + this.equals + this.val3
        }
    }
})
