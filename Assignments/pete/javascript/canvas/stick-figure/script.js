let cnv = document.querySelector('canvas');
let ctx = cnv.getContext('2d');
let width = 500;
let height = 500;


class StickFigure {
    constructor(px, py, r, color) {
        this.px = px;//position x
        this.py = py;//position y
        this.r = r;//radius
        // this.lW = this.r/7//line width
        this.fillColor = color
    }
    get lW() {
        return this.r/7
    }
    drawHead() {
        ctx.beginPath();
        ctx.arc(this.px, this.py, this.r, 0, 2 * Math.PI, false);
        ctx.fillStyle = this.fillColor;
        ctx.fill();
    }
    drawTorso() {
        ctx.strokeStyle = this.fillColor;
        ctx.lineWidth = this.lW;
        ctx.beginPath();
        ctx.moveTo(this.px, this.py);
        ctx.lineTo(this.px, this.py + 4*this.r);
        ctx.stroke();
    }
    drawArm(lOR) {//left or right
        ctx.strokeStyle = this.fillColor;
        ctx.lineWidth = this.lW;
        ctx.beginPath();
        ctx.moveTo(this.px, this.py + 1.5*this.r);
        ctx.lineTo(this.px + 1.5*this.r*lOR, this.py + 1.5*this.r);
        ctx.stroke();
    }
    drawLeg(lOR) {
        ctx.strokeStyle = this.fillColor;
        ctx.lineWidth = this.lW;
        ctx.beginPath();
        ctx.moveTo(this.px, this.py + 4*this.r);
        ctx.lineTo(this.px + 1.5*this.r*lOR, this.py + 5.5*this.r);
        ctx.stroke();
    }
}

let jebediah = new StickFigure(250, 100, 70, 'green');
// jebediah.drawHead()
let cleetus = new StickFigure(50, 50, 25, 'red')

function stickFigureLoop() {
    ctx.clearRect(0, 0, width, height);
    jebediah.drawHead();
    jebediah.drawTorso();
    jebediah.drawArm(1);
    jebediah.drawArm(-1);
    jebediah.drawLeg(1);
    jebediah.drawLeg(-1);
    cleetus.drawHead();
    cleetus.drawTorso();
    cleetus.drawArm(1);
    cleetus.drawArm(-1);
    cleetus.drawLeg(1);
    cleetus.drawLeg(-1);
    requestAnimationFrame(stickFigureLoop)
}
stickFigureLoop();

addEventListener('keydown', function(e) {
    if (e.which === 65) {
        jebediah.px -= 1;
    } else if (e.which === 87) {
        jebediah.py -= 1;
    } else if (e.which === 68) {
        jebediah.px += 1;
    } else if (e.which === 83) {
        jebediah.py += 1;
    } else if (e.which === 82) {
        jebediah.r += 1;
    } else if (e.which === 70) {
        jebediah.r -= 1;
    }
    if (e.which === 37) {
        cleetus.px -= 1;
    } else if (e.which === 38) {
        cleetus.py -= 1;
    } else if (e.which === 39) {
        cleetus.px += 1;
    } else if (e.which === 40) {
        cleetus.py += 1;
    } else if (e.which === 13) {
        cleetus.r += 1;
    } else if (e.which === 222) {
        cleetus.r -= 1;
    }


})