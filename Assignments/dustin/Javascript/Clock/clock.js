window.onload = function() {
    let monthField = document.querySelector("#month");
    let dayField = document.querySelector("#day");
    let yearField = document.querySelector("#year");
    let hourField = document.querySelector("#hour");
    let minuteField = document.querySelector("#minute");
    let secondField = document.querySelector("#second");

    let fullDate = new Date();

    let month = fullDate.getMonth()+1;
    let day = fullDate.getDate();
    let year = fullDate.getFullYear();
    let hour = fullDate.getHours();
    let minute = fullDate.getMinutes();
    let second = fullDate.getSeconds();

    var counter = 0;

    setInterval(function() {

    let fullDate = new Date();

    let month = fullDate.getMonth()+1;
    let day = fullDate.getDate();
    let year = fullDate.getFullYear();
    let hour = fullDate.getHours();
    let minute = fullDate.getMinutes();
    let second = fullDate.getSeconds();

        counter++;

        monthField.innerText = month;
        dayField.innerHTML = day;
        yearField.innerHTML = year;
        hourField.innerHTML = hour;
        minuteField.innerHTML = minute;
        secondField.innerHTML = second;

        

    }, 1000)
}