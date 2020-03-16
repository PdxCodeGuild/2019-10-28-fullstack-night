

  
var backgrnd = document.getElementById("back");
var ctx2 = backgrnd.getContext("2d"); 

backgrnd.width = 1000;
backgrnd.height = 630;

  

var alley =  new Image();
alley.src = "https://cdn4.vectorstock.com/i/1000x1000/28/93/art-scenery-cartoon-style-game-background-vector-14922893.jpg";

var enemy = new Image();
enemy.src = "stone-guy.PNG";

var brick = new Image();
brick.src = "brick.png";

window.onload = function drawImage(){

  var scrollval = 0;
  var scrollspeed = 5; 

  function loop(){

    ctx2.drawImage(alley, -scrollval, 0);
    ctx2.drawImage(alley, backgrnd.width - scrollval, 0 );
    ctx2.drawImage(enemy,backgrnd.width - scrollval, 460 );
    ctx2.drawImage(brick,backgrnd.width - scrollval, 100, )


    scrollval += scrollspeed;

    if (scrollval == backgrnd.width)
    scrollval = 0;

    window.requestAnimationFrame(loop);



  }

  loop();

};



console.log(enemy);













var cnv = document.getElementById("my_canvas");
var ctx = cnv.getContext('2d');




var ball = {
    radius: 15,
    gravity: 0.5,
    friction: 0.90,
    px: Math.random()*1000,
    py: Math.random()*500,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10,


    

draw: function() {
ctx.beginPath();
ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
ctx.fillStyle = 'pink';
ctx.fill();
}

};






function bounce(){
    ctx.clearRect(0,0, cnv.width, cnv.height);
    window.requestAnimationFrame(bounce);
    ball.draw();
    ball.px += ball.vx;
    ball.py += ball.vy;
    ball.vy += ball.gravity;
    var enemy = enemy;
    
    if (ball.py + ball.vy > cnv.height-ball.radius || ball.py + ball.vy < 0) {
        ball.vy = -ball.vy * -ball.friction;
        ball.vy = -ball.vy;
        
      }
      if (ball.px + ball.vx > cnv.width-ball.radius || ball.px + ball.vx < 0) {
        ball.vx = -ball.vx * -ball.friction;
        ball.vx = -ball.vx;
      }
        //trying to get the ball to collide with coordinates where enemy image is?
        
      /* if (ball.px + ball.vx < (0,460) || ball.px + ball.vx > 0  ){
      ball.vx = -ball.vx * -ball.friction;
      ball.vx = -ball.vx*10;
      }

      if (ball.py + ball.vy < (0,460) || ball.py + ball.vy > 0 ){
        ball.vy = -ball.vy * -ball.friction;
        ball.vy = -ball.vy;
      } */
}


window.requestAnimationFrame(bounce);








