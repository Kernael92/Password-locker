import random
import string
from user_credential import User
class Credential:
    '''
    Class to create user account credentials, generate passwords and store their information.
    '''
    credentials_list = [] #Empty credentials list
    user_credentials_list [] #Empty user credential list
    def __init__(self,user_name,site_name,account_name,password):
        '''
        Helps define properties for our credential objects
        '''
        #instance variables
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password
    def save_credential(self):
        '''
        save_credential method saves credential objects into credentials list
        '''
        Credential.credentials_list.append(self)
    @classmethod
    def display_credential(self):
        '''
        Class method to display the list of credentials saved.
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list
    @classmethod
    
