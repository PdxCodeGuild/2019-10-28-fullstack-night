function getGuggly () {
    let linksArray = ['../../../html_css/lab01_bio/lab01_bio_v1.html', '../../../html_css/lab02_blog/lab02_blog_v1.html', '../../../html_css/lab03_company/homepage.html', '../../../html_css/lab04_portfolio/homepage.html', '../../../html_css/lab05_burrito/lab05.html'];
    window.location = linksArray[Math.floor (Math.random() * linksArray.length)];
    console.log('it ran');
}

function getGuggled () {
    let feelingGuggly = document.querySelector('button')
    let getGuggledIn = document.createElement('div');
    let guggledSpan = document.createElement('span');
    let guggledIn = document.createElement('span');
    guggledSpan.innerText = 'Get Guggled In:  '
    for (i=5; i > 0; i--) {
        guggledIn.innerText = `00:0${i}`;
        getGuggledIn.appendChild(guggledSpan);
        getGuggledIn.appendChild(guggledIn);
        feelingGuggly.parentElement.appendChild(getGuggledIn)
        //version of python sleep() would be really nice here
        
    }
}

window.onload = function() {

    let feelingGuggly = document.querySelector('button');
    feelingGuggly.onclick = function() {
        setTimeout(getGuggly, 5000);
        getGuggled(this);
        
    }
}