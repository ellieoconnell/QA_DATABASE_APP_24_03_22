import database

# defining the get all function by pulling the function from the db file 
def get_all():
    query = "SELECT * FROM phonetool"
    data = database.run_query(query)
    return data

# defining the create single order record by pulling the function from the db file 
def create_single_record(alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_AI2_program):
    query = f"INSERT INTO phonetool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_AI2_program) VALUES ('{alias}', '{first_name}', '{last_name}', '{email_address}', {employee_level}, {years_of_employment}, {in_the_AI2_program})"
    database.run_query(query)
    return "The new employee has been recorded!"

def update_db():
    print("Table has been updated")
    return database.commit_changes()