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

    def register(self,name,email,password):
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}')
            """.format(name,email,password))
            self.con.commit()
        except:
            return  -1
        else:
            return 1
    def search(self,email,password):
        try:
            self.mycursor.execute("""
            SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}' 
            """.format(email,password))
            data = self.mycursor.fetchall()
            return data
        except:
            print('error')


