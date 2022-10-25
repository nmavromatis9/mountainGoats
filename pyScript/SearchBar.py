#!/usr/bin/python3
#Script by Nicolas Mavromatis, nima6629
#source:https://stackoverflow.com/questions/14949833/searching-sqlite-database-with-python-variables

#Script to access db by procedure name/cpt code, and generate SQL results
import pandas as pd
import os, sys, string
import sqlalchemy
from sqlalchemy import *
import sqlite3
import csv

print("Testing...")


try:
    con = sqlite3.connect("../DB_Setup/hospital.db")
except:
    print("ERROR CONNECTING TO DB")
    
    cur = con.cursor()



testVar1="10160"
testString="puncture"
#check variable substring, from stackoverflow. ||var|| needed to insert variable. || is the concatenation operator.
#r2=cur.execute("SELECT * FROM tblCPT WHERE (DESCRIPTION LIKE '%'||?||'%')", (testString,))

r3=cur.execute("SELECT c.CPT_CODE, c.Description, c.Category, t.Hospital_name, i.Name, h.Cost, h.Gross_charge, h.Cash_discount FROM tblCPT c, tblHospitalPrices h, tblInsurer i, tblHospitals t  WHERE ((c.CPT_CODE=?) OR (c.DESCRIPTION LIKE '%'||?||'%')) AND (c.CPT_CODE==h.CPT_CODE) AND (h.Hospital_ID==t.Hospital_ID) AND (h.InsurerID==i.Insurer_ID) ", (testVar1, testVar1))
results=r3.fetchall()
#print(results)
#print(len(results))

#CSV writer for debug...
#csvWriter = csv.writer(open("output.csv", "w"))
#csvWriter.writerows(results)


