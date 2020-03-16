let quote_btn = document.getElementById('quote_btn');
let text_area = document.getElementById('text_area');
let search_btn = document.getElementById('search_btn');
let back_btn = document.getElementById("back_btn");
let next_btn = document.getElementById("next_btn");




let page = 0;

if (page === 0){
    document.getElementById('back_btn').setAttribute('style','visibility:hidden');
};

if (page === 0){
    document.getElementById('next_btn').setAttribute('style','visibility:hidden');
}

console.log(page)

quote_btn.addEventListener("click", function(e){

    let config = {
        headers: {
          Authorization: 'Token token=""',
        }
      }
      



axios.get('https://favqs.com/api/quotes', config)
  .then(function (response) {
      console.log(response.data)
      page += 1;

    
      
      let quotes = (response.data.quotes)
    //   quotes.length = 10;            // limits the quotes to 10 results
    
      for (let quote of quotes){
          console.log(quote)
        
            
            
            let outputHTML = `
            <p>
            <span>${quote.body}</span><span><p style="margin-left:20px;"> -${quote.author}</p></span> 
            </p>
            <br>
            

            
            `;
            
            text_area.innerHTML += outputHTML;

            console.log(outputHTML);
            console.log(page)

            
            

        };

        
        if (page === 1){
            document.getElementById('next_btn').setAttribute('style','visibility:visible');
        }

        


  })
  .catch(function (error) {
    console.log(error);
  });




});



next_btn.addEventListener("click", function(e){

    let config = {
        headers: {
          Authorization: 'Token token=""',
        },
        params:{
            page: +1
        }
      };
      

    
    
    


axios.get('https://favqs.com/api/quotes', config)
    .then(function (response) {
        console.log(response.data)
        
        
        
        let quotes = (response.data.quotes)

        
        text_area.innerHTML = "";

        
        for (let quote of quotes){
            console.log(quote)

            let outputHTML = `
            <p>
            <span>${quote.body}</span><span><p style="margin-left:20px;"> -${quote.author}</p></span> 
            </p>
            <br>
            `;
            
            document.getElementById("text_area").innerHTML += outputHTML;
            

            console.log(outputHTML);

            


        };

        page += 1;

        if (page >= 1){
            document.getElementById('back_btn').setAttribute('style','visibility:visible');
        

        }

        
        
        console.log(page);
        

    });




});






    

back_btn.addEventListener("click", function(e){

    let config = {
        headers: {
          Authorization: 'Token token=""',
        },
        params:{
            page: -1
        }
      };
      

    




axios.get('https://favqs.com/api/quotes', config)
    .then(function (response) {
        console.log(response.data)
        

        
        let quotes = (response.data.quotes)
        
        
        text_area.innerHTML = "";

        
        for (let quote of quotes){
            console.log(quote)

            let outputHTML = `
            <p>
            <span>${quote.body}</span><span><p style="margin-left:20px;"> -${quote.author}</p></span> 
            </p>
            <br>
            `;
            
            document.getElementById("text_area").innerHTML += outputHTML;
            

            console.log(outputHTML);



        };
        page -= 1;
        console.log(page)
        if (page <= 1){
            document.getElementById('back_btn').setAttribute('style','visibility:hidden');
        }




    });
    



});


search_btn.addEventListener("click", function(e){
    let userchoice = document.getElementById("author_name").value;
    let config = {
        headers: {
          Authorization: 'Token token=""',
        },
        params:{
            filter: userchoice,
            type: 'author',
            page: page
        }
      };
      
    

    




axios.get('https://favqs.com/api/quotes/', config)
    .then(function (response) {
        console.log(response.data)
        

        
        let quotes = (response.data.quotes)
        
        
        text_area.innerHTML = "";

        
        for (let quote of quotes){
            console.log(quote)

            let outputHTML = `
            <p>
            <span>${quote.body}</span><span><p style="margin-left:20px;"> -${quote.author}</p></span> 
            </p>
            <br>
            `;
            
            document.getElementById("text_area").innerHTML += outputHTML;
            

            console.log(outputHTML);



        };
        page += 1;
        if (page === 1){
            document.getElementById('next_btn').setAttribute('style','visibility:visible');
        }

        console.log(page)
        if (page <= 1){
            document.getElementById('back_btn').setAttribute('style','visibility:hidden');
        }




    });
    



});


   




