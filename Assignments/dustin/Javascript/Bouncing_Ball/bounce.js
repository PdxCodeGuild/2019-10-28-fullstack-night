window.onload = function() {
    let cnv = document.querySelector("canvas");
        let ctx = cnv.getContext("2d");
        let colorArr = ["red", "green", "orange", "blue", "violet", "yellow"];
        let colorCounter = 0;
        let width = 500;
        let height = 500;
        let ball = {
            x: 2,
            y: height-1,
            radius: 200,
            vx: 2,
            vy: -2,
            ay: .02,
        }

        console.log(ball["radius"])
        console.log(ball.radius)

        function draw() {
            console.log('drawing');
            ctx.clearRect(0, 0, width, height);
            if ((ball.y < 0) || (ball.y > height) || (ball.x < 0) || (ball.x > width)) {
                ball.radius *=1.01;
                ctx.fillStyle = "red";
                ctx.arc(ball.x, ball.y, ball.radius, 0, 2*Math.PI);
                ctx.fill();
                ctx.beginPath;
                if (ball.radius < 50) {
                    window.requestAnimationFrame(draw);
                }
                else {
                    ball = {
                        x: 1,
                        y: height-1,
                        radius: 5,
                        vx: 1,
                        vy: -1.5,
                        ay: .01,
                    }
                    window.requestAnimationFrame(draw);
                }
            } else { 
                ctx.arc(ball.x, ball.y, ball.radius, 0, 2*Math.PI);
                ball.vy += ball.ay;
                ball.x += ball.vx;
                ball.y += ball.vy;
                ctx.fillStyle = colorArr[Math.floor(colorCounter++/20)%colorArr.length];
                ctx.fill();
                ctx.beginPath();
                window.requestAnimationFrame(draw);
            }
        }
        draw();
}