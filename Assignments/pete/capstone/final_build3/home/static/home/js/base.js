var userBool = JSON.parse(document.querySelector("#user").textContent);

// main nav bar
let homeAnchor = document.querySelector('#a-home');
let calcAnchor = document.querySelector('#a-calc');
let trackerAnchor = document.querySelector('#a-tracker');
let loginAnchor = document.querySelector('#a-login');
let logoutAnchor = document.querySelector('#a-logout');
anchorArr = [homeAnchor, calcAnchor, trackerAnchor, logoutAnchor];

// sub nav bars
let welcomeNav = document.querySelector('#welcome-nav');
let homeNav = document.querySelector('#home-nav');
let calcNav = document.querySelector('#calc-nav');
let trackerNav = document.querySelector('#tracker-nav');
let navArr = [homeNav, calcNav, trackerNav, welcomeNav]

for (let i=0; i<anchorArr.length-1; i++) {
    anchorArr[i].onclick = function() {
        console.log('hey')
        for (let j=0; j<navArr.length; j++) {
            navArr[j].style.display = 'none';
        }
        navArr[i].style.display = 'flex';
    }
}
