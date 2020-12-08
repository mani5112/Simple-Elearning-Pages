# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:32:03 2020

@author: mani
"""


import tkinter as tk 
import mysql.connector  
from tkinter import * 
import PIL 
from tkinter.messagebox import showinfo,showerror
   
  
def submitact(): 
      
    user = Username.get() 
    passw = password.get() 
   
    print(f"The name entered by you is {user} {passw}") 
   
    logintodb(user, passw) 
   
   
def logintodb(user, passw):
    
    mydb = mysql.connector.connect(
                   host="localhost",  user="root",  password="root",  database="Tripuupdb")
    mycursor = mydb.cursor()
    savequery='select * from registration where email= %s and password= %s'
    mycursor.execute(savequery,(user,passw))
    if mycursor.fetchall():
        showinfo(title="success", message="Welcome {user}")
    else:
        showerror(title="warning", message="incorrect username or password")
    mycursor.close();
    
     
   
   
root = tk.Tk() 
root.geometry("500x500") 
root.title("Login Page") 



label_0 = Label(root, text="Login",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="UserName/Email",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

Username = Entry(root)
Username.place(x=240,y=130)

label_2 = Label(root, text="Password",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

password = Entry(root)
password.place(x=240,y=180)


  
submitbtn = tk.Button(root, text ="Login",  
                      bg ='blue', command = submitact) 
submitbtn.place(x = 225, y = 225, width = 55) 
  
root.mainloop() 
