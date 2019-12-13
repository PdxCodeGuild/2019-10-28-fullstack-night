window.onload = function() {
    // let todoObj = {}
    let addItem = document.querySelector('#add')
    let todoList = document.querySelector('#list')
    let newItem
    let newItemHTML
    let newListElement
    let removeItem
    let crossOutItem
    addItem.addEventListener('keypress', function(e) {
        console.log(e)
        let key = e.which || e.keyCode;
        if (key === 13) {
            newItem = addItem.value
            // // if (!(newItem in todoObj)) {
            //     // todoObj[newItem] = 'in'
            //     // console.log(todoObj)
            // }
            
            // else {return}
            newItemHTML = `<span>${newItem}</span> <button class="remove">Remove Item</button><button class="cross-out">Cross-Out Item</button>`
            newListElement = document.createElement('li')
            newListElement.innerHTML = newItemHTML
            todoList.appendChild(newListElement)

            removeItem = document.querySelectorAll('.remove')
            for (let i=0; i<removeItem.length; i++) {
                removeItem[i].onclick = function() {
                    this.parentNode.parentElement.removeChild(this.parentNode)
    
            }
            }

            crossOutItem = document.querySelectorAll('.cross-out')
            for (let i=0; i<crossOutItem.length; i++) {
                crossOutItem[i].onclick = function() {
                    this.parentNode.firstChild.style.textDecoration = "line-through"
                }
            }
        }
    })




    // let crossOutItem = document.querySelectorAll('.cross-out')

}

// function writeList (todoObj, todoList) {
//     for ()
// }