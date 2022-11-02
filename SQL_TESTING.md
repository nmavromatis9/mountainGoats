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

|   Table           |   Field       |   Data Type    |   Description                                          |   Key                     |
|-------------------|---------------|----------------|--------------------------------------------------------|---------------------------|
| tblHospitalPrices | T             | Int            | Primary Key of Hospital Prices Table                   | Primary                   |
| tblHospitalPrices | CPT_code      | Int            | Code of specific Procedure or Service                  | Foreign from tblCPT_Codes |
| tblHospitalPrices | Hospital_ID   | Int            | Unique Identifier of Hospital                          | Foreign from tblHospitals |
| tblHospitalPrices | Insurer_ID    | Int            | Unique Identifier of Insurance Plan                    | Foreign from tblInsurer   |
| tblHospitalPrices | Cost          | Money          | Insurer's Negotiated Rate for Procedure or Service     |                           |
| tblHospitalPrices | Gross_charge  | Money          | Hospital's Undiscounted Sticker Price                  |                           |
| tblHospitalPrices | Cash_discount | Decimal        | Discount for Cash Payment Method                       |                           |

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

Tests to verify: To verify the table is loaded properly we plan to perform the SQL query, `SELECT * FROM users;`.  This step will be performed after we have used the website to sign up some "dummy" users.

---

#### List of Data Access Methods
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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Check that results are correct and results page (table) renders.  Plan on creating unit tests.  <br>
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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Check that results are correct and results page (table) renders. Plan on creating unit tests. <br>
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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Check that results are correct and results page (table) renders. Plan on creating unit tests. <br>
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
Description: This method will be used to test the sign up page.  The user should be able to enter an email or username, and a password.  This information should be added to the login database if it does not already exist.

Parameters: Takes two parameters: a username or email address and a password.

Return values: If username does not already exist in login database, open up user_added.html page with message welcoming the user.  If username already exists in the login database, the message "User Already Exists! Try Again" should be displayed.

Use case name: SignUp page <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Verify that users are able to successfully sign up and that users who already exist are not allowed to sign up again. <br>
Description <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Test of the signup.html page. <br>
Pre-conditions <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Two cases: (1) User does not already exist, enter new username and password or (2) User already exists, enter known username and password <br>
Test Steps <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Case: User does not already exist <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. Navigate to the SignUp page <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. Enter new username and password <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Check that user_added.html renders with welcome message and new user added to user table in login.db <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Case: User already exists <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. Navigate to the SignUp page <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. Enter known username and password <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Check that "User Already Exists! Try Again" renders and user table in login.db does not change <br>
Expected result <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For successful sign up, user_added.html renders with welcome message and new user is added to the database.  For an unsuccessful sign up, "User Already Exists! Try Again" renders and databse does not change. <br>
Actual result <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; New user is able to sign up, existing user is prevented from re-signing up. <br>
Status (Pass/Fail) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pass <br>
Notes <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Will need to test multiple users, some using email addresses others using usernames. <br>
Post-conditions <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; New users are validated in login.db.  Existing users are prevented from signing up and login.db does not change. <br>

---

##### login
Description: This method will be used to test the login page.  The user should be able to enter an email or username, and a password.  This information should be checked against the login.db database.  If a valid username and password is entered, logged_in.html should be rendered.  If an invalid username or password is entered, bad_login.html should be rendered.

Parameters: Takes two parameters: a username/email address and a password.

Return values: Should render either logged_in.html for valid username and password, and render bad_login for invalid username or password.

Use case name: Login page <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Verify that users are able to successfully login with valid credentials and that users with invalid credentials are not. <br>
Description <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Test of the login.html page. <br>
Pre-conditions <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Two cases: (1) User has valid credentials or (2) User has invalid credentials <br>
Test Steps <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Case: User has valid credentials <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. Navigate to the Login page <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. Enter valid username/email and password <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Check that logged_in.html renders with welcome message. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Case: User already exists <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. Navigate to the Login page <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. Enter invalid username/email and password <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Check that bad_login.html renders <br>
Expected result <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For successful log in, logged_in.html renders with welcome message.  For an unsuccessful log in, bad_login.html renders. <br>
Actual result <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Users with valid credentials are able to log in. Users with invalid credentials are not able to log in. <br>
Status (Pass/Fail) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pass <br>
Notes <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Will need to test multiple users, some with valid usernames but invalid passwords and vice versa. <br>
Post-conditions <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Users with valid credentials are able to login.  Users with invalid credentials are not allowed to log in. <br>

---

##### logout

Description: This method will be used to test the logout page.  The user should be able to click the Logout link in the navigation bar and be directed to logged_out.html. 

Parameters: No parameters

Return values: Should render logged_out.html

Use case name: Logout page <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Verify that users are directed to logged_out.html <br>
Description <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Test of the logged_out.html page. <br>
Pre-conditions <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; User is logged in <br>
Test Steps <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. Log in a valid user and navigate to any page with navigation bar <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. Click the Logout link <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Check that logged_out.html renders <br>
Expected result <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The logged_out.html page renders <br>
Actual result <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The page successfully renders indicating the user has been logged out. <br>
Status (Pass/Fail) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pass <br>
Notes <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Will need to test navigation bar on multiple webpages. <br>
Post-conditions <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; User is successfully logged out. <br>


