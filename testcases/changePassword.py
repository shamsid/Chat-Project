'''
Created on Oct 16, 2015

@author: shamsher.ahmed
'''
from classes import User
from validations import validate_methods
from exceptions import CustomExceptions;
'''user with 
positive test cases'''

user=User.User()
user.set_pwd('Aa.1234')
user.set_confirm_pwd('Aa.1234')

validate_methods.validate_password(user)
validate_methods.validate_confirm_password(user)

'''user with 
Negative test cases'''

user=User.User()
user.set_pwd('target')
user.set_confirm_pwd('target1')
        
try:
    validate_methods.validate_password(user)
except CustomExceptions.InvalidPasswordException as e:
        print(e)
try:
    validate_methods.validate_confirm_password(user)
except CustomExceptions.InvalidConfirmPasswordException as e:
        print(e)