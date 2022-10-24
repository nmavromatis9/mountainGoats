#!/usr/bin/python3
#Script by Nicolas Mavromatis, nima6629
#source:https://stackoverflow.com/questions/14949833/searching-sqlite-database-with-python-variables

#Script to access db by procedure name/cpt code, and generate SQL results
import pandas as pd
import os, sys, string
import sqlalchemy
from sqlalchemy import *
import sqlite3

print("Testing...")


try:
    con = sqlite3.connect("../DB_Setup/hospital.db")
except:
    print("ERROR CONNECTING TO DB")
    
cur = con.cursor()


testVar1="10160"

#print(cur.execute("PRAGMA table_info('tblCPT')"))
r=cur.execute("SELECT c.name FROM pragma_table_info('tblCPT') c;")
print(r.fetchall())

#cur.execute("SELECT * FROM list WHERE InstitutionName=?", (Variable,))

#r1=cur.execute("SELECT * FROM tblCPT WHERE (CPT_CODE=?)", (testVar1,))
#print(r1.fetchall())

#SELECT * FROM users WHERE column LIKE '%mystring%'

testString="puncture"
#check variable substring, from stackoverflow. ||var|| needed to insert variable...
#r2=cur.execute("SELECT * FROM tblCPT WHERE (DESCRIPTION LIKE '%'||?||'%')", (testString,))
#print(r2.fetchall())

r3=cur.execute("SELECT * FROM tblCPT WHERE (CPT_CODE=?) OR (DESCRIPTION LIKE '%'||?||'%')", (testVar1, testString))
print(r3.fetchall())


