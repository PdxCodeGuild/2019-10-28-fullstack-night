let url = 'https://trackapi.nutritionix.com/v2/natural/nutrients/'

let foodItem = {
    props: ['food'],
    template: `<div>{{food.serving_qty}} {{food.serving_unit}} {{food.food_name}} kcal: {{food.nf_calories}} fat: {{food.nf_total_fat}} carb: {{food.nf_total_carbohydrate}} protein: {{food.nf_protein}}</div>`,
}

let foodName = {
    props: ['food'],
    template: `<div>{{food.serving_qty}} {{food.serving_unit}} {{food.food_name}}</div>`,
}

let foodKcal = {
    props: ['food'],
    template: `<div>{{kcalRound}}</div>`,
    computed: {
        kcalRound: function() {
            return Math.round(this.food.nf_calories)
        }
    }
}

let totalKcal = {
    props: ['totalsObj'],
    template: `<div>{{totalsObj.kcal}}</div>`
}

let foodFat = {
    props: ['food'],
    template: `<div>{{fatRound}}</div>`,
    computed: {
        fatRound: function() {
            return Math.round(this.food.nf_total_fat)
        }
    }
}

let foodCarb = {
    props: ['food'],
    template: `<div>{{carbRound}}</div>`,
    computed: {
        carbRound: function() {
            return Math.round(this.food.nf_total_carbohydrate)
        }
    }
}

let foodProtein = {
    props: ['food'],
    template: `<div>{{proteinRound}}</div>`,
    computed: {
        proteinRound: function() {
            return Math.round(this.food.nf_protein)
        }
    }
}

let totalsDiv = {
    // props: ['totals'],
    template: `<div>Totals: kcal: {{totals.nf_calories}} fat: {{totals.nf_total_fat}} carb: {{totals.nf_total_carbohydrate}} protein: {{totals.nf_protein}}</div>`,
    computed: {
        totals: function() {
            totalObj = {'nf_calories': 0, 'nf_total_fat': 0, 'nf_total_carbohydrate': 0, 'nf_protein': 0};
            for (let i=0; i<app.foodItems.length; i++) {
                totalObj.nf_calories += app.foodItems[i].nf_calories
                totalObj.nf_total_fat += app.foodItems[i].nf_total_fat
                totalObj.nf_total_carbohydrate += app.foodItems[i].nf_total_carbohydrate
                totalObj.nf_protein += app.foodItems[i].nf_protein
            }
            return totalObj
        }
    }
}

var app = new Vue({
    el: '#app',
    data: {
        query: 'apple',
        foodItems: [],
        totalsObj: {
            'kcal': 0,
            'fat': 0,
            'carb': 0,
            'protein': 0,
        },
    },
    components: {
        foodItem,
        totalsDiv,
        foodName,
        foodKcal,
        foodFat,
        foodCarb,
        foodProtein,
        totalKcal,
    },
    methods: {

        axiosCall: function() {
            axios({
                method: 'post',
                url: url,
                headers: {
                    'Content-Type': 'application/json',
                    'x-app-id': '9d6f794a',
                    'x-app-key': '0a43551440794adf00f2b58777f29d2e',
                },
                data: {
                    query: app.query,
                },
            }).then((response) => {
                let foods = response.data.foods;
                for (let i=0; i<foods.length; i++) {
                    app.foodItems.push(foods[i])
                }
            })
            // this.totalsAdd();
        },
        
    computed: {
        totalsObj: function() {
            totalsObj = {'kcal': 0, 'fat': 0, 'carb': 0, 'protein': 0};
            for (let i=0; i<app.foodItems.length; i++) {
                totalObj.kcal += app.foodItems[i].nf_calories
                totalObj.fat += app.foodItems[i].nf_total_fat
                totalObj.carb += app.foodItems[i].nf_total_carbohydrate
                totalObj.protein += app.foodItems[i].nf_protein
            }
            for (let property in totalObj) {
                totalObj[property] = Math.round(totalObj[property])
            }
            return totalsObj
        }
    }

        // totalsAdd: function() {
        //     let keys = Object.keys(app.totalsObj)
        //     for (let i=0; i<app.foodItems.length; i++) {
        //         for (let j=0; j<keys.length; j++) {
        //             app.totalsObj[keys[j]] += app.foodItems[i][keys[j]];
        //         }
        //     }
        // }
    }
})