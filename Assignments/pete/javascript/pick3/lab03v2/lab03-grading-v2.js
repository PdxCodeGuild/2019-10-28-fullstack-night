function numberToLetter(number) {
    onesDigit = number % 10

    if (onesDigit < 3) { //begin finding whether there's a +/- for the letter grade
        plusMinus = '-'
    }

    else if (onesDigit > 6) {
        plusMinus = '+'
    }

    else {
        plusMinus = ''
    }

    if (number < 60) {//begin finding letterGrade
        letterGrade = 'F'
    }


    else if (number < 70) {
        letterGrade = 'D'
    }

    else if (number < 80) {
        letterGrade = 'C'
    }

    else if (number < 90) {
        letterGrade = 'B'
    }

    else {
        letterGrade = 'A'
        if (onesDigit < 5) {
            plusMinus = '-'
        }
        else {
            plusMinus = ''
        }
        if (number == 100) {
            plusMinus = ''
        }
    }

    if (letterGrade == 'F') {
        plusMinus = ''
}


}

window.onload = function() {
    let numberInput = document.querySelector('#number-input');
    let letterOutput = document.querySelector('#letter-output');
    let number;
    numberInput.addEventListener('keypress', function(e) {
        console.log(e)
        let key = e.which || e.keyCode;
        if (key === 13) {
            number = numberInput.value;
            let letter = numberToLetter(number);
            letterOutput.innerText = letterGrade + plusMinus
        }
        
        
    })



}

