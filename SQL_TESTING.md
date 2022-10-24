Project Milestone 5

# Team 5 - Mountain Goats
## Weekly Status Report for Medical Procedure Price Checker
#### Members
- Nicolas Mavromatis (Nima6629)
- Cooper Ide (coid6456)
- Patrick Chesnut (chesnutp)

Search Bar Table:

This table is generated dynamically after searching by hospital, procedure name, test code, or insurer in the main page search bar or in the "browse by" pages. 

A slight variation on this table will be generated within the browse by procedure, browse by insurer, and browse by hospital pages, with different parameters passed to SQL.

Fields: Associated Codes-The CPT code associated with each test.
Cash-Discount Price:???
Deidentified Max Allowed:???
Deidentified Min Allowed:???
Description: Short text description of procedure.
Gross Charge:???
iob Selection: Inpatient or Outpatient procedure
Payer: Insurance Company
Payer Allowed Amount:???

Tests:

Main Page Search Bar Test
    Verify a variety of searches by different fields    
Description
    Verify correct results appear and render in the table
Pre-Conditions
    User has entered correct search parameter
Test Steps
    1.Navigate to welcome/home page
    2.Search by parameter (test a variety of parameter types and values)
    3.Check that results are correct and results page (table) renders
Expected Result
    Table with correct results renders correctly
Actual Result
    Page scrolls correctly with results
Notes
    There will need to be a variety of tests, for different parameter types and values, to make sure the SQL code generates the correct results. There will also need to be tests checking rendering.
Post Conditions
    Correct table is displayed. User is able to enter in another search, or browse to a different page.
    
Main Search Bar Access Methods
User search by hospital, procedure name, test code, or insurer
Parameters are the hospital name, procedure name, test code, or insurer, passed to the SQL database to return results.
Return value will be a table with all results that match the search parameter and value.
There will be multiple tests for each search parameter type consisting of multiple values for each type. It is unclear if it is best to create formal python tests matching specific SQL values, to test a variety of searches manually, or do a mix of both.


Browse by Tables:
 
These tables are generated dynamically using the same database as the main search bar. In each of specific pages, the user can browse by 