let url = "https://favqs.com/api/qotd"
let body = document.querySelector('body')
let author = document.querySelector('#author')
let quote = document.querySelector('#quote')
axios.get(url)
.then(function(response) {
    console.log(response)
    author.innerText = response.data.quote.author
    quote.innerText = response.data.quote.body
})