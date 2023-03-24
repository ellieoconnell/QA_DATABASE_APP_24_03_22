import database

def get_all():
    data = database.check_all_records()
    return data