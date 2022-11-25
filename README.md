# HARVARD-CS50-WEB
CS50’s Web Programming with Python and JavaScript

# Welcome

This repo contains my project from [CS50’s Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/) course.

## Project 0
This project consist into building a clone for google search respecting a bunch of [specifications](https://cs50.harvard.edu/web/2020/projects/0/search/#specification) . 

Your website must meet the following requirements:

 - Your website should have at least three pages: one for regular Google Search (which must be called index.html), one for Google Image Search, and one for Google Advanced Search.

 - On the Google Search page, there should be links in the upper-right of the page to go to Image Search or Advanced Search. On each of the other two pages, there should be a link in the upper-right to go back to Google Search.
 - On the Google Search page, the user should be able to type in a query, click “Google Search”, and be taken to the Google search results for that page.
 
- The CSS you write should resemble Google’s own aesthetics.

- ....

The final result looks like :

<br />
<br />

<img  src='https://user-images.githubusercontent.com/90383672/203099502-92783dd5-4554-4af8-8f99-b878d50cd012.png' width=500px />
<img  src='https://user-images.githubusercontent.com/90383672/203100703-7440e665-6308-4184-a5c5-8015c6d1d0a4.png' width=500px />
<img  src='https://user-images.githubusercontent.com/90383672/203100209-57d645f3-e9f0-4fb4-824e-c6e2415de6de.png' width=500px />

## Project 1
This project consist into building a wiki like wikipedia with a bunch of [features](https://cs50.harvard.edu/web/2020/projects/1/wiki/#specification)

In my wiki a implement all the [required specifications](https://cs50.harvard.edu/web/2020/projects/1/wiki/#specification)  listed below :

#### Entry Page

 - Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.
 - The view should get the content of the encyclopedia entry by calling the appropriate util function.
 - If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.
 - If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.

#### Index Page
 - Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.
 
#### Search

 - Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
 - If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
 - If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results.
 
 - Clicking on any of the entry names on the search results page should take the user to that entry’s page.
 
#### New Page

 - Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.
 - Users should be able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page.
 - Users should be able to click a button to save their new page.
 - When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.
 - Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.

#### Edit page

 - On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
 - The textarea should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial value of the textarea).
 - The user should be able to click a button to save the changes made to the entry.
 - Once the entry is saved, the user should be redirected back to that entry’s page.
 
 
#### Random Page

 - Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.

The final result looks like :

<br />
<br />


<img src='https://user-images.githubusercontent.com/90383672/204035762-110eb7a2-501f-483b-9ded-511aedc52721.png'  width=500px /> 

 

 

 


