# Sokly Proposal

## Project Overview 

Sokly will have features that will include, basic CRUD operations. The user or manager will be able to input a soccer players information such as name, position and include a picture. The user will only be able to access his or her data after login. The user will have the choice to go to a 'field' page view which allows the user to see a view that shows all player positions on a soccer field for reference and the user will be able to make adjustments as needed by slecting different positions and assigning a player to that position from a drop down menu populated by all players in the database. Sokly will try and address any accountabilty issues on and off the field. 

I will be using Django, Django Rest Framework and Vue.js in order to develop this web application. I will be researching any weather and location retrieving Api's to incorporate with Sokly. 

## Features

Sokly will employ features for coaches or management professionals. From a management perspective the following examples could apply:
 >" As a coach of a soccer team i want checklist of who my players are and how to get ahold of them in case there is a change to the game schedule". 

The tasks for Sokly in this situation would be:
  * Show list of players 
  * Show list of players contact information 
  
  >" As a coach i want to double check who is playing what position and be able to change players positions according to any new formations or stratagies i want to employ during the game."
  
The tasks for Sokly in this situation would be:
  * Show players in current position on field and allow user to make changes 
  * Display my current players and what positions they are playing .
  
  
## Data Model

In order for Sokly to record and display information that will help coaches track and improve commiunications with thier players it will need to track and record the following data:

   * User login data
     - Name
     * Email
     - Title 
     
   * User login permissions
     - coach 


   * Player field view
     * Player position on field (Drop down menus at specific field locations over soccer field image )    
     * Current weather in state (Weather icon and conditions in navbar)

   * Player image roster
     * Player information (All player information including: name, phone number, position and photograph of player)    



     
   * Player data
     - Name
     - Position
     - Phone number
     - Address
     - Image
       
       
 ## Schedule
 
   #### Stage 1 - Preperation 
        * Create virtual environment for Sokly project 
        * Install frameworks needed into new Django project 
        * Research api to incorporate into Sokly project 
        * Read over api documenentation 
        
   #### Stage 2 - Development of MVP
        * create mock user data in database
        * create/style webpage header with Sokly logo, login button, and signup button 
        * create/style webpage body with player discription and images of players 
        * store user login and signup data in database 
        * test redirect of users to new webpage with list of player field view
        * display create,delete, and edit player options on webpage
        
   #### Stage 3 - Adding Features for Coach
        * create webpage for coaches with Sokly logo and nav bar with login and logout options  
        * display in coach webpage all current players with pertinent information 
        * display current weather conditions on all webpages 
       
        
        
        
   