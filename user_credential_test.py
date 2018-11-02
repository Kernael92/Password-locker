import unittest #Importing the unittest module
from user_credential import User



class TestUser(unittest.TestCase): 
    '''
    Test class that defines test cases for the user class behaviours.

    Agrs:
        unittest.TestCase: TestCase class that helps in creating test cases 

    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Kernael", "Apuko","oketch92") #create user object
    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Kernael")
        self.assertEqual(self.new_user.last_name,"Apuko")
        self.assertEqual(self.new_user.password,"oketch92")

    def test_save_user(self):
        '''
        test case to test if the new user info is saved into the users list.
        '''
        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.users_list),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to the users list
        '''
        self.new_user.save_user()
        test_user = User("Test","User","usert001") #new user
        test_user.save_user()
        self.assertEqual(len(User.users_list),2)

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.
    Agrs:
        unittest.TestCase: TestCase class that helps in creating test cases 
    '''


if __name__ == '__main__':
    unittest.main()
