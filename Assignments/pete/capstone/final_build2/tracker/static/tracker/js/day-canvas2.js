var macros = JSON.parse(document.querySelector('#macros').textContent);
var totals = JSON.parse(document.querySelector('#totals').textContent);
var feedback = JSON.parse(document.querySelector('#over_under').textContent);

feedbackToColor = {
    'over': 'hsl(0, 100%, 50%)', //red
    'under': 'hsl(240, 100%, 50%)', //blue
    'goal': 'hsl(120, 100%, 25%)', //green
}

keyToColor = {
    'kcal': 'blue',
    'fat': 'purple',
    'carb': 'yellow',
    'protein': 'red',
}

var keys = Object.keys(macros);
console.log(keys);
var yPos = [10, 85, 160, 235]

let ctx = document.querySelector('canvas').getContext('2d');

let w = 600;
let h = 300;

function mainLoop() {

    
    ctx.font = 'Odibee Sans';

    for (let i=0; i<keys.length; i++) {
        let key = keys[i];
        let goal = macros[key]
        let total = totals[key]
        let prog = total/goal
        let t = w*.70 //t=target

        //filled bar gradient selection
        // let grd = ctx.createLinearGradient(0, yPos[i] + 10, 0, yPos[i] + 45);
        // grd.addColorStop(0, feedbackToColor[feedback[key]]);
        // grd.addColorStop(0.5, 'hsla(0, 0%, 100%');
        // grd.addColorStop(1, feedbackToColor[feedback[key]]);

        //empty bar
        ctx.fillStyle = 'hsla(0, 0%, 0%, 0.5)'
        ctx.fillRect(0, yPos[i], t, 55);
        // ctx.strokeRect(0, yPos[i], t, 55);
        ctx.beginPath();
        ctx.arc(t, yPos[i] + 27.5, 27.5, 1.5*Math.PI, 0.5*Math.PI);
        ctx.fill();

        //filled bar
        // ctx.fillStyle = feedbackToColor[feedback[key]];
        ctx.fillStyle = keyToColor[key];
        if (feedback[key] === 'under') {
            ctx.fillRect(0, yPos[i], prog*t, 55);
        } else {
            ctx.fillRect(0, yPos[i], t, 55);
            // let grdr = ctx.createRadialGradient(t, yPos[i] + 27.5, 0, t, yPos[i] + 27.5, 17.5);
            // grdr.addColorStop(0, 'hsla(0, 0%, 50%');
            // grdr.addColorStop(1, feedbackToColor[feedback[key]]);
            // ctx.fillStyle = feedbackToColor[feedback[key]];
            ctx.beginPath();
            ctx.arc(t, yPos[i] + 27.5, 27.5, 1.5*Math.PI, 0.5*Math.PI);
            ctx.fill();
        }
        
        //outline stroke
        ctx.beginPath();
        ctx.strokeStyle = 'white';
        ctx.lineWidth = 2;
        ctx.moveTo(0, yPos[i]);
        ctx.lineTo(t, yPos[i]);
        ctx.arc(t, yPos[i] + 27.5, 27.5, 1.5*Math.PI, 0.5*Math.PI);
        ctx.lineTo(0, yPos[i] + 55);
        ctx.stroke();
        // ctx.stroke();
        // ctx.stroke();
        // ctx.moveTo()

        ctx.fillStyle = 'black';
        ctx.fillText(key, t*1.1, yPos[i] + 10);
        ctx.fillText(`${total} / ${goal}`, t*1.1, yPos[i] + 30);
        ctx.fillText(feedback[key], t*1.1, yPos[i] + 50);

    }
    if (totals.carb < macros.carb) {
        totals.carb ++
        requestAnimationFrame(mainLoop)
    }
}

mainLoop()