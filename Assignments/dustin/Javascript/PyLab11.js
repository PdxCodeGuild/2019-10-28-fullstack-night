window.onload = function() {
    let keys = document.querySelectorAll('.keys')
    let answerDiv = document.querySelector('#answer')
    let equalDiv = document.querySelector('#equals')
    let textDiv = document.querySelector('#textbox')
    for (let i=0; i<keys.length; i++) {
        keys[i].onclick=function(e) {
                console.log(e)
                console.log(this)
                answerDiv.innerText += this.innerText
                document.getElementById("textbox").innerHTML = answerDiv.innerText
                //alert(keys[i].innerText)
            }
        console.log(keys[i].innerHTML)
    }
    equalDiv.onclick=showAnswer

function showAnswer() {
    document.getElementById("textbox").innerHTML = answerDiv.innerText + "=" + eval(answerDiv.innerText);
    }
    
