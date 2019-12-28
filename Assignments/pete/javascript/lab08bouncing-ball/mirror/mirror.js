let cnv = document.querySelector('canvas');
let ctx = cnv.getContext('2d')
let width = 1920;
let height = 1080;

let blocky = {
    px: 500,
    py: 500,
    width: 50,
    height: 150,
    color: 'hsla(0, 0%, 0%, 0.50)',
    // color: 'black',

}

// ctx.fillStyle = 'hsla(0, 0%, 0%, 0.5)';
// ctx.fillRect(0, 0, width, height);

function mainLoop() {
    ctx.clearRect(0, 0, width, height);
    ctx.fillStyle = 'hsla(0, 0%, 0%, 0.5)';
    ctx.fillRect(0, 0, width, height);
    ctx.fillStyle = 'grey';
    ctx.fillRect((width / 2) - 5, 0, 10, height)//vert
    ctx.fillRect(0, (height / 2) - 5, width, 10);
    drawBlocky();
    blockyReflectionX();
    blockyReflectionY();
    blockyReflectionXY();
    requestAnimationFrame(mainLoop);
}
mainLoop()

function drawBlocky() {
    ctx.fillStyle = blocky.color
    ctx.fillRect(blocky.px, blocky.py, blocky.width, blocky.height);
}

function blockyReflectionX() {
    ctx.fillStyle = blocky.color;
    ctx.fillRect(width - blocky.px - blocky.width, blocky.py, blocky.width, blocky.height)
}

function blockyReflectionY() {
    ctx.fillStyle = blocky.color;
    ctx.fillRect(blocky.px, height - blocky.py - blocky.height, blocky.width, blocky.height)
}

function blockyReflectionXY() {
    ctx.fillStyle = blocky.color;
    ctx.fillRect(width - blocky.px - blocky.width, height - blocky.py - blocky.height, blocky.width, blocky.height);
}

addEventListener('keydown', function(e) {
    if (e.which === 65 || e.which === 37) {
        blocky.px -= 10
    } if (e.which === 68 || e.which === 39) {
        blocky.px += 10
    } if (e.which === 87 || e.which === 38) {
        blocky.py -= 10
    } if (e.which === 83 || e.which === 40) {
        blocky.py += 10
    }
})