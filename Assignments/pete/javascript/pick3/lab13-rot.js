let inString = prompt("Enter your secret message: ")
inString = inString.toLowerCase();
// alert (inString)

let rot13 = {
    'a':'n',
    'b':'o',
    'c':'p',
    'd':'q',
    'e':'r',
    'f':'s',
    'g':'t',
    'h':'u',
    'i':'v',
    'j':'w',
    'k':'x',
    'l':'y',
    'm':'z',
    
    'n':'a',
    'o':'b',
    'p':'c',
    'q':'d',
    'r':'e',
    's':'f',
    't':'g',
    'u':'h',
    'v':'i',
    'w':'j',
    'x':'k',
    'y':'l',
    'z':'m',

}

let outString = ''
for (let i = 0; i<inString.length; ++i) {
    outString += rot13[inString[i]]
}
outString = outString.toUpperCase();
alert(outString)