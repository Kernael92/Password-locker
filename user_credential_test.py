import unittest #Importing the unittest module
from user_credential import User 
from credentials import Credential
import pyperclip



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
        Credential.credentials_list = []
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
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved.
        '''
        self.assertEqual(Credential.display_credentials(),Credential.credentials_list)
    def test_find_by_site_name(self):
        '''
        Test to check if the find_by_site_name method returns the correct credentials
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Bobby","facebook","bobbyjoe","bobby001") #new credential
        test_credential.save_credential()
        found_credential = Credential.find_by_site_name("facebook")
        self.assertEqual(found_credential.site_name,test_credential.site_name)
    # def test_generate_password(self):
    #     '''
    #     Test to generate a new password.
    #     '''
    #     self.new_credential.save_credential()
    #     gmail = Credential("Bobby","gmail","bobbyjoe","") #new credential
    #     gmail.save_credential()
    #     gen_password = gmail.password("")
    #     self.assertEqual(gen_password(),gmail.password)

    def test_copy_credential(self):
        '''
        Test to confirm that we are copying the account name from a found credential
        '''
        self.new_credential.save_credential()
        facebook = Credential("Bobby","facebook","bobbyjoe","bobby001") #new credential
        facebook.save_credential()
        find_credential = None
        for credential in Credential.credentials_list:
		        find_credential =Credential.find_by_site_name(credential.site_name)
		        return pyperclip.copy(find_credential.password)
        Credential.copy_credential(self.new_credential.site_name)
        self.assertEqual("bobby001",pyperclip.paste())


    




    




if __name__ == '__main__':
    unittest.main()
