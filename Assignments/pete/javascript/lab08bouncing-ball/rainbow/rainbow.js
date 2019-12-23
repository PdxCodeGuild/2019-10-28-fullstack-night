let cnv = document.querySelector('canvas');
let ctx = cnv.getContext('2d');
let width = 1920;
let height = 1080;
let gravity = {
    ax: 0.5,
    ay: 0.
}
// let ax = 0
// let ay = 0.5
let r = 2

let rainbowBalls = [
    red = {
        color: 'red',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
    orange = {
        color: 'orange',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
    yellow = {
        color: 'yellow',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
    green = {
        color: 'green',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
    blue = {
        color: 'blue',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
    indigo = {
        color: 'indigo',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
    violet = {
        color: 'violet',
        radius: r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
    },
]

function borderCollision(rainbowBalls) {
    for (let i=0; i<rainbowBalls.length; i++) {
        if (rainbowBalls[i].px <= rainbowBalls[i].radius || rainbowBalls[i].px >= width - rainbowBalls[i].radius) {
            rainbowBalls[i].vx *= -0.99
            rainbowBalls[i].vy *= 0.99
        }
        if (rainbowBalls[i].py <= rainbowBalls[i].radius || rainbowBalls[i].py >= height - rainbowBalls[i].radius) {
            rainbowBalls[i].vy *= -0.99
            rainbowBalls[i].vx *= 0.99
        } 
    }
}

function drawBalls(rainbowBalls) {
    for (let i=0; i<rainbowBalls.length; i++) {
        ctx.beginPath();
        ctx.arc(rainbowBalls[i].px, rainbowBalls[i].py, rainbowBalls[i].radius, 0, 2 * Math.PI, false);
        ctx.fillStyle = rainbowBalls[i].color;
        ctx.fill();
    }
}

function moveBalls(rainbowBalls) {
    for (let i=0; i<rainbowBalls.length; i++) {
        let ball = rainbowBalls[i]
        ball.vx += gravity.ax
        ball.vy += gravity.ay
        ball.px += ball.vx
        ball.py += ball.vy
    }
}

function rainbowLoop() {
    ctx.fillStyle = 'hsla(0, 0%, 0%, 0.01)'
    ctx.fillRect(0, 0, width, height);
    moveBalls(rainbowBalls);
    borderCollision(rainbowBalls);
    drawBalls(rainbowBalls);
    requestAnimationFrame(rainbowLoop)
}

rainbowLoop()

function changeGrav () {
    setTimeout(changeGrav, 15000)
    // ctx.clearRect(0, 0, width, height);
    if (gravity.ay === 0.5) {
        gravity.ay = 0;
        gravity.ax = -0.5;
    } else if (gravity.ax === -0.5) {
        gravity.ax = 0;
        gravity.ay = -0.5;
    } else if (gravity.ay === -0.5) {
        gravity.ay = 0;
        gravity.ax = 0.5;
    } else if (gravity.ax = 0.5) {
        gravity.ax = 0;
        gravity.ay = 0.5
    }
}
changeGrav()