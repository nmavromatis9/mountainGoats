from flask import Flask, request, render_template
from markupsafe import escape
import os, sys, string
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


#Script by: Nicolas Mavromatis, nima6629 
#Flask script
#To access webpages:
#https://coding.CSEL.io/user/nima6629/proxy/5000
#flask --app routes run

#Sources:https://flask-wtf.readthedocs.io/en/0.15.x/quickstart/
#https://hackersandslackers.com/flask-wtforms-forms/
#https://wtforms.readthedocs.io/en/2.3.x/fields/

app = Flask(__name__)
################################################################


@app.route("/",methods =['POST','GET'])
def index():
    #Call function that uses Flask-WTF’s class FlaskForm
    form = MyForm()
    #pass this as parameter to render html, which accesses param as 'var'
    return render_template("index.html", var=form)


@app.route('/results', methods=['GET', 'POST'])
def results():
    form=MyForm()
    if request.method=="POST":
        search=form.name.data
        res=getSQL(search)
        if(len(res)==0):
            return "No results found for search: "+str(search)
        return render_template("table.html", res=res)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return 'Hello, World'

#function to access db by procedure name/cpt code, and generate SQL results
def getSQL(searchTerm):

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

###############################################################################
## This section allows us to set the prefix information to access
## url's that access our JupyterHub environment.
##
## Every call to url_for will be given the prefix for accessing via PROXY.
## Before releasing this to an external site or use in your local machine,
## make the 'SCRIPT_NAME' an empty string.
##

class PrefixMiddleware(object):

   def __init__(self, app, prefix=''):
       self.app = app
       self.prefix = prefix

   def __call__(self, environ, start_response):
       # set the prefix for all url to the Jupyterhub URL for my virtual machine
       # this path is set to my user [nima6629] and port [3308]
       # (see the code at bottom to see how port is set to 3308 instead of 5000)
       environ[''] = "/user/nima6629/proxy/5000/"

       # call the default processing
       return self.app(environ, start_response)

# insert our proxy setting url class as wrapper to the app
app.wsgi_app = PrefixMiddleware(app.wsgi_app)

# Flask-WTF requires an encryption key - the string can be anything
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

#Next, we configure a form that inherits from Flask-WTF’s class FlaskForm.
#StringField() and SubmitField() inherit form wtforms to fill forms easily
#this passes MyFormObj.name to html template
class MyForm(FlaskForm):
    #MyformObj.name() is the user input, label is what is displayed to human
    #StringField is one line
    #Make sure data is entered (validator)  
    
    #This field is the base for most of the more complicated fields, and represents an <input type="text">.
    name = StringField('Enter CPT Code or Description:', validators=[DataRequired()])
    #Represents an <input type="submit">. This allows checking if a given submit button has been pressed.
    submit = SubmitField()