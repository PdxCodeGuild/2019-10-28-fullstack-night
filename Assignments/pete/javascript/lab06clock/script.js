let nav = document.querySelector('nav');
let main = document.querySelector('main.river');
let allMain = document.querySelectorAll('main');
let blockQuote = document.querySelector('blockquote');
// hidden divs
let clockDiv = document.querySelector('#clock')
let stopwatchDiv = document.querySelector('#stopwatch')
let countdownDiv = document.querySelector('#countdown')

// nav buttons
let clockButton = document.querySelector('button.clock');
let stopwatchButton = document.querySelector('button.stopwatch');
let countdownButton = document.querySelector('button.countdown');
// stopwatch elements
let stopwatchField = document.querySelector('#stopwatch-field');
let startButton = document.querySelector('#start');
let stopButton = document.querySelector('#stop');
// countdown elements
let countdownField = document.querySelector('#countdown-field');
let enterCountdown = document.querySelector('#enter-countdown');
let beginCountdown = document.querySelector('#begin-countdown');
let setCountdown = document.querySelector('select')

//Clock
clockButton.onclick = function() {
    clockDiv.style.display = 'block';
    main.classList.remove('river');
    main.classList.remove('stopwatch');
    main.classList.remove('countdown');
    main.classList.add('clock');
    blockQuote.style.display = 'none';
    stopwatchDiv.style.display = 'none';
    countdownDiv.style.display = 'none';
    nav.classList.add('clock');
    
    clockDiv.classList.add('clock')
    // main.innerHTML = ''
    main.appendChild(clockDiv);
    function clockFunction() {
        setTimeout(clockFunction, 1000)
        let date = new Date();
        clockDiv.innerText = `It's ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`

    }
    clockFunction()
}

//Stopwatch
stopwatchButton.onclick = function() {
    // main.innerHTML = ''
    main.classList.remove('clock')
    main.classList.remove('river');
    main.classList.remove('countdown')
    main.classList.add('stopwatch');
    clockDiv.style.display = 'none';
    blockQuote.style.display = 'none';
    countdownDiv.style.display = 'none';
    stopwatchDiv.style.display = 'flex';

}

//stopwatch JavaScript
function stopwatchFunction() {
    stopwatchField.innerText = `${stopwatchDate.getHours()} : ${stopwatchDate.getMinutes()} : ${stopwatchDate.getSeconds()} . ${stopwatchDate.getMilliseconds() / 100}`
}

//stopwatchDate
let stopwatchDate = new Date();
stopwatchDate.setHours(0, 0, 0, 0);

//stopwatchBool
let stopwatchBool = false
startButton.onclick = function() {
    if (stopwatchBool === false) {
        stopwatchBool = true;
        intervalID = setInterval(function() {
            stopwatchDate.setMilliseconds(stopwatchDate.getMilliseconds() + 100)
            stopwatchFunction()
        }, 100)

    }
}
stopButton.onclick = function() {
    if (stopwatchBool === true) {
        stopwatchBool = false;
        clearInterval(intervalID);
    }
}

//countdown
countdownButton.onclick = function() {
    //hide all non-countdown divs
    blockQuote.style.display = 'none';
    clockDiv.style.display = 'none';
    stopwatchDiv.style.display = 'none';
    countdownDiv.style.display = 'flex';
    main.classList.remove('river');
    main.classList.remove('clock');
    main.classList.remove('stopwatch');
    main.classList.add('countdown');
}

//countdown function
let countdownDate
let countdownMinutes
function countdownFunction() {
    // console.log("it has begun")
    if (!(countdownDate.getMinutes())) {
        console.log('under1minute')
        if (countdownDate.getSeconds() < 11  && !(countdownDate.getMilliseconds())) {
            main.classList.remove('counting-down-thirty')
            main.classList.add('counting-down-ten')
        } else if (countdownDate.getSeconds() < 31  && !(countdownDate.getMilliseconds())) {
            main.classList.remove('counting-down')
            main.classList.add('counting-down-thirty')
        }
        if (!(countdownDate.getSeconds()) && !(countdownDate.getMilliseconds())) {
            main.innerHTML = ''
            main.classList.remove('couning-down-ten');
            main.classList.add('explosion');
            alert("Your computer has exploded.  Thanks for using TimePage.com")
        }
        
    }
    if (countdownDate.getMinutes()) {
        countdownField.innerText = `${countdownDate.getMinutes()} : ${countdownDate.getSeconds()}`
    }
    else {
        countdownField.innerText = `${countdownDate.getSeconds()}.${countdownDate.getMilliseconds() / 100}`
    }
}

//countdown bool
let countingDown = false;
let lastMinute = false
//countdown onclick
beginCountdown.onclick = function() {
    // console.log(countdownDate)
    nav.style.display = 'none';
    enterCountdown.style.display = 'none';
    beginCountdown.style.display = 'none';
    setCountdown.style.display = 'none';
    countdownField.style.display = 'flex';
    main.classList.remove('countdown')
    main.classList.add('counting-down')
    if (!(countingDown)) {
        countdownDate = new Date();
        countdownMinutes = setCountdown.value
        countdownDate.setHours(0, countdownMinutes, 1, 0);
        countingDown = true;
    }

    setInterval(function() {

        countdownFunction()
        countdownDate.setMilliseconds(countdownDate.getMilliseconds() - 100)
    }, 100)
    
}
    
