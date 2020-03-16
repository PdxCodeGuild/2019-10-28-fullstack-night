


var rand_link = [
"https://exxonsuarez.com/","https://www.pexels.com","https://github.com","https://pixabay.com"];




function countdown(){

    setTimeout(myTimeout1, 1000) 
    setTimeout(myTimeout2, 2000) 
    setTimeout(myTimeout3, 3000)
    setTimeout(myTimeout4, 4000)
    setTimeout(myTimeout5, 5000)
    setTimeout(new_page, 6000)

    function myTimeout1() {
        document.getElementById("text").innerHTML = "5";
      }
      function myTimeout2() {
        document.getElementById("text").innerHTML = "4";
      }
      function myTimeout3() {
        document.getElementById("text").innerHTML = "3";
      }
      function myTimeout4() {
        document.getElementById("text").innerHTML = "2";
      }
      function myTimeout5() {
        document.getElementById("text").innerHTML = "1";
      }


        function new_page(){
    
    
    
            var rand_url = Math.random() * rand_link.length;
            rand_url = parseInt(rand_url,10);
            var final_url = rand_link[rand_url];
            console.log(final_url);
            window.location.assign(final_url)
        
        
            return final_url; 
        }






    

}    









    
    

    
    
    
    
    
    
    
    
    
    
    
    






