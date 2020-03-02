// let ctx = document.querySelector('canvas').getContext('2d');
// let w = 500;
// let h = 300;

var app = new Vue({
    el: '#app',
    data: {

        goalKcal: '',
        goalFat: '',
        goalCarb: '',
        goalProtein: '',

        kcal: '',
        fat: '',
        carb: '',
        protein: '',

        progressObj: {
            'goalKcal': this.goalKcal,
            'goalFat': this.goalFat,
            'goalCarb': this.goalCarb,
            'goalProtein': this.goalProtein,
    
            'kcal': this.kcal,
            'fat': this.fat,
            'carb': this.carb,
            'protein': this.protein,
        },

        w: 500,
        h: 300,
    },

    mounted: function() {
        this.ctx = document.querySelector('canvas').getContext('2d');
        // let w = 500;
        // let h = 300;
    },
    directives: {
        loadCanvas: function(el, binding) {
            console.log(el)
            console.log(binding)
            // let ctx = el.getContext('2d');
            // ctx.clearRect(0, 0, this.w, this.h);
            this.ctx.fillStyle = 'hotpink';
            this.ctx.fillRect(0, 0, this.w, this.h);
            console.log(this.w, this.h);
        }
    }
});

