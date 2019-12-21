let width = 1000;
let height = 1000;
let cnv = document.querySelector('canvas');
let ctx = cnv.getContext('2d');

let ball1 = {
    color: 'red',
    radius: 75,
    mass: 75,
    px: 75 + Math.random()*(width - 75),
    py: 75 + Math.random()*(height - 75),
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10,
    ay: Math.random() / 10,//gravity
};

let ball2 = {
    color: 'blue',
    radius: 75,
    mass: 75,
    px: 75 + Math.random()*(width - 75),
    py: 75 + Math.random()*(height - 75),
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10,
    ay: Math.random() / 10,//gravity
}

// let ball3 = {
//     color: 'yellow',
//     radius: 4,
//     px: Math.random()*width,
//     py: Math.random()*height,
//     vx: (2*Math.random()-1)*10,
//     vy: (2*Math.random()-1)*10,
//     ay: Math.random() / 10,//gravity
// }

let ballsArray = [ball1, ball2]
let warningCount = 0
let collisionCount = 0
let collisionBool
let distanceBool
let distance
let checkD = 9999

function main_loop() {
    ctx.clearRect(0, 0, width, height);
    // ctx.fillStyle = 'red', 0.0000000001;
    // ctx.fillRect(0, 0, width, height);
    // update the ball's position
    for (let i=0; i < ballsArray.length; i++) {
        collisionBool = false;
        // ballsArray[i].vy += ballsArray[i].ay //gravity
        ballsArray[i].px += ballsArray[i].vx
        ballsArray[i].py += ballsArray[i].vy
        
        // check if it hit a boundary
        if (ballsArray[i].px + ballsArray[i].vx < ballsArray[i].radius || ballsArray[i].px > width - ballsArray[i].radius) {
            ballsArray[i].vx *= -1
            // ballsArray[i].vx *= .99 //friction
            // ballsArray[i].vy *= .99 //friction
        }
        if (ballsArray[i].py + ballsArray[i].vy < ballsArray[i].radius || ballsArray[i].py > height - ballsArray[i].radius) {
            ballsArray[i].vy *= -1
            // ballsArray[i].vx *= .99 //friction
            // ballsArray[i].vy *= .99 //friction
        }
        
        // draw the ballsArray[i]
        ctx.beginPath();
        ctx.arc(ballsArray[i].px, ballsArray[i].py, ballsArray[i].radius, 0, 2 * Math.PI, false);
        ctx.fillStyle = ballsArray[i].color;
        ctx.fill();
    }
    for (n=0; n<ballsArray.length; n++) {
        let ballA = ballsArray[n];
        let ballB = ballsArray[(n+1)%2]
        distance = Math.sqrt(
            (Math.pow((ballA.px - ballB.px), 2)) + (Math.pow((ballA.py - ballB.py), 2))
            );

        // if (distance > ballA.radius + ballB.radius)
        if (ballA.px + ballA.radius + ballB.radius > ballB.px 
            && ballA.px < ballB.px + ballA.radius + ballB.radius
            && ballA.py + ballA.radius + ballB.radius > ballB.py 
            && ballA.py < ballB.py + ballA.radius + ballB.radius) {
                warningCount ++
                console.log(`warning collision! ${warningCount}`)
                distance = Math.sqrt(
                    (Math.pow((ballA.px - ballB.px), 2)) + (Math.pow((ballA.py - ballB.py), 2))
                    );
                if (distance <= ballA.radius + ballB.radius && checkD > distance) {   
                    checkD = distance
                    collisionCount ++
                    console.log(`COLLISION! ${collisionCount}`)
                    // ballA.vx = (ballA.vx * (ballA.mass - ballB.mass) + (2 * ballB.mass * ballB.vx)) / (ballA.mass + ballB.mass);
                    ballA.vx = (ballA.vx * (ballA.mass - ballB.mass) + (2 * ballB.mass * ballB.vx)) / (ballA.mass + ballB.mass);
                    ballA.vy = (ballA.vy * (ballA.mass - ballB.mass) + (2 * ballB.mass * ballB.vy)) / (ballA.mass + ballB.mass);
                    ballB.vx = (ballB.vx * (ballB.mass - ballA.mass) + (2 * ballA.mass * ballA.vx)) / (ballB.mass + ballA.mass);
                    ballB.vy = (ballB.vy * (ballB.mass - ballA.mass) + (2 * ballA.mass * ballA.vy)) / (ballB.mass + ballA.mass);
                    ballA.px += ballA.vx
                    ballA.py += ballA.vy
                    ballB.px += ballB.vx
                    ballB.py += ballB.vy
                    collisionBool = true;
                    // distanceBool = true;
                    console.log('tried to do collision thing right')
                    // break
                    
                }
            }
        if (collisionBool === true) {break}   
    }
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);