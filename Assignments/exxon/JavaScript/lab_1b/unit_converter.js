
let calculate_button = document.getElementById("calculate");

//let user_feet = document.getElementById("name");
//user_feet = user_feet.value;
//user_feet = parseInt(user_feet);

function calculate(){
    let user_feet = document.getElementById("name");
    user_feet = parseInt(user_feet.value);
    
    user_feet = user_feet * 0.3048;

    alert("Your Ft are now: "  +  user_feet +'m');
};

calculate_button.addEventListener("click", calculate);
