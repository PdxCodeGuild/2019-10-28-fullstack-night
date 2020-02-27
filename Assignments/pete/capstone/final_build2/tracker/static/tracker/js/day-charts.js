var macros = JSON.parse(document.querySelector('#macros').textContent);
var totals = JSON.parse(document.querySelector('#totals').textContent);

var ctxGoals = document.querySelector('#goals-pie').getContext('2d');

var ctxProgress = document.querySelector('#progress-bar').getContext('2d');

var goalsChart = new Chart(ctxGoals, {
    type: 'pie',

    data: {
        labels: ['Fat', 'Carbs', 'Protein'],

        datasets: [{
            label: 'g per day',
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
        legend: {
            display: false,
        }
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