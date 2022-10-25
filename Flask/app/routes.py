from flask import Flask, request, render_template
from markupsafe import escape
import os, sys, string
import sqlite3


#Script by: Nicolas Mavromatis, nima6629 
#Flask script
#To access webpages:
#https://coding.CSEL.io/user/nima6629/proxy/5000
app = Flask(__name__)
################################################################
#Required Routes

@app.route('/')
def index():
    return 'Index Page'

@app.route('/results')
def results():
    results=getSQL()
    return render_template("table.html", res=results)


@app.route('/hello')
def hello():
    return 'Hello, World'

#function to access db by procedure name/cpt code, and generate SQL results
def getSQL():

    print("Testing...")
    try:
        con = sqlite3.connect("../../DB_Setup/hospital.db")
    except:
        print("ERROR CONNECTING TO DB")
    
    cur = con.cursor()
    testVar1="10160"
    r3=cur.execute("SELECT c.CPT_CODE, c.Description, c.Category, t.Hospital_name, i.Name, h.Cost, h.Gross_charge, h.Cash_discount FROM tblCPT c, tblHospitalPrices h, tblInsurer i, tblHospitals t  WHERE ((c.CPT_CODE=?) OR (c.DESCRIPTION LIKE '%'||?||'%')) AND (c.CPT_CODE==h.CPT_CODE) AND (h.Hospital_ID==t.Hospital_ID) AND (h.InsurerID==i.Insurer_ID) ", (testVar1, testVar1))
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
