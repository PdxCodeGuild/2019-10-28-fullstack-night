let meters = 0
let output = 0
let feetToMeters = function(x) {meters = x * 0.3048; return meters;}
let milesToMeters = function(x) {meters = x * 1609.34; return meters;}
let metersToMeters = function(x) {meters = x * 1; return meters;}
let kilometersToMeters = function(x) {meters = x * 1000; return meters;}
let yardsToMeters = function(x) {meters = x * 0.9144; return meters;}
let inchesToMeters = function(x) {meters = x * 1/0.0254; return meters;}

let metersToFeet = function(meters) {output = meters * 1/0.3048; return output;}
let metersToMiles = function(meters) {output = meters * 1/1609.34; return output;}
let metersEqualsMeters = function(meters) {output = meters * 1; return output;}
let metersToKilometers = function(meters) {output = meters * 1/1000; return output;}
let metersToYards = function(meters) {output = meters * 1/0.9144; return output;}
let metersToInches = function(meters) {output = meters * 0.0254; return output;}


window.onload = function() {
    let startingUnits = document.querySelectorAll(".startUnits")
    let endingUnits = document.querySelectorAll(".endUnits")
    let userIn = document.querySelector("#userInput")


    for (let i=0; i<startingUnits.length; i++) {
        startingUnits[i].onclick=function(x) {
            
            if (startingUnits[i].innerText == "Feet") {feetToMeters(userIn.value)}
            if (startingUnits[i].innerText == "Miles") {milesToMeters(userIn.value)}
            if (startingUnits[i].innerText == "Meters") {metersToMeters(userIn.value)}
            if (startingUnits[i].innerText == "Kilometers") {kilometersToMeters(userIn.value)}
            if (startingUnits[i].innerText == "Yards") {yardsToMeters(userIn.value)}
            if (startingUnits[i].innerText == "Inches") {inchesToMeters(userIn.value)}
            console.log(userIn.value, startingUnits[i].innerText)
            console.log(meters, 'm')
        }
    }


    for (let i=0; i<endingUnits.length; i++) {
        endingUnits[i].onclick=function() {
            
            if (endingUnits[i].innerText == "Feet") {metersToFeet(meters)}
            if (endingUnits[i].innerText == "Miles") {metersToMiles(meters)}
            if (endingUnits[i].innerText == "Meters") {metersEqualsMeters(meters)}
            if (endingUnits[i].innerText == "Kilometers") {metersToKilometers(meters)}
            if (endingUnits[i].innerText == "Yards") {metersToYards(meters)}
            if (endingUnits[i].innerText == "Inches") {output = metersToInches(meters)}
            //console.log(meters)
            console.log(output)
            showUser(output);
        }
    }



    function showUser(output) {
        document.getElementById("outputDiv").innerHTML = output;
        }
}