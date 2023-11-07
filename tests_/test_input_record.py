# this file uses unit testing to test the create_single_record function in the service.py file
# unit testing only tests single functions and not the entire app
# to unit test service.py I am using mocking 
# it is best to use a test_db for this test

# importing the service file for testing
from service import create_single_record


# creating the testing function to test the record creation function 
def test_inputRecord(mocker):
    # arrange - setting the variables and their values to put into test_db
    test_proven = "Test complete :)"
    test_alias = "namtes"
    test_first_name = "test"
    test_last_name = "name"
    test_email_address = "namtes@amazon.co.uk"
    test_employee_level = 3
    test_years_of_employment = 2
    test_in_the_learning_program = True
    mocker.patch("service.create_single_record", return_value = test_proven)

    # act - setting out what function I want to test
    result = create_single_record(test_alias, test_first_name, test_last_name, test_email_address, test_employee_level, test_years_of_employment, test_in_the_learning_program)

    # providing the assumption about what I want the result of the testing to be 
    assert result == "The new employee has been recorded!"
