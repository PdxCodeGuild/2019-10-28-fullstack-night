let daysArr = JSON.parse(document.querySelector("#days_json").textContent);
let datePicker = document.querySelector('#date-picker');
let dateSubmit = document.querySelector('#date-submit');

// datePicker.addEventListener('click', function(event) {
//     datePicker.
// })

dateSubmit.addEventListener('click', function(e) {
    if (!datePicker.value) {
        e.preventDefault();
        console.log(datePicker.value)
    } else if (daysArr.includes(datePicker.value)) {
        e.preventDefault();
        console.log(datePicker.value);
    }
})