# this file will test the functions of controller.py with unit testing
# unit testing only tests single functions and not the entire app
# to unit test controller.py the function is being mocked 
# it is best to use a test_db for th

# importing the controller and service files for testing
import application.service as service

# creating the testing function to test the record creation function 
def test_inputRecord(mocker):
    # arrange - setting the varaibles and their values to but into the test_db
    test_proven = "Test complete :)"
    test_alias = "namtes"
    test_first_name = "test"
    test_last_name = "name"
    test_email_address = "namtes@amazon.co.uk"
    test_employee_level = 3
    test_years_of_employment = 2
    test_in_the_AI2_program = True
    mocker.patch("service.create_single_record", return_value = test_proven)

    # act - setting out what function I want to test
    result = service.create_single_record(test_alias, test_first_name, test_last_name, test_email_address, test_employee_level, test_years_of_employment, test_in_the_AI2_program)

    # providing the assumption about what I want the result of the testing to be 
    assert result == test_proven
