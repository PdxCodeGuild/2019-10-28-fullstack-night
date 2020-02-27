let url = 'https://trackapi.nutritionix.com/v2/natural/nutrients/'
let query = JSON.stringify({
    "query": '1 cup flour',
    "timezone": 'US/Eastern',
})
axios({
    method: 'post',
    url: url,
    headers: {
        'Content-Type': 'application/json',
        'x-app-id': '9d6f794a',
        'x-app-key': '0a43551440794adf00f2b58777f29d2e',
        // 'x-remote-user-id': 'pjz987',
    },
    data: query
}).then((response)=>{
    console.log(response)
}).catch((response) => {
    console.log(response.response.data)
})