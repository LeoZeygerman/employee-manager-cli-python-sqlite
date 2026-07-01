import sqlite3 as sq

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

def add_staff(name, last_name, age, post, salary):
    with connect() as con:
        cur = con.cursor()
        cur.execute('''INSERT INTO staff(name, last_name, age, post, salary) VALUES(?,?,?,?,?)''' (name, last_name, age, post, salary)) 