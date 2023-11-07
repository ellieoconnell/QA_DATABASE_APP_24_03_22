# the database file contains all the functions that creates the database and connects to it so queries can be run

# importing the sqlite3 module
import sqlite3 as sql

# creating the connection to the SQL table and defining the cursor to navigate through the db table
conn = sql.connect('test_db')
cursor = conn.cursor()

# creating the SQL table in the db
def set_up_table():
    sql_file = open("lookuptool.sql")
    sql_string = sql_file.read()
    cursor.executescript(sql_string)


# defining the run query function to fetch data from the table
def run_query(query):
    data = cursor.execute(query).fetchall()
    return data


# defining function to commit all changes to the db when a request is made
def commit_changes():
    conn.commit()


# run the set_up_table function once to create the table, when run successfully make sure to comment it out like below
# set_up_table()
commit_changes()