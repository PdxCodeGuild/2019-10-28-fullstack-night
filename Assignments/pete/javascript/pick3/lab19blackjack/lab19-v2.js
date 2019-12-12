let cardObject = { //This object doesn't work I have no idea what I'm doing wrong
    'A' :  1,
    '2' :  2,
    '3' :  3,
    '4' :  4,
    '5' :  5,
    '6' :  5,
    '7' :  7,
    '8' :  8,
    '9' :  9,
    '10': 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
}
let blackjackAdvice
function blackjackAdvisor(card1, card2, card3) {
    let num1 = cardObject[card1];
    console.log(num1)
    // let num1 = parseInt(str1);
    let num2 = cardObject[card2];
    // let num2 = parseInt(str2);
    let num3 = cardObject[card3];
    // let num3 = parseInt(str3);
    let cardTotal = num1 + num2 + num3;
    console.log(cardTotal)
    if (cardTotal < 17) {
        blackjackAdvice = "Hit"
    }
    else if (cardTotal < 21) {
        blackjackAdvice = "Stay"
    }
    else if (cardTotal == 21) {
        blackjackAdvice = "Blackjack!"
    }
    else {
        blackjackAdvice = "Already Busted"
    }
    return blackjackAdvice
}

window.onload = function() {
    let adviceButton = document.querySelector('#advice-button')
    let adviceSpan = document.querySelector('#advice')
    let card1 = document.querySelector('#card1')
    card1Value = card1.value //ask al why let b4 card1Value didn't work
    let card2 = document.querySelector('#card2')
    card2Value = card2.value
    let card3 = document.querySelector('#card3')
    card3Value = card3.value
    blackjackAdvice = blackjackAdvisor(card1Value, card2Value, card3Value)
    adviceButton.onclick = function() {
        adviceSpan.innerText = blackjackAdvice
    }
}