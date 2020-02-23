
var calcMacrosUrl = JSON.parse(document.querySelector('#calc_macros').textContent);
var csrftoken = document.querySelector("input[name='csrfmiddlewaretoken']").value;

// let cnvTrain = document.querySelector('#training-chart');
// let ctxTrain = cnvTrain.getContext('2d');
// let cnvRest = document.querySelector('#rest-chart');
// let ctxRest = cnvRest.getContext('2d');

var calcApp = new Vue({
    el: '#calc-app',
    delimiters: ['d(', ')b'],
    data: {
        weight: '',
        measSys: '',
        bfp: '',
        actLvl: '',
        goal: '',
        trainKcal: '',
        trainFat: '',
        trainCarb: '',
        restKcal: '',
        restFat: '',
        restCarb: '',
        protein: '',
        macrosBool: false,
        calcBool: true,
    },
    methods: {
        calcMacros: function() {
            axios({
                method: 'POST',
                url: calcMacrosUrl,
                data: {
                    weight: this.weight,
                    measSys: this.measSys,
                    bfp: this.bfp,
                    actLvl: this.actLvl,
                    goal: this.goal,
                },
                headers: {
                    "X-CSRFToken": csrftoken,
                }
            }).then(
                (response) => {
                    console.log(response.data);
                    this.trainKcal = response.data['trainKcal'];
                    this.trainFat = response.data['trainFat'];
                    this.trainCarb = response.data['trainCarb'];
                    this.restKcal = response.data['restKcal'];
                    this.restFat = response.data['restFat'];
                    this.restCarb = response.data['restCarb'];
                    this.protein = response.data['protein'];
                    this.macrosBool = true;
                    this.calcBool = false;
                }
            )
        }
    }
})