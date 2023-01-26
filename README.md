# HARVARD-CS50-WEB
CS50’s Web Programming with Python and JavaScript

## Welcome

This repo contains my projects from [CS50’s Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/) course.

# Project 0 - Search
This project consist into building a clone for google search respecting a bunch of [specifications](https://cs50.harvard.edu/web/2020/projects/0/search/#specification) . 

 - ***Your website should have at least three pages: one for regular Google Search (which must be called index.html), one for Google Image Search, and one for Google Advanced Search.***


   - ***On the Google Search page, there should be links in the upper-right of the page to go to Image Search or Advanced Search. On each of the other two pages, there should be a link in the upper-right to go back to Google Search.***


 - ***On the Google Search page, the user should be able to type in a query, click “Google Search”, and be taken to the Google search results for that page.***


   - ***Like Google’s own, your search bar should be centered with rounded corners. The search button should also be centered, and should be beneath the search bar.***


 - ***On the Google Image Search page, the user should be able to type in a query, click a search button, and be taken to the Google Image search results for that page.***


 - ***On the Google Advanced Search page, the user should be able to provide input for the following four fields (taken from Google’s own advanced search options)***


   - Find pages with… “all these words:”
   - Find pages with… “this exact word or phrase:”
   - Find pages with… “any of these words:”
   - Find pages with… “none of these words:”
   
   
 - ***Like Google’s own Advanced Search page, the four options should be stacked vertically, and all of the text fields should be left aligned.***

   - ***Consistent with Google’s own CSS, the “Advanced Search” button should be blue with white text.***

   - ***When the “Advanced Search” button is clicked, the user should be taken to the search results page for their given query.***


 - ***Add an “I’m Feeling Lucky” button to the main Google Search page. Consistent with Google’s own behavior, clicking this link should take users directly to the first Google search result for the query, bypassing the normal results page.***


   - ***You may encounter a redirect notice when using the “I’m Feeling Lucky” button. Not to worry! This is an expected consequence of a security feature implemented by Google.***

 - ***The CSS you write should resemble Google’s own aesthetics.***

<br />
<br />

<img  src='https://user-images.githubusercontent.com/90383672/203099502-92783dd5-4554-4af8-8f99-b878d50cd012.png' width= 1000 /> 



# Project 1 - WIKI
This project consist into building a wiki like wikipedia with a bunch of [features](https://cs50.harvard.edu/web/2020/projects/1/wiki/#specification)

 - ***Entry Page***: Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.


   - ***The view should get the content of the encyclopedia entry by calling the appropriate util function.***
   
   - ***If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.***
   
   
   - ***If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.***


 - ***Index Page***: Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.


 - ***Search***: Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.


   - ***If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.***

   - ***If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results.***


   - ***Clicking on any of the entry names on the search results page should take the user to that entry’s page.***
   
 - ***New Page***: Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.

   - ***Users should be able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page.***
   - ***Users should be able to click a button to save their new page.***
   
   - ***When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.***
   
   - ***Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.***

 - ***Edit Page***: On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.

   - ***The textarea should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial value of the textarea).***


   - ***The user should be able to click a button to save the changes made to the entry.***
   - ***Once the entry is saved, the user should be redirected back to that entry’s page.***

 - ***Random Page***: Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.


 - ***Markdown to HTML Conversion***: On each entry’s page, any Markdown content in the entry file should be converted to HTML before being displayed to the user. You may use the python-markdown2 package to perform this conversion, installable via pip3 install markdown2.

   - ***Challenge for those more comfortable: If you’re feeling more comfortable, try implementing the Markdown to HTML conversion without using any external libraries, supporting headings, boldface text, unordered lists, links, and paragraphs. You may find using regular expressions in Python helpful.***


<br />
<br />


<img src='https://user-images.githubusercontent.com/90383672/204035762-110eb7a2-501f-483b-9ded-511aedc52721.png'  width=1000px /> 



# Project 2 - COMMERCE

This project consist into Designing an eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”

The project should meet these [requirements](https://cs50.harvard.edu/web/2020/projects/2/commerce/#specification)


 - ***Models: Your application should have at least three models in addition to the User model: one for auction listings, one for bids, and one for comments made on auction listings. It’s up to you to decide what fields each model should have, and what the types of those fields should be. You may have additional models if you would like.***

 - ***Create Listing: Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).***

 - ***Active Listings Page: The default route of your web application should let users view all of the currently active auction listings. For each active listing, this page should display (at minimum) the title, description, current price, and photo (if one exists for the listing).***
 
 - ***Listing Page***: Clicking on a listing should take users to a page specific to that listing. On that page, users should be able to view all details about the listing, including the current price for the listing.

    - ***If the user is signed in, the user should be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user should be able to remove it.***

    - ***If the user is signed in, the user should be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user should be presented with an error.***


    - ***If the user is signed in and is the one who created the listing, the user should have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.***


    - ***If a user is signed in on a closed listing page, and the user has won that auction, the page should say so.***

    - ***Users who are signed in should be able to add comments to the listing page. The listing page should display all comments that have been made on the listing.*** 

 - ***Watchlist***: Users who are signed in should be able to visit a Watchlist page, which should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page.

 - ***Categories***: Users should be able to visit a page that displays a list of all listing categories. Clicking on the name of any category should take the user to a page that displays all of the active listings in that category.
 
 - ***Django Admin Interface***: Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site.


<img src='https://user-images.githubusercontent.com/90383672/207636104-8f84f660-c19a-4bb7-aeaa-734117ea913b.png' width=1000px /> | <img src='https://user-images.githubusercontent.com/90383672/207634331-cc4d6ab5-2e28-41a0-871b-9b0c202b50ef.png' width=1000px />   
--- | ---  
<img src='https://user-images.githubusercontent.com/90383672/207636373-c1f59b18-36d6-40cc-81ec-b39c5986e433.png' width=1000px /> | <img src='https://user-images.githubusercontent.com/90383672/207635704-ff41f211-3966-4592-8456-af124c53b9d0.png' width=1000px />

 


# Project 3 - Mail

This project consist into Designing a front-end for an email client that makes API calls to send and receive emails.

The project should meet these [requirements](https://cs50.harvard.edu/web/2020/projects/3/mail/#specification)


 - ***Mailbox***: When a user visits their Inbox, Sent mailbox, or Archive, load the appropriate mailbox.
 
    - ***You’ll likely want to make a GET request to /emails/<mailbox> to request the emails for a particular mailbox.***

    - ***When a mailbox is visited, the application should first query the API for the latest emails in that mailbox.***

    - ***When a mailbox is visited, the name of the mailbox should appear at the top of the page (this part is done for you).***

    - ***Each email should then be rendered in its own box (e.g. as a <div> with a border) that displays who the email is from, what the subject line is, and the timestamp of the email.***

    - ***If the email is unread, it should appear with a white background. If the email has been read, it should appear with a gray background.***

 - ***View Email***: When a user clicks on an email, the user should be taken to a view where they see the content of that email.

    - ***You’ll likely want to make a GET request to /emails/<email_id> to request the email.***
    
    - ***Your application should show the email’s sender, recipients, subject, timestamp, and body.***

    - ***You’ll likely want to add an additional div to inbox.html (in addition to emails-view and compose-view) for displaying the email. Be sure to update your code to hide and show the right views when navigation options are clicked.***

 - ***See the hint in the Hints section about how to add an event listener to an HTML element that you’ve added to the DOM.***

 - ***Once the email has been clicked on, you should mark the email as read. Recall that you can send a PUT request to /emails/<email_id> to update whether an email is read or not.***


 - ***Archive and Unarchive***: Allow users to archive and unarchive emails that they have received.

    - ***When viewing an Inbox email, the user should be presented with a button that lets them archive the email. When viewing an Archive email, the user should be presented with a button that lets them unarchive the email. This requirement does not apply to emails in the Sent mailbox.***


    - ***Recall that you can send a PUT request to /emails/<email_id> to mark an email as archived or unarchived.***

    - ***Once an email has been archived or unarchived, load the user’s inbox.***

 - ***Reply***: Allow users to reply to an email.

    - ***When viewing an email, the user should be presented with a “Reply” button that lets them reply to the email.***

    - ***When the user clicks the “Reply” button, they should be taken to the email composition form.***

    - ***Pre-fill the composition form with the recipient field set to whoever sent the original email.***

    - ***Pre-fill the subject line. If the original email had a subject line of foo, the new subject line should be Re: foo. (If the subject line already begins with Re: , no need to add it again.)***

    - ***Pre-fill the body of the email with a line like "On Jan 1 2020, 12:00 AM foo@example.com wrote:" followed by the original text of the email.***

<img src="https://user-images.githubusercontent.com/90383672/209667616-c06301de-6d64-4bbc-830b-d9d672144943.png" width=1000px />




