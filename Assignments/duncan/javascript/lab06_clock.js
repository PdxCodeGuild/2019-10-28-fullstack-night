let showDate_button = document.querySelector("#time_button")

showDate_button.onclick = function() {
    let full_date = new Date();
    document.querySelector("#clock_field").innerText = full_date;
    setTimeout(showDate_button.onclick, 1000);
}

let timer_button = document.querySelector("#stopwatch_button")

timer_button.onclick = function() {
    if (timer_button.className === "unclicked") {
        timer_button.className = "clicked";
        let start_time = new Date();
        start_time.setHours(0, 0, 0, 0);
        document.querySelector("#stopwatch_field").innerText = start_time;
        setTimeout(timer_button.onclick, 1000);
    }
}