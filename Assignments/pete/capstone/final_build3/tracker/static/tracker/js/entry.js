var queryDiv = {
    props: ['query'],
    template: `<div id="query-container">
        <input :query="query" v-on:input="$emit('input', $event.target.value)">
        <button>Add</button>
        </div>`,
}

var nameDiv = {
    props: ['foodItems'],
    template: `<div id="name-container">
        <header class="small">Name</header>
        <div class="inner-container">
            <slot></slot>
            <div>Total</div>
        </div>
    </div>`,

}

var foodName = {
    props: ['food'],
    template: `<div>{{food.serving_qty}} {{food.serving_unit}} {{food.food_name}}</div>`,
}

var kcalDiv = {
    props: ['foodItems'],
    template: `<div id="kcal-container">
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
    template: `<div>{{totalsObj.kcal}}</div>`,
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
        ],
    },

    components: {
        'query-div': queryDiv,
        'name-div': nameDiv,
        'kcal-div': kcalDiv,
        'food-name': foodName,
        'food-kcal': foodKcal,
        'total-kcal': totalKcal,
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