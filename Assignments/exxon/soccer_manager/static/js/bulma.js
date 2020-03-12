

// (function () {
//     var burger = document.querySelector('.burger');
//     var menu = document.querySelector('#' + burger.dataset.target);
//     burger.addEventListener('click', function () {
//         burger.classList.toggle('is-active');
//         menu.classList.toggle('is-active');
//     });
// })();


document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  
    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {
      

      // Add a click event on each of them
      $navbarBurgers.forEach( el => {
        el.addEventListener('click',  () => {
  
          // Get the target from the "data-target" attribute
          const target = el.dataset.target;
          const $target = document.getElementById(target);
  
          // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
          el.classList.toggle('is-active');
          $target.classList.toggle('is-active');
  
        });
      });
    }
  
  });



  document.querySelectorAll('.modal-button').forEach(function(el) {


    el.addEventListener('click', function() {
      var target = document.querySelector(el.getAttribute('data-target'));
      
      target.classList.add('is-active');

        //  gets click event from X on pop-up  and closes pop-up and then reloads page

      target.querySelector('.modal-close').addEventListener('click',   function() {
          target.classList.remove('is-active');

          
       });

      //  this is the issues with the mobile form submit button the location.reload() function makes the file uplaod fail
      //  gets click event from submit button on add new player pop-up and closes pop-up and then reloads page
       target.querySelector('#close-submit').addEventListener('click',   function() {
        target.classList.remove('is-active'); 
      
      });

    

  });

 });



