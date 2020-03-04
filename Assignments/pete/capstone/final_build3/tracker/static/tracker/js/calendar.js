var dateTime = JSON.parse(document.querySelector('#date_time').textContent);
var monthStart = JSON.parse(document.querySelector('#month_start').textContent);
var monthLength = JSON.parse(document.querySelector('#month_length').textContent);

if (monthStart===6) {
    var dayCounter = 0
} else {
    var dayCounter = monthStart + 1;
}
let dayArr = document.querySelectorAll('.day');

for (let i=0; i<monthLength; i++) {
    dayArr[dayCounter].innerText = i+1;
    dayCounter ++;
}

// let changeCal = false
// function al() {
//     if (changeCal) {
//         for (let i=0; i<7;i++) {
//             dayArr.slice(dayArr.length-7)[i].style.display = changeCal?'none':'block';
//             document.querySelector("#calendar-container").style.gridTemplate = `7% repeat(${rows}, 1fr) / repeat(7, 1fr)`
//         }
//     }
// }

var app = new Vue({
    el: '#app',
    
})