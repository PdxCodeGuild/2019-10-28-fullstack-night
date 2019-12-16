window.onload = function() {
    let main = document.querySelector('main')
    let blockQuote = document.querySelector('blockquote')
    let clockButton = document.querySelector('button.clock')
    let stopwatchButton = document.querySelector('button.stopwatch')
    let countdownButton = document.querySelectorAll('button.countdown')
    clockButton.onclick = function() {
        main.classList.remove('river')
        main.classList.add('clock')
        blockQuote.style.display = 'none'
    }

}