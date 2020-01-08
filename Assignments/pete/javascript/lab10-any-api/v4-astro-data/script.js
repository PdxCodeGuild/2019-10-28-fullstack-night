let apiKey = "<api key here"
let url = `https://api.nasa.gov/planetary/apod?api_key=${apiKey}`

let todayNodeList = document.querySelectorAll('.today')

axios.get(url)
.then(function(response) {
    console.log(response)
    apod(response.data, todayNodeList)

})
console.log(todayNodeList)
function apod(data, nodeList) {
    for (item of todayNodeList) {
        if (item.id === 'image') {
            item.src = data.hdurl
        } else if (item.id === 'copyright') {
            item.innerText = data.copyright
        } else if (item.id === 'date') {
            item.innerText = data.date
        } else if (item.id === 'explanation') {
            item.innerText = data.explanation
        }
    }
    // let copyright = data.copyright
    // let date = data.date
    // let explanation = data.explanation
    // let hdurl = data.hdurl
}