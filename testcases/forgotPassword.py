'''
Created on Oct 16, 2015

@author: shamsher.ahmed
'''
from validations import Validations
from classes import User
from validations import validate_methods
from exceptions import CustomExceptions;

'''user with 
positive test cases'''

user=User.User()
user.set_mob_no(9886331306)
user.set_sec_ans('yellow')
validate_methods.validate_mobile_number(user)
validate_methods.valdiate_security_answer(user)

'''user with 
Negative test cases'''

user=User.User()
user.set_mob_no(988623)
user.set_sec_ans('yell')
try:
    validate_methods.validate_mobile_number(user)
except CustomExceptions.InvalidMobileNumberException as e:
        print(e)
try:
    validate_methods.valdiate_security_answer(user)
except CustomExceptions.InvalidSecurityAnswerException as e:
        print(e)