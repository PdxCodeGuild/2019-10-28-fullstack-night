window.onload = function() {
    let nav = document.querySelector('nav');
    let main = document.querySelector('main.river');
    // let mainClock = document.querySelector('main.clock')
    let stopwatchDiv = document.querySelector('#stopwatch')
    let allMain = document.querySelectorAll('main');
    // allMain.style.display = 'none'
    // mainClock.style.display = 'none'
    let blockQuote = document.querySelector('blockquote');
    let clockButton = document.querySelector('button.clock');
    let stopwatchButton = document.querySelector('button.stopwatch');
    let countdownButton = document.querySelectorAll('button.countdown');
    let clockDiv = document.createElement('div');
    // let clockDiv = document.querySelector('#clock')
    //Clock
    let stopwatchDiv = document.querySelector('#stopwatch')
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
        stopwatchDiv.style.display = 'block';

    }

}