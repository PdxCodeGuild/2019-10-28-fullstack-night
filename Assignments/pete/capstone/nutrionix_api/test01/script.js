let input = document.querySelector('input')
let div = document.querySelector('div')

let url = 'https://trackapi.nutritionix.com/v2/natural/nutrients/'

function axiosGet(query) {
    axios({
        method: 'post',
        url: url,
        headers: {
            'Content-Type': 'application/json',
            'x-app-id': '9d6f794a',
            'x-app-key': '0a43551440794adf00f2b58777f29d2e',
            // 'x-remote-user-id': 'pjz987',
        },
        data: {
            'query': query,
        }
    }).then((response)=>{
        console.log(response);
        foodsArr = response.data.foods;
        let divString = '';
        let totalObj = {'kcal': 0, 'fat': 0, 'carb': 0, 'protein': 0};
        for (let i=0; i<foodsArr.length; i++) {
            food = foodsArr[i]
            divString += `${food.food_name}: kcal: ${food.nf_calories}; fat: ${food.nf_total_fat}; carb: ${food.nf_total_carbohydrate}; protein: ${food.nf_protein} ... `
            totalObj['kcal'] += food.nf_calories;
            totalObj['fat'] += food.nf_total_fat;
            totalObj['carb'] += food.nf_total_carbohydrate;
            totalObj['protein'] += food.nf_protein;
        }
        divString += `total: kcal: ${totalObj.kcal}; fat: ${totalObj.fat}; carb: ${totalObj.carb}; protein: ${totalObj.protein}`
        div.innerText = divString
    })
}

input.addEventListener('keypress', function(e) {
    if (e.which===13) {
        axiosGet(input.value)
    }
})