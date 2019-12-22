/*
NEXT TIME: Add a blocky key to each platform (or rectangle).  This will be a boolean to see if blocky is on that particular platform.
*/
let width = 1000;
let height = 1000;
let cnv = document.querySelector('canvas')
let ctx = cnv.getContext('2d');
let ground

ctx.fillStyle = 'brown'
ctx.fillRect(25, 750, 250, 50)
ctx.fillRect(375, 750, 250, 50)
ctx.fillRect(725, 750, 250, 50)


let blocky = {
    color: 'green',
    height: 75,
    width: 35,
    px: 75,
    py: 500,
    vx: 0,
    vy: 0,
    ay: 0.1,
    ground: '',
}

let rect1 = {
    color: 'red',
    px: 25,
    py: 750,
    width: 250,
    height: 50,
    blockyContact = '',
}

let rect2 = {
    color: 'yellow',
    px: 375,
    py: 750,
    width: 250,
    height: 50,
    blockyContact: '',
}

let rect3 = {
    color: 'blue',
    px: 725,
    py: 750,
    width: 250,
    height: 50,
    blockyContact: '',
}

let rectArr = [rect1, rect2, rect3]

function mainLoop() {
    ctx.clearRect(0, 0, width, height)
    for (let i=0; i<rectArr.length; i++) {

        ctx.fillStyle = rectArr[i].color
        ctx.fillRect(rectArr[i].px, rectArr[i].py, rectArr[i].width, rectArr[i].height)
        
        //text
        ctx.fillStyle = 'black';
        ctx.font = "3rem Arial";
        ctx.fillText("The Adventures of Blocky", 225, 315)

        //update blocky
        blocky.px += blocky.vx
        blocky.py += blocky.vy
        blocky.vy += blocky.ay//grav

        //draw blocky
        ctx.fillStyle = blocky.color
        ctx.fillRect(blocky.px, blocky.py, blocky.width, blocky.height);

        //check collision
        //if blocky.ground {see whether blocky walks off the platform}
        if (blocky.ground) {
            if (blocky.px + blocky.width > rectArr[i].px && blocky.px < rectArr[i].px + rectArr[i].width) {
                blocky.ground = false;
                blocky.ay = 0.1;
                continue;
            }
        }
        if (blocky.ground) {
            blocky.ay = 0;
            continue;
        }
        


        else if (
            (blocky.py + blocky.height > rectArr[i].py//blocky.py check1
                && blocky.py < rectArr[i].py + rectArr[i].height)//blocky.py check2
            && (blocky.px + blocky.width > rectArr[i].px//blocky.px check1
                && blocky.px < rectArr[i].px + rectArr[i].width)//blocky.px check2
            ) {
            // rectArr[i].blockyContact = true;
            blocky.py = rectArr[i].py - blocky.height;
            blocky.vy = 0;
            blocky.ay = 0;
            blocky.ground = true;
            continue;
        }
    }
    // console.log(blocky.ground)
    window.requestAnimationFrame(mainLoop)
}
window.requestAnimationFrame(mainLoop)


document.addEventListener('keydown', function(e) {

    if (e.which === 37 || e.which === 65) {
        blocky.vx = -1.5;
    }
    if (e.which === 39 || e.which === 68) {
        blocky.vx = 1.5;
    }
    if (e.which === 32  && blocky.ground) {
        blocky.vy = -5;
        blocky.ay = 0.1;
        blocky.ground = false;
    }
})
document.addEventListener('keyup', function(e) {
    if (e.which === 37 || e.which === 39 || e.which === 65 || e.which === 68){
        blocky.vx = 0;
    }
})