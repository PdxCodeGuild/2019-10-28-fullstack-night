

let user_word = prompt("which word would you like to check to see if its a palindrome?").toLowerCase();

var userPalword;






function check_anagram () {
    
    
    palword_2 = userPalword.replace(/\s/g,'');
    palword_2 = userPalword.split('').sort().join('');
    console.log(palword_2);
    
    
    
    lower_case = `${user_word2}`.toLowerCase();
    
    no_space_string = lower_case.replace(/\s/g,'');

    
    non_arranged_word = no_space_string;

    no_space_string = non_arranged_word.split('').sort().join('');

    arranged_word = no_space_string;
    
    
    console.log(no_space_string);

    if (palword_2 === no_space_string) {
        alert(`${userPalword} and ${user_word2} are anagrams!`);
    } else {
        alert(`${userPalword} and ${user_word2} are not anagrams!`);
    }


}








function check_palindrome() {
    
    var str = user_word;
    
    lower = str.toLowerCase();

    userPalword = lower 
        .split('')
        .reverse()
        .join('');
        
        console.log(userPalword);
        

        if (user_word === userPalword){
            alert(`The word is a palindrome`);
        } else {    alert('Sorry, thats not a palindrome.');
    };


}








check_palindrome(); 


let user_word2 = prompt("now enter another word to see if it is an anagram for your word:");


check_anagram();



