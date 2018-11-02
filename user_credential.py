import random
import string
class User:
    '''
    Class to create user account and store their information
    '''
    users_list = [] #Empty users list
    def __init__(self,first_name,last_name,password): 
        '''
        --init__ method that helps us define properties for our objects.
        '''
        #instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    class Credential:
        '''
        Class to create user account credentials, generate passwords and store their information.
        '''
        credentials_list = [] #Empty credentials list
    def  save_user(self):
        '''
        save_user method saves contact objects into users list
        '''
        User.users_list.append(self)

