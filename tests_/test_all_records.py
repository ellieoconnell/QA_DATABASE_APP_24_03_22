# this file uses unit testing to test the get_all function in the service.py file
# unit testing only tests single functions and not the entire app
# to unit test service.py I am using mocking

# importing the service file for testing
from service import get_all


# creating the testing function to test the get all records function
def test_getAll(mocker):
    # arrange - setting the variables and their values to put into test_db
    mocker.patch("service.get_all")

    # act - setting out what function I want to test 
    result = get_all()

    # providing the assumption what what I want the result of the test to be
    assert result == [(1, 'nelszak', 'Zakaria', 'Nelson', 'nelszak@amazon.co.uk', 4, 2, 1), (2, 'vachon', 'Cohen', 'Vasquez', 'vachon@amazon.co.uk', 4, 2, 1), \
                    (3, 'budeaco', 'Deacon', 'Butler', 'budeaco@amazon.co.uk', 4, 5, 1), (4, 'bradcarl', 'Carlo', 'Bradshaw', 'bradcarl@amazon.co.uk', 6, 7, 0), \
                    (5, 'mcdhas', 'Hasan', 'McDaniel', 'mcdhas@amazon.co.uk', 5, 5, 0), (6, 'pattay', 'Taya', 'Patel', 'pattay@amazon.co.uk', 5, 5, 0), \
                    (7, 'sanchch', 'Charles', 'Sanchez', 'sanchch@amazon.co.uk', 6, 1, 1), (8, 'thorzac', 'Zachery', 'Thorton', 'thorzac@amazon.co.uk', 4, 1, 1), \
                    (9, 'mullola', 'Lola', 'Mullen', 'mullola@amazon.co.uk', 5, 3, 1), (10, 'roapopp', 'Poppie', 'Roach', 'roapopp@amazon.co.uk', 5, 5, 0), \
                    (11, 'reelil', 'Lila', 'Reeves', 'reelil@amazon.co.uk', 4, 7, 0), (12, 'boltjea', 'Jean', 'Bolten', 'boltjea@amazon.co.uk', 4, 6, 1), \
                    (13, 'edwsolo', 'Solomon', 'Edwards', 'edwsolo@amazon.co.uk', 6, 4, 0), (14, 'mccelli', 'Elliot', 'McCain', 'mccelli@amazon.co.uk', 7, 8, 0), \
                    (15, 'frlee', 'Lee', 'Fry', 'frlee@amazon.co.uk', 5, 3, 1), (16, 'fletang', 'Angus', 'Fletcher', 'fletang@amazon.co.uk', 5, 2, 1), \
                    (17, 'sykdeli', 'Delilah', 'Sykes', 'sykdeli@amazon.co.uk', 5, 2, 0), (18, 'joylex', 'Lexie', 'Joyce', 'joylex@amazon.co.uk', 4, 3, 0), \
                    (19, 'irwric', 'Rico', 'Irwin', 'irwric@amazon.co.uk', 6, 1, 1), (20, 'romhass', 'Hassan', 'Roman', 'romhass@amazon.co.uk', 4, 4, 1)]
