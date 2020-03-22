
let my_keys = document.querySelectorAll(".keys");
console.log((my_keys[0]).innerText);

for (i = 0; i < my_keys.length; i++){
 my_keys[i].addEventListener("click", function(e) {input_function(e)});
}

function input_function(e) {
    console.log(e.target);
    let input_value = e.target.innerText;
    console.log(e.target.innerText);
    document.querySelector("#screen1").append(input_value);
}

document.querySelector(".answer").onclick = function() {output_function()};

function output_function() {
    let enumAnswer = eval(document.querySelector("#screen1").innerText);
    document.querySelector("#screen2").append(enumAnswer);
}

document.querySelector("#clear").onclick = function() {clear_function()};

function clear_function() {
    document.querySelector("#screen1").innerText = "";
    document.querySelector("#screen2").innerText = "";
}