function mad_lib_func() {
    let user_name = prompt('What is your name?');
    alert(`Hello ${user_name},welcome to Madlibs!`);
    let space_obj = prompt(`What is an object that is in space?`);
    let place = prompt(`Where are you?`);
    let birth_stone = prompt(`What is your birthstone?`);
    let question = prompt(`Ask me a question.`);
    let mad_text = document.createElement("P");
    mad_text.innerHTML = (`Twinkle, twinkle, little ${space_obj},<br/>
    How I wonder what you are!<br/>
    Up above ${place} so high,<br/>
    Like a ${birth_stone} in the sky.<br/>
    Twinkle, twinkle, little ${space_obj},<br/>
    How I wonder ${question}`);
    document.querySelector("#mad_div").appendChild(mad_text);
};

function rps_func() {
    let rps = {
        "rock":["paper","scissors"],
        "paper":["scissors","rock"],
        "scissors":["rock","paper"],
    };
    let comp_rps = ["rock", "paper", "scissors"];
    let game_in_session = "yes";
    while(game_in_session == "yes") {
        let player = prompt("Make your selection; Rock, Paper, or Scissors: ").toLowerCase();
        let computer_rand = comp_rps[Math.floor(Math.random() * comp_rps.length)];
        if (!(player in rps)) {
            alert("Error");
        }
        else if (player == computer_rand) {
            let rps_text = document.createElement("P");
            rps_text.innerHTML = (`<br/>Player Choice: ${player}<br/>Computer Choice: ${computer_rand}<br/>Outcome: Tie`);
            document.querySelector("#rps_div").appendChild(rps_text);
            game_in_session = "no";
        }
        else if (computer_rand == rps[player][0]) {
            let rps_text = document.createElement("P");
            rps_text.innerHTML = (`<br/>Player Choice: ${player}<br/>Computer Choice: ${computer_rand}<br/>Outcome: You Lose`);
            document.querySelector("#rps_div").appendChild(rps_text);
            game_in_session = "no";
        }
        else if (computer_rand == rps[player][1]) {
            let rps_text = document.createElement("P");
            rps_text.innerHTML = (`<br/>Player Choice: ${player}<br/>Computer Choice: ${computer_rand}<br/>Outcome: You Win`);
            document.querySelector("#rps_div").appendChild(rps_text);
            game_in_session = "no";
        }
    };
}

function pal_func() {
    let pal_word = prompt(`Enter a potential palindrome:`).toLowerCase();
    if (pal_word == pal_word.split("").reverse().join("")) {
        let pal_text = document.createElement("P");
        pal_text.innerHTML = (`${pal_word} is a palindrome.`);
        document.querySelector("#pal_div").appendChild(pal_text);
    }
    else if (!(pal_word == pal_word.split("").reverse().join(""))) {
        let pal_text = document.createElement("P");
        pal_text.innerHTML = (`${pal_word} is NOT a palindrome.`);
        document.querySelector("#pal_div").appendChild(pal_text);
    }

}


function ana_func() {
    let ana_word1 = prompt(`Enter the first potential anagram:`);
    let ana_word1a = ana_word1.toLowerCase().split("").sort().join("");
    let ana_word2 = prompt(`Enter the second potential anagram:`);
    let ana_word2a = ana_word2.toLowerCase().split("").sort().join("");
    if (ana_word1a == ana_word2a) {
        let ana_text = document.createElement("P");
        ana_text.innerHTML = (`Yes, ${ana_word1} is an anagram of ${ana_word2}.`);
        document.querySelector("#ana_div").appendChild(ana_text);
    }
    else if (!(ana_word1a == ana_word2a)) {
        let ana_text = document.createElement("P");
        ana_text.innerHTML = (`No, ${ana_word1} and ${ana_word2} are not anagrams.`);
        document.querySelector("#ana_div").appendChild(ana_text);
    }
}