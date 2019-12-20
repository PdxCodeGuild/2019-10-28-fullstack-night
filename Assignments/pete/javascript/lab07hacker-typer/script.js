let hillHouseDiv = document.querySelector('pre');
let hillHouseText = hillHouseDiv.innerText;
let letterCounter = 0
hillHouseDiv.innerText = ''
document.addEventListener('keydown', function() {
    if (letterCounter<hillHouseText.length){
        hillHouseDiv.innerText += hillHouseText[letterCounter++]
    }
})