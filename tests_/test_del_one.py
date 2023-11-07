# this file uses unit testing to test the del_record function in the service.py file
# unit testing only tests single functions and not the entire app
# to unit test service.py I am using mocking

# importing the service file for testing
from service import del_record


# creating the testing function to test the deleting one record function
def test_del_oneRecord(mocker):
    # arrange - setting the variables and their values to use for the test
    test_id = 1 
    mocker.patch("service.del_record")

    # act - setting out what function I want to test
    result = del_record(test_id)

    # providing the assumption about what I want the result of the testing to be
    assert result == "The employee record you have choosen has been removed"
