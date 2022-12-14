# Team 5 - Mountain Goats
## Weekly Status Report for Medical Procedure Price Checker
#### Members
- Nicolas Mavromatis (Nima6629)
- Cooper Ide (coid6456)
- Patrick Chesnut (chesnutp)
---
#### Week 6 Update (26 Sept to 2 Oct)
    
During our first week, Patrick collected JSON and csv files of medical prices for several hospitals, Medicare, and Medicaid.  He also gathered CPT code descriptions so we know what procedure each billing code represents.  Data from the JSON and csv files was extracted by Nick with python scripts into an excel file.  Each sheet in the Excel file will represent a different table in a SQL database.  A data dictionary was also created to describe the data by Cooper, who organized the table structure.

#### Week 7 Update (3 Oct to 9 Oct)
During the second week, Nick wrote a python script that created a sqlite database file. We made a first iteration of placing tasks on Trello.  We also started to brainstorm what features the app should have and the major web pages.

Plans for next week include continuing to learn Flask, the basics of SQL, and working early on milestone 4 to develop web page structure. We feel we are in an early stage and still learning many new tools so progress is slow. 

Our top priorities are to learn Flask and plan our web layout.
We plan to make a mockup of pages, and create a list of page descriptions after organizing the structure of the application. 

#### Week 8 Update (10 Oct to 16 Oct)
During our third week, we continued to learn Flask, and started on the web layout design. 
We plan to think about implementation details for python scripts for passing parameters to the database engine.

#### Week 9 Update (17 Oct to 23 Oct)
During the fourth week, we finalized the web page layout design. We also started thinking about the SQL design for milestone 5. 
We decided on what happens when a user logs in. After a successful login, it should return to the welcome page. 

#### Week 10 Update (24 Oct to 30 Oct)
During the fifth week, we started planning milestone 5 and how the SQL queries should function. Nick also worked on python scripts to run SQL in the main page search bar.
We have settled on Flask for the backend framework, and heroku. We still need to look into how to integrate flask with Heroku and some external database. 

#### Week 11 Update (31 Oct to 6 Nov)
During the sixth week, Nick got a basic version of Flask running, created a search bar for each page that runs SQL, and created a basic login and signup system. Patrick reviewed Milestone 5 requirements and got started on it. Cooper researched Bootstrap and started designing a navigation bar.

#### Week 12 Update (7 Nov to 14 Nov)
During the seventh week, Nick created the python script to dynamically generate each "browse by link" from SQL and populate each browse by page with these links automatically. Cooper agreed to continue to work on the CSS, and Patrick agreed to work on other extra features such as a page to add/update results to the database. 

#### Week 13 Update (15 Nov to 22 Nov)
During the eighth week, Cooper implemented bootstrap for styling on the user account page, the nav bar from this will extend to all pages. Patrick completed the Admin page and might make a few tweaks here and there. Nick provided help with the backend python script to wire up some of the front end features with the database. In the coming weeks we will finish up small tweaks and look towards a deployment plan.

<figure>
  <IMG SRC="TrelloSC.PNG">
</figure>

---
