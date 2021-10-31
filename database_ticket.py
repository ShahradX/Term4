from logging import setLogRecordFactory
from tkinter.constants import NONE
from mysql.connector import connect


class Databse:

    def __init__(self, u, p, h, d):
        self.username = u
        self.password = p
        self.host = h
        self.database = d
        self.connection()

    def connection(self):
        self.cnx = connect(
            user = self.username,
            password = self.password,
            host = self.host,
            database = self.database
        )
        self.cursor = self.cnx.cursor()

class Passenger(Databse):


    def __init__(self, u, p, h, d):
        super().__init__(u, p, h, d)


    def insert(self , f ,l ,p ,n ,g):
        query = f"""
        INSERT INTO passenger_profile
        (first_name , last_name, phone, nationality, gender)
        VALUES
        ('{f}' , '{l}' , '{p}', '{n}' , '{g}')"""
        self.cursor.execute(query)
        self.cnx.commit()

    def update(self , f, l, p, n, g, p_id):
        query = f"""
        UPDATE passenger_profile 
        SET first_name='{f}' , last_name='{l}', phone='{p}', nationality='{n}', gender='{g}'
        WHERE passenger_id={p_id}"""
        self.cursor.execute(query)
        self.cnx.commit()



    def DQL(self, p_id=None):
        if p_id is None:
            query = f"SELECT * FROM passenger_profile"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        else:
            query = f"SELECT * FROM passenger_profile WHERE passenger_id={p_id}"
            self.cursor.execute(query)
            return self.cursor.fetchone()

class Flight(Databse):


    def __init__(self, u, p, h, d):
        super().__init__(u, p, h, d)


    def insert(self , a_id, a_name, f_, to, d_time, a_time, s):
        query = f"""
        INSERT INTO flight_info
        (airline_id , airline_name, from_location, to_location, deprature_time, arrival_time, total_seats)
        VALUES
        ('{a_id}' , '{a_name}' , '{f_}', '{to}' , '{d_time}' , '{a_time}', '{s}')"""
        self.cursor.execute(query)
        self.cnx.commit()

    def update(self , a_id, a_name, f_, to, d_time, a_time, s, f_id):
        query = f"""
        UPDATE flight_info 
        SET airline_id='{a_id}' , airline_name='{a_name}', from_location='{f_}', to_location='{to}', deprature_time='{d_time}', arrival_time='{a_time}', total_seats='{s}'
        WHERE flight_id={f_id}"""
        self.cursor.execute(query)
        self.cnx.commit()



    def DQL(self, p_id=None):
        if p_id is None:
            query = f"SELECT * FROM flight_info"
        else:
            query = f"SELECT * FROM flight_info WHERE flight_id={p_id}"
        self.cursor.execute(query)
        return self.cursor.fetchball()

class Ticket(Databse):


    def __init__(self, u, p, h, d):
        super().__init__(u, p, h, d)


    def insert(self , f_id, p_id, s, pr):
        query = f"""
        INSERT INTO ticket_info
        (flight_id , passenger_id, seat_number, price)
        VALUES
        ('{f_id}' , '{p_id}' , '{s}', '{pr}')"""
        self.cursor.execute(query)
        self.cnx.commit()

    def update(self , f_id, p_id, s, m, p, t_id):
        query = f"""
        UPDATE ticket_info 
        SET flight_id='{f_id}' , passenger_id='{p_id}', seat_number='{s}', models='{m}', price='{p}'
        WHERE ticket_id={t_id}"""
        self.cursor.execute(query)
        self.cnx.commit()



    def DQL(self, t_id=None, flight_id=NONE):
        if t_id is None:
            query = f"SELECT * FROM ticket_info"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        if flight_id:
            query = f"SELECT * FROM ticket_info WHERE flight_id={flight_id}"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        else:
            query = f"SELECT * FROM ticket_info WHERE ticket_id={t_id}"
            self.cursor.execute(query)
            return self.cursor.fetchone()

