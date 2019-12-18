let a_input = document.querySelector("#add_text")
let a_button = document.getElementById("add_button")

let s_input = document.querySelector("#sub_text")
let s_button = document.querySelector("#sub_button")

let ul_text = document.querySelector("UL");

a_button.onclick = function() {
    let node = document.createElement("LI");
    console.log(node);
    ul_text.appendChild(node).append(a_input.value);
    a_input.value = " ";
}

s_button.onclick = function() {
    let s_song = document.querySelector("#sub_text").value;
    console.log(s_song);
    for (let i=0; i < document.querySelector("#list_id").children.length; i++) {
        if (s_song == document.querySelector("#list_id").children[i].innerText) {
            document.querySelector("#list_id").removeChild(document.querySelector("#list_id").children[i]);
            break;
        }
    }
}

ul_text.addEventListener("click", function(e) {
    if (e.target.tagName === "LI") {
        e.target.classList.toggle("checked");
    }
})

document.querySelector("LI").onclick = function() {list_click()};

function list_click() {
  document.querySelector("LI").className = "clicked";
}