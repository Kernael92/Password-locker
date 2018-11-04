#!/usr/bin/env python3.7
from user_credential import User 
from credentials import Credential
def  save_user(user):
        '''
        Function to save user
        '''
        user.save_user()
def  save_credential(credential):
        '''
        Function to save user
        '''
        credential.save_credential()
def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()
def find_credential(site_name):
    '''
    Function that finds a credential by site_name
    '''
    return Credential.find_by_site_name(site_name)
def credential_exist(site_name):
    '''
    Function that check if a credential exists with that site_name and return a Boolean
    '''
    return Credential.credential_exist(site_name)
def generate_password(self,min_char = 8, max_char = 12, allchar = string.ascii_letters + string.punctuation + string.digits):
    '''
    Function that generates a password
    '''
    return ''.join(random.choice(allchar) for x in range(min_char,max_char))