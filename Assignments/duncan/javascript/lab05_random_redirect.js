let url_list = [
    "https://www.google.com/",
    "https://www.yahoo.com/",
    "https://www.ask.com/",
    "https://www.bing.com/"
]

function redirect_function() {
    let new_location = url_list[Math.floor(Math.random() * url_list.length)];
    alert(`Redirecting to ${new_location}`);
    location.assign(new_location);
    location.reload(True);
}