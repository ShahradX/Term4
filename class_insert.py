from mysql.connector import Connect, connect

class Database:
    def __init__(self, u, p, h, d):
        self.username = u
        self.password = p
        self.host = h
        self.database = d
        self.connection()

    def connection(self):
        self.cnx  = connect(
            user = self.username,
            password = self.password,
            host = self.host,
            database = self.database
        )
        self.cursor = self.cnx.cursor()
    def insert(self ,query):
        self.cursor.execute(query)
        self.cnx.commit()



d = Database('root', 'shahrad.f.99', 'localhost', 'class')
query = "INSERT INTO persons(f,l)VALUES('sina', 'bakhshande');"
d.insert(query)