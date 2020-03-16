function add_numbers(x,y){
    return x+y; 

};

function sub_numbers(x,y){
    return x-y;
};

function mult_numbers(x,y){
    return x*y;
};

function div_numbers(x,y){
    return x/y;
};



let solve_button = document.getElementById('solve_button');


function solve_problem(){
    
    if (user_op.value === ""){
    alert ('please enter any of these operations [ + , - , * , / ]')
    };

    if (user_num1.value === ""){
        alert('please enter a number to continue')
    };

    if (user_num2.value === ""){
        alert('please enter a second number to continue')
    };
    
    

    if (user_op.value === "+"){
        user_number = parseInt(user_num1.value);
        user_number2 = parseInt(user_num2.value);
        sum_of_add = add_numbers(user_number,user_number2);
        
        
        document.getElementById("user_sol").value = (`${user_number} + ${user_number2} =   ${sum_of_add}`);

    };

    if (user_op.value === "-"){
        user_number = parseInt(user_num1.value);
        user_number2 = parseInt(user_num2.value);
        sum_of_sub = sub_numbers(user_number,user_number2);
        
        
        document.getElementById("user_sol").value = (`${user_number} - ${user_number2} =   ${sum_of_sub}`);
    };


    if (user_op.value === "*"){
        user_number = parseInt(user_num1.value);
        user_number2 = parseInt(user_num2.value);
        sum_of_mult = mult_numbers(user_number,user_number2);
        
        
        document.getElementById("user_sol").value = (`${user_number} * ${user_number2} =   ${sum_of_mult}`);
    };


    if (user_op.value === "/"){
        user_number = parseInt(user_num1.value);
        user_number2 = parseInt(user_num2.value);
        sum_of_div = div_numbers(user_number,user_number2);
        
        
        document.getElementById("user_sol").value = (`${user_number} / ${user_number2} =   ${sum_of_div}`);
        
    };




}






solve_button.addEventListener('click', solve_problem);