import random
import string
class User:
    '''
    Class to create user account and store their information
    '''
    user_list = [] #Empty user list
def __init__(self,first_name,last_name,password): 
    '''
    --init__ method that helps us define properties for our objects.
    '''
    #instance variables
    self.first_name = first_name
    self.last_name = last_name
    self.password = password
