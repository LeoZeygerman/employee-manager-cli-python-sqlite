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
        con.row_factory = sq.Row
        cur = con.cursor()
        cur.execute('''INSERT INTO staff(name, last_name, age, post, salary) VALUES(?,?,?,?,?)''', (worker.name, worker.last_name, worker.age, worker.post, worker.salary)) 

def get_all():
    workers = []
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        
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
            workers.append(worker)
    return workers

def find_by_name(name):
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        
        cur.execute('''SELECT * FROM staff WHERE LOWER(name) = LOWER(?)''', (name,))
        workers = []
        for row in cur:
            worker = Workers(
                row['staff_id'],
                row['name'],
                row['last_name'],
                row['age'],
                row['post'],
                row['salary']
            )
            workers.append(worker)
        return workers
    
def delete_staff(name):
    with connect() as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        
        cur.execute('''DELETE FROM staff WHERE LOWER(name) = LOWER(?)''', (name,))
        cur.execute('''SELECT * FROM staff WHERE LOWER(name) = LOWER(?)''', (name,))
        workers = []
        for row in cur:
            worker = Workers(
                row['staff_id'],
                row['name'],
                row['last_name'],
                row['age'],
                row['post'],
                row['salary']
            )
            workers.append(worker)
        return workers
                
def delete_by_id(staff_id):
        with connect() as con:
            con.row_factory = sq.Row
            cur = con.cursor()
            
            cur.execute('''DELETE FROM staff WHERE staff_id = ?''', (staff_id,))
            cur.execute('''SELECT * FROM staff WHERE staff_id = ?''', (staff_id,))
        workers = []
        for row in cur:
            worker = Workers(
                row['staff_id'],
                row['name'],
                row['last_name'],
                row['age'],
                row['post'],
                row['salary']
            )
            workers.append(worker)
        return workers
    
def find_by_id(staff_id):
    with connect() as con:
            con.row_factory = sq.Row
            cur = con.cursor()
            cur.execute('''SELECT * FROM staff WHERE staff_id = ?''', (staff_id,))
            workers = []
            for row in cur:
                worker = Workers(
                    row['staff_id'],
                    row['name'],
                    row['last_name'],
                    row['age'],
                    row['post'],
                    row['salary']
                )
                workers.append(worker)
            return workers