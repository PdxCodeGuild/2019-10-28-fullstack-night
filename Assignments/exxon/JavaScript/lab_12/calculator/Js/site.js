let app = new Vue({
    el: '#app',
    data: {
        previous:null,
        current:"",
        operator:null,
        operatorClicked: false,

},

    
methods:{
    clear: function(){
        this.current = "";

    },

    sign: function(){
        this.current = this.current.charAt(0) === "-" ?
        this.current.slice(1) : `-${this.current}`;
    },

    percent: function(){
        this.current = `${parseFloat(this.current) / 100}`
    },

    append: function(number){
        if (this.operatorClicked){
            this.current = "";
            this.operatorClicked = false;
        }
        this.current = `${this.current}${number}`;

    },

    dot: function(){
        if (this.current.indexOf('.') === -1){
            this.append('.');
        }
    },



    setPrevious(){
        this.previous = this.current;
        this.operatorClicked = true;
    },
    divide: function(){
        this.operator = (a, b) => a / b;
        this.setPrevious();
    },

    times: function(){
        this.operator = (a, b) => a * b;
        this.setPrevious();

    },

    minus: function(){
        this.operator = (a, b) => a - b;
        this.setPrevious();
    },

    add: function(){
        this.operator = (a, b) => a + b;
        this.setPrevious();
    },


    equal: function(){
        this.current = `${this.operator(
            parseFloat(this.current), 
            parseFloat(this.previous)
          )}`;
          this.previous = null;

    },









}

})

    

