import unittest #Importing the unittest module
from user_credential import User 
from credentials import Credential



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
    def tearDown(self):
        '''
        tearDown method that does clean up after case has run.
        ''' 
        User.users_list = []
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
    def setUp(self):
        '''
        Function to create an account's credentials before each test.
        '''
        self.new_credential = Credential("Glenn","Instagram","glennjoy","oketch001")

    def tearDown(self):
        '''
        tearDown method that does clean up after case has run.
        ''' 
    def test_init(self):
        '''
        To check if the object is initialized properly.
        '''
        self.assertEqual(self.new_credential.user_name,"Glenn")
        self.assertEqual(self.new_credential.site_name,"Instagram")
        self.assertEqual(self.new_credential.account_name,"glennjoy")
        self.assertEqual(self.new_credential.password,"oketch001")
    def test_save_credential(self):
        '''
        To check if the new credentials are saved into the credential list
        '''
        self.new_credential.save_credential()
        facebook = Credential("Bobby","facebook","bobbyjoe","bobby001") #new credential
        facebook.save_credential()
        self.assertEqual(len(Credential.credentials_list),2)
    def test_display_credential(self):
        '''
        To check if the test_display_credential method displays the correct dredentials
        '''
        self.new_credential.save_credential()
        facebook = Credential("Bobby","facebook","bobbyjoe","bobby001") #new credential
        facebook.save_credential()
        twitter = Credential("Jane","twitter","janejay","jayjan01")
        twitter.save_credential()
        self.assertEqual(len(Credential.display_credential(twitter.user_name)),2)
    def test_find_by_site_name(self):
        '''
        Test to check if the find_by_site_name method returns the correct credentials
        '''
        self.new_credential.save_credentials()
        facebook = Credential("Bobby","facebook","bobbyjoe","bobby001") #new credential
        facebook.save_credential()
        credential_exists = Credential.find_by_site_name('facebook')
        self.assertEqual(credential_exists,facebook)




if __name__ == '__main__':
    unittest.main()
