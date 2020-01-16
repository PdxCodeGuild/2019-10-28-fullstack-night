window.onload=function() {
    let newItemButton = document.querySelector('#newItem');
    let listToDo = document.querySelector("#listToDo");
    let listDone = document.querySelector("#listDone");
    
    for (let i=0; i<100; i++) {
        newItemButton.onclick=function() { 
            let addItem = prompt("Item to add?: ")
            let newestItem = document.createElement("li")
            newestItem.classList.add("listItem")
            newDoneItem = newestItem.cloneNode(true)
            newDoneItem.style.display = "none"
            let checkBox = document.createElement("input")
            let checkBoxDone = document.createElement("input")

            checkBox.classList.add("checkboxItem")
            checkBox.setAttribute("type", "checkbox")
            checkBox.checked = false;
            checkBoxDone.classList.add("checkboxDoneItem")
            checkBoxDone.setAttribute("type", "checkbox")
            checkBoxDone.checked = true;
            newestItem.appendChild(checkBox)
            newDoneItem.appendChild(checkBoxDone)

            let spanItem = document.createElement("span")
            let spanItemDone = document.createElement("span")
            spanItem.innerText = addItem
            spanItemDone.innerText = addItem
            newestItem.appendChild(spanItem)
            newDoneItem.appendChild(spanItemDone)
            newDoneItem.style.display = "none"
            listToDo.appendChild(newestItem)
            listDone.appendChild(newDoneItem)
            checkBox.addEventListener('change', checkAction)
            checkBoxDone.addEventListener('change', checkAction)
        }
    }
    
    let checkAction = function() {
            if (this.checked == true) {
                let checkBoxDone = document.querySelector(".checkboxDoneItem")
                let checkedDiv = this.parentNode
                let doneDiv = checkBoxDone.parentNode
                checkedDiv.style.display = "none"
                doneDiv.style.display = "block"
                checkBoxDone.checked = true
            }
            console.log(this.checked)
            if (this.checked == false) {
                let checkBox = document.querySelector(".checkboxItem")
                let uncheckedDiv = this.parentNode
                let toDoDiv = checkBox.parentNode
                uncheckedDiv.style.display = "none"
                toDoDiv.style.display = "block"
                checkBox.checked = false


            }
                

            }
        }
