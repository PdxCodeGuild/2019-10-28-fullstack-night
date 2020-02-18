# Creative Crossroads
## Capstone Proposal
___
### The Endgame
    A website dedicated to the cross-section of all creative arts whether those be visual, audible, readable, or otherwise.
___

#### The Works
    - User interface that allows a user to select a series of layouts or even customize the layout of their page/gallery to display their artistic talents.  (Modular layout)
    - Optional comments and reviews section that allows feedback from other users.
    - Direct messaging between users.
    -  Community pages geared towards artist discovery and self-promotion.
    - Real money or in-house currency integration to purchase digital files from artists for prints or personal/commercial use.

___

#### The Reason
    Artists exist in nearly every medium.  As of yet, no site exists that allows multi-faceted artists to express their talents in one comprehensive location.  The aim of this site is to change that.
___

#### The Tools
    - Python 3.7
    - Django 2.2.9
    - Normalize/Skeleton CSS
    - HTML5/Javascript
___

#### The Walkthrough
    Landing Page:  A view of the most up-voted works of each artistic category with links to each of said categories and links to user functions(homepage, login/logout, favorites, etc).

    Category Pages: Nuanced view that can be sorted by date/time published, upvotes, editor's picks.

    User Homepage:  Collection of their own artwork or a collection of artwork they've gathered from around the site.  Customized modular layout options

    Artwork Pages:  Centrally displayed focus piece with associated art arrayed underneath or to the side.  Example:  Album artwork, media player for song or songlist, and lyrics.  Example 2:  Digital art tutorial, associated renders and templates used in creation.  

    User Account Settings Page:  Select settings to toggle media autoplay, site theme, payment information.

    User Login/Register User pages: Standard

    Favorites pages:  To be determined.
___
    
#### The Glue
    - For all but text input, site will be point and click.  Forms will have submit buttons.  Media players will be embedded open source players with their own buttons. 
    - Each piece of art will have a hyperlinked title which will take the user to the artpage.  Artpages will be subsectioned under the art owner's header.  
    - Possibly setup multiple themes that the user can select which will load different CSS files.
___
#### The Building Blocks
    - User
        - Settings
        - Artwork
        - Favorites
    - Artwork
        - Title
        - Type
        - Content
        - Associated art
        - Publish date
        - Owner
    - Categories
___
#### The Inkscape Timeline
    - Week 1
        - Django base setup
        - Write models and model functions
        - Draw up rough drafts for page templates
        - Research payment and media player integration
    - Week 2
        - Write views and page templates
        - Integrate APIs
        - Achieve base cross-site functionality
        - Start CSS/JS implementation
    - Week 3
        - Troubleshoot everything
    - Final days
        - Finishing touches and site testing
    - Post-presentation
        - Fix everything I didn't have time for before making it functional.  
        - Create tiered accounts for moderators, site curators, administrators.
        - Implement more mediums(Video, coding, music, etc.)
        - Search functionality
        - Discussion forums
    