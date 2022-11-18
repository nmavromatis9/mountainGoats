from flask import Flask
from flask import *
from markupsafe import escape
import os, sys, string
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import flask_login

# The following are used for the admin page
from flask import render_template, request, jsonify, make_response

## Import "prefix" code into your Flask app to make your app usable when running
## Flask either in the csel.io virtual machine or running on your local machine.
import prefix

#READ ME:*************************************************************

#Search bar, Login, Signup, Browse by page generation and basic Flask Script by: Nicolas Mavromatis, nima6629 

#Flask script
#To access webpages:
#https://coding.CSEL.io/user/nima6629/proxy/5000
#flask --app routes run

#Sources:https://flask-wtf.readthedocs.io/en/0.15.x/quickstart/
#https://hackersandslackers.com/flask-wtforms-forms/
#https://wtforms.readthedocs.io/en/2.3.x/fields/
#https://pypi.org/project/Flask-Login/

app = Flask(__name__)

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
prefix.use_PrefixMiddleware(app) 

# test route to show prefix settings
@app.route('/prefix_url')
def prefix_url():
    return 'The URL for this page is {}'.format(url_for('prefix_url'))


app.secret_key = 'super secret string'  # Change this!
login_manager = flask_login.LoginManager()

login_manager.init_app(app)
################################################################
#ROUTES:

@app.route("/",methods =['POST','GET'])
def index():
    #Call function that uses Flask-WTF’s class FlaskForm
    form = MyForm()
    #pass this as parameter to render html, which accesses param as 'var'
    # return render_template("index.html", var=form)
    return render_template("index.html", var=form, path=url_for('index'))

@app.route('/results', methods=['GET', 'POST'])
def CPTresults():
    form=MyForm()
    if request.method=="POST":
        search=form.name.data
        res=getCPT(search)
        if(len(res)==0):
            return "No results found for search: "+str(search)
        return render_template("table.html", res=res);
  
@app.route('/insurer-results', methods=['GET', 'POST'])
def Insurer_results():
    form=MyForm2()
    if request.method=="POST":
        search=form.name.data
        res=getInsurers(search)
        if(len(res)==0):
            return "No results found for search: "+str(search)
        return render_template("table.html", res=res);
    
@app.route('/hospital-results', methods=['GET', 'POST'])
def Hospital_results():
    form=MyForm3()
    if request.method=="POST":
        search=form.name.data
        res=getHospitals(search)
        if(len(res)==0):
            return "No results found for search: "+str(search)
        return render_template("table.html", res=res);
        

@app.route('/logins', methods=['GET', 'POST'])
def login():
    try:
        con = sqlite3.connect("../../DB_Setup/login.db")
        cur=con.cursor()
    except:
        print("BAD CONNECTION")
    if request.method == 'GET':
        return render_template("login.html", path=url_for('index'))
    
    name = request.form['email']
    passwo=request.form['password']

    cur.execute("SELECT email from users WHERE (email=? AND password=?)", (name, passwo))
    if cur.fetchone(): 
        user = User()
        user.id = name
        flask_login.login_user(user)
        # return redirect('https://coding.csel.io/user/nima6629/proxy/5000/protected')
        return redirect(url_for('protected'))
        
    return render_template("bad_login.html", path=url_for('index'))

@app.route('/protected')
@flask_login.login_required
def protected():
    print(flask_login.current_user.id)
    return render_template("logged_in.html", usr=flask_login.current_user.id, path=url_for('index'))

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return render_template("logged_out.html", path=url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html", path=url_for('index'))
    
    name = request.form['signupE']
    passwo=request.form['signupP']
    #if email in users and request.form['password'] == users[email]['password']:
    try:
        con = sqlite3.connect("../../DB_Setup/login.db")
        cur=con.cursor()
    except:
        print("BAD CONNECTION")
        
    cur.execute("SELECT email from users WHERE (email=?)", (name,))
    if cur.fetchone(): 
        return "User Already Exists! Try Again"
    else:
        addUser(name, passwo)
         
        return render_template("user_added.html", usr=name, path=url_for('index'))


@app.route('/browseInsurers/<insurer>', methods=['GET', 'POST'])
def browseIns(insurer):
    res=getInsurers(insurer)
    return render_template("table2.html", res=res)

@app.route('/browseHospitals/<hospital>', methods=['GET', 'POST'])
def browseHosp(hospital):
    res=getHospitals(hospital)
    return render_template("table2.html", res=res)
#Routes to generate browse by pages

@app.route('/browseCPT/<CPT>', methods=['GET', 'POST'])
def browseCPT(CPT):
    res=getCPT(CPT)
    return render_template("table2.html", res=res)
#Routes to generate browse by pages

@app.route("/browse-insurer",methods =['POST','GET'])
def browse_insurer():
    #Call function that uses Flask-WTF’s class FlaskForm
    form = MyForm2()
    #Generate dynamic links
    #Get all insurers from SQL call, then...
    res=getAllInsurers()
    paths=[]
    names=[]
    #first, convert tuple to string, then take slice,
    #then create links
    for i in res:
        i=str(i)
        i=i[2:len(i)-3]
        names.append(i)
        paths.append((url_for('browseIns', insurer=str(i))))
        
    #pass these parameters to render template.
    #p is path length for <a> links, n is names variable
    return render_template("browse_insurer.html", var=form, p=paths, n=names, path=url_for('index'))

@app.route("/browse-hospital",methods =['POST','GET'])
def browse_hospital():
    #Call function that uses Flask-WTF’s class FlaskForm
    form = MyForm3()
    #get all hospitals to generate links dynamically
    res=getAllHospitals()
    paths=[]
    names=[]
    #first, convert tuple to string, then take slice,
    #then create links
    for i in res:
        i=str(i)
        i=i[2:len(i)-3]
        names.append(i)
        paths.append((url_for('browseHosp', hospital=str(i))))
    #pass this as parameter to render html, which accesses param as 'var'
    return render_template("browse_hospital.html", var=form, p=paths, n=names, path=url_for('index'))

@app.route("/browse-procedure",methods =['POST','GET'])
def browse_procedure():
    #Call function that uses Flask-WTF’s class FlaskForm
    form = MyForm()
    res=getAllCPT()
    paths=[]
    names=[]
    #first, convert tuple to string, then take slice,
    #then create links
    #Must match description to code for names.
    try:
        con = sqlite3.connect("../../DB_Setup/hospital.db")
    except:
        print("ERROR CONNECTING TO DB")
    cur = con.cursor()
    for i in res:
        i=str(i)
        i=i[1:len(i)-2]
        r3=cur.execute("SELECT DISTINCT c.CPT_CODE, c.Description FROM tblCPT c, tblHospitalPrices h, tblInsurer i, tblHospitals t WHERE ((c.CPT_CODE=?) AND (c.CPT_CODE==h.CPT_CODE) AND (h.Hospital_ID==t.Hospital_ID) AND (h.InsurerID==i.Insurer_ID) AND (h.cost IS NOT NULL OR h.Gross_Charge IS NOT NULL OR h.Cash_discount IS NOT NULL))", (i,))
        names.append(r3.fetchone())
        paths.append((url_for('browseCPT', CPT=str(i))))
    #pass this as parameter to render html, which accesses param as 'var'
    return render_template("browse_procedure.html", var=form, p=paths, n=names, path=url_for('index'))

@app.route("/account",methods =['POST','GET'])
def user_account():
    #Call function that uses Flask-WTF’s class FlaskForm
    form = MyForm()
    #pass this as parameter to render html, which accesses param as 'var'
    return render_template("user_account.html", var=form, path=url_for('index'))



################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################

@app.route("/admin")
def admin():
    return render_template("change_price.html")

@app.route("/search", methods=["POST"])
def search():
    # req will take in the post from admin.html, get_json() will parse the request
    # to a python dictionary
    req = request.get_json()
    print(req)
    
    # SQL query to get the price
    # extract values from dictionary
    hospital = req["hospital"]
    insurer = req["insurer"]
    procedure = req["procedure"]

    # connect to database
    try:
        con = sqlite3.connect("../../DB_Setup/hospital.db")
    except:
        print("ERROR CONNECTING TO DB")
    
    # query the database for procedures
    cur = con.cursor()
    query = cur.execute("SELECT Description from tblCPT WHERE Description LIKE ? ", ('%'+procedure+'%',))
    procedures=query.fetchall()
    #print(procedures)
    con.close()
    
    # Response with procedures in JSON form, status code 200
    res = make_response(jsonify({"procedures" : procedures}), 200)
    # res will be sent back to admin.html as json object
    return res


@app.route("/get_price", methods=["POST"])
def get_price():
    # req will take in the post from admin.html, get_json() will parse the request
    # to a python dictionary
    req = request.get_json()
    print(req)
    
    # SQL query to get the price
    # extract values from dictionary
    hospital = req["hospital"]
    insurer = req["insurer"]
    procedure = req["procedure"]
    print(procedure)
    
    # connect to database
    try:
        con = sqlite3.connect("../../DB_Setup/hospital.db")
    except:
        print("ERROR CONNECTING TO DB")
    
    # query the database for price
    cur = con.cursor()
    query = cur.execute("SELECT Cost from tblHospitalPrices WHERE Hospital_ID = ( SELECT Hospital_ID FROM tblHospitals WHERE Hospital_name = ? ) AND InsurerID = ( SELECT Insurer_ID FROM tblInsurer WHERE name = ? ) AND CPT_code = ( SELECT CPT_code FROM tblCPT WHERE Description = ? ) ", (hospital, insurer, procedure))
    price=query.fetchall()
    print(price)
    con.close()
    
    # Response with price in JSON form, status code 200
    res = make_response(jsonify({"price" : price}), 200)
    # res will be sent back to admin.html as json object
    return res

@app.route("/set_price", methods=["POST"])
def set_price():
    # req will take in the post from admin.html, get_json() will parse the request
    # to a python dictionary
    req = request.get_json()
    print(req)
    
    # SQL update statement to set the new price
    # extract values from dictionary
    hospital = req["hospital"]
    insurer = req["insurer"]
    procedure = req["procedure"]
    desired_price = req["desired_price"]
    
    # connect to database
    try:
        con = sqlite3.connect("../../DB_Setup/hospital.db")
    except:
        print("ERROR CONNECTING TO DB")
    
    # stmt to update the database
    cur = con.cursor()
    stmt = cur.execute("UPDATE tblHospitalPrices SET Cost = ? WHERE Hospital_ID = ( SELECT Hospital_ID FROM tblHospitals WHERE Hospital_name = ? ) AND InsurerID = ( SELECT Insurer_ID FROM tblInsurer WHERE name = ? ) AND CPT_code = ( SELECT CPT_code FROM tblCPT WHERE Description = ? ) ", (desired_price, hospital, insurer, procedure))
    
    # query to get the updated price
    query = cur.execute("SELECT Cost from tblHospitalPrices WHERE Hospital_ID = ( SELECT Hospital_ID FROM tblHospitals WHERE Hospital_name = ? ) AND InsurerID = ( SELECT Insurer_ID FROM tblInsurer WHERE name = ? ) AND CPT_code = ( SELECT CPT_code FROM tblCPT WHERE Description = ? ) ", (hospital, insurer, procedure))

    new_price=query.fetchall()
    con.commit()
    con.close()

    # Response with price in JSON form, status code 200
    res = make_response(jsonify({"new_price" : new_price}), 200)
    # res will be sent back to admin.html as json object
    return res
    
    

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################

#FUNCTIONS:

#############################################################################

#function to access db by procedure name/cpt code, and generate SQL results
def getCPT(searchTerm):

    print("Testing...")
    try:
        con = sqlite3.connect("../../DB_Setup/hospital.db")
    except:
        print("ERROR CONNECTING TO DB")
    
    cur = con.cursor()
    r3=cur.execute("SELECT c.CPT_CODE, c.Description, c.Category, t.Hospital_name, i.Name, h.Cost, h.Gross_charge, h.Cash_discount FROM tblCPT c, tblHospitalPrices h, tblInsurer i, tblHospitals t  WHERE ((c.CPT_CODE=?) OR (c.DESCRIPTION LIKE '%'||?||'%')) AND (c.CPT_CODE==h.CPT_CODE) AND (h.Hospital_ID==t.Hospital_ID) AND (h.InsurerID==i.Insurer_ID) AND (h.cost IS NOT NULL OR h.Gross_Charge IS NOT NULL OR h.Cash_discount IS NOT NULL)", (searchTerm, searchTerm))
    results=r3.fetchall()
    con.close()
    return results

#function to access db by procedure name/cpt code, and generate SQL results
def getInsurers(searchTerm):

    print("Testing...")
    try:
        con = sqlite3.connect("../../DB_Setup/hospital.db")
    except:
        print("ERROR CONNECTING TO DB")
    
    cur = con.cursor()
    r3=cur.execute("SELECT c.CPT_CODE, c.Description, c.Category, t.Hospital_name, i.Name, h.Cost, h.Gross_charge, h.Cash_discount FROM tblCPT c, tblHospitalPrices h, tblInsurer i, tblHospitals t  WHERE ((i.name LIKE '%'||?||'%') AND (c.CPT_CODE==h.CPT_CODE) AND (h.Hospital_ID==t.Hospital_ID) AND (h.InsurerID==i.Insurer_ID) AND (h.cost IS NOT NULL OR h.Gross_Charge IS NOT NULL OR h.Cash_discount IS NOT NULL))", (searchTerm,))
    results=r3.fetchall()
    con.close()
    return results


#function to access db by procedure name/cpt code, and generate SQL results
def getHospitals(searchTerm):

    print("Testing...")
    try:
        con = sqlite3.connect("../../DB_Setup/hospital.db")
    except:
        print("ERROR CONNECTING TO DB")
    
    cur = con.cursor()
    r3=cur.execute("SELECT c.CPT_CODE, c.Description, c.Category, t.Hospital_name, i.Name, h.Cost, h.Gross_charge, h.Cash_discount FROM tblCPT c, tblHospitalPrices h, tblInsurer i, tblHospitals t  WHERE ((t.Hospital_name LIKE '%'||?||'%') AND (c.CPT_CODE==h.CPT_CODE) AND (h.Hospital_ID==t.Hospital_ID) AND (h.InsurerID==i.Insurer_ID) AND (h.cost IS NOT NULL OR h.Gross_Charge IS NOT NULL OR h.Cash_discount IS NOT NULL))", (searchTerm,))
    results=r3.fetchall()
    con.close()
    return results

#Functions to get all of a category to populate Browse By pages
def getAllInsurers():
    try:
        con = sqlite3.connect("../../DB_Setup/hospital.db")
    except:
        print("ERROR CONNECTING TO DB")
    cur = con.cursor()
    r3=cur.execute("SELECT DISTINCT i.Name FROM tblCPT c, tblHospitalPrices h, tblInsurer i, tblHospitals t  WHERE (h.InsurerID==i.Insurer_ID)")
    results=r3.fetchall()
    con.close()
    return results

def getAllHospitals():
    try:
        con = sqlite3.connect("../../DB_Setup/hospital.db")
    except:
        print("ERROR CONNECTING TO DB")
    cur = con.cursor()
    r3=cur.execute("SELECT DISTINCT t.Hospital_name FROM tblCPT c, tblHospitalPrices h, tblInsurer i, tblHospitals t  WHERE (h.Hospital_ID==t.Hospital_ID)")
    results=r3.fetchall()
    con.close()
    return results

def getAllCPT():
    try:
        con = sqlite3.connect("../../DB_Setup/hospital.db")
    except:
        print("ERROR CONNECTING TO DB")
    cur = con.cursor()
    r3=cur.execute("SELECT DISTINCT c.CPT_CODE FROM tblCPT c, tblHospitalPrices h, tblInsurer i, tblHospitals t  WHERE ( (c.CPT_CODE==h.CPT_CODE) AND (h.Hospital_ID==t.Hospital_ID) AND (h.InsurerID==i.Insurer_ID) )")
    results=r3.fetchall()
    con.close()
    return results

#Configure a form that inherits from Flask-WTF’s class FlaskForm.
#StringField() and SubmitField() inherit form wtforms to fill forms easily
#this passes MyFormObj.name to html template

#form for cpt code/procedure
class MyForm(FlaskForm):
    #MyformObj.name() is the user input, label is what is displayed to human
    #StringField is one line
    #Make sure data is entered (validator)  
    
    #This field is the base for most of the more complicated fields, and represents an <input type="text">.
    name = StringField('Enter CPT Code or Description:', validators=[DataRequired()])
    #Represents an <input type="submit">. This allows checking if a given submit button has been pressed.
    submit = SubmitField()
    
#form for insurer
class MyForm2(FlaskForm):
    #MyformObj.name() is the user input, label is what is displayed to human
    #StringField is one line
    #Make sure data is entered (validator)  
    
    #This field is the base for most of the more complicated fields, and represents an <input type="text">.
    name = StringField('Enter Insurer', validators=[DataRequired()])
    #Represents an <input type="submit">. This allows checking if a given submit button has been pressed.
    submit = SubmitField()

#form for hospital
class MyForm3(FlaskForm):
    #MyformObj.name() is the user input, label is what is displayed to human
    #StringField is one line
    #Make sure data is entered (validator)  
    
    #This field is the base for most of the more complicated fields, and represents an <input type="text">.
    name = StringField('Enter Hospital', validators=[DataRequired()])
    #Represents an <input type="submit">. This allows checking if a given submit button has been pressed.
    submit = SubmitField()
    
# Flask-WTF requires an encryption key - the string can be anything
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

################################################################################

#Functions to login. uses many inherited member vars from flask_login module

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(email2):
    con = sqlite3.connect("../../DB_Setup/login.db")
    cur = con.cursor()
    cur.execute("SELECT email from users WHERE (email=?)", (email2,))
    if not cur.fetchone():
        return

    user = User()
    user.id = email2
    return user

@login_manager.request_loader
def request_loader(request):
    name = request.form.get('email')
    con = sqlite3.connect("../../DB_Setup/login.db")
    cur = con.cursor()
    cur.execute("SELECT email from users WHERE (email=?)", (name,))
    if not cur.fetchone(): 
        return

    user = User()
    user.id = name
    return user

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401

#Function to add new user to db file
def addUser(name, passw):
    con = sqlite3.connect("../../DB_Setup/login.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users VALUES (?, ?);",(name, passw))
    con.commit()
    con.close()
        
        
        

        
#### Prefix code to correctly route URL is in prefix.py