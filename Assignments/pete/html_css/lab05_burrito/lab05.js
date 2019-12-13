window.onload = function() {
    let inputs = document.querySelectorAll('input');
    let tortillas = document.querySelectorAll('.tortilla')
    // tortillasArray = []
    // for (let i=0; i< tortillas.length, i++) {
    //     tortillasArray.push(tortillas[i].value)
    // }
    this.console.log(tortillas)
    let totalList = document.querySelector('#order-list');
    // let totalArray = []

    for (let i=0; i < inputs.length; i++) {
        inputs[i].addEventListener('click', function() {
            // console.log('sup')
            // let orderItem = inputs[i].value;
            // console.log('.tortilla' ) 
            // let breakOut = false
            // for (let i = 0; i<totalArray.length; i++) {
            //     if (totalArray[i] === orderItem) {
            //         breakOut = true
            //         break;
            //     }
            // }
            // if (breakOut === true) return;
            // console.log(totalArray);
            totalList.innerHTML = ''
            for (let i=0; i<inputs.length; i++){
                if (inputs[i].checked) {
                    console.log('inputs.checked')
                    // totalArray.push(orderItem);
                    let newLi = document.createElement('li');
                    // console.log(newLi, orderItem)
                    let orderItem = inputs[i].value;
                    newLi.innerText = orderItem;
                    totalList.appendChild(newLi);
            }
            
            }
            
        })
    }
}