let newTaskInput = document.querySelector('input')
let addButton = document.querySelector('#add')

var app = new Vue({
    el: '#app',
    data: {
        tasks: []
    }
});

addButton.addEventListener('click', function() {
    app.tasks.push(newTaskInput.value);
    newTaskInput.value = ''
})