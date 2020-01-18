let apiKey = "9879d44a7f4636eecc8f684768c5cbf3"
let url1 = "https://cors-anywhere.herokuapp.com/https://api-v3.igdb.com/games/"
axios({
    method: 'get',
    url: url1,
    // params: {
    //     "user-key": apiKey,
    // },
    headers: {
        "user-key": apiKey,
    },

})
.then(function(response) {
    console.log(response)
})
