window.onload = function() {
    let choices = document.querySelectorAll('.choice');
    let resultsDiv = document.querySelector('#results');
    let computerDiv = document.querySelector('#computer');
    let userDiv = document.querySelector('user');

    var choiceArray = ["Rock", "Paper", "Scissors"];

     

    for (let i=0; i<choices.length; i++) {
        choices[i].onclick=function(e) {
            console.log(e)
            console.log(this)
            let compChoice = choiceArray[Math.floor(Math.random() * choiceArray.length)];   

            let resultAnnounce = "";
            if (choices[i].innerText == "Rock") {
                if (compChoice == "Paper") {resultAnnounce = "You lost!"}
                else if (compChoice == "Scissors") {resultAnnounce = "You won!" }
                else if (compChoice == "Rock") {resultAnnounce = "You tied!" }
                }
            if (choices[i].innerText == "Paper") {
                if (compChoice == "Scissors") {resultAnnounce = "You lost!"}
                else if (compChoice == "Rock") {resultAnnounce = "You won!" }
                else if (compChoice == "Paper") {resultAnnounce = "You tied!" }
                }
            if (choices[i].innerText == "Scissors") {
                if (compChoice == "Rock") {resultAnnounce = "You lost!"}
                else if (compChoice == "Paper") {resultAnnounce = "You won!" }
                else if (compChoice == "Scissors") {resultAnnounce = "You tied!" }
                }
            document.getElementById("user").innerHTML = choices[i].innerText;
            document.getElementById("computer").innerHTML = compChoice;
            document.getElementById("results").innerHTML = resultAnnounce;
            }
        }
    }