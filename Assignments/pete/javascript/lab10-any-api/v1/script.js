let url = "https://randomuser.me/api/"
let body = document.querySelector('body')
let nameDiv = document.querySelector('#name')
let genderDiv = document.querySelector('#gender')
let emailDiv = document.querySelector('#email')
let cellDiv = document.querySelector('#cell')
let phoneDiv = document.querySelector('#phone')
let ageDiv = document.querySelector('#age')
let addressDiv = document.querySelector('#address')
let cityDiv = document.querySelector('#city')
let stateDiv = document.querySelector('#state')
let countryDiv = document.querySelector('#country')
let postcodeDiv = document.querySelector('#postcode')
let usernameDiv = document.querySelector('#username')
let passwordDiv = document.querySelector('#password')
let membersinceDiv = document.querySelector('#membersince')
let photoImg = document.querySelector('#photo')

axios.get(url)
.then(function(response) {
    console.log(response)
    let info = response.data.results[0]
    console.log(info)
    let name = `${info.name.title} ${info.name.first} ${info.name.last}`
    let gender = info.gender
    let email = info.email
    let cell = info.cell
    let phone = info.phone
    let age = info.dob.age
    let address = `${info.location.street.number} ${info.location.street.name}`
    let city = info.location.city
    let state = info.location.state
    let country = info.location.country
    let postcode = info.location.postcode
    let username = info.login.username
    let password = info.login.password
    let membersince = `${info.registered.date} age ${info.registered.age}`
    let photo = info.picture.large
    nameDiv.innerText = `Name: ${name}`
    genderDiv.innerText = `Gender: ${gender}`
    emailDiv.innerText = `email: ${email}`
    cellDiv.innerText = `Cell #: ${cell}`
    phoneDiv.innerText = `Phone #: ${phone}`
    ageDiv.innerText = `Age: ${age}`
    addressDiv.innerText = `Address: ${address}`
    cityDiv = `City: ${city}`
    stateDiv.innerText = `State: ${state}`
    countryDiv.innerText = `Country: ${countryDiv}`
    postcodeDiv.innerText = `Postcode: ${postcode}`
    usernameDiv.innerText = `Username: ${username}`
    passwordDiv.innerText = `Passwod: ${password}`
    membersinceDiv.innerText = `Member Since: ${membersince}`
    photoImg.src = photo
})