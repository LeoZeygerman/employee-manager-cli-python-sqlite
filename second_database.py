import sqlite3 as sq

DATABASE = 'fine_bonus.db'
def connect():
    return sq.connect(DATABASE)

def create_base_fine():
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        
        cur.execute('''CREATE TABLE IF NOT EXISTS fine_bonus(
            staff_id INTEGER,
            fine INTEGER,
            bonus INTEGER)''')
        
def add_fine(worker_id, fine):
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        
        cur.execute('''UPDATE fine_bonus SET fine = ? WHERE worker_id = ?''', (fine, worker_id))