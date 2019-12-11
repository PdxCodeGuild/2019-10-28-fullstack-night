window.onload = function() {
    let listItem = document.querySelector('input');
    let totalList = document.querySelector('#order-list');
    listItem.addEventListener('click', function() {
        let totalListText = document.getElementsByTagName('input').value;
        let newLi = document.createElement('li');
        newLi.appendChild(totalListText);
        totalList.appendChild(newLi);
    })
}