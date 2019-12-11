let strNnumberGrade = prompt("Enter number grade: ")
intNumberGrade = parseInt(strNnumberGrade)

onesDigit = intNumberGrade % 10

if (onesDigit < 3) { //begin finding whether there's a +/- for the letter grade
    plusMinus = '-'
}

else if (onesDigit > 6) {
    plusMinus = '+'
}

else {
    plusMinus = ''
}

if (intNumberGrade < 60) {//begin finding letterGrade
    letterGrade = 'F'
}


else if (intNumberGrade < 70) {
    letterGrade = 'D'
}

else if (intNumberGrade < 80) {
    letterGrade = 'C'
}

else if (intNumberGrade < 90) {
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
}

if (letterGrade == 'F') {
    plusMinus = ''
}

alert ("Your letter grade is " + letterGrade + plusMinus + '.')