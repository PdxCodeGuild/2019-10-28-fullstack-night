
function randomColor(){
    return `hsl(${Math.floor(Math.random()*360)}, 75%, 85%)`;
};


Vue.component('colorDiv', {
    template: `<p v-bind:style="{ backgroundColor: color}"><slot></slot></p>`,
    data:() => ({
        color: randomColor(),
    }),

});


Vue.component('custombutton', {
    template: '<p> Hi {{ name }} how are you?  <button v-on:click="changeName"> Change me </button></p>',
    data: function(){
        return {
            name: 'Theo'
        }
    },
    methods:{
        changeName:function(){
            this.name = "Galilea";
        }
    
    }

});

Vue.component('exxonspage',{
    template:'<button v-on:click="changePage"> Exxon Page </button>',
    methods:{
        changePage:function(){
            window.location.href = "http://exxonsuarez.com";
        }
    }
})

Vue.component('taskvpage',{
    template:'<button v-on:click="changePage"> TaskV Page </button>',
    methods:{
        changePage:function(){
            window.location.href = "http://suarez21.pythonanywhere.com";
        }
    }
})



Vue.component('changeitems',{
    props:['items'],
    template: '<button v-on:click="changeThings"> change 1 and 5 color </button>',
    methods:{
        changeThings:function(){
            five.style.backgroundColor = randomColor();
            one.style.backgroundColor = randomColor();
        }

    }
})
  



let app = new Vue({

    el: "#app",
    data: {
        items:['one', 'two', 'three', 'four', 'five'],
    },

    
});