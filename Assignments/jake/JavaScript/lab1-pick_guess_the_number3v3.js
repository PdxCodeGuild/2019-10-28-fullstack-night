 // generating my random value
 var y = Math.floor(Math.random() * 10 + 1); 
      
 // number of guesses the user has taken
 var guess = 1; 
   
 document.getElementById("submitguess").onclick = function(){ 
   
// number guessed by user      
var x = document.getElementById("guessField").value; 

if(x == y) 
{     
    alert("CONGRATULATIONS!!! YOU GUESSED IT RIGHT IN "
            + guess + " GUESS "); 
} 
else if(x > y) /* if guessed number is greater 
                than actual number*/ 
{     
    guess++; 
    alert("OOPS SORRY!! TRY A SMALLER NUMBER"); 
} 
else /*if guessed number is less than the actual number */
{ 
    guess++; 
    alert("OOPS SORRY!! TRY A GREATER NUMBER") 
} 
} 

<input type="button" value="Reload Page" onClick="document.location.reload(true)">