import service
import database

# defining the while loop that loops through all the menu options 
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

# defining the all orders function for when the use selects option 1
# uses the function definined in the service file
def all_orders():
    return service.get_all()

# menu displayed when requests are made to the db
menu = (
    """
    Welcome to the Phone Tool! Please select a choice.
    1. Read all entries
    2. Exit
    """
)

start_app()
