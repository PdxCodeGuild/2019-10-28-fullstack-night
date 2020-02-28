// let macrosCreateAccount = document.querySelector('#create-account.macros');
// let macrosReCalc = document.querySelector('#recalc-button.macros');

// macrosCreateAccount.style.display = 'none';
// macrosReCalc.style.display = 'none';
// if (userBool) {
//     macrosReCalc.style.display = 'block';
// } else {
//     macrosCreateAccount.style.display = 'block';
// }

var macrosDict = JSON.parse(document.querySelector('#macros_dict').textContent);

let cnvT = document.querySelector('#training-chart');
let trainGram = true;
let cnvR = document.querySelector('#rest-chart');
let restGram = true;

var ctxTrain = document.querySelector('#training-chart').getContext('2d')
var ctxRest = document.querySelector('#rest-chart').getContext('2d')

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

cnvT.addEventListener('click', function() {
    console.log(trainingChart)
    if (trainGram) {
        trainGram = false;
        trainingChart.data.datasets[0].data[0] *= 9;
        trainingChart.data.datasets[0].data[1] *= 4;
        trainingChart.data.datasets[0].data[2] *= 4;
        trainingChart.update();
    } else {
        trainGram = true;
        trainingChart.data.datasets[0].data[0] /= 9;
        trainingChart.data.datasets[0].data[1] /= 4;
        trainingChart.data.datasets[0].data[2] /= 4;
        trainingChart.update();
    }
})

cnvR.addEventListener('click', function() {
    console.log(restingChart)
    if (restGram) {
        restGram = false;
        restingChart.data.datasets[0].data[0] *= 9;
        restingChart.data.datasets[0].data[1] *= 4;
        restingChart.data.datasets[0].data[2] *= 4;
        restingChart.update();
    } else {
        restGram = true;
        restingChart.data.datasets[0].data[0] /= 9;
        restingChart.data.datasets[0].data[1] /= 4;
        restingChart.data.datasets[0].data[2] /= 4;
        restingChart.update();
    }
})