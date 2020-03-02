var macros = JSON.parse(document.querySelector('#macros').textContent);
var totals = JSON.parse(document.querySelector('#totals').textContent);
var feedback = JSON.parse(document.querySelector('#over_under').textContent);

let dpi = window.devicePixelRatio;
let cnv = document.querySelector('canvas');
let ctx = cnv.getContext('2d');
function fix_dpi() {
    let style_height = +getComputedStyle(cnv).getPropertyValue('height').slice(0, -2);
    let style_width = +getComputedStyle(cnv).getPropertyValue('width').slice(0, -2);
    console.log(style_width, style_height);
    cnv.setAttribute('height', style_height * dpi);
    cnv.setAttribute('width', style_width * dpi);
}



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

let w = 600;
let h = 300;

function mainLoop() {
    ctx.clearRect(0, 0, w, h);
    // fix_dpi();
    ctx.font = 'Odibee Sans';

    for (let i=0; i<keys.length; i++) {
        let key = keys[i];
        let goal = macros[key]
        let total = totals[key]
        let prog = total/goal
        let t = w*.70 //t=target

        //empty bar
        ctx.fillStyle = 'hsla(0, 0%, 0%, 0.5)'
        ctx.fillRect(0, yPos[i], t, 55);
        ctx.beginPath();
        ctx.arc(t, yPos[i] + 27.5, 27.5, 1.5*Math.PI, 0.5*Math.PI);
        ctx.fill();

        //filled bar
        ctx.fillStyle = keyToColor[key];
        if (feedback[key] === 'under') {
            ctx.fillRect(0, yPos[i], prog*t, 55);
        } else {
            ctx.fillRect(0, yPos[i], t, 55);
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

        ctx.fillStyle = 'black';
        ctx.fillText(key, t*1.1, yPos[i] + 10);
        ctx.fillText(`${total} / ${goal}`, t*1.1, yPos[i] + 30);
        ctx.fillText(feedback[key], t*1.1, yPos[i] + 50);

    }
    if (totals.carb < macros.carb) {
        totals.carb ++
    }
    requestAnimationFrame(mainLoop)
}

mainLoop();