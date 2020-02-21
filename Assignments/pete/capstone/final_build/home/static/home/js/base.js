var userBool = JSON.parse(document.querySelector("#user").textContent);
var getStartedUrl = JSON.parse(document.querySelector("#get_started").textContent);
var csrftoken = document.querySelector("input[name='csrfmiddlewaretoken']").value;

// main nav bar
let homeButton = document.querySelector('#home');
let calcButton = document.querySelector('#calc');
let trackerButton = document.querySelector('#tracker');
let logoutButton = document.querySelector('#logout');
buttonArr = [homeButton, calcButton, trackerButton, logoutButton];

// sub nav bars
let homeNav = document.querySelector('#home-nav');
let calcNav = document.querySelector('#calc-nav');
let trackerNav = document.querySelector('#tracker-nav');
let navArr = [homeNav, calcNav, trackerNav]

let userClassArr = document.querySelectorAll('.user');
let guestClassArr = document.querySelectorAll('.guest');

if (userBool===true) {
    for(let i=0; i<guestClassArr.length; i++) {
        guestClassArr[i].style.display = 'none';
    }
} else {
    for(let i=0; i<userClassArr.length; i++) {
        userClassArr[i].style.display = 'none';
    }
}

for (let i=0; i<buttonArr.length-1; i++) {
    buttonArr[i].onclick = function() {
        console.log('hey')
        for (let j=0; j<navArr.length; j++) {
            navArr[j].style.display = 'none';
        }
        navArr[i].style.display = 'flex';
    }
}

var mainApp = new Vue({
    el: '#main-app',
    methods: {
        getStarted: function() {
            console.log('get started')
            location.href = getStartedUrl
        }
    }
})