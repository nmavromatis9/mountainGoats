# Project Milestone 5
## Team 5 - Mountain Goats
#### Members
- Nicolas Mavromatis (Nima6629)
- Cooper Ide (coid6456)
- Patrick Chesnut (chesnutp)

---

#### List of Tables
Our website will utilize two sqlite databases consisting of 5 tables total.  The first database is named "hospital.db" and contains the tables: tblHospitalPrices, tblInsurer, tblHospitals, and tblCPT_Codes.  This database contains the information that will be displayed to the user on the website.  The second database is named "login.db" and contains one table, users.  This database is used to keep track of all registered users on the site.
- ##### tblHospitalPrices
Description: This is the main table of the database.  It lists the prices of procedures and services by hospital and insurer.  Three prcies are included cost, gross charge, and cash discount.

|   Table           |   Field       |   Data Type    |   Description                                          |   Key   |
|-------------------|---------------|----------------|--------------------------------------------------------|---------|
| tblHospitalPrices | CPT_code      | Int            | Code of specific Procedure or Service                  | Foreign |
| tblHospitalPrices | Hospital_ID   | Int            | Unique Identifier of Hospital                          | Foreign |
| tblHospitalPrices | Insurer_ID    | Int            | Unique Identifier of Insurance Plan                    | Foreign |
| tblHospitalPrices | Cost          | Money          | Insurer's Negotiated Rate for Procedure or Service     |         |
| tblHospitalPrices | Gross_charge  | Money          | Hospital's Undiscounted Sticker Price                  |         |
| tblHospitalPrices | Cash_discount | Decimal        | Discount for Cash Payment Method                       |         | 

Tests to verify: To verify the table is loaded properly we plan to perform the SQL query, `SELECT * FROM tblHospitalPrices;`.  We will then compare this data with the data present in the Excel file located in the DB_XLSX_Files directory.

- ##### tblInsurer
Description: This table lists all of the insurers that we gathered price data for.  It includes two public insurers and four private insurers.
| Table             | Field         | Data Type      | Description                                                        | Key     |
|-------------------|---------------|----------------|--------------------------------------------------------------------|---------|
| tblInsurer        | Insurer_ID    | Int            | Primary Key of Insurer table                                       | Primary |
| tblInsurer        | Name          | Nvarchar(100)  | Name of Insurer                                                    |         |
| tblInsurer        | Detailed      | Nvarchar(200)  | Plan Name                                                          |         |

Tests to verify: To verify the table is loaded properly we plan to perform the SQL query, `SELECT * FROM tblInsurer;`.  We will then compare this data with the data present in the Excel file located in the DB_XLSX_Files directory.

- ##### tblHospitals
Description: This table lists all of the hospitals that we gathered price data for.  It includes four hospitals from Colorado and one hospital from Ohio.
| Table             | Field         | Data Type      | Description                                                        | Key     |
|-------------------|---------------|----------------|--------------------------------------------------------------------|---------|
| tblHospitals      | Hospital_ID   | Int            | Primary Key of Hospital table                                      | Primary |
| tblHospitals      | Hospital name | Nvarchar(200)  | Name of Hospital                                                   |         |

Tests to verify: To verify the table is loaded properly we plan to perform the SQL query, `SELECT * FROM tblHospitals;`.  We will then compare this data with the data present in the Excel file located in the DB_XLSX_Files directory.

- ##### tblCPT_Codes
Description: CPT codes are standard industry codes that uniquely identify all possible servies or procedures that can be performed on a patient.  We selected a subset of 50 of these codes to include in our project.
| Table             | Field         | Data Type      | Description                                                        | Key     |
|-------------------|---------------|----------------|--------------------------------------------------------------------|---------|
| tblCPT_Codes      | CPT_code      | Int            | Current Procedural Terminology codes - Prim Key of CPT_Codes table | Primary |
| tblCPT_Codes      | Description   | Nvarchar(1000) | Description of Service or Procedure                                |         |
| tblCPT_Codes      | Category      | Nvarchar(100)  | Category of service or procedure                                   |         |

Tests to verify: To verify the table is loaded properly we plan to perform the SQL query, `SELECT * FROM tblCPT_Codes;`.  We will then compare this data with the data present in the Excel file located in the DB_XLSX_Files directory.

- ##### users
Description: The final table simply lists users and their associated passwords.
| Table             | Field         | Data Type      | Description                                                        | Key     |
|-------------------|---------------|----------------|--------------------------------------------------------------------|---------|
| users             | email         | TEXT           | Unique username                                                    | Primary |
| users             | password      | TEXT           | Password                                                           |         |

Tests to verify: To verify the table is loaded properly we plan to perform the SQL query, `SELECT * FROM tblCPT_Codes;`.  This step will be performed after we have used the website to sign up some "dummy" users.

---

#### List of Data Access Methods
Our website will utilize four methods to access the underlying sqlite database
##### getCPT
Description: This method will be used on the browse by procedure page to pull up a table showing the price of a procedure.  The method executes a SQL query producing a table where rows are populated by hospitals and the columns are populated by rates (insurers, self-pay, charge).

Parameters: The method takes only one parameter, the input from the user contained in the textbox.  The input should be the name of a procedure or CPT code.

Return values: The method will return the results of the SQL query using sqlite's built-in fetchall() function.  A list of tuples is returned which is then processed into an HTML table for display on the webpage.

Use case name: Browse by procedure page / getCPT <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Verify a variety of searches by different test codes and procedure names. <br>
Description <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Verify correct results appear and render in the table <br>
Pre-conditions <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; User has entered correct search parameter <br>
Test Steps <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. Navigate to the browse by procedure page <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. Search by parameter (test a variety of parameter values, procedures and CPT codes) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Check that results are correct and results page (table) renders <br>
Expected result <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Table with correct results renders correctly <br>
Actual result <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Page scrolls correctly with results <br>
Status (Pass/Fail) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pass <br>
Notes <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; There will need to be a variety of tests, for both parameter types and values, to make sure the SQL code generates the correct results. There will also need to be tests checking rendering. <br>
Post-conditions <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Correct table is displayed. User is able to enter in another search, or browse to a different page. <br>

---

##### getInsurers
Description: This method will be used on the browse by insurers page to pull up a table showing the price of a procedure.  The method executes a SQL query producing a table where rows are populated by procedures and the columns are populated by hospitals. The prices displayed are the rates the selected insurer negotiated with each hospital.

Parameters: The method takes only one parameter, the input from the user contained in the textbox.  The input should be the name of an insurer.

Return values: The method will return the results of the SQL query using sqlite's built-in fetchall() function.  A list of tuples is returned which is then processed into an HTML table for display on the webpage.

Use case name: Browse by insurer page / getInsurer <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Verify a variety of searches by entering different insurers. <br>
Description <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Verify correct results appear and render in the table <br>
Pre-conditions <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; User has entered correct search parameter <br>
Test Steps <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. Navigate to browse by insurer page <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. Search by parameter (test a variety of parameter values, insurers) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Check that results are correct and results page (table) renders <br>
Expected result <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Table with correct results renders correctly <br>
Actual result <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Page scrolls correctly with results <br>
Status (Pass/Fail) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pass <br>
Notes <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; There will need to be a variety of tests to make sure the SQL code generates the correct results. There will also need to be tests checking rendering. <br>
Post-conditions <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Correct table is displayed. User is able to enter in another search, or browse to a different page. <br>

---

##### getHospitals
Description: This method will be used on the browse by hospitals page to pull up a table showing the price of procedures at a particular hospital.  The method executes a SQL query producing a table where rows are populated by procedure/insurer combinations and one column is populated by the cost.

Parameters: The method takes only one parameter, the input from the user contained in the textbox.  The input should be the name of a hospital.

Return values: The method will return the results of the SQL query using sqlite's built-in fetchall() function.  A list of tuples is returned which is then processed into an HTML table for display on the webpage.

Use case name: Browse by hospital page / getHospitals <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Verify a variety of searches by entering different hospitals. <br>
Description <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Verify correct results appear and render in the table <br>
Pre-conditions <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; User has entered correct search parameter <br>
Test Steps <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. Navigate to browse by hospital page <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. Search by parameter (test a variety of parameter values, hospitals) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Check that results are correct and results page (table) renders <br>
Expected result <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Table with correct results renders correctly <br>
Actual result <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Page scrolls correctly with results <br>
Status (Pass/Fail) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pass <br>
Notes <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; There will need to be a variety of tests to make sure the SQL code generates the correct results. There will also need to be tests checking rendering. <br>
Post-conditions <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Correct table is displayed. User is able to enter in another search, or browse to a different page. <br>

---

##### signup
Description: This method will be used to test the sign up page.  





<br>
<br>
<br>
<br>
---
---
---
Search Bar Table:

This table is generated dynamically after searching by procedure name or test code in the main search bar.

A slight variation on this table will be generated within the browse by procedure, browse by insurer, and browse by hospital pages, with different parameters passed to SQL.

Fields: Associated Codes-The CPT code associated with each test.
Cash-Discount Price: This is the price patients without insurance pay.
Deidentified Max Allowed: This is the hospital's maximum contracted rate with a health insurer.
Deidentified Min Allowed: This is the hospital's minimum contracted rate with a health insurer.
Description: Short text description of procedure.
Gross Charge: This is the sticker price for a procedure.  Insurer's and self-pay patients always pay less than this amount.
iob Selection: Inpatient or Outpatient procedure
Payer: Insurance Company
Payer Allowed Amount: This is the amount the insurer has negotiated with the hospital.

Tests:

Main Page Search Bar Test
    Verify a variety of searches by different test codes and procedure names.   
Description
    Verify correct results appear and render in the table
Pre-Conditions
    User has entered correct search parameter
Test Steps
    1. Navigate to welcome/home page
    2. Search by parameter (test a variety of parameter values)
    3. Check that results are correct and results page (table) renders
Expected Result
    Table with correct results renders correctly
Actual Result
    Page scrolls correctly with results
Notes
    There will need to be a variety of tests, for both parameter types and values, to make sure the SQL code generates the correct results. There will also need to be tests checking rendering.
Post Conditions
    Correct table is displayed. User is able to enter in another search, or browse to a different page.
    
Main Search Bar Access Methods
User search by procedure name or test code
Parameters are the procedure name or test code passed to the SQL database to return results.
Return value will be a table with all results that match the search parameter and value.
There will be multiple tests for each search parameter type consisting of multiple values for each type. It is unclear if it is best to create formal python tests matching specific SQL values, to test a variety of searches manually, or do a mix of both.


Browse by Tables:
 
These tables are generated dynamically using the same database as the main search bar. In each of specific pages, the user can browse by insurer, hospital, or procedure.
In each page, the user can either ###.... search by a specific parameter???...browse a menu with all results...???###

User Login:
