let width = 1000;
let height = 1000;
let cnv = document.querySelector('canvas');
let ctx = cnv.getContext('2d');
let vxLog
let vyLog

let ballArr = [
    ball1 = {
        color: 'white',
        radius: 20,
        px: Math.random()*460 + 20,
        py: Math.random()*460 + 20,
        vx: (2*Math.random()-1)*5,
        vy: (2*Math.random()-1)*5,
    },
    ball2 = {
        color: 'black',
        radius: 20,
        px: Math.random()*460 + 530,
        py: Math.random()*460 + 20,
        vx: (2*Math.random()-1)*5,
        vy: (2*Math.random()-1)*5,
    },
    ball3 = {
        color: 'black',
        radius: 20,
        px: Math.random()*460 + 20,
        py: Math.random()*460 + 530,
        vx: (2*Math.random()-1)*5,
        vy: (2*Math.random()-1)*5,
    },
    ball4 = {
        color: 'white',
        radius: 20,
        px: Math.random()*460 + 530,
        py: Math.random()*460 + 530,
        vx: (2*Math.random()-1)*5,
        vy: (2*Math.random()-1)*5,
    },
]

let wallArr = [
    w01 = {
        px: 490,
        py: 0,
        width: 20,
        height: 490,
        ID: 'wall01',
        orient: 'vert',
    },
    w02 = {
        px: 490,
        py: 510,
        width: 20,
        height: 490,
        ID: 'wall02',
        orient: 'vert',
    },
    w03 = {
        px: 0,
        py: 490,
        width: 490,
        height: 20,
        ID: 'wall03',
        orient: 'hori',
    },
    w04 = {
        px: 510,
        py: 490,
        width: 490,
        height: 20,
        ID: 'wall04',
        orient: 'hori',
    },
    ]

//create horiz on vert test arrays
// let vertArr = []
// for (let i=0; i<wallArr.length; i++) {
//     if (wallArr[i].orient === 'vert') {
//         vertArr.push(wallArr[i])
//     }
// }
// let horiArr = []
// for (let i=0; i<wallArr.length; i++) {
//     if (wallArr[i].orient === 'hori') {
//         horiArr.push(wallArr[i])
//     }
// }


function mainLoop() {
    ctx.clearRect(0, 0, width, height);
    drawWalls(wallArr)//final version
    // drawWalls(vertArr)//test version
    // drawWalls(horiArr)//test version
    moveBalls(ballArr);
    borderCollision(ballArr);
    wallCollision(ballArr, wallArr);//final version
    // wallCollision(ballArr, vertArr)//test version
    // wallCollision(ballArr, horiArr)//test version
    drawBalls(ballArr);
    window.requestAnimationFrame(mainLoop);
}

// window.requestAnimationFrame(mainLoop)
mainLoop()

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
    for (let i=0; i<wallArr.length; i++) {
        let color = 'grey'
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
        if (ball.vx === 0 && ball.vy ===0) {
            continue
    }
        for (let j=0; j<ballArr.length; j++) {
            //test line below
            let wall = wallArr[j];
            if ((ball.py + ball.radius >= wall.py) && (ball.py - ball.radius <= wall.py + wall.height)) {
                if (ball.vx > 0) {
                    if (ball.px + ball.radius >= wall.px  && ball.px - ball.radius <= wall.px + wall.width) {
                        vxLog, vyLog = vxVyLog(ball)
                        ball.vx *= -1
                        ball.px += ball.vx
                        // ball.vx = 0
                        // ball.vy = 0
                        console.log(`${ball.color} ${wall.ID} vx: ${vxLog} vy: ${vyLog} condition: if vx > 0`)
                    }
                } else {
                    if ((ball.px + ball.radius >= wall.px)  && (ball.px - ball.radius <= wall.px + wall.width)) {
                        vxLog, vyLog = vxVyLog(ball)
                        ball.vx *= -1
                        ball.px += ball.vx
                        // ball.vx = 0
                        // ball.vy = 0
                        console.log(`${ball.color} ${wall.ID} vx: ${vxLog} vy: ${vyLog} condition: if vx < 0`)
                    }
                }
            }
            if (ball.px + ball.radius >= wall.px && ball.px - ball.radius <= wall.px + wall.width) {
                if (ball.vy > 0) {
                    if ((ball.py + ball.radius >= wall.py) && (ball.py - ball.radius <= wall.py + width)) {
                        vxLog, vyLog = vxVyLog(ball)
                        ball.vy *= -1
                        ball.py += ball.vy
                        // ball.vx = 0
                        // ball.vy = 0
                        console.log(`${ball.color} ${wall.ID} vx: ${vxLog} vy: ${vyLog} condition: if vy > 0`)
                    }
                } else {
                    if ((ball.py + ball.radius >= wall.py) && (ball.py - ball.radius <= wall.py + wall.height)) {
                        vxLog, vyLog = vxVyLog(ball)
                        ball.vy *= -1
                        ball.py += ball.vy
                        // ball.vx = 0
                        // ball.vy = 0
                        console.log(`${ball.color} ${wall.ID} vx: ${vxLog} vy: ${vyLog} condition: if vy < 0`)

                    }
                }
            }
        }
    }
}


function vxVyLog(ball) {
    vxLog = ball.vx
    vyLog = ball.vy
    return vxLog, vyLog
}
//check pixels by mouse
// window.addEventListener('mousemove', function(e) {
//     this.console.log(e.x, e.y)
// })