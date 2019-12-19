let keys = document.querySelectorAll('.keys')
let output = document.querySelector('#output')
let equals = document.querySelector('#equals')
let readout = ''
for (let i = 0; i < keys.length; i++) {
    console.log(keys[i])
    keys[i].addEventListener('click', function() {
        readout += `${keys[i].innerText} `
        output.innerText = readout
    })
    
}

equals.addEventListener('click', function() {
    output.innerText = `${readout} = ${eval(readout)}`
})