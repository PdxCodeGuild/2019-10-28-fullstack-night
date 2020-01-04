let body = document.querySelector('body')

let xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
        console.log(this.responseText);
        body.innerText = this.responseText
    }
}
xhttp.open("GET", "https://favqs.com/api/qotd");
xhttp.send();
