function getGuggly () {
    let linksArray = ['../../../html_css/lab01_bio/lab01_bio_v1.html', '../../../html_css/lab02_blog/lab02_blog_v1.html', '../../../html_css/lab03_company/homepage.html', '../../../html_css/lab04_portfolio/homepage.html', '../../../html_css/lab05_burrito/lab05.html'];
    window.location = linksArray[Math.floor (Math.random() * linksArray.length)];
    console.log('it ran');
}

function getGuggled () {
    let feelingGuggly = document.querySelector('button')
    let getGuggledIn = document.createElement('div'); //parent div of...
    // let guggledSpan = document.createElement('span');//span1 of timer
    // let guggledIn = document.createElement('span');//span2 of timer
    // getGuggledIn.appendChild(guggledSpan);
    // getGuggledIn.appendChild(guggledIn);
    
    feelingGuggly.parentElement.appendChild(getGuggledIn)

    let timerString = '543210';
    let timerArray = timerString.split('');
    let timerArrayIndex = 0;
    getGuggledIn.innerText = '';
    let gettinGuggledID = setInterval(function() {
        getGuggledIn.innerText = `Get Guggled In:  00:0${timerArray[timerArrayIndex]}`;

        if (++timerArrayIndex >= timerArray.length) {

            clearInterval(gettinGuggledID)
            getGuggly()
        }
    }, 1000);

}

window.onload = function() {

    let feelingGuggly = document.querySelector('button');

    feelingGuggly.onclick = getGuggled

}