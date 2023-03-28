import service
import database
import sys

# defining the while loop that loops through all the menu options 
def start_app():
    print(menu)
    exit = False
    while not exit:
        choice = input("Please select a choice: ")
        if choice == "1":
            print(all_orders())
        if choice == "2":
            print(input_record())
        if choice == "3":
            print(one_order())
        if choice == "4":
            confirm_update()
            database.commit_changes()
            sys.exit("Goodbye for now!")

# defining the all orders function for when the user selects option 1
def all_orders():
    return service.get_all()

# defining the input record function for when the user selects option 2 
def input_record():
    shortname = input("Please enter the alias of the new employee: ")
    first = input("Please enter the first name of the new employee: ")
    last = input("Please enter the last name of the new employee: ")
    email = input("Please enter the email address of the new employee: ")
    level = input("Please enter the level of the new employee: ")
    years = input("Please enter how many years the employee has been with Amazon: ")
    ai2 = input("Is the employee in the AI2 program? True or False?: ")
    return service.create_single_record(shortname, first, last, email, level, years, ai2)

# defines a function for when user selects option 3
def one_order():
    id = input("Please enter the id of the employee you would like you see: ")
    return service.get_one_record(id)

# menu displayed when requests are made to the db
menu = (
    """
    Welcome to the Phone Tool! Please select a choice.
    1. Read all entries
    2. Enter a new record 
    3. Read one order by id number
    4. Exit
    """
)

def confirm_update():
    return service.update_db()

start_app()
