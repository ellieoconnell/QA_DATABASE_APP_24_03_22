import service
import database

def start_app():
    print(menu)
    exit = False
    while not exit:
        choice = input("Please select a choice: ")
        if choice == "1":
            print(all_orders())
        else:
            exit = True
            database.commit_changes()

def all_orders():
    return service.get_all()

menu = (
    """
    Welcome to the Phone Tool! Please select a choice.
    1. Read all entries
    2. Exit
    """
)

start_app()
