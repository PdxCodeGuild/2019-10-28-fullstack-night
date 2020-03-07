let url = 'https://trackapi.nutritionix.com/v2/natural/nutrients/'


var queryDiv = {
    props: ['query'],
    template: `<div id="query-container">
        <input :query="query" @input="$emit('input', $event.target.value)" @keyup.enter="$emit('axios-call-event', $event)">
        <button @click="$emit('axios-call-event', $event)">Add</button>
        </div>`,
}
//name
var nameDiv = {
    props: ['foodItems'],
    template: `<div id="name-container" class="middle-container">
        <header class="small">Name</header>
        <div class="inner-container">
            <slot></slot>
            <div class="total">Total</div>
        </div>
    </div>`,

}

var foodName = {
    props: ['food'],
    template: `<div>{{food.serving_qty}} {{food.serving_unit}} {{food.food_name}}</div>`,
}
//kcal
var kcalDiv = {
    props: ['foodItems'],
    template: `<div id="kcal-container" class="middle-container">
        <header class="small">Calories</header>
        <div class="inner-container">
            <slot></slot>
        </div>
    </div>`
}

var foodKcal = {
    props: ['food'],
    template: `<div>{{kcalRound}}</div>`,
    computed: {
        kcalRound: function() {
            return Math.round(this.food.nf_calories);
        }
    }
}

let totalKcal = {
    props: ['totalsObj'],
    template: `<div class="total">{{totalsObj.kcal}}</div>`,
}
///Fat
var fatDiv = {
    props: ['foodItems'],
    template: `<div id="fat-container" class="middle-container">
        <header class="small">Fat (g)</header>
        <div class="inner-container">
            <slot></slot>
        </div>
    </div>`
}

var foodFat = {
    props: ['food'],
    template: `<div>{{fatRound}}</div>`,
    computed: {
        fatRound: function() {
            return Math.round(this.food.nf_total_fat);
        }
    }
}

let totalFat = {
    props: ['totalsObj'],
    template: `<div class="total">{{totalsObj.fat}}</div>`,
}
//carb
var carbDiv = {
    props: ['foodItems'],
    template: `<div id="carb-container" class="middle-container">
        <header class="small">Carbs (g)</header>
        <div class="inner-container">
            <slot></slot>
        </div>
    </div>`
}

var foodCarb = {
    props: ['food'],
    template: `<div>{{carbRound}}</div>`,
    computed: {
        carbRound: function() {
            return Math.round(this.food.nf_total_carbohydrate);
        }
    }
}

let totalCarb = {
    props: ['totalsObj'],
    template: `<div class="total">{{totalsObj.carb}}</div>`,
}
//protein
var proteinDiv = {
    props: ['foodItems'],
    template: `<div id="protein-container" class="middle-container">
        <header class="small">Protein (g)</header>
        <div class="inner-container">
            <slot></slot>
        </div>
    </div>`
}

var foodProtein = {
    props: ['food'],
    template: `<div>{{proteinRound}}</div>`,
    computed: {
        proteinRound: function() {
            return Math.round(this.food.nf_protein);
        }
    }
}

let totalProtein = {
    props: ['totalsObj'],
    template: `<div class="total">{{totalsObj.protein}}</div>`,
}

var nutritionix = new Vue({
    el: '#nutritionix',
    data: {
        query: '',
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
            {
                'serving_qty': '3',
                'serving_unit': 'test',
                'food_name': 'food',
                'nf_calories': 123,
                'nf_total_fat': 123,
                'nf_total_carbohydrate': 123,
                'nf_protein': 123,
            },
            {
                'serving_qty': '4',
                'serving_unit': 'test',
                'food_name': 'food',
                'nf_calories': 123,
                'nf_total_fat': 123,
                'nf_total_carbohydrate': 123,
                'nf_protein': 123,
            },
            {
                'serving_qty': '5',
                'serving_unit': 'test',
                'food_name': 'food',
                'nf_calories': 123,
                'nf_total_fat': 123,
                'nf_total_carbohydrate': 123,
                'nf_protein': 123,
            },
            {
                'serving_qty': '6',
                'serving_unit': 'super long super long super long test',
                'food_name': 'food',
                'nf_calories': 123,
                'nf_total_fat': 123,
                'nf_total_carbohydrate': 123,
                'nf_protein': 123,
            },

        ],
    },

    components: {
        'query-div': queryDiv,
        'name-div': nameDiv,
        'kcal-div': kcalDiv,
        'fat-div': fatDiv,
        'carb-div': carbDiv,
        'protein-div': proteinDiv,

        'food-name': foodName,
        'food-kcal': foodKcal,
        'food-fat': foodFat,
        'food-carb': foodCarb,
        'food-protein': foodProtein,

        'total-kcal': totalKcal,
        'total-fat': totalFat,
        'total-carb': totalCarb,
        'total-protein': totalProtein,
    },

    methods: {
        axiosCall: function() {
            console.log('hey')
            axios({
                method: 'post',
                url: url,
                headers: {
                    'Content-Type': 'application/json',
                    'x-app-id': '9d6f794a',
                    'x-app-key': '0a43551440794adf00f2b58777f29d2e',
                },
                data: {
                    query: this.query,
                },
            }).then((response) => {
                let foods = response.data.foods;
                for (let i=0; i<foods.length; i++) {
                    this.foodItems.push(foods[i])
                }
            })
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
        },
    },
})

// var custom = new Vue({
//     el: '#custom',
//     data: {

//     }
// })