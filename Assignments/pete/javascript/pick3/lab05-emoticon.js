eyesArray = [':', ';']
noseArray = ['@', '>', '<']
mouthArray = ['(', ')', '#', '/']

eyes = eyesArray[Math.floor(Math.random()*eyesArray.length)];
nose = noseArray[Math.floor(Math.random()*noseArray.length)];
mouth = mouthArray[Math.floor(Math.random()*mouthArray.length)];

alert(eyes +  nose +  mouth)