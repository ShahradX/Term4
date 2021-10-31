from tkinter.constants import INSERT, LEFT, N, W
from database_ticket import Flight , Passenger , Ticket
from tkinter import Button, Frame, Label, OptionMenu, StringVar ,Tk, Variable, Widget , ttk , Entry , IntVar
from tkinter import END , VERTICAL, NO



def book_ticket():
    t = Ticket('root', 'shahrad.f.99', 'localhost' , 'airline_ticket')
    t.insert(
        ticket_flight_id_left.get(),
        ticket_pass_id_left.get(),
        int(ticket_price_left.get()),
        ticket_seat_left.get()
    )
    ticket_flight_id_left.set(0),
    ticket_pass_id_left.set(0),
    ticket_price_left.set(0),
    ticket_seat_left.set(100)

def check_pass_id(a, b, c):
    try:
        pass_id = ticket_pass_id_left.get()
        f = Passenger('root', 'shahrad.f.99', 'localhost' , 'airline_ticket')
        if not f.DQL(p_id=pass_id):
            pass_id_entry.config(bg='white')
        else:
            pass_id_entry.config(bg='green')
            notebook_right.select(0)
            tree_passenger.selection_set(pass_id)

    except:
        ticket_pass_id_left.set('')
        pass_id_entry.config(bg='white')

def check_flight_id(a, b, c):
    try:
        flight_id = ticket_flight_id_left.get()
        f = Flight('root' , 'shahrad.f.99' , 'localhost', 'airline_ticket')
        flight = f.DQL(f_id=flight_id)
        if not flight:
            flight_id_entry.config(bg='red')
        else:
            flight_id_entry.config(bg='green')
            notebook_right.select(2)
            tree_flight.selection_set(flight_id)
            total = flight[-1]
            t = Ticket('root' , 'root' , 'localhost', 'airline_ticket')
            all = t.DQL(flight_id=flight_id)
            if not all :
                ticket_seat_left.set(1)
            else:
                last = all[-1][3]
                if last == total:
                    ticket_seat_left.set('FULL')
                else:
                    ticket_seat_left.set(last+1)
           
    except:
        ticket_flight_id_left.set('')
        flight_id_entry.config(bg='white')

def flight_treeview_update():
    tree_flight.delete(*tree_flight.get_children())
    flights = []
    f = Flight('root' , 'shahrad.f.99' , 'localhost', 'airline_ticket')
    for tu in f.DQL():
        flights.append(tu)

    for flight in flights:
        tree_flight.insert('', END, iid=flight[0], values=flight)

def ticket_treeview_update():
    tree_ticket.delete(*tree_ticket.get_children())
    tickets = []
    t = Ticket('root' , 'shahrad.f.99' , 'localhost', 'airline_ticket')
    for tu in t.DQL():
        tickets.append(tu)

    for ticket in tickets:
        tree_ticket.insert('', END, iid=ticket[0], values=ticket)

def register_flight():
    f = Flight('root' , 'shahrad.f.99' , 'localhost', 'airline_ticket')
    f.insert(
        airline_id_left.get(),
        airline_name_left.get(),
        from_left.get(),
        to_left.get(),
        deprature_time_left.get(),
        arrival_time_left.get(),
        seats_left.get()
    )
    del f
    airline_id_left.set(0),
    airline_name_left.set(''),
    from_left.set(''),
    to_left.set(''),
    deprature_time_left.set(''),
    arrival_time_left.set(''),
    seats_left.set(0)
    
    flight_treeview_update()

def passenger_treeview_update():
    tree_passenger.delete(*tree_passenger.get_children())
    passengers = []
    psg = Passenger('root' , 'shahrad.f.99' , 'localhost', 'airline_ticket')
    for tu in psg.DQL():
        passengers.append(tu)
    for passenger in passengers:
        tree_passenger.insert('', END, iid=passenger[0], values=passengers)

def register_passenger():
    tree_passenger.delete(*tree_passenger.get_children())
    psg = Passenger('root' , 'shahrad.f.99' , 'localhost', 'airline_ticket')
    psg.insert(
        first_name_left.get(),
        last_name_left.get(),
        phone_left.get(),
        nationality_left.get(),
        gender_left.get()
    )
    del psg
    first_name_left.set(''),
    last_name_left.set(''),
    phone_left.set(''),
    nationality_left.set('')
    gender_left.set('Male')
    passenger_treeview_update()

root = Tk()
left_frame = Frame()
left_frame.grid(row=0 , column=0, pady=(15, 15) , padx=(15, 0))
right_frame = Frame()
right_frame.grid(row=0 , column=1, pady=(15, 15) , padx=(15, 15))

notebook_left = ttk.Notebook(right_frame)
notebook_left.pack(expand=True)

passenger_left = ttk.Frame(notebook_left)
ticket_left = ttk.Frame(notebook_left)
flight_left = ttk.Frame(notebook_left)

passenger_left.pack(fill='both', expand=True)
ticket_left.pack(fill='both', expand=True)
flight_left.pack(fill='both', expand=True)

notebook_left.add(passenger_left, text='Passenger')
notebook_left.add(ticket_left, text='Ticket')
notebook_left.add(flight_left, text='Flight')

# PASSENGER LEFT

Label(passenger_left ,text = "First Name").grid(row = 0,column = 0)
Label(passenger_left ,text = "Last Name").grid(row = 1,column = 0)
Label(passenger_left ,text = "Phone").grid(row = 2,column = 0)
Label(passenger_left ,text = "Nationality").grid(row = 3,column = 0)
Label(passenger_left ,text = "Gender").grid(row = 4,column = 0)
first_name_left = StringVar()
Entry(passenger_left, textvariable=first_name_left).grid(row = 0,column = 1)
last_name_left = StringVar()
Entry(passenger_left, textvariable=last_name_left).grid(row = 1,column = 1)
phone_left = StringVar()
Entry(passenger_left, textvariable=phone_left).grid(row = 2,column = 1)
nationality_left = StringVar()
Entry(passenger_left, textvariable=nationality_left).grid(row = 3,column = 1)
genders = ['Male', 'Female', 'Other']
gender_left = StringVar()
gender_left.set('GB')
OptionMenu(passenger_left, gender_left , *genders).grid(row=4 , column=1)
Button(passenger_left, text="Register", command=register_passenger).grid(row=5 , column=0)

#FLIGHT LEFT

Label(flight_left ,text = "AIR ID").grid(row = 0,column = 0)
Label(flight_left ,text = "AIR Name").grid(row = 1,column = 0)
Label(flight_left ,text = "From").grid(row = 2,column = 0)
Label(flight_left ,text = "To").grid(row = 3,column = 0)
Label(flight_left ,text = "DP.Time").grid(row = 4,column = 0)
Label(flight_left ,text = "AR.Time").grid(row = 5,column = 0)
Label(flight_left ,text = "T.Seats").grid(row = 6,column = 0)
airline_id_left = IntVar()
Entry(flight_left, textvariable=airline_id_left).grid(row = 0,column = 1)
airline_name_left = StringVar()
Entry(flight_left, textvariable=airline_name_left).grid(row = 1,column = 1)
from_left = StringVar()
Entry(flight_left, textvariable=from_left).grid(row = 2,column = 1)
to_left = StringVar()
Entry(flight_left, textvariable=to_left).grid(row = 3,column = 1)
deprature_time_left = StringVar()
Entry(flight_left, textvariable=deprature_time_left).grid(row = 4,column = 1)
arrival_time_left = StringVar()
Entry(flight_left, textvariable=arrival_time_left).grid(row = 5,column = 1)
seats_left = IntVar()
Entry(flight_left, textvariable=seats_left).grid(row = 6,column = 1)
Button(flight_left, text="Register", command=register_flight).grid(row=7 , column=0)
notebook_right = ttk.Notebook(right_frame)
notebook_right.pack(expand=True)
passenger_right = ttk.Frame(notebook_right)
ticket_right = ttk.Frame(notebook_right)
flight_right = ttk.Frame(notebook_right)
passenger_right.pack(fill='both', expand=True)
ticket_right.pack(fill='both', expand=True)
flight_right.pack(fill='both', expand=True)
notebook_right.add(passenger_right, text='Passenger List')
notebook_right.add(ticket_right, text='Ticket List')
notebook_right.add(flight_right, text='Flight List')


#Ticket Left
Label(ticket_left ,text = "FLT.ID").grid(row = 0,column = 0)
Label(ticket_left ,text = "PSG.ID").grid(row = 1,column = 0)
Label(ticket_left ,text = "Seat").grid(row = 2,column = 0)
Label(ticket_left ,text = "Price").grid(row = 3,column = 0)

#Ticket
ticket_flight_id_left = IntVar()
flight_id_entry = Entry(ticket_left, textvariable=ticket_flight_id_left)
flight_id_entry.grid(row=0 , column=1)
ticket_flight_id_left.trace('w', check_flight_id)

#Pass
ticket_pass_id_left = IntVar()
pass_id_entry = Entry(ticket_left, textvariable=ticket_pass_id_left)
pass_id_entry.grid(row=1 , column=1)
ticket_pass_id_left.trace('w', check_pass_id)

#Seat
ticket_seat_left = StringVar()
ticket_seat_left.set(0)
Label(ticket_left ,textvariable=ticket_seat_left).grid(row = 2,column = 1)


#Price
ticket_price_left = IntVar()
ticket_price_left.set('100$')
price_entry = Label(ticket_left, textvariable=ticket_price_left)
price_entry.grid(row=3 , column=1)
Button(ticket_left, text="Book", command=book_ticket).grid(row=4 , column=0)




# Treeview Passengers
columns = ('#1', '#2', '#3', '#4', '#5', '#6')
tree_passenger = ttk.Treeview(passenger_right, columns=columns, show='headings')
tree_passenger.heading('#1', text='PSNG.ID')
tree_passenger.column('#1', minwidth=0 , width=70 , stretch=NO)
tree_passenger.heading('#2', text='First Name')
tree_passenger.column('#2', minwidth=0 , width=100 , stretch=NO)
tree_passenger.heading('#3', text='Last Name')
tree_passenger.column('#3', minwidth=0 , width=100 , stretch=NO)
tree_passenger.heading('#4', text='Phone')
tree_passenger.column('#4', minwidth=0 , width=120 , stretch=NO)
tree_passenger.heading('#5', text='NATI')
tree_passenger.column('#5', minwidth=0 , width=70 , stretch=NO)
tree_passenger.heading('#6', text='Gender')
tree_passenger.column('#6', minwidth=0 , width=60 , stretch=NO)
#def item_selected(event):
#for selected_item in tree_passenger.selection():
#dictionary
#item = tree_passenger.item(selected_item)
# list
#record = item['values']
#showinfo(title='Information',
#message=','.join(record))
#tree_passenger.bind('<<TreeviewSelect>>', item_selected)
tree_passenger.grid(row=0, column=0, sticky='nsew')


# Treeview Ticket
columns = ('#1', '#2', '#3', '#4', '#5', '#6')
tree_ticket = ttk.Treeview(ticket_right, columns=columns, show='headings')
tree_ticket.heading('#1', text='Ticket.ID')
tree_ticket.column('#1', minwidth=0 , width=70 , stretch=NO)
tree_ticket.heading('#2', text='FLT.ID')
tree_ticket.column('#2', minwidth=0 , width=100 , stretch=NO)
tree_ticket.heading('#3', text='PSG.ID')
tree_ticket.column('#3', minwidth=0 , width=100 , stretch=NO)
tree_ticket.heading('#4', text='Seat')
tree_ticket.column('#4', minwidth=0 , width=120 , stretch=NO)
tree_ticket.heading('#5', text='Price')
tree_ticket.column('#5', minwidth=0 , width=70 , stretch=NO)

ticket_treeview_update()

#def item_selected(event):
#for selected_item in tree_passenger.selection():
#dictionary
#item = tree_passenger.item(selected_item)
# list
#record = item['values']
#showinfo(title='Information',
#message=','.join(record))
#tree_passenger.bind('<<TreeviewSelect>>', item_selected)
tree_ticket.grid(row=0, column=0, sticky='nsew')



#Treeview Flight
columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8')
tree_flight = ttk.Treeview(flight_right, columns=columns, show='headings')
tree_flight.heading('#1', text='FLT.ID')
tree_flight.column('#1', minwidth=0 , width=70 , stretch=NO)
tree_flight.heading('#2', text='AIR.ID')
tree_flight.column('#2', minwidth=0 , width=100 , stretch=NO)
tree_flight.heading('#3', text='AIR.Name')
tree_flight.column('#3', minwidth=0 , width=100 , stretch=NO)
tree_flight.heading('#4', text='From')
tree_flight.column('#4', minwidth=0 , width=120 , stretch=NO)
tree_flight.heading('#5', text='To')
tree_flight.column('#5', minwidth=0 , width=70 , stretch=NO)
tree_flight.heading('#6', text='DP.Time')
tree_flight.column('#6', minwidth=0 , width=60 , stretch=NO)
tree_flight.heading('#7', text='AR.Time')
tree_flight.column('#7', minwidth=0 , width=60 , stretch=NO)
tree_flight.heading('#8', text='Seats')
tree_flight.column('#8', minwidth=0 , width=60 , stretch=NO)

#flight_treeview_update()

#def item_selected(event):
 #   for selected_item in tree_flight.selection():
        # dictionary
  #      item = tree_flight.item(selected_item)
        # list
   #     record = item['values']
        #
    #    showinfo(title='Information',
     #           message=','.join(record))


#tree_flight.bind('<<TreeviewSelect>>', item_selected)

tree_flight.grid(row=0, column=0, sticky='nsew')
# add a scrollbar
scrollbar = ttk.Scrollbar(passenger_right, orient=VERTICAL, command=tree_flight.yview)
tree_flight.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')
root.mainloop()






