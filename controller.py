# the controller files acts as the API for the application and
# represents that content that will be presented in the terminal

# importing the service and database file to use the functions
# importing the sys module
import sys
import service
import database


# defining the while loop that loops through all the menu options
def start_app():
    print(MENU)
    exit = False
    while not exit:
        choice = input("Please select a choice: ")
        if choice == "1":
            print(all_orders())
        if choice == "2":
            print(input_record())
        if choice == "3":
            print(one_record())
        if choice == "4":
            print(change_record())
        if choice == "5":
            print(del_single_record())
        if choice == "6":
            print(del_all_records())
        if choice == "7":
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
    ai2 = input("Is the employee in the AI2 program? True or False: ")
    return service.create_single_record(shortname, first, last, email, level, years, ai2)


# defines a function for when user selects option 3
def one_record():
    id = input("Please enter the id of the employee you would like you see: ")
    return service.get_one_record(id)


# defining a function when a user selects option 4
def change_record():
    record_id = input("Please enter the id of the record you would like to update: ")
    shortname = input("Please enter the new alias of the employee for this record: ")
    first = input("Please enter the new name of the employee for this record: ")
    last = input("Please enter the new last name of the employee for this record: ")
    email = input("Please enter the new email address of the employee for this record: ")
    level = input("Please enter the new level of the employee for this record: ")
    years = input("Please enter the new amount of years the employee has been with Amazon: ")
    learning = input("Has the employee now left the learning program? or have they just joined it? True or False: ")
    return service.update_record(record_id, shortname, first, last, email, level, years, learning)


# defining a function for when a user selecrs option 5
def del_single_record():
    id = input("Please enter the id of the record you would like to delete: ")
    return service.del_record(id)


# defining a function for when a user selects option 6
def del_all_records():
    choice = input("Are you sure you want to delete all the records in Look Up Tool? Yes or No: ")
    if choice == "yes":
        print("All records have been deleted")
        return service.del_all()
    else:
        return "No records deleted."


# menu displayed when requests are made to the db
MENU = (
    """
    Welcome to the Look Up Tool! Please select a choice.
    1. Read all entries
    2. Enter a new record
    3. Read one record by id number
    4. Update a record by id number
    5. Delete one record by id number
    6. Delete all records in the table
    7. Exit
    """
)

start_app()
