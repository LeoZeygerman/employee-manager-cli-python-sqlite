import sqlite3 as sq
from models import Workers, Transactions

DATABASE = 'staff.db'
def connect():
    return sq.connect(DATABASE)

def create_base_fine():
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        
        cur.execute('''CREATE TABLE IF NOT EXISTS fine_bonus(
            staff_id INTEGER,
            type TEXT,
            amount INTEGER NOT NULL DEFAULT 0,
            reason TEXT)''')
        
def add_fine_bonus(worker_id, type, amount, reason):
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        cur.execute('''INSERT INTO fine_bonus VALUES(?,?,?,?)''',(worker_id,type,amount,reason))
        cur.execute('''SELECT staff.name, fine_bonus.type, fine_bonus.amount, fine_bonus.reason FROM fine_bonus JOIN staff ON fine_bonus.staff_id = staff.staff_id''')
        
        workers = []
        for row in cur:
            worker = Transactions(
                row['name'],
                row['type'],
                row['amount'],
                row['reason']
            )
            workers.append(worker)
        return workers
    
def show_history():
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        cur.execute('''SELECT staff.name, fine_bonus.type, fine_bonus.amount, fine_bonus.reason FROM fine_bonus JOIN staff ON fine_bonus.staff_id = staff.staff_id''')
        
        workers = []
        for row in cur:
            worker = Transactions(
                row['name'],
                row['type'],
                row['amount'],
                row['reason']
            )
            workers.append(worker)
        return workers
    