import tkinter
from tkinter import *
import mysql.connector as sql

def connection():
    cnx = sql.connect(
        user = 'root',
        password = 'shahrad.f.99',
        host = 'localhost',
        database = 'legends'
    )
    cursor = cnx.cursor()
    return cnx, cursor


def insert(first_name, last_name, code_meli, age=None):
    cnx , cursor = connection()

    if age is None:
        query = f"INSERT INTO persons(first_name, last_name ,code_meli)VALUES('{first_name}','{last_name}','{code_meli}')"
    else:
        query =f"INSERT INTO persons(first_name, last_name, code_meli, age)VALUES('{first_name}','{last_name}','{code_meli}', {age})"
    cursor.execute(query)
    cnx.commit()
    print('One person registered')
    cnx.close()

#Tk root
root = Tk()

root.geometry("500x500")

#Title
root.title('Registration form')

#Label
label_0 =Label(root,text="Registration form", width=20,font=("Commons",20))
label_0.place(x=90,y=40)

#First Name
First_name_Label =Label(root,text="First Name : ", width=20,font=("Alex Brush",20))
First_name_Label.place(x=8,y=120)

First_name_entry=Entry(root)
First_name_entry.place(x=240,y=130)


#Last Name
Last_name_Label =Label(root,text="Last Name : ", width=20,font=("Alex Brush",20))
Last_name_Label.place(x=8,y=170)

Last_name_entry=Entry(root)
Last_name_entry.place(x=240,y=180)

#Code Meli
code_meli_Label =Label(root,text="Meli Code : ", width=20,font=("Alex Brush",20))
code_meli_Label.place(x=8,y=220)

code_meli_entry=Entry(root)
code_meli_entry.place(x=240,y=230)

#Age
Age_Label =Label(root,text="Age : ", width=20,font=("Alex Brush",20))
Age_Label.place(x=8,y=270)

Age_entry=Entry(root)
Age_entry.place(x=240,y=280)

#Submit Button
def submitFunction() :
    insert(first_name=First_name_entry.get(), last_name=Last_name_entry.get(), code_meli=code_meli_entry.get(), age=Age_entry.get())

button_submit = tkinter.Button(root, text ="Submit", font="Constantia",width=15, bg="black",fg='white', command=submitFunction)
button_submit.place(x=180,y=380)
 

root.mainloop()