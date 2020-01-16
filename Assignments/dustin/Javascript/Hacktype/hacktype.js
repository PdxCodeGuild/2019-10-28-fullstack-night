window.onload = function() {
    let textArea = document.querySelector("#userIn");
    let totalAmount = 0;
    

    textArea.addEventListener("keypress", function(event) {
        
        event.preventDefault();
        let testText = "This is randomly generated text. Your computer has been infected with a virus.  Please shutdown and unplug your computer to stop the spread to your other appliances.  This message has been brought to you by Skynet.";
        
        totalAmount += randomAmount()
        
        textArea.innerHTML = testText.slice(0, totalAmount);
        

    }, false);

    function randomAmount() {
        let amount = Math.floor(Math.random() * 6) + 1;
        return amount;

    } 
    
    //let testText = "This is randomly generated text.";
}