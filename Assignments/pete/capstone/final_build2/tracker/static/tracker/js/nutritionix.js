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
    template: `<div>{{totalsObj.kcal}}</div>`,
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

let totalFat = {
    props: ['totalsObj'],
    template: `<div>{{totalsObj.fat}}</div>`,
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

let totalCarb = {
    props: ['totalsObj'],
    template: `<div>{{totalsObj.carb}}</div>`,
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

let totalProtein = {
    props: ['totalsObj'],
    template: `<div>{{totalsObj.protein}}</div>`,
}


// let totalsDiv = {
//     // props: ['totals'],
//     template: `<div>Totals: kcal: {{totals.nf_calories}} fat: {{totals.nf_total_fat}} carb: {{totals.nf_total_carbohydrate}} protein: {{totals.nf_protein}}</div>`,
//     computed: {
//         totals: function() {
//             totalsObj = {'nf_calories': 0, 'nf_total_fat': 0, 'nf_total_carbohydrate': 0, 'nf_protein': 0};
//             for (let i=0; i<this.foodItems.length; i++) {
//                 totalsObj.nf_calories += this.foodItems[i].nf_calories
//                 totalsObj.nf_total_fat += this.foodItems[i].nf_total_fat
//                 totalsObj.nf_total_carbohydrate += this.foodItems[i].nf_total_carbohydrate
//                 totalsObj.nf_protein += this.foodItems[i].nf_protein
//             }
//             return totalsObj
//         }
//     }
// }

var app = new Vue({
    el: '#app',
    data: {
        query: 'apple',
        foodItems: [
            {
                'serving_qty': '1',
                'serving_unit': 'test',
                'food_name': 'food',
                'nf_calories': 123,
                'nf_total_fat': 123,
                'nf_total_carbohydrate': 123,
                'nf_protein': 123,
            },
            {
                'serving_qty': '2',
                'serving_unit': 'test',
                'food_name': 'food',
                'nf_calories': 123,
                'nf_total_fat': 123,
                'nf_total_carbohydrate': 123,
                'nf_protein': 123,
            },

        ],
        // totalsObj: {
        //     'kcal': 0,
        //     'fat': 0,
        //     'carb': 0,
        //     'protein': 0,
        // },
    },
    components: {
        foodItem,
        foodName,
        foodKcal,
        foodFat,
        foodCarb,
        foodProtein,
        // totalsDiv,
        totalKcal,
        totalFat,
        totalCarb,
        totalProtein,
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
    },
        
    computed: {
        totalsObj: function() {
            totalsObj = {'kcal': 0, 'fat': 0, 'carb': 0, 'protein': 0};
            for (let i=0; i<this.foodItems.length; i++) {
                totalsObj.kcal += this.foodItems[i].nf_calories
                totalsObj.fat += this.foodItems[i].nf_total_fat
                totalsObj.carb += this.foodItems[i].nf_total_carbohydrate
                totalsObj.protein += this.foodItems[i].nf_protein
            }
            for (let property in totalsObj) {
                totalsObj[property] = Math.round(totalsObj[property])
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
})