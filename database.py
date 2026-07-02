import sqlite3 as sq
from models import Workers

DATABASE = 'staff.db'

def connect():
    return sq.connect(DATABASE)

def create_base():
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        
        cur.execute('''CREATE TABLE IF NOT EXISTS staff(
            staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            last_name TEXT,
            age INTEGER,
            post TEXT,
            salary INTEGER)''')

def add_staff(worker):
    with connect() as con:
        cur = con.cursor()
        cur.execute('''INSERT INTO staff(name, last_name, age, post, salary) VALUES(?,?,?,?,?)''', (worker.name, worker.last_name, worker.age, worker.post, worker.salary)) 

def get_all():
    with connect() as con:
        cur = con.cursor()
        con.row_factory = sq.Row
        
        cur.execute('''SELECT * FROM staff''')
        
        for row in cur:
            worker = Workers(
                row['staff_id'],
                row['name'],
                row['last_name'],
                row['age'],
                row['post'],
                row['salary']
            )
            worker.show_all()
                
        