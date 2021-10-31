import tkinter
import tkinter as tk
from tkinter import *
import mysql.connector as sql
from tkinter import ttk
from PIL import ImageTk,Image
from mysql.connector import cursor

class Database:
    def __init__(self, u, p, h, d):
        self.username: u
        self.password: p
        self.host: h
        self.database: d
        self.connection()
def connection(self):
    self.cnx = sql.connect(
        user = self.username,
        password = self.password,
        host = self.host,
        database = self.databse
    )
    self.cursor = self.cnx.cursor()

class Passenger(Database):

    def __init__(self, u, p, h, d):
        super().__init__(u, p, h, d)


    def insert(self, f, l, p, n, g):
        query = f"""
        INSERT INTO passenger_profile
        (first_name, last_name, phone, nationality, gender)
        VALUES
        ('{f}', '{l}', '{p}', '{n}', '{g}')"""
        self.curos.execute(query)
        self.cnx.commit()

def Update(self ,f ,l ,p ,n ,g ,p_id ):
    query = f""""
    UPDATE passenger_profile
    SET first_name='{f}', last_name='{l}', phone='{p}', nationality='{n}', gender='{g}', passeneger_id='{p_id}'
    WHERE passenger_id = {p_id}"""
    self.cursor.execute(query)
    self.cnx.commit()

def DQL(self, p_id=NONE):
    if p_id is None:
        query = f"SELECT * FROM passenger_profile"
    else:
        query = f"SELECT * FROM passenger_profile WHERE passenger_id={p_id}" 
    self.curosr.execute(query)
    return self.cursor.fetchball()

passenger = Passenger('root', 'shahrad.f.99', 'localhost', 'airline_system')





def item_selected(event):
    global record , Update_first_name, Update_last_name, Update_code_meli, Update_destination, Update_ticket_number
    item = tree.item(tree.selection()[0])
    record = item['values']

    top = Toplevel(root)
    first_name_Label = Label(top,text="First Name : ", font=("Averia",15)).grid(row=0,column=0)
    Update_first_name = tk.StringVar()
    tk.Entry(top, textvariable=Update_first_name , font=("Averia",15)).grid(row=0 , column=1)
    Update_first_name.set(record[1])

    last_name_Label =Label(top,text="Last Name : ", font=("Averia",15)).grid(row=1,column=0)
    Update_last_name = tk.StringVar()
    tk.Entry(top, textvariable=Update_last_name , font=("Averia",15)).grid(row=1 , column=1)
    Update_last_name.set(record[2])

    code_Meli_Lable =Label(top,text="Meli Code : ", font=("Averia",15)).grid(row=2,column=0)
    Update_code_meli = tk.StringVar()
    tk.Entry(top, textvariable=Update_code_meli , font=("Averia",15)).grid(row=2 , column=1)
    Update_code_meli.set(record[3])

    destination_Label =Label(top,text="Destination : ", font=("Averia",15)).grid(row=3,column=0)
    Update_destination = tk.StringVar()
    tk.Entry(top, textvariable=Update_destination, font=("Averia",15)).grid(row=3 , column=1)
    Update_destination.set(record[4])

    ticket_number_Label =Label(top,text="Ticket Number : ", font=("Averia",15)).grid(row=3,column=0)
    Update_ticket_number = tk.StringVar()
    tk.Entry(top, textvariable=Update_ticket_number, font=("Averia",15)).grid(row=3 , column=1)
    Update_ticket_number.set(record[5])

    tk.Button(top, text ="Update", command=update).grid(row = 4,column = 0)
    tk.Button(top, text ="Delete", command=lambda x=record[0] : delete(x)).grid(row = 5,column = 0)
    tk.Button(top, text ="Cancel", command=top.destroy).grid(row=6,column=0)


def update():
    id = record[0]
    first_name = Update_first_name.get()
    last_name = Update_last_name.get()
    code_meli = Update_code_meli.get()
    destination = Update_destination.get()
    ticket_number = Update_ticket_number.get()

    cnx , cursor = connection()
    query = f"UPDATE persons SET first_name='{first_name}', last_name='{last_name}', code_meli='{code_meli}', destination={destination}, ticket_number={ticket_number} WHERE id={id}"
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
root.title('Airline')

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

notebook.add(frame1, text='Register')
notebook.add(frame2, text='List')

first_name_Label =Label(frame1,text="First Name : ", font=("Averia",15)).grid(row=0,column=0)
first_name_entry=Entry(frame1)
first_name_entry.grid(row=0,column=1)

last_name_Label =Label(frame1,text="Last Name : ", font=("Averia",15)).grid(row=1,column=0)
last_name_entry=Entry(frame1)
last_name_entry.grid(row=1,column=1)

code_meli_Label =Label(frame1,text="Meli Code : ", font=("Averia",15)).grid(row=2,column=0)
code_meli_entry=Entry(frame1)
code_meli_entry.grid(row=2,column=1)

destination_Label =Label(frame1,text="Destination : ", font=("Averia",15)).grid(row=3,column=0)
destination_entry=Entry(frame1)
destination_entry.grid(row=3,column=1)

ticket_number_Label =Label(frame1,text="Ticket Number : ", font=("Averia",15)).grid(row=4,column=0)
ticket_number_entry=Entry(frame1)
ticket_number_entry.grid(row=4,column=1)

def submitFunction() :
    insert(first_name=first_name_entry.get(), last_name=last_name_entry.get(), code_meli=code_meli_entry.get(), destination=destination_entry.get(), ticket_number=ticket_number_entry.get())

button_submit = tkinter.Button(frame1, text ="Submit", font="Constantia", bg="black",fg='white', command=submitFunction).grid(row=5,column=0)
 
button_submit = tkinter.Button(frame2, text ="Check List", font="Constantia", bg="black",fg='white', command=Checklist).grid(row=0,column=0)

# columns
columns = ('#1','#2', '#3', '#4', '#5', '#6')

tree = ttk.Treeview(frame2, columns=columns, show='headings')
tree.heading('#1', text='ID')
tree.heading('#2', text='First Name')
tree.heading('#3', text='Last Name')
tree.heading('#4', text='Meli Code')
tree.heading('#5', text='Destination')
tree.heading('#6', text='Ticket Number')
tree.bind('<<TreeviewSelect>>', item_selected)
tree.grid(row=1, column=0, sticky='nsew')

root.mainloop()