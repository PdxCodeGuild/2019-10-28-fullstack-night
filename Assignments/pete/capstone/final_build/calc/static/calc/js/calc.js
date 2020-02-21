var calcMacrosUrl = JSON.parse(document.querySelector('#calc_macros').textContent);
var csrftoken = document.querySelector("input[name='csrfmiddlewaretoken']").value;

var calcApp = new Vue({
    el: '#calc-app',
    data: {
        weight: '',
        measSys: '',
        bfp: '',
        actLvl: '',
        goal: '',
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
                    console.log(response.data)
                }
            )
        }
    }
})