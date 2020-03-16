






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


user_operation = prompt('what operation would you like to perform?:');


if (user_operation === 'done') {
    alert('see ya later..');

}

if (user_operation === '+'){
    
    user_number = prompt('what is the first number?');
    user_number = parseInt(user_number);
    


    user_number2 = prompt('What is the 2nd number?'),parseInt(user_number2);
    user_number2 = parseInt(user_number2);

    sum_of_add = add_numbers(user_number,user_number2);

    alert(`${user_number} + ${user_number2} =   ${sum_of_add}`);



}



if (user_operation === '-'){
    
    user_number = prompt('what is the first number?');
    user_number = parseInt(user_number);
    


    user_number2 = prompt('What is the 2nd number?'),parseInt(user_number2);
    user_number2 = parseInt(user_number2);

    sum_of_sub = sub_numbers(user_number,user_number2);

    alert(`${user_number} - ${user_number2} =   ${sum_of_sub}`);



}



if (user_operation === '*'){
    
    user_number = prompt('what is the first number?');
    user_number = parseInt(user_number);
    


    user_number2 = prompt('What is the 2nd number?'),parseInt(user_number2);
    user_number2 = parseInt(user_number2);

    sum_of_mult = mult_numbers(user_number,user_number2);

    alert(`${user_number} * ${user_number2} =   ${sum_of_mult}`);



}



if (user_operation === '/'){
    
    user_number = prompt('what is the first number?');
    user_number = parseInt(user_number);
    


    user_number2 = prompt('What is the 2nd number?'),parseInt(user_number2);
    user_number2 = parseInt(user_number2);

    sum_of_div = div_numbers(user_number,user_number2);

    alert(`${user_number} / ${user_number2} =   ${sum_of_div}`);



}




