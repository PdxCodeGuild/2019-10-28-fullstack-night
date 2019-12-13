var questions = 5;
var questionsLeft = ' [' + questions + ' questions left]';
var action = prompt('Please type an action' + questionsLeft);

questions -= 1;
questionsLeft = ' [' + questions + ' questions left]';
var sound = prompt('Please enter a sound  ' + questionsLeft);

questions -= 1;
questionsLeft = ' [' + questions + ' questions left]';
var monster = prompt('Name a monster' + questionsLeft);

questions -= 1;
questionsLeft = ' [' + questions + ' questions left]';
var adjective = prompt('Name an adjective' + questionsLeft);

questions -= 1;
questionsLeft = ' [' + questions + ' questions left]';
var monster1 = prompt('Name a different monster' + questionsLeft);

alert('All done. Ready for the message?');
var sentence = '<h2>The dragon ' + action;
sentence += ' through the sky, as ' + sound;
sentence += ' can be heard over the wind by what appears to be a  ' + monster;
sentence += '. The dragon' + adjective;
sentence += 'from the' + monster1;
sentence += '! The End! Fine! GO TO SLEEP NOW!'
 '.</h2>';
document.write(sentence);

