from re import I
import re
import tkinter
import tkinter as tk
from tkinter import *
from types import new_class
import mysql.connector as sql
from tkinter import ttk

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


def read():
    cnx , cursor = connection()
    query = "SELECT * FROM persons"
    cursor.execute(query)
    persons = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return persons


def Checklist():
    persons = read()

    tree.delete(*tree.get_children())
    for person in persons:
        tree.insert('', tk.END, values=person)


def item_selected(event):
    global record , Update_First_name, Update_Last_name, Update_code_meli, Update_Age
    item = tree.item(tree.selection()[0])
    record = item['values']

    top = Toplevel(root)
    First_name_Label = Label(top,text="First Name : ", font=("Averia",15)).grid(row=0,column=0)
    Update_First_name = tk.StringVar()
    tk.Entry(top, textvariable=Update_First_name , font=("Averia",15)).grid(row=0 , column=1)
    Update_First_name.set(record[1])

    Last_name_Label =Label(top,text="Last Name : ", font=("Averia",15)).grid(row=1,column=0)
    Update_Last_name = tk.StringVar()
    tk.Entry(top, textvariable=Update_Last_name , font=("Averia",15)).grid(row=1 , column=1)
    Update_Last_name.set(record[2])

    Code_Meli_Lable =Label(top,text="Meli Code : ", font=("Averia",15)).grid(row=2,column=0)
    Update_code_meli = tk.StringVar()
    tk.Entry(top, textvariable=Update_code_meli , font=("Averia",15)).grid(row=2 , column=1)
    Update_code_meli.set(record[3])

    Age_Label =Label(top,text="Age : ", font=("Averia",15)).grid(row=3,column=0)
    Update_Age = tk.StringVar()
    tk.Entry(top, textvariable=Update_Age, font=("Averia",15)).grid(row=3 , column=1)
    Update_Age.set(record[4])

    tk.Button(top, text ="Update", command=update).grid(row = 4,column = 0)
    tk.Button(top, text ="Delete", command=lambda x=record[0] : delete(x)).grid(row = 5,column = 0)
    tk.Button(top, text ="Cancel", command=top.destroy).grid(row=6,column=0)


def update():
    id = record[0]
    first_name = Update_First_name.get()
    last_name = Update_Last_name.get()
    code_meli = Update_code_meli.get()
    age = Update_Age.get()
    cnx , cursor = connection()
    query = f"UPDATE persons SET first_name='{first_name}', last_name='{last_name}', code_meli='{code_meli}', age={age} WHERE id={id}"
    cursor.execute(query)
    cnx.commit()
    cnx.close()


def delete(id):
    cnx , cursor = connection()
    query = f"DELETE FROM persons WHERE id={id}"
    cursor.execute(query)
    cnx.commit()
    cnx.close()

root = tk.Tk()
root.geometry('400x300')
root.title('Notebook Demo')

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

notebook.add(frame1, text='Register')
notebook.add(frame2, text='List')

First_name_Label =Label(frame1,text="First Name : ", font=("Averia",15)).grid(row=0,column=0)
First_name_entry=Entry(frame1)
First_name_entry.grid(row=0,column=1)

Last_name_Label =Label(frame1,text="Last Name : ", font=("Averia",15)).grid(row=1,column=0)
Last_name_entry=Entry(frame1)
Last_name_entry.grid(row=1,column=1)

code_meli_Label =Label(frame1,text="Meli Code : ", font=("Averia",15)).grid(row=2,column=0)
code_meli_entry=Entry(frame1)
code_meli_entry.grid(row=2,column=1)

Age_Label =Label(frame1,text="Age : ", font=("Averia",15)).grid(row=3,column=0)
Age_entry=Entry(frame1)
Age_entry.grid(row=3,column=1)

def submitFunction() :
    insert(first_name=First_name_entry.get(), last_name=Last_name_entry.get(), code_meli=code_meli_entry.get(), age=Age_entry.get())

button_submit = tkinter.Button(frame1, text ="Submit", font="Constantia", bg="black",fg='white', command=submitFunction).grid(row=4,column=0)
 
button_submit = tkinter.Button(frame2, text ="Check List", font="Constantia", bg="black",fg='white', command=Checklist).grid(row=0,column=0)

# columns
columns = ('#1','#2', '#3', '#4', '#5')

tree = ttk.Treeview(frame2, columns=columns, show='headings')
tree.heading('#1', text='ID')
tree.heading('#2', text='First Name')
tree.heading('#3', text='Last Name')
tree.heading('#4', text='Meli Code')
tree.heading('#5', text='Age')
tree.bind('<<TreeviewSelect>>', item_selected)
tree.grid(row=1, column=0, sticky='nsew')


root.mainloop()