p5 clock bs

function setup() {
  createCanvas(400, 400);
  //frameRate(36000);
}


let angle = 0;
let angle2 = 0;
let angle3 = 0;
function draw() {
  background(220)
  let v0 = createVector(0, -141);
  let v1 = createVector(200, 200);
  let v2 = createVector(0, -135);
  let v3 = createVector(200, 200);
  let v4 = createVector(0, -120);
  let v5 = createVector(200, 200);
  
  circle(200, 200, 300);
  circle(200, 200, 5);
  drawArrow(v1, v0.rotate(angle), "black");
  angle+=(2*PI)/60;
  
  drawArrow(v3, v2.rotate(angle2), "red");
  angle2+=PI/1800;
  
  drawArrow(v5, v4.rotate(angle3), "blue");
  angle3+=PI/27000;
  
}

function drawArrow(base, vec, myColor) {
  push();
  stroke(myColor);
  strokeWeight(3);
  fill(myColor);
  translate(base.x, base.y);
  line(0, 0, vec.x, vec.y);
  rotate(vec.heading());
  let arrowSize = 3;
  translate(vec.mag() - arrowSize, 0);
  pop();
}


