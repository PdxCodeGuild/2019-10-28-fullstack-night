eyesArray = [':', ';']
noseArray = ['@', '>', '<']
mouthArray = ['(', ')', '#', '/']

let i = 0;
while (i < 5) {
    eyes = eyesArray[Math.floor(Math.random()*eyesArray.length)];
    nose = noseArray[Math.floor(Math.random()*noseArray.length)];
    mouth = mouthArray[Math.floor(Math.random()*mouthArray.length)];
    alert(eyes +  nose +  mouth);
    i++;
}

