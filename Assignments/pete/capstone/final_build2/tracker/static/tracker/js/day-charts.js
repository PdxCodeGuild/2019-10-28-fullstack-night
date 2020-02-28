var macros = JSON.parse(document.querySelector('#macros').textContent);
var totals = JSON.parse(document.querySelector('#totals').textContent);

let goalsGram = true
let cnvG = document.querySelector('#goals-pie');
var ctxGoals = document.querySelector('#goals-pie').getContext('2d');

var ctxProgress = document.querySelector('#progress-bar').getContext('2d');

var goalsChart = new Chart(ctxGoals, {
    type: 'pie',

    data: {
        labels: ['Fat (g)', 'Carbs (g)', 'Protein (g)'],

        datasets: [{
            // label: 'g per day',
            data: [macros.fat, macros.carb, macros.protein],
            backgroundColor: [
                'purple',
                'yellow',
                'red',
            ]
        }]
    },
    options: {

        responsive: false,
        // legend: {
        //     display: false,
        // }
    }
})

cnvG.addEventListener('click', function() {
    if (goalsGram) {
        goalsGram = false;

        goalsChart.data.datasets[0].data[0] *= 9;
        goalsChart.data.datasets[0].data[1] *= 4;
        goalsChart.data.datasets[0].data[2] *= 4;

        goalsChart.data.labels = ['Fat (kcal)', 'Carbs (kcal)', 'Protein (kcal)'];

        goalsChart.update();
    } else {
        goalsGram = true;

        goalsChart.data.datasets[0].data[0] /= 9;
        goalsChart.data.datasets[0].data[1] /= 4;
        goalsChart.data.datasets[0].data[2] /= 4;

        goalsChart.data.labels = ['Fat (g)', 'Carbs (g)', 'Protein (g)'];

        goalsChart.update();
    }
})

var progressChart = new Chart(ctxProgress, {
    type: 'horizontalBar',
    data: {
        labels: ['KCAL', 'FAT', 'CARB', 'PROTEIN'],
        datasets: [{
            label: 'Progress',
            data: [totals.kcal/macros.kcal, totals.fat/macros.fat, totals.carb/macros.carb, totals.protein/macros.protein],
        }]
    },
    options: {
        scales: {
            xAxes: [{
                ticks: {
                    beginAtZero: true,
                    max: 1,
                }
            }]
        }
    }
})