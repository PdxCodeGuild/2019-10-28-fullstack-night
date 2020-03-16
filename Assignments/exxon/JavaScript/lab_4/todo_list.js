
//<i class="far fa-times-circle"></i>
function todolist(){
    
    let item = document.getElementById("user-item").value;
    let clearText = document.getElementById("user-item");
    clearText.value = "";
    let xmark = document.createElement("i");
    xmark.className = "far fa-times-circle";
    let text = document.createTextNode(item);
    let bomb = document.createElement('i');
    bomb.className = "fas fa-bomb"; 
    let newitem = document.createElement('li');
    newitem.appendChild(xmark);
    newitem.appendChild(text);
    newitem.appendChild(bomb);
    let ol = document.getElementById("todolist");
    ol.appendChild(newitem);
    xmark.addEventListener("click", completed);
    bomb.addEventListener('click',erase);

}

let add_item = document.getElementById('add_item');


add_item.addEventListener("click", todolist);


function erase(){
    this.parentNode.remove();
}

function completed(){

    let item = this.parentNode.innerText;
    console.log(item);
    this.parentNode.remove();
    item = document.createTextNode(item);
    let item_new = document.createElement('li');
    item_new.className = 'completed';
    item_new.appendChild(item);
    let ol = document.getElementById("completed_list");
    ol.appendChild(item_new);
    



}


