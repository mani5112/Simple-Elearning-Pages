from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Mobile Number:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)


entry_3 = Entry(root)
entry_3.place(x=240,y=280)


label_pass=Label(root, text="Password", width=20,font=("bold", 10))
label_pass.place(x=70,y=330)

entry_pass=Entry(root)
entry_pass.place(x=240,y=338)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=lambda: add_data()).place(x=180,y=390)
# it is use for display the registration form on the window

def add_data():
    flag_validation=True
    name=entry_1.get()
    email=entry_2.get()
    gender=var.get()
    Mobi_num=entry_3.get()
    password=entry_pass.get()
    try:
        from sqlalchemy.exc import SQLAlchemyError
        import mysql.connector
        mydb = mysql.connector.connect(
                   host="localhost",  user="root",  password="root",  database="Tripuupdb")
        mycursor = mydb.cursor()
        query="INSERT INTO  `registration` (`name` ,`email`,`gender`,`Mobile_Number`,`password`) \
            VALUES(%s,%s,%s,%s,%s)"
        my_data=(name,email,gender,Mobi_num,password)
        mycursor.execute(query, my_data)
        mydb.commit()
    except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            
        



root.mainloop()
print("registration form  seccussfully created...")
print(entry_1.get())
