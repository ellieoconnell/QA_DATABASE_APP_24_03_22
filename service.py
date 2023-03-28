import database

# defining the get all function by oulling the function from the db file 
def get_all():
    data = database.check_all_records()
    return data