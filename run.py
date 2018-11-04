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
    Function that finds a contact by number and returns the contact
    '''
    return Credential.find_by_site_name(site_name)
