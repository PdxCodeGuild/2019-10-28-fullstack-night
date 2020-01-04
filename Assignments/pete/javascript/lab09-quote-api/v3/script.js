let url = "https://favqs.com/api/quotes/"
let body = document.querySelector('body')
let author = document.querySelector('#author')
let quote = document.querySelector('#quote')
axios.get(url, {
    params: {
        page: 2,
        filter: 'war',
        type: 'tag',

    },
        headers: {
            Authorization: 'Token token=<api token goes here>'
        }
    })
.then(function (response) {
    console.log(response)
    author.innerText = response.data.quote.author
    quote.innerText = response.data.quote.body
})