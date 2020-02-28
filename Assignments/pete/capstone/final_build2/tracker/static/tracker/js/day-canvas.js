var macros = JSON.parse(document.querySelector('#macros').textContent);
var totals = JSON.parse(document.querySelector('#totals').textContent);
var feedback = JSON.parse(document.querySelector('#over_under').textContent);

feedbackToColor = {
    'over': 'hsl(0, 100%, 50%, 0.5)', //red
    'under': 'hsl(240, 100%, 50%, 0.5)', //blue
    'goal': 'hsl(120, 100%, 25%, 0.5)', //green
}

var keys = Object.keys(macros);
console.log(keys);
var yPos = [10, 85, 160, 235]

let ctx = document.querySelector('canvas').getContext('2d');

let w = 600;
let h = 300;

function mainLoop() {
    ctx.fillStyle = 'hsl(0,0%,50%)';
    // ctx.fillStyle = 'hsl(0,0%,100%)';
    // ctx.fillStyle = 'hsla(0, 0%, 0%)';
    // ctx.fillStyle = 'hotpink';
    ctx.fillRect(0, 0, w, h);
    ctx.font = '20px Arial';

    for (let i=0; i<keys.length; i++) {
        let key = keys[i];
        let goal = macros[key]
        let total = totals[key]
        let prog = total/goal
        let t = w*.70 //t=target

        let grd = ctx.createLinearGradient(0, yPos[i] + 10, 0, yPos[i] + 45);
        grd.addColorStop(0, feedbackToColor[feedback[key]]);
        grd.addColorStop(0.5, 'hsla(0, 0%, 50%');
        // grd.addColorStop(0.5, 'hsla(0, 0%, 50%, 0.5');
        grd.addColorStop(1, feedbackToColor[feedback[key]]);

        //empty bar
        ctx.fillStyle = 'hsla(0, 0%, 0%, 0.5)'
        ctx.fillRect(0, yPos[i], t, 55);
        ctx.beginPath();
        ctx.arc(t, yPos[i] + 27.5, 30, 1.5*Math.PI, 0.5*Math.PI);
        ctx.fill();

        //filled bar
        ctx.fillStyle = grd
        if (feedback[key] === 'under') {
            ctx.fillRect(0, yPos[i], prog*t, 55);
        } else {
            ctx.fillRect(0, yPos[i], t, 55);
            let grdr = ctx.createRadialGradient(t, yPos[i] + 27.5, 0, t, yPos[i] + 27.5, 30);
            grdr.addColorStop(0, 'hsla(0, 0%, 50%');
            grdr.addColorStop(1, feedbackToColor[feedback[key]]);
            ctx.beginPath();
            ctx.arc(t, yPos[i] + 27.5, 30, 1.5*Math.PI, 0.5*Math.PI);
            ctx.fill();
        }
        
        ctx.fillStyle = 'black';
        ctx.fillText(key, t*1.1, yPos[i] + 20);
        ctx.fillText(`${total} / ${goal}`, t*1.1, yPos[i] + 45);

        // ctx.fillText(`G: ${goal} ${key}`, t, yPos[i] + 20);
        // ctx.fillText(`P: ${total} ${key}`, prog*t, yPos[i] + 45);
        // console.log(`key ${key}; goal ${goal}; prog ${prog}`);
        // totals.protein += 0.001;
        // requestAnimationFrame(mainLoop)
    }

}

mainLoop()