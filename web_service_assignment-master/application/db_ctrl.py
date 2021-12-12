import sqlite3
import os
import uuid 

__db_location__ = "/db"
__user_file__ = f"{__db_location__}/user.db"
__loan_file__ = f"{__db_location__}/loan.db"


def init():
    if_exits = os.path.exists(__db_location__)
    if if_exits==False:
        os.makedirs(__db_location__)

class UserLoan:
    def __init__(self):
        os.path.exists(__user_file__)

    def save(self):
        conItem = sqlite3.connect(__user_file__)  
        cur = conItem.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users
               (id text, name text,loan_balance real, save_balance real)''')
        cur.execute("INSERT INTO users (id,name,loan_balance,save_balance) VALUES (?,?,?,?)",(str(3),"Perera",0.00,300.00))
        items = cur.execute('SELECT * from users')
        for item in items:
            print(item)
        conItem.commit()
        conItem.close()
    
    def getSingleUserIfValid(self):
        conItem = sqlite3.connect(__user_file__)  
        cur = conItem.cursor()
        items = cur.execute("SELECT * FROM users WHERE id LIKE '%s'" % self.u_id)
        loan_balance  = 0
        save_balance  = 0
        for item in items:
            loan_balance = item[2]
            save_balance = item[3]
        print(loan_balance)
        print(save_balance)
        user_confirmer = cur.execute("SELECT * FROM users WHERE id LIKE '%s'" % self.confirmed_user_id)
        user_confirmer_balance = 0
        for u in user_confirmer:
            user_confirmer_balance = u[3]
        if(user_confirmer_balance>float(self.load_amount)):
            print("You can get the load...")
        conItem.commit()
        conItem.close()
        return "You can get the load..."
    