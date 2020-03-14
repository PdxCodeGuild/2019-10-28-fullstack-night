var csrftoken = document.querySelector("input[name='csrfmiddlewaretoken']").value;
var dateLink = JSON.parse(document.querySelector('#date_link').textContent);
var trackCustom = JSON.parse(document.querySelector('#track_custom').textContent);
var trackNutritionix = JSON.parse(document.querySelector('#track_nutritionix').textContent);
var day = JSON.parse(document.querySelector('#day').textContent);
console.log('abcde')
let url = 'https://trackapi.nutritionix.com/v2/natural/nutrients/'

var queryDiv = {
    props: ['value'],
    template: `<div id="query-container">
        <input id="query-input" :value="value" @input="$emit('input', $event.target.value)" @keyup.enter="$emit('axios-call-event', $event)">
        <button @click="$emit('axios-call-event', $event)">Add</button>
    </div>`,
}

// var recipeDiv = {
//     props: ['value'],
//     template: `<div id="recipe-container>
//         <input type="checkbox"
//     </div>`
// }

var headerDiv = {
    props: ['header'],
    template: `<header class="small">{{ header }}</header>`
}

var foodValDiv = {
    props: ['foodVal'],
    template: `<div :class="nameOrNo">{{ foodValComputed }}</div>`,
    computed: {
        foodValComputed: function() {
            if (typeof this.foodVal === 'number') {
                return Math.round(this.foodVal);
            }
            return this.foodVal;
        },
        nameOrNo: function() {
            if (typeof this.foodVal === 'number') {
                return '';
            }
            return 'name';
        },
    },
};

var totalDiv = {
    props: ['total'],
    template: `<div :class="nameOrNo" class="total">{{ totalComputed }}</div>`,
    computed: {
        totalComputed: function() {
            if (typeof this.total === 'number') {
                return Math.round(this.total);
            }
            return this.total;
        },
        nameOrNo: function() {
            if (typeof this.total === 'number') {
                return '';
            };
            return 'name';
        },
    },

};

var nutritionix = new Vue({
    el: '#nutritionix',
    data: {
        headers: ['Name', 'Calories', 'Fat (g)', 'Carb (g)', 'Protein (g)'],
        query: '',
        foodItems: [],
        recipe: false,
    },

    components: {
        'query-div': queryDiv,
        'header-div': headerDiv,
        'food-val-div': foodValDiv,
        'total-div': totalDiv,
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
                    foodObj.protein = food.nf_protein;
                    this.foodItems.push(foodObj)
                }
            })
            // I WANT TO CLEAR THE INPUT FIELD AT THE END OF THIS METHOD
            this.query = '';
            // event.target.reset();
        },

        trackIt: function() {
            console.log('track it')
            axios({
                method: 'POST',
                url: this.trackNutritionixDate,
                data: this.foodItems,
                headers: {
                    'X-CSRFToken': csrftoken,
                },
            }).then((response) => {
                window.location = this.day3Date
            })
        },
    },
        
    computed: {
        day3Date: function() {
            return day.slice(0, day.length - 2) + dateLink + '/';
        },

        trackNutritionixDate: function() {
            return trackNutritionix.slice(0, trackNutritionix.length - 2) + dateLink + '/';
        },

        totalsObj: function() {
            totalsObj = {'kcal': 0, 'fat': 0, 'carb': 0, 'protein': 0};
            for (let i=0; i<this.foodItems.length; i++) {
                totalsObj.kcal += this.foodItems[i].kcal
                totalsObj.fat += this.foodItems[i].fat
                totalsObj.carb += this.foodItems[i].carb
                totalsObj.protein += this.foodItems[i].protein
            }
            return totalsObj
        },

        totals: function() {
            let totals = ['Total']
            let values = Object.values(this.totalsObj);
            for (let i=0; i<values.length; i++) {
                totals.push(values[i]);
            }
            return totals;
        },

        foodVals: function() {
            // outArr = []
            // this.foodItems.map((el)=>outArr.push(...Object.values(el).map((el)=>(typeof el === 'number' ? Math.round(el):el))))
            // return outArr
            let foodVals = [];
            for (let i=0; i<this.foodItems.length; i++) {
                let foodItem = this.foodItems[i];
                let values = Object.values(foodItem)
                console.log(values)
                for (let j=0; j<values.length; j++) {
                    foodVals.push(values[j]);
                }
            }
            return foodVals
        },
    },
})

let customName = {
    props: ['name'],
    template: `<div>
        <span>Name:</span>
        <input class="custom" type="text" :name="name" @input="$emit('input', $event.target.value)">
    </div>`
};

let customKcal = {
    props: ['kcal'],
    template: `<div>
        <span>Calories:</span>
        <input class="custom" type="number" :kcal="kcal" @input="$emit('input', $event.target.value)">
    </div>`
};

let customFat = {
    props: ['fat'],
    template: `<div>
        <span>Grams of Fat</span>
        <input class="custom" type="number" :fat="fat" @input="$emit('input', $event.target.value)">
    </div>`
};

let customCarb = {
    props: ['carb'],
    template: `<div>
        <span>Grams of Carbohydrates:</span>
        <input class="custom" type="number" :carb="carb" @input="$emit('input', $event.target.value)">
    </div>`
};

let customProtein = {
    props: ['protein'],
    template: `<div>
        <span>Grams of Protein:</span>
        <input class="custom" type="number" :protein="protein" @input="$emit('input', $event.target.value)">
    </div>`
};


var custom = new Vue({
    el: '#custom',
    data: {
        name: '',
        kcal: '',
        fat: '',
        carb: '',
        protein: '',
    },
    components: {
        'custom-name': customName,
        'custom-kcal': customKcal,
        'custom-fat': customFat,
        'custom-carb': customCarb,
        'custom-protein': customProtein,
    },
    computed: {
        trackCustomDate: function() {
            return trackCustom.slice(0, trackCustom.length - 2) + dateLink + '/';
        },
        day3Date: function() {
            return day.slice(0, day.length - 2) + dateLink + '/';
        },
    },
    methods: {
        trackIt: function() {
            console.log('track it')
            axios({
                method: 'POST',
                url: this.trackCustomDate,
                data: {
                    name: this.name,
                    kcal: parseInt(this.kcal),
                    fat: parseInt(this.fat),
                    carb: parseInt(this.carb),
                    protein: parseInt(this.protein),
                },
                headers: {
                    'X-CSRFToken': csrftoken,
                },
            }).then((response) => {
                window.location = this.day3Date

            });
        }
    }
})