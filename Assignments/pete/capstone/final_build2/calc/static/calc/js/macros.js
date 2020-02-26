let macrosCreateAccount = document.querySelector('#create-account.macros');
let macrosReCalc = document.querySelector('#recalc-button.macros');

macrosCreateAccount.style.display = 'none';
macrosReCalc.style.display = 'none';
if (userBool) {
    macrosReCalc.style.display = 'block';
} else {
    macrosCreateAccount.style.display = 'block';
}

var macrosDict = JSON.parse(document.querySelector('#macros_dict').textContent);

var ctxTrain = document.querySelector('#training-chart').getContext('2d')

var trainingChart = new Chart(ctxTrain, {
    type: 'pie',

    data: {
        labels: ['Fat', 'Carbs', 'Protein'],

        datasets: [{
            label: "g per day",
            data: [macrosDict.train_fat, macrosDict.train_carb, macrosDict.protein],
            backgroundColor: [
                'purple',
                'yellow',
                'red',
            ]
        }]
    }
})

var ctxRest = document.querySelector('#rest-chart').getContext('2d')

var restingChart = new Chart(ctxRest, {
    type: 'pie',

    data: {
        labels: ['Fat', 'Carbs', 'Protein'],
        
        datasets: [{
            label: "g per day",
            data: [macrosDict.rest_fat, macrosDict.rest_carb, macrosDict.protein],
            backgroundColor: [
                'purple',
                'yellow',
                'red',
            ]
        }]
    }
})

console.log(userBool)