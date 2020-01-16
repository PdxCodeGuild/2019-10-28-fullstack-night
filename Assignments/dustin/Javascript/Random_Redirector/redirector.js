

window.onload = function() {
    let actionOne = document.querySelector("#actionButton");    
    let randomChoice = Math.floor((Math.random() * 5) + 1);
 
    actionOne.onclick = function startTimer(){
            var counter = 0;
            setInterval(function() {
                counter++;
                if(counter==5) { actionJump(); }
                console.log(counter);
                actionOne.innerText = 5 - counter;
            }, 1000)
        
    }

    function actionJump() {
        if(randomChoice == 1) {
            window.location.assign("https://www.google.com")
            }
        else if(randomChoice == 2) {
            window.location.assign("https://www.bing.com")
        }
        else if(randomChoice == 3) {
            window.location.assign("https://www.yahoo.com")
        }
        else if(randomChoice == 4) {
            window.location.assign("https://www.duckduckgo.com")
        }
        else if(randomChoice == 5) {
            window.location.assign("https://www.ask.com")
        }
    }
}