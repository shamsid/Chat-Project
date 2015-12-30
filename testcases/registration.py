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
user.set_mob_no(9886331306)
user.set_pwd('Aa.1234')
user.set_confirm_pwd('Aa.1234')
user.set_sec_ques('fav color?')
user.set_sec_ans('yellow')
user.set_dob('13-Jun-1992')

validate_methods.validate_mobile_number(user)
validate_methods.validate_password(user)
validate_methods.validate_security_question(user)
validate_methods.validate_confirm_password(user)
validate_methods.valdiate_security_answer(user)

'''user with 
Negative test cases'''

user=User.User()
user.set_mob_no(988623)
user.set_pwd('target')
user.set_confirm_pwd('target1')
user.set_sec_ques('name')
user.set_sec_ans('abhi')
user.set_dob('13-06-1992')
try:
    validate_methods.validate_mobile_number(user)
except CustomExceptions.InvalidMobileNumberException as e:
        print(e)
        
try:
    validate_methods.validate_password(user)
except CustomExceptions.InvalidPasswordException as e:
        print(e)
try:
    validate_methods.validate_confirm_password(user)
except CustomExceptions.InvalidConfirmPasswordException as e:
        print(e)
try:
    validate_methods.validate_security_question(user)
except CustomExceptions.InvalidSecurityQuestionException as e:
        print(e)

try:
    validate_methods.valdiate_security_answer(user)
except CustomExceptions.InvalidSecurityAnswerException as e:
        print(e)