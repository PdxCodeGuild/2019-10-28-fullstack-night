let goals = {
    kcal: document.querySelector('#goalKcal').value,
    fat: document.querySelector('#goalFat').value,
    carb: document.querySelector('#goalCarb').value,
    protein: document.querySelector('#goalProtein').value,
}

let goalsArr = document.querySelectorAll('.goal');
for (let i=0; i<goalsArr.length; i++) {
    let goal = goalsArr[i];
    goal.addEventListener('change', function() {
        goals[goal['id']] = goal.value;
    })
};

let currents = {
    kcal: document.querySelector('#kcal').value,
    fat: document.querySelector('#fat').value,
    carb: document.querySelector('#carb').value,
    protein: document.querySelector('#protein').value,
};

let currentArr = document.querySelectorAll('.current');
for (let i=0; i<currentArr.length; i++) {
    let current = currentArr[i];
    current.addEventListener('change', function() {
        currents[current['id']] = current.value;
    })
}

let countUp = {
    kcal: 0,
    fat: 0,
    carb: 0,
    protein: 0,
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
console.log(keys)
function drawGraph() {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = 'hotpink';
    ctx.fillRect(0, 0, w, h);

    //target range
    ctx.strokeStyle = 'black'
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(t*.9, 0);
    ctx.lineTo(t*.9, h);
    ctx.moveTo(t*1.1, 0);
    ctx.lineTo(t*1.1, h);
    ctx.stroke();

    for (let i=0; i<keys.length; i++) {
        let y = yPos[i]
        let key = keys[i];
        let goal = goals[key]
        let current = currents[key]
        let counter = countUp[key]
        let prog = counter/goal

        //empty bars
        ctx.fillStyle = 'hsla(0, 0%, 0%, 0.25)';
        ctx.fillRect(0, y + h/35, w, barH);

        //filled bars
        ctx.fillStyle = keyToColor[key];
        ctx.fillRect(0, y + h/35, prog*t, barH);

        //arc
        ctx.beginPath();
        ctx.arc(prog*t - 0.5, y + h/35 + 0.5*barH, 0.5*barH, 1.5*Math.PI, 0.5*Math.PI);// had to subtract 1 from the startingx... not sure why...
        ctx.fill();

        //outline
        ctx.beginPath();
        ctx.strokeStyle = 'white';
        ctx.lineWidth = 2;
        ctx.moveTo(0, y + h/35);
        ctx.lineTo(prog*t, y + h/35);
        ctx.arc(prog*t - 0.5, y + h/35 + 0.5*barH, 0.5*barH, 1.5*Math.PI, 0.5*Math.PI);
        ctx.lineTo(0, y + h/35 + barH);
        ctx.stroke();
        
        //text
        ctx.font = '20px Odibee Sans'
        ctx.fillStyle = 'black';
        ctx.fillText(counter, t*prog, y + 0.75*barH)
    }

    //target line
    ctx.strokeStyle = 'hsla(0, 0%, 0%, 0.5)'
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(t, 0);
    ctx.lineTo(t, h);
    ctx.stroke();

    if (countUp.kcal < currents.kcal) {
        countUp.kcal ++
        requestAnimationFrame(drawGraph);
    } else if (countUp.fat < currents.fat) {
        countUp.fat ++
        requestAnimationFrame(drawGraph);
    }  else if (countUp.carb < currents.carb) {
        countUp.carb ++
        requestAnimationFrame(drawGraph);
    }  else if (countUp.protein < currents.protein) {
        countUp.protein ++
        requestAnimationFrame(drawGraph); 
    } else {
        console.log('meep')
        // return;
    }
}
drawGraph();

let drawButton = document.querySelector('button')
drawButton.addEventListener('click', function() {
    drawGraph();
    console.log('test');
});
