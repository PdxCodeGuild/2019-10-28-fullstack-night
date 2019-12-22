let width = 1000;
let height = 1000;
let cnv = document.querySelector('canvas');
let ctx = cnv.getContext('2d');

let ballArr = [
    ball1 = {
        color: 'green',
        radius: 20,
        px: Math.random()*320 + 340,
        py: Math.random()*320 + 340,
        vx: (2*Math.random()-1)*5,
        vy: (2*Math.random()-1)*5,
    },
    ball2 = {
        color: 'orange',
        radius: 20,
        px: Math.random()*320 + 340,
        py: Math.random()*320 + 340,
        vx: (2*Math.random()-1)*5,
        vy: (2*Math.random()-1)*5,
    },
    ball3 = {
        color: 'purple',
        radius: 20,
        px: Math.random()*320 + 340,
        py: Math.random()*320 + 340,
        vx: (2*Math.random()-1)*5,
        vy: (2*Math.random()-1)*5,
    },
]

let wallArr = [
    w01 = {
        px: 300,
        py: 300,
        width: 20,
        height: 150,
    },
    w02 = {
        px: 300,
        py: 550,
        width: 20,
        height: 150,
    },
    w03 = {
        px: 680,
        py: 300,
        width: 20,
        height: 150,
    },
    w04 = {
        px: 680,
        py: 550,
        width: 20,
        height: 150,
    },
    w05 = {
        px: 320,
        py: 300,
        width: 130,
        height: 20,
    },
    w06 = {
        px: 320,
        py: 680,
        width: 130,
        height: 20,
    },
    w07 = {
        px: 550,
        py: 300,
        width: 130,
        height: 20,
    },
    w08 = {
        px: 550,
        py: 680,
        width: 130,
        height: 20,
    },
    ]


function mainLoop() {
    drawWalls(wallArr)
    moveBalls(ballArr)
    borderCollision(ballArr)
    wallCollision(ballArr, wallArr);
    drawBalls(ballArr)
    window.requestAnimationFrame(mainLoop)
}

window.requestAnimationFrame(mainLoop)


function moveBalls(ballArr) {
    for (let i=0; i<ballArr.length; i++) {
        let ball = ballArr[i]
        ball.px += ball.vx
        ball.py += ball.vy
        // ballArr[i].px += ballArr[i].vx;
        // ballArr[i].py += ballArr[i].vy;
    }
}

function drawBalls(ballArr) {
    for (let i=0; i<ballArr.length; i++) {
        ctx.beginPath();
        ctx.arc(ballArr[i].px, ballArr[i].py, ballArr[i].radius, 0, 2 * Math.PI, false);
        ctx.fillStyle = ballArr[i].color;
        ctx.fill();
    }
}

function drawWalls(wallArr) {
    ctx.clearRect(0, 0, width, height);
    for (let i=0; i<wallArr.length; i++) {
        let color = 'brown'
        ctx.fillStyle = color
        ctx.fillRect(wallArr[i].px, wallArr[i].py, wallArr[i].width, wallArr[i].height);
    }
}

function borderCollision(ballArr) {
    for (let i=0; i<ballArr.length; i++) {
        if (ballArr[i].px <= ballArr[i].radius || ballArr[i].px >= width - ballArr[i].radius) {
            ballArr[i].vx *= -1
        }
        if (ballArr[i].py <= ballArr[i].radius || ballArr[i].py >= height - ballArr[i].radius) {
            ballArr[i].vy *= -1
        } 
    }
}

function wallCollision(ballArr, wallArr) {
    for (let i=0; i<ballArr.length; i++) {
        let ball = ballArr[i];
        for (let j=0; j<ballArr.length; j++) {
            let wall = wallArr[j];
            // if ((ball.px + ball.radius >= wall.px && ball.px - ball.radius <= wall.px + wall.width) || (ball.py + ball.radius >=wall.py && ball.py - ball.radius <= wall.py + wall.height)) {
            //     ball.vx = 0
            //     ball.vy = 0
                // console.log('hit', ball.color)
                // if (ball.px + ball.radius >= wall.px && ball.px - ball.radius <= wall.px + wall.width) {
                //     ball.vx *= -1
                // } if (ball.py + ball.radius >= wall.py && ball.py - ball.radius <= wall.py + wall.height) {
                //     ball.vy *= -1
                // }
            // }
            if ((ball.py + ball.radius + 1 >= wall.py) && (ball.py - ball.radius + 1 <= wall.py + wall.height)) {
                if (ball.vx >= 0) {
                    if (ball.px + ball.radius + 1 >= wall.px) {
                        ball.vx *= -1
                    }
                } else {
                    if (ball.px - ball.radius + 1 <= wall.px + wall.width) {
                        ball.vx *= -1
                    }
                }
            }
            if (ball.px + ball.radius + 1 >= wall.px && ball.px - ball.radius + 1 <= wall.px + wall.width) {
                if (((ball.vy >= 0) && (ball.py + ball.radius + 1 >= wall.py) || ((ball.vy <= 0) && (ball.py - ball.radius <= wall.py + wall.height)))) {
                    ball.vy *= -1
                }
            }
        }
    }
}

//check pixels by mouse
// window.addEventListener('mousemove', function(e) {
//     this.console.log(e.x, e.y)
// })