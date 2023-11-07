# the service file contains all the functions for each query option the app can query ont the database

# importing the database file so the functions can be referenced
import database


# defining the get all function by pulling the function from the db file
def get_all():
    query = "SELECT * FROM lookuptool"
    data = database.run_query(query)
    return data


# defining the create single order record by pulling the function from the db file 
def create_single_record(alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program):
    query = f"INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ('{alias}', '{first_name}', '{last_name}', '{email_address}', {employee_level}, {years_of_employment}, {in_the_learning_program})"
    database.run_query(query)
    return "The new employee has been recorded!"


# defining a function to read a single record by its id number 
def get_one_record(user_id_no):
    query = f"SELECT * FROM lookuptool WHERE user_id_no = {user_id_no};"
    print("Below is the employee you requested by id number")
    return database.run_query(query)


# defining a function to alter records already in the database table by its id number
def update_record(id, alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program):
    query = f"UPDATE lookuptool SET alias = '{alias}', first_name = '{first_name}', last_name = '{last_name}', email_address = '{email_address}', employee_level = {employee_level}, years_of_employment = {years_of_employment}, in_the_learning_program = {in_the_learning_program} WHERE user_id_no = {id};"
    database.run_query(query)
    return "The record has been changed to fit the new details you entered"


# defining a function to delete a record in the database table by its id number
def del_record(user_id_no):
    query = f"DELETE FROM lookuptool WHERE user_id_no = {user_id_no};"
    database.run_query(query)
    return "The employee record you have choosen has been removed"


# defining a function that deletes all records from the db table
def del_all():
    query = "DELETE FROM lookuptool WHERE user_id_no > 0;"
    database.run_query(query)
    return "All data on the table has been deleted"
