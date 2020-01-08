let body = document.querySelector('body')

let xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
        console.log(this.responseText);
        body.innerText = this.responseText
    }
}
xhttp.open("GET", "https://favqs.com/api/qotd");
xhttp.send();let url = "https://favqs.com/api/qotd"
let body = document.querySelector('body')
let author = document.querySelector('#author')
let quote = document.querySelector('#quote')
axios.get(url)
.then(function(response) {
    console.log(response)
    author.innerText = response.data.quote.author
    quote.innerText = response.data.quote.body
})