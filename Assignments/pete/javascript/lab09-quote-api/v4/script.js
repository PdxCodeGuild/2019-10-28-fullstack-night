let url = "https://favqs.com/api/quotes/"
let body = document.querySelector('body')
let authorDiv = document.querySelector('#author')
let quoteDiv = document.querySelector('#quote')
let input = document.querySelector('input')
let tag = input.value
let button = document.querySelector('button')
input.addEventListener('keypress', function() {
    tag = input.value
})
button.onclick = function() {
    
    axios.get(url, {
        params: {
            // page: 2,
            filter: tag,
            type: 'tag',
    
        },
            headers: {
                Authorization: 'Token token=<api token goes here>'
            }
        })
    .then(function (response) {
        console.log(response)
        let quoteArr = response.data.quotes
        let quote = quoteArr[Math.floor(Math.random()*quoteArr.length)]
        if (quote.author) {
            authorDiv.innerText = quote.author

        }
        quoteDiv.innerText = quote.body
    })
}