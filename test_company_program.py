"""
Code to test all functions related to company database.
"""
from pytest import mark
from unittest import mock, TestCase, main
from re import match

# import local module
import company_program
from mocked_database import users_list_from_mocked_db

# @pytest.mark to mark the tests that require access to a database
@mark.database_access
class TestDb(TestCase):
    """
    Class that tests all the database related functions.

    
    * The setUp() classmethod initializes a mocked database at the beginning of the tests.
    * The tearDown() classmethod stops the mock at the end of the tests.
    """

    @classmethod
    def setUpClass(cls):
        cls.users_list_patcher = mock.patch('company_program.get_users_list_from_db', return_value=users_list_from_mocked_db)
        cls.users_list_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.users_list_patcher.stop()
    

    def test_connect_to_db(self):
        """
        Method that tests if the function connect_to_db(connection_string: str) connects to the database:
        * The first assert tests that the 'ConnectionDatabaseError' exception is raised when the database connection fails.
        * The second assert tests that 'TestDbError' exception is raised when a unit test tries to connect to the database. 
        """
        self.assertRaises(
            company_program.ConnectionDatabaseError,
            company_program.connect_to_db,
            "some_connection_string",
        )
        self.assertRaises(
            company_program.TestDbError, company_program.connect_to_db, "test"
        )

    @mark.xfail
    def test_connect_to_db_expected_failure(self):
        """
        Method that tests expected failure cases when trying to connect to the database.
        """
        self.assertRaises(
            company_program.ConnectionDatabaseError,
            company_program.connect_to_db,
            "test",
        )
        self.assertRaises(
            company_program.TestDbError,
            company_program.connect_to_db,
            "some_connection_string",
        )
    
    def test_get_users_list_from_db(self):
        """
        Method that tests if the function get_users_list_from_db(connection_string: str) 
        gets the list of users from the database and returns them as a list of dict.
        """
        
        actual_users_list = company_program.get_users_list_from_db("connection_string")
        expected_users_list = users_list_from_mocked_db
        self.assertEqual(expected_users_list, actual_users_list)

    @mark.xfail
    def test_get_users_list_from_db_expected_failure(self):
        """
        Method that tests expected failure cases 
        when to get the list of users from the database and returns them as a list of dict.
        """
        
        actual_users_list = company_program.get_users_list_from_db("connection_string")
        expected_users_list = users_list_from_mocked_db[:]
        
        # adding an extra user that is not in the database
        expected_users_list.append({"username": "spy from the future", "birthday": "01/01/2100", "role": "hacker"})
        self.assertEqual(expected_users_list, actual_users_list)

    def test_users_info(self):
        """
        Method that tests if all the users have a username, a birthday and a role.
        The users info must be formatted like this: 
        { 'username': 'John Doe', 'birthday': '02/12/1985', 'role': 'admin' }
        """

        #check that the user has a birthday and in the right format
        actual_users_list = company_program.get_users_list_from_db("connection_string")

        for user in actual_users_list:
            self.assertTrue(bool(match(r"\w+ \w*", user['username'])))
            self.assertTrue(bool(match(r"\d{2}/\d{2}/\d{4}", user['birthday'])))
            self.assertTrue(bool(match(r"\w+", user['role'])))


if __name__ == "__main__":
    main()
