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
    def display_credentials(cls):
        '''
        Class method to display the list of credentials saved.
        '''
       return cls.credentials_list
    @classmethod
    def find_by_site_name(cls,site_name):
        '''
        Method that takes in a site name and returns a credential that matches the site name.

        Args:
            site_name: site name to search.
        Return:
            Site name of the credential that matches the site_name

        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return site_name



