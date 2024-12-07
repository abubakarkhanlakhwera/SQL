import sys
from db_helper import  DBhelper
class Flipkart:
    def __init__(self):
        self.db = DBhelper()
        self.menu()

    def menu(self):

        user_input = input("""
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anything else to leave
        """)

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)
    def register(self):
        pass
    def login(self):
        pass
obj = Flipkart()