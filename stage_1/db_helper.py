import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.con =  mysql.connector.connect(host='localhost',user='root',password='qwerty.',database='vu-bs-cs')
            self.mycursor = self.con.cursor()

        except:
            print('Connection failed')
        else:
            print(f'Connected to  database')
