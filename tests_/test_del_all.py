# this file uses unit testing to test the del_all function in the service.py file
# unit testing only tests single functions and not the entire app
# to unit test service.py I am using mocking 

# importing the service file for testing
from service import del_all


# creating the testing function to test the record creation function
def test_delAll(mocker):
    # arrange - setting the variables and their values to put into test_db
    mocker.patch("service.del_all")

    # act - setting out what function I want to test 
    result = del_all()

    # providing the assumption about what I want the result of the testing to be
    assert result == "All data on the table has been deleted"
