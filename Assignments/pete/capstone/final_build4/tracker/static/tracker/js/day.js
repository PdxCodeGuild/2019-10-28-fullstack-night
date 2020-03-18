var macros = JSON.parse(document.querySelector('#macros').textContent);
var totals = JSON.parse(document.querySelector('#totals').textContent);
var overUnder = JSON.parse(document.querySelector('#over_under').textContent);

let countUp = {
    kcal: 0,
    fat: 0,
    carb: 0,
    protein: 0,
};
// let countUp = totals

let ctx = document.querySelector('#progCnv').getContext('2d');
let w = 700;
let h = 350;

let yPos = [
    h*.1,
    h*.35,
    h*.6,
    h*.85,
];

let barH = h*(9/60);

let t = w*.65;

let keyToColor = {
    'kcal': 'blue',
    'fat': 'purple',
    'carb': 'yellow',
    'protein': 'red',
}

let keyToLabel = {
    'kcal': 'CALORIES',
    'fat': 'FAT',
    'carb': 'CARBS',
    'protein': 'PROTEIN',
}

let keys = Object.keys(keyToColor);

function drawGraph() {
    ctx.clearRect(0, 0, w, h + 3);

    //target range
    ctx.strokeStyle = 'hsla(0, 0%, 0%, 0.5)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(t*.9 + 0.5*barH, 0);
    ctx.lineTo(t*.9 + 0.5*barH, h);
    ctx.moveTo(t*1.1 + 0.5*barH, 0);
    ctx.lineTo(t*1.1 + 0.5*barH, h);
    ctx.stroke();

    for (let i=0; i<keys.length; i++) {
        let y = yPos[i];
        let key = keys[i];
        let goal = macros[key];
        let label = keyToLabel[key];
        let counter = countUp[key];
        let prog = counter/goal;

        //empty bars
        ctx.fillStyle = 'hsla(0, 0%, 0%, 0.25)'
        ctx.fillRect(0, y, w, barH);

        //text
        ////goal
        ctx.font = '2.5rem Odibee Sans';
        ctx.fillStyle = 'black';

        ctx.textAlign = 'end';
        ctx.fillText(
            '/' + goal,
            w,
            y + .775*barH
        );

        ////label
        ctx.font = 'italic 2rem Odibee Sans';
        ctx.textAlign = 'start';
        ctx.fillText(
            label + ':',
            0,
            y - .1125*barH,
        )

        //filled bars
        ctx.fillStyle = keyToColor[key];
        ctx.fillRect(0, y, prog*t, barH);

        //arc
        ctx.beginPath();
        ctx.arc(
            prog*t -.5,
            y + 0.5*barH,
            0.5*barH,
            1.5*Math.PI,
            0.5*Math.PI
        );
        ctx.fill();

        //outline
        let strokeColor = counter < goal*.9 ? 'white'
            : counter >= goal*.9 && counter <= goal*1.1 ? 'green'
            : 'black';
        ctx.strokeStyle = strokeColor;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(prog*t, y);
        ctx.arc(
            prog*t,
            y + 0.5*barH,
            0.5*barH,
            1.5*Math.PI,
            0.5*Math.PI
        );
        ctx.lineTo(0, y + barH);
        ctx.stroke();

        //text
        ////progress
        ctx.font = '2.5rem Odibee Sans';
        ctx.fillStyle = 'black';

        ctx.textAlign = 'end';
        ctx.fillText(
            Math.round(counter),
            t*prog + .375*barH,
            y + .775*barH
        );
    };
    //target line
    ctx.strokeStyle = 'hsla(0, 0%, 0%, 0.5)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(t + 0.5*barH, 0);
    ctx.lineTo(t + 0.5*barH, h);
    ctx.stroke();

    //animation
    // if (countUp.kcal < totals.kcal) {
    //     countUp.kcal ++;
    //     requestAnimationFrame(drawGraph);
    if (countUp.kcal < totals.kcal - macros.kcal / 50) {
        countUp.kcal = countUp.kcal + (macros.kcal / 240)
        if (countUp.kcal > totals.kcal - macros.kcal / 50) {
            countUp.kcal = totals.kcal
        }
        requestAnimationFrame(drawGraph);
    // } else if (countUp.kcal < totals.kcal) {
    //     countUp.kcal++
    //     requestAnimationFrame(drawGraph);

    } else if (countUp.fat < totals.fat - macros.fat / 50) {
        countUp.fat = countUp.fat + (macros.fat / 240)
        if (countUp.fat > totals.fat - macros.fat / 50) {
            countUp.fat = totals.fat
        }
        requestAnimationFrame(drawGraph);
    // } else if (countUp.fat < totals.fat) {
    //     countUp.fat++
    //     requestAnimationFrame(drawGraph);

    } else if (countUp.carb < totals.carb - macros.carb / 50) {
        countUp.carb = countUp.carb + (macros.carb / 240)
        if (countUp.carb > totals.carb - macros.carb / 50) {
            countUp.carb = totals.carb
        }
        requestAnimationFrame(drawGraph);
    // } else if (countUp.carb < totals.carb) {
    //     countUp.carb++
    //     requestAnimationFrame(drawGraph);

    } else if (countUp.protein < totals.protein - macros.protein / 50) {
        countUp.protein = countUp.protein + (macros.protein / 240)
        if (countUp.protein > totals.protein - macros.protein / 50) {
            countUp.protein = totals.protein
        }
        requestAnimationFrame(drawGraph);
    // } else if (countUp.protein < totals.protein) {
    //     countUp.protein++
    //     requestAnimationFrame(drawGraph);

    } else {
        console.log('meep');



    // else if (countUp.kcal > totals.kcal) {
    //     countUp.kcal --;
    //     requestAnimationFrame(drawGraph);
    // } else if (countUp.fat < totals.fat) {
    //     countUp.fat ++;
    //     requestAnimationFrame(drawGraph);
    // } else if (countUp.fat > totals.fat) {
    //     countUp.fat --;
    //     requestAnimationFrame(drawGraph);
    // } else if (countUp.carb < totals.carb) {
    //     countUp.carb ++;
    //     requestAnimationFrame(drawGraph);
    // } else if (countUp.carb > totals.carb) {
    //     countUp.carb --;
    //     requestAnimationFrame(drawGraph);
    // } else if (countUp.protein < totals.protein) {
    //     countUp.protein ++;
    //     requestAnimationFrame(drawGraph); 
    // } else if (countUp.protein > totals.protein) {
    //     countUp.protein --;
    //     requestAnimationFrame(drawGraph);
        // return;
    };
};

drawGraph();

// function drawGraph(startObj, endObj, addOrRemove) {
//     ctx.clearRect(0, 0, w, h + 3);
//     console.log(startObj, endObj, addOrRemove)
//     //target range
//     ctx.strokeStyle = 'hsla(0, 0%, 0%, 0.5)';
//     ctx.lineWidth = 2;
//     ctx.beginPath();
//     ctx.moveTo(t*.9 + 0.5*barH, 0);
//     ctx.lineTo(t*.9 + 0.5*barH, h);
//     ctx.moveTo(t*1.1 + 0.5*barH, 0);
//     ctx.lineTo(t*1.1 + 0.5*barH, h);
//     ctx.stroke();

//     for (let i=0; i<keys.length; i++) {
//         let y = yPos[i];
//         let key = keys[i];
//         let goal = macros[key];
//         let label = keyToLabel[key];
//         let counter = startObj[key];
//         // console.log(counter)
//         let prog = counter/goal;

//         //empty bars
//         ctx.fillStyle = 'hsla(0, 0%, 0%, 0.25)'
//         ctx.fillRect(0, y, w, barH);

//         //text
//         ////goal
//         ctx.font = '2.5rem Odibee Sans';
//         ctx.fillStyle = 'black';

//         ctx.textAlign = 'end';
//         ctx.fillText(
//             '/' + goal,
//             w,
//             y + .775*barH
//         );

//         ////label
//         ctx.font = 'italic 2rem Odibee Sans';
//         ctx.textAlign = 'start';
//         ctx.fillText(
//             label + ':',
//             0,
//             y - .1125*barH,
//         );

//         //filled bars
//         ctx.fillStyle = keyToColor[key];
//         ctx.fillRect(0, y, prog*t, barH);
//         //arc
//         ctx.beginPath();
//         ctx.arc(
//             prog*t -.5,
//             y + 0.5*barH,
//             0.5*barH,
//             1.5*Math.PI,
//             0.5*Math.PI
//         );
//         ctx.fill();

//         //outline
//         let strokeColor = counter < goal*.9 ? 'white'
//             : counter >= goal*.9 && counter <= goal*1.1 ? 'green'
//             : 'black';
//         ctx.strokeStyle = strokeColor;
//         ctx.lineWidth = 2;
//         ctx.beginPath();
//         ctx.moveTo(0, y);
//         ctx.lineTo(prog*t, y);
//         ctx.arc(
//             prog*t,
//             y + 0.5*barH,
//             0.5*barH,
//             1.5*Math.PI,
//             0.5*Math.PI
//         );
//         ctx.lineTo(0, y + barH);
//         ctx.stroke();

//         //text
//         ////progress
//         ctx.font = '2.5rem Odibee Sans';
//         ctx.fillStyle = 'black';

//         ctx.textAlign = 'end';
//         ctx.fillText(
//             counter,
//             t*prog + .375*barH,
//             y + .775*barH
//         );
//     };
//     //target line
//     ctx.strokeStyle = 'hsla(0, 0%, 0%, 0.5)';
//     ctx.lineWidth = 2;
//     ctx.beginPath();
//     ctx.moveTo(t + 0.5*barH, 0);
//     ctx.lineTo(t + 0.5*barH, h);
//     ctx.stroke();
    
//     //animation
//     if (addOrRemove) {
//         // console.log('hey')
//         if (startObj.kcal < endObj.kcal) {
//             console.log('kcal')
//             // console.log(startObj, endObj, addOrRemove)
//             startObj.kcal += 10;
//             // console.log(startObj, endObj, addOrRemove)
//             requestAnimationFrame(drawGraph(startObj, endObj, addOrRemove));
//         } else if (startObj.fat < endObj.fat) {
//             console.log('fat')
//             startObj.fat ++;
//             requestAnimationFrame(drawGraph(startObj, endObj, addOrRemove));
//         }  else if (startObj.carb < endObj.carb) {
//             console.log('carb')
//             startObj.carb ++;
//             requestAnimationFrame(drawGraph(startObj, endObj, addOrRemove));
//         }  else if (startObj.protein < endObj.protein) {
//             console.log('protein')
//             startObj.protein ++;
//             requestAnimationFrame(drawGraph(startObj, endObj, addOrRemove)); 
//         } else {
//             console.log('meep');
//             // return;
//         };

//     }

// };
