let progress = {
    goalKcal: document.querySelector('#goalKcal').value,
    goalFat: document.querySelector('#goalFat').value,
    goalCarb: document.querySelector('#goalCarb').value,
    goalProtein: document.querySelector('#goalProtein').value,
    
    kcal: document.querySelector('#kcal').value,
    fat: document.querySelector('#fat').value,
    carb: document.querySelector('#carb').value,
    protein: document.querySelector('#protein').value,
};

let goals = {
    goalKcal: document.querySelector('#goalKcal').value,
    goalFat: document.querySelector('#goalFat').value,
    goalCarb: document.querySelector('#goalCarb').value,
    goalProtein: document.querySelector('#goalProtein').value,
}

let goalsArr = document.querySelectorAll('.goal');
for (let i=0; i<goalsArr.length; i++) {
    let goal = goalsArr[i];
    goals[goal['id']] = goal.value;
}

let current = {
    goalKcal: document.querySelector('#goalKcal').value,
    goalFat: document.querySelector('#goalFat').value,
    goalCarb: document.querySelector('#goalCarb').value,
    goalProtein: document.querySelector('#goalProtein').value,
}

let goalsArr = document.querySelectorAll('.goal');
for (let i=0; i<goalsArr.length; i++) {
    let goal = goalsArr[i];
    goals[goal['id']] = goal.value;
}

let inputArr = document.querySelectorAll('.input')
for (let i=0; i<inputArr.length; i++){
    inputArr[i].addEventListener('change', function() {
        console.log(inputArr[i]['id']);
        let input = inputArr[i];
        progress[input['id']] = input.value;
    });
};

let ctx = document.querySelector('#cnv').getContext('2d');
let w = 500;
let h = 300;

let yPos = [
    h/30,
    h*(17/60),
    h*(8/15),
    h*(47/60),
]

let barH = h*(11/60)

let t = w*.7

keyToColor = {
    'kcal': 'blue',
    'fat': 'purple',
    'carb': 'yellow',
    'protein': 'red',
}

let keys = Object.keys(keyToColor);

function drawGraph() {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = 'hotpink';
    ctx.fillRect(0, 0, w, h);

    for (let i=0; i<keys.length; i++) {
        //empty bars
        ctx.fillStyle = 'hsla(0, 0%, 0%, 0.25)';
        ctx.fillRect(0, yPos[i]+ h/30, w, barH);

    }

    //target
    ctx.strokeStyle = 'black'
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(t*.9, 0);
    ctx.lineTo(t*.9, h);
    ctx.moveTo(t*1.1, 0);
    ctx.lineTo(t*1.1, h);
    ctx.stroke();
}
drawGraph();