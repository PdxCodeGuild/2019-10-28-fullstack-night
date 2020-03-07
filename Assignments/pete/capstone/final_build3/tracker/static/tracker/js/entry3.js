let url = 'https://trackapi.nutritionix.com/v2/natural/nutrients/'


var queryDiv = {
    props: ['query'],
    template: `<div id="query-container">
        <input :query="query" @input="$emit('input', $event.target.value)" @keyup.enter="$emit('axios-call-event', $event)">
        <button @click="$emit('axios-call-event', $event)">Add</button>
        </div>`,
}

var headerDiv = {
    props: ['header'],
    template: `<header class="small">{{ header }}</header>`
}

var foodValDiv = {
    props: ['foodVal'],
    template: `<div>{{foodValComputed}}</div>`,
    computed: {
        foodValComputed: function() {
            if (typeof this.foodVal === 'number') {
                return Math.round(this.foodVal)
            }
            return this.foodVal
        }
    }
}

var totalDiv = {
    props: ['total'],
    template: `<div>{{ totalComputed }}</div>`,
    computed: {
        totalComputed: function() {
            if (typeof total === 'number') {
                return Math.round(total)
            }
            return total
        }
    },

}

var nutritionix = new Vue({
    el: '#nutritionix',
    data: {
        headers: ['Name', 'Calories', 'Fat (g)', 'Carb (g)', 'Protein (g)'],
        query: '',
        foodItems: [
            {
                'name': 'test name 1',
                'kcal': 123,
                'fat': 234,
                'carb': 34.543,
                'protein': 12.53,
            },
            {
                'name': 'test name 1',
                'kcal': 123,
                'fat': 234,
                'carb': 34.543,
                'protein': 12.53,
            },
            {
                'name': 'test name 1',
                'kcal': 123,
                'fat': 234,
                'carb': 34.543,
                'protein': 12.53,
            },

            {
                'name': 'test name 1',
                'kcal': 123,
                'fat': 234,
                'carb': 34.543,
                'protein': 12.53,
            },

            {
                'name': 'test name 1',
                'kcal': 123,
                'fat': 234,
                'carb': 34.543,
                'protein': 12.53,
            },

            {
                'name': 'test name 1',
                'kcal': 123,
                'fat': 234,
                'carb': 34.543,
                'protein': 12.53,
            },


        ],
    },

    components: {
        'query-div': queryDiv,
        'header-div': headerDiv,
        'food-val-div': foodValDiv,
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
                    let food = foods[i]
                    let foodObj = {}
                    foodObj.name = `${food.serving_qty} ${food.serving_unit} ${food.food_name}`;
                    foodObj.kcal = food.nf_calories;
                    foodObj.fat = food.nf_total_fat;
                    foodObj.carb = food.nf_total_carbohydrate;
                    foodObj.protein = food.protein
                    this.foodItems.push(food)
                }
            })
        },
    },
        
    computed: {
        totalsObj: function() {
            totalsObj = {'kcal': 0, 'fat': 0, 'carb': 0, 'protein': 0};
            for (let i=0; i<this.foodItems.length; i++) {
                totalsObj.kcal += this.foodItems[i].kcal
                totalsObj.fat += this.foodItems[i].fat
                totalsObj.carb += this.foodItems[i].carb
                totalsObj.protein += this.foodItems[i].protein
            }
            for (let property in totalsObj) {
                totalsObj[property] = Math.round(totalsObj[property])
            }
            return totalsObj
        },

        totals: function() {
            let totals = []
            let values = Object.values(this.totalsObj);
            for (let i=0; i<values.length; i++) {
                totals.push(values[i]);
            }
        },
        foodVals: function() {
            // outArr = []
            // this.foodItems.map((el)=>outArr.push(...Object.values(el).map((el)=>(typeof el === 'number' ? Math.round(el):el))))
            // return outArr
            let foodVals = ['Total']
            for (let i=0; i<this.foodItems.length; i++) {
                let foodItem = this.foodItems[i];
                let values = Object.values(foodItem)
                for (let j=0; j<values.length; j++) {
                    foodVals.push(values[j]);
                }
            }
            return foodVals
        }
    },
})

// var custom = new Vue({
//     el: '#custom',
//     data: {

//     }
// })