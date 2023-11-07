# this file uses unit testing to test the update_record function in the service.py file
# unit testing only tests single functions and not the entire app
# to unit test service.py I am using mocking

# importing the service file for testing 
from service import update_record

# creating the function to test the update record function
def test_updateRecord(mocker):
    # arrange - setting the varibles and their values to put into the test_db
    test_id = 1
    test_alias = "nelszak"
    test_first_name = "Zac"
    test_last_name = "Nelson"
    test_email_address = "test@emailaddress"
    test_employee_level = 4
    test_years_of_employee = 2
    test_in_the_learning_program = True
    mocker.patch("service.update_record")

    # act - setting out what function I want to test
    result = update_record(test_id, test_alias, test_first_name, test_last_name, test_email_address, test_employee_level, test_years_of_employee, test_in_the_learning_program)

    # providing the assumption about what I want the result of the testing to be
    assert result == "The record has been changed to fit the new details you entered"
