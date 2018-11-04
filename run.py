#!/usr/bin/env python3.7
from user_credential import User 
from credentials import Credential
import string
import random
import pyperclip
from random import choice


def create_credential(user_name,site_name,account_name,password):
    '''
    Function that create a new credential
    '''
    new_credential = Credential(user_name,site_name,account_name,password)
    return new_credential

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
def generate_password(min_char = 8, max_char = 12, allchar = string.ascii_letters + string.punctuation + string.digits):
    '''
    Function that generates a password
    '''
    password =  ''.join(random.choice(allchar) for x in range(min_char,max_char))
    return password
def copy_credential(site_name):
        '''
        Function  that copies a credential's info
        '''
        return pyperclip.copy(site_name)
def check_user(current_user):
        '''
        Function that checks if the name and password entered match entries in the users_list
        '''
        return current_user

def main():
    print("Hello, Welcome to your credential list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, cp-copy credential, gp-generate password ex -exit the credential list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Credential")
                    print("-"*10)

                    print ("User name ....")
                    user_name = input()

                    print("Site name ...")
                    site_name = input()

                    print("Account name ...")
                    account_name = input()

                    print("password ...")
                    password = input()

        


                    save_credential(create_credential(user_name,site_name,account_name,password)) # create and save new credential.
                    print ('\n')
                    print(f"New credential {user_name} {site_name} {account_name} {password} created")
                    print ('\n')

            elif short_code == 'dc':

                    if display_credentials():
                            print("Here is a list of all your credentials")
                            print('\n')

                            for credential in display_credentials():
                                    print(f"{credential.user_name} {credential.site_name} {credential.account}.....{credential.password}")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any credentials saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the name of the site you want to search for")

                    search_site_name = input()
                    if credential_exist(search_site_name):
                            search_credential = find_credential(search_site_name)
                            print(f"{search_credential.user_name} {search_credential.site_name} {search_credential.account_name}")
                            print('-' * 20)

                            print(f"site_name.......{search_credential.site_name}")
                            print(f"account name.......{search_credential.account_name}")
                    else:
                            print("That credential does not exist")
            elif short_code =='gp':
                if generate_password(min_char = 8, max_char = 12, allchar = string.ascii_letters + string.punctuation + string.digits):
                    
                    print ("This is your password:", password)

            elif short_code == 'cp':
                print("Enter the name of the site you want to copy")
                copy_site_name = input()
                if credential_exist(copy_site_name):
                    copy_credential = find_credential(copy_site_name)
                    print(f"{copy_credential.user_name} {copy_credential.site_name} {copy_credential.account_name} {copy_credential.password}")
                    print('_' * 20)
                    print(f"site_name.......{copy_credential.site_name}")
                    print(f"account name.......{copy_credential.account_name}")
                else:
                    print("This credential does not exist")


                    

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
    main()


