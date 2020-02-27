var macros = JSON.parse(document.querySelector('#macros').textContent);
var totals = JSON.parse(document.querySelector('#totals').textContent);
var keys = Object.keys(macros);
console.log(keys);
var yPos = [10, 85, 160, 235]

let ctx = document.querySelector('canvas').getContext('2d');

let w = 600;
let h = 300;

function mainLoop() {
    ctx.fillStyle = 'hsla(0, 0%, 0%, 0.5)';
    ctx.fillRect(0, 0, w, h);
    ctx.font = '20px Arial';
    // for (let i=0; i<yPos.length; i++) {
    //     ctx.fillRect(0, yPos[i], w, 55);
    // }
    for (let i=0; i<keys.length; i++) {
        let key = keys[i];
        let goal = macros[key]
        let total = totals[key]
        let prog = total/goal
        let t = w*.8 //t=target

        ctx.fillRect(0, yPos[i], 1*t, 55);
        ctx.fillText(`G: ${goal} ${key}`,t , yPos[i] + 20);

        ctx.fillRect(0, yPos[i], prog*t, 55);
        ctx.fillText(`P: ${total} ${key}`,prog*t , yPos[i] + 45);
        console.log(`key ${key}; goal ${goal}; prog ${prog}`);
    }

}

mainLoop()