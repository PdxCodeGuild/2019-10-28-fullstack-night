window.onload = function() {
    // console.log('hey')
    let todoObj = {}
    let addItem = document.querySelector('#add')
    let todoList = document.querySelector('#list')
    let newItem
    let newItemHTML
    let newListElement
    addItem.addEventListener('keypress', function(e) {
        console.log(e)
        // console.log('hey you got this fuckin far')
        let key = e.which || e.keyCode;
        if (key === 13) {
            // console.log('fuck you')
            newItem = addItem.value
            if (!(newItem in todoObj)) {
                todoObj[newItem] = 'in'
                console.log(todoObj)
            }
            
            else {return}
            newItemHTML = `${newItem} <button id="remove">Remove Item</button><button id="cross-out">Cross-Out Item</button>`
            newListElement = document.createElement('li')
            newListElement.innerHTML = newItemHTML
            todoList.appendChild(newListElement)
            
        }
        
    })
    let removeItem = document.querySelectorAll('#remove')
    let crossOutItem = document.querySelectorAll('#cross-out')

}

// function writeList (todoObj, todoList) {
//     for ()
// }