


function clock(){
var date = new Date();

var h = date.getHours();
var m = date.getMinutes();
var s = date.getSeconds();
var am_pm = " AM";

if (h == 0){
    h = 12
}

if (h > 12){
    h = h - 12
    am_pm = " PM";
}

if (h < 10){
    h = "0" + h;

}

if (m < 10){
    m = "0" + m;
}

if (s < 10){
    s = "0" + s;
}


var time = h + ":" + m + ":" + s +  am_pm;

document.getElementById("display_clock").innerHTML = time;
setTimeout(clock, 1000);

}