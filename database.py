import sqlite3 as sql 

conn = sql.connect('test_db')
cursor = conn.cursor()

def set_up_table():
    sql_file = open("phonetool.sql")
    sql_string = sql_file.read()
    cursor.executescript(sql_string)

def run_query(query):
    data = cursor.execute(query).fetchall()
    return data 

def check_all_records():
    query = "SELECT * FROM phonetool;"
    data = run_query(query)
    return data

def commit_changes():
    conn.commit()

#set_up_table()
commit_changes()