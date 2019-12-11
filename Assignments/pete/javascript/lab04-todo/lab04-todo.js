let todoArray = [];
let listDiv = document.querySelector('#listdiv')

window.onload = function() {
    let todoList = document.querySelector('ul');

    //button version below
    // let addInput = document.querySelector('#add');
    // addInput.addEventListener('click', function() {
    //     let input = prompt("Add Item To List:");
    //     let newLi = document.createElement('li');
    //     let newLiText = document.createTextNode(input);
    //     newLi.appendChild(newLiText);
    //     todoList.appendChild(newLi);
    //     todoArray.push(newLiText)
    // });

    //input version below
    // let addInput = document.querySelector();
    let newLiText = document.querySelector('#add');

    newLiText.addEventListener('keypress', function(e) {
        var key = e.which || e.keyCode;
        if (key === 13 ){

            let newLi = document.createElement('li');
            newLi.appendChild(newLiText);
            todoList.appendChild(newLi);
            todoArray.push(newLiText);
        }
        
        // let newInput = document.createElement('input');
        // newInput.innerHTML = ;
        listDiv.appendChild('<input id="add" type="text" placeholder="Add item to list..."></input>');

    });





    let removeInput = document.querySelector('#remove');
    removeInput.addEventListener('click', function() {
        let input = prompt("Remove Item From List");
        let remLi = document.removeChild();
        let remLiText = document.createTextNode(input);
        

    })

    let crossOutInput = document.querySelector('#cross-out');
}