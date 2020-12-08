# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:27:06 2020

@author: mani
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="Tripuupdb"
)

print(mydb)
'''mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
mycursor = mydb.cursor()

mycursor.execute("create database Tripuupdb")'''