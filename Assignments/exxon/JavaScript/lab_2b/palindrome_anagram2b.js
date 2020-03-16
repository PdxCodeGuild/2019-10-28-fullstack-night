





let check_button = document.getElementById("check_button");



function check_palindrome() {
    
    
    str = user_word.value;
    
    lower = str.toLowerCase();
    
    console.log(lower);
    
    userPalword = lower 
        .split('')
        .reverse()
        .join('');
        
        console.log(userPalword);
        user_word = lower;
        console.log(user_word);

        if (user_word === userPalword){
            yes_no_text.innerText = ("Is a palindrome");
        } else {
        console.log(yes_no_text);   
        yes_no_text.innerText = ("Is NOT a palindrome");
    };
    
    
    document.getElementById("palindrome_word_display").textContent += user_word;



}

check_button.addEventListener("click", check_palindrome);






// made user_word2 a global variable need to do this without making it global variable
var user_word2;


let start_check = document.getElementById("try_anagram");

function pick_word() {
    
    user_word2 = prompt("what do you think is an anagram for your word?");
    user_word2 = user_word2;
    console.log(user_word2);
    

    document.getElementById("anagram_word_display").textContent += user_word2;
    
    
}


start_check.addEventListener("click", pick_word);




let check_now = document.getElementById("check_anagram_button");





function check_anagram () {
    
    
    
    
    palword_2 = userPalword.replace(/\s/g,'');
    palword_2 = userPalword.split('').sort().join('');
    console.log(palword_2);
    
    
    
    lower_case = user_word2.toLowerCase();
    console.log(user_word2);
    no_space_string = lower_case.replace(/\s/g,'');

    
    non_arranged_word = no_space_string;

    no_space_string = non_arranged_word.split('').sort().join('');

    arranged_word = no_space_string;
    
    
    console.log(no_space_string);

    if (palword_2 === no_space_string) {
        anagram_yes_no.innerText = ("is an anagram!");
    } else {
        anagram_yes_no.innerText = ("is not an anagram");
    }


}
check_now.addEventListener("click", check_anagram);