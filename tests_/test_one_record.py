# this file uses unit testing to test the get_one_record function in the service file
# unit testing only tests single functions and not the entire application
# to unit test service.py I am using mocking 
# it is best to use a test_db for this test

# importing the service file
from service import get_one_record


# creating the testing function to test the record creation function 
def test_oneRecord(mocker):
    # arrange - setting the varaibles and their values to but into the test_db
    test_id = 1
    mocker.patch("service.get_one_record")

    # act - setting out what function I want to test
    result = get_one_record(test_id)

    # providing the assumption about what I want the result of the testing to be
    assert result == [(1, 'nelszak', 'Zakaria', 'Nelson', 'nelszak@amazon.co.uk', 4, 2, 1)]
