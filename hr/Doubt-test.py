# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:37:35 2020

@author: mani
"""

from tkinter import*
from tkinter.messagebox import showinfo,showerror
root = Tk()
root.geometry('500x500')
root.title("Doubts Form")

label_0 = Label(root, text="Raise a doubt form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="roll_no",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Subject",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
'''
var = IntVar()
Radiobutton(root, text="Maths",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Physics",padx = 20, variable=var, value=2).place(x=290,y=230)'''

label_4 = Label(root, text="Enter your doubt:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)


entry_3 = Entry(root)
entry_3.place(x=240,y=280)




Doubt_Type = Menubutton(root,text= 'Doubt in which subject',font = ('Helvetica', 12))
Doubt_Type.grid() 
Doubt_Type.menu  =  Menu ( Doubt_Type, tearoff = 0 ) 
Doubt_Type['menu']  =  Doubt_Type.menu 
var=IntVar()
Doubt_Type.menu.add_checkbutton ( label ='Maths',variable=var,font = ('Helvetica', 12) ) 
Doubt_Type.menu.add_checkbutton ( label = 'Physics',variable=var, font = ('Helvetica', 12))
Doubt_Type.menu.add_checkbutton ( label ='Chemistry',variable=var,font = ('Helvetica', 12) ) 
Doubt_Type.menu.add_checkbutton ( label = 'Biology',variable=var, font = ('Helvetica', 12))
Doubt_Type.menu.add_checkbutton ( label = 'Other', variable=var,font = ('Helvetica', 12))
Doubt_Type.pack()
Doubt_Type.place(height= 30, width = 250, x= 235,y=230)







Button(root, text='Submit',width=20,bg='brown',fg='white',command=lambda: add_data()).place(x=180,y=390)
# it is use for display the registration form on the window
def add_data():
    flag_validation=True
    name=entry_1.get()
    roll_no=entry_2.get()
    doubt=entry_3.get()
    subject=var.get()
    try:
        from sqlalchemy.exc import SQLAlchemyError
        import mysql.connector
        mydb = mysql.connector.connect(
                   host="localhost",  user="root",  password="root",  database="Tripuupdb")
        mycursor = mydb.cursor()
        query="INSERT INTO  `doubts` (`name` ,`roll_no`,`doubt`,subject) \
            VALUES(%s,%s,%s,%s)"
        my_data=(name,roll_no,doubt,subject)
        mycursor.execute(query, my_data)
        mydb.commit()
        showinfo(title="success", message="Doubt Sent")
    except SQLAlchemyError as e:
            showerror(title="warning", message="Check the details")
            #error = str(e.__dict__['orig'])
            #print(error)
        



root.mainloop()
print("Doubt seccussfully Sent...")

