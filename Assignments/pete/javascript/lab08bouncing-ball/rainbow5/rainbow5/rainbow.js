let cnv = document.querySelector('canvas');
let ctx = cnv.getContext('2d');
let width = 1920;
let height = 1080;
let gravity = {
    ax: 0.0,
    ay: 0.5,
}
accDir = {
    x: '',
    y: '',
}
// let explodeBool


let gravObjs = [
    obj01 = {ax:  0.0, ay:  0.5},
    obj02 = {ax: -0.1, ay:  0.4},
    obj03 = {ax: -0.2, ay:  0.3},
    obj04 = {ax: -0.3, ay:  0.2},
    obj05 = {ax: -0.4, ay:  0.1},

    obj06 = {ax: -0.5, ay:  0.0},
    obj07 = {ax: -0.4, ay: -0.1},
    obj08 = {ax: -0.3, ay: -0.2},
    obj09 = {ax: -0.2, ay: -0.3},
    obj10 = {ax: -0.1, ay: -0.4},

    obj11 = {ax:  0.0, ay: -0.5},
    obj12 = {ax:  0.1, ay: -0.4},
    obj13 = {ax:  0.2, ay: -0.3},
    obj14 = {ax:  0.3, ay: -0.2},
    obj15 = {ax:  0.4, ay: -0.1},

    obj16 = {ax:  0.5, ay:  0.0},
    obj17 = {ax:  0.4, ay:  0.1},
    obj18 = {ax:  0.3, ay:  0.2},
    obj19 = {ax:  0.2, ay:  0.3},
    obj20 = {ax:  0.1, ay:  0.4},
]
// let ax = 0.1
// let ay = 0.4
let r = 3
rainbowArray = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

function ballGenerator(oldBall) {
    newBall = {
        color: rainbowArray[Math.floor(Math.random() * rainbowArray.length)],
        radius: r,
        px : oldBall.px,
        py : oldBall.py,
        vx : (2*Math.random() - 1)*15,
        vy : (2*Math.random() - 1)*15,
        children: getChildren(),
    }
    return newBall
}

let rainbowBalls = [
    firstBall = {
        color : rainbowArray[Math.floor(Math.random() * rainbowArray.length)],
        radius : r,
        px : Math.random()*width,
        py : Math.random()*(height/2),
        vx : (2*Math.random() - 1)*15,
        vy : (Math.random()*-1)*15,
        children : getChildren(),
    }
]

function borderCollision(rainbowBalls) {
    for (let i=0; i<rainbowBalls.length; i++) {
        if (rainbowBalls[i].px <= rainbowBalls[i].radius || rainbowBalls[i].px >= width - rainbowBalls[i].radius) {
            //friction
            // rainbowBalls[i].vx *= -0.99
            // rainbowBalls[i].vy *= 0.99
            //no friction
            rainbowBalls[i].vx *= -1



        }
        if (rainbowBalls[i].py >= height - rainbowBalls[i].radius) { //rainbowBalls[i].py < rainbowBalls[i].radius || add this for top border collision
            //friction
            // rainbowBalls[i].vy *= -0.99
            // rainbowBalls[i].vx *= 0.99
            //no friction
            rainbowBalls[i].vy *= -1
        } 
        rainbowBalls[i].px += rainbowBalls[i].vx
        rainbowBalls[i].py += rainbowBalls[i].vy

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
    ctx.fillStyle = 'hsla(0, 0%, 0%, 0.05)'
    ctx.fillRect(0, 0, width, height);
    moveBalls(rainbowBalls);
    borderCollision(rainbowBalls);
    explode();
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

function changeGrav2 () {
    setTimeout(changeGrav2, 1000)

    if ((gravity.ax <= 0 && gravity.ax > -0.5) && (gravity.ay > 0 && gravity.ay <= 0.5)) {
        accDir.x = 'left';
        accDir.y = 'up';
    } else if ((gravity.ax >= -0.5 && gravity.ax < 0) && (gravity.ay <= 0 && gravity.ay > -0.5)) {
        accDir.x = 'right';
        accDir.y = 'up';
    } else if ((gravity.ax >= 0 && gravity.ax <0.5) && (gravity.ay >= -0.5 &&gravity.ay < 0)) {
        accDir.x = 'right';
        accDir.y = 'down';
    } else if ((gravity.ax <= 0.5 && gravity.ax > 0) && (gravity.ay > 0 && gravity.ay < 0.5)) {
        accDir.x = 'left';
        accDir.y = 'down'
    }
    
    if (accDir.x === 'left') {
        gravity.ax -= .1;
    } else if (accDir.x === 'right') {
        gravity.ax += .1
    }

    if (accDir.y === 'up') {
        gravity.ay -= .1;
    } else if (accDir.y === 'down') {
        gravity.ay += .1;
    }
    console.log(gravity)
    console.log(accDir)
}

function changeGrav3 () {
    setTimeout(changeGrav3, 5000)

    for (let i=0; i<gravObjs.length; i++) {
        if (gravity.ax === gravObjs[i].ax && gravity.ay === gravObjs[i].ay) {
            gravity.ax = gravObjs[(i + 1) % gravObjs.length].ax
            gravity.ay = gravObjs[(i + 1) % gravObjs.length].ay
            break
        }
    }
}

function getBigger() {
    setTimeout(getBigger, 5000)
    for (let i=0; i<rainbowBalls.length; i++) {
        rainbowBalls[i].radius += 1
    }
}

function getBigger2() {
    setTimeout(getBigger2, 1000)
    for (let i=0; i<rainbowBalls.length; i++) {
        rainbowBalls[i].radius += Math.random()*rainbowBalls[i].radius
    }
}

function getBigger3() {
    setTimeout(getBigger3, 100)
    for (let i=0; i<rainbowBalls.length; i++) {
        rainbowBalls[i].radius += rainbowBalls[i].radius * 0.05;
    }
}

function getBigger4() {
    setTimeout(getBigger4, 100)
    for (let i=0; i<rainbowBalls.length; i++) {
        rainbowBalls[i].radius += rainbowBalls[i].radius * Math.random()*0.01;
    }
}

function explode() {
    for (let i=0; i<rainbowBalls.length; i++) {
        let ball = rainbowBalls[i];

        if (ball.children === 1 && ball.radius >= 25) {
            for (let j=0; j<ball.children; j++) {
                let newBall = ballGenerator(ball);
                rainbowBalls.push(newBall);
            }
            rainbowBalls[i] = ballGenerator(ball);

        } else if (ball.children === 3 && ball.radius >= 50) {
            for (let j=0; j<ball.children; j++) {
                let newBall = ballGenerator(ball);
                rainbowBalls.push(newBall);
            }
            rainbowBalls[i] = ballGenerator(ball);

        } else if (ball.children === 6 && ball.radius >= 100) {
            for (let j=0; j<ball.children; j++) {
                let newBall = ballGenerator(ball);
                rainbowBalls.push(newBall);
            }
            rainbowBalls[i] = ballGenerator(ball);

        } else if (ball.children === 24 && ball.radius >= 200) {
            for (let j=0; j<ball.children; j++) {
                let newBall = ballGenerator(ball);
                rainbowBalls.push(newBall);
            }
            rainbowBalls[i] = ballGenerator(ball);
            console.log('the big one')

        } else if (ball.children === 99 && ball.radius >= 500) {
            for (let j=0; j<ball.children; j++) {
                let newBall = ballGenerator(ball);
                rainbowBalls.push(newBall);
            }
            rainbowBalls[i] = ballGenerator(ball);
            console.log('the bigger one')
        }
    
    }
}

function getChildren() {
    let randChild = Math.random() * 100;
    if (randChild >= 0 && randChild < 50) {
        children = 1;
    } else if (randChild >= 50 && randChild < 80) {
        children = 3;
    } else if (randChild >= 80 && randChild < 95) {
        children = 6;
    } else if (randChild >= 95 && randChild < 99) {
        children = 24;
    } else {
        children = 99;
    }
    return children

}

function changeGrav0 () {
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

// changeGrav()
getBigger4()