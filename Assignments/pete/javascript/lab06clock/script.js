let nav = document.querySelector('nav');
let main = document.querySelector('main.river');
let allMain = document.querySelectorAll('main');
let blockQuote = document.querySelector('blockquote');
// hidden divs
let clockDiv = document.querySelector('#clock')
let stopwatchDiv = document.querySelector('#stopwatch')

// nav buttons
let clockButton = document.querySelector('button.clock');
let stopwatchButton = document.querySelector('button.stopwatch');
let countdownButton = document.querySelectorAll('button.countdown');
// stopwatch elements
let stopwatchField = document.querySelector('#stopwatch-field')
let startButton = document.querySelector('#start')
let stopButton = document.querySelector('#stop')

//Clock
clockButton.onclick = function() {
    clockDiv.style.display = 'block';
    main.classList.remove('river');
    main.classList.remove('stopwatch');
    main.classList.add('clock');
    // allMain.style.display = 'none'
    blockQuote.style.display = 'none';
    stopwatchDiv.style.display = 'none';
    // mainClock.style.display = 'block'
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
    clockDiv.style.display = 'none';
    main.classList.remove('clock')
    main.classList.remove('river');
    main.classList.add('stopwatch');
    blockQuote.style.display = 'none';
    stopwatchDiv.style.display = 'flex';

}

let stopwatchDate = new Date();
stopwatchDate.setHours(0, 0, 0, 0);
function stopwatchFunction() {
    stopwatchField.innerText = `${stopwatchDate.getHours()} : ${stopwatchDate.getMinutes()} : ${stopwatchDate.getSeconds()} . ${stopwatchDate.getMilliseconds()}`
}
startButton.onclick = function() {
    interval = setInterval(function() {
        stopwatchDate.setMilliseconds(stopwatchDate.getMilliseconds() + 100)
        stopwatchFunction()
    }, 100)

}
