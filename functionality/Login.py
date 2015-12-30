'''
Created on Oct 16, 2015
@author: vikas.yadav09
'''

from datetime import datetime
from database import viewDB
import database
import functionality
from functionality import changePassword, checkMyChats
import validations
from exceptions import CustomExceptions
from classes import  User

def pychat_login(mobile_number =-99999999, count_no_of_logins=0):
    #print(mobile_number)
    from_where =''
    if mobile_number == -99999999:
        mobile_number = input("Mobile Number: ")
        password = input("Password: ")
        try:
            user= User.User()
            user.set_mob_no(mobile_number)
            if not validations.validate_methods.validate_mobile_number(user):
                raise CustomExceptions.InvalidMobileNumberException
            
        except CustomExceptions.InvalidMobileNumberException as e:
            print(e)
            return

    else:
        password = input("Password: ")
        from_where = 'register'
        
    if count_no_of_logins <2:
        status = login_module(mobile_number,password,from_where)
        if status == False:
            if viewDB.get_blocked_status(mobile_number)=='False' :
                print("LOGIN UNSUCCESSFUL \nDo you want wish to continue login (Y/N)? ")
                choice = input()
                while True:
                    if choice in ('Y','y'):
                        pychat_login(-99999999,count_no_of_logins+1)
                        break
                    elif choice in ('N','n'):
                        return
                    else:
                        print("Invalid Choice \n ")
                        choice = input()
        
            else:
                    print("Invalid Password")
                
    else:
        print("LOGIN UNSUCCESSFUL \n Sorry, your account is blocked")
        viewDB.change_blocked_status(mobile_number, 'True')
        account_reset_choice = input("Do you wish to go to Forgot Password (Y/N)? ")
        if account_reset_choice in ('Y','y'):
            functionality.forgotPassword.forget_password()
            exit
        else:
            exit


def is_login_password_correct(mobile_number,password):
    if viewDB.get_password(mobile_number) == password:
        return True
    else:
        return False    
    
def login_module(mobile_number,password,from_where='login'):
    if is_login_password_correct(mobile_number,password)  :
        if viewDB.get_blocked_status(mobile_number)=='True':
            print('Your account is blocked kindly change the password!!')
            return False
        
        database.viewDB.insert_login_timestamp_into_database(mobile_number)
        if from_where == 'register':
            print("Hi " + str(viewDB.get_display_name(mobile_number)) +"\n Your Account is Created " +
                database.viewDB.get_last_login_day(mobile_number)+" at "+database.viewDB.get_last_login_time(mobile_number) +"!" +
                "   What would you like to do? \n1 : Check My Chats \n2 : Change Password \n3 : Logout \n" )
        else:
            print("Hi " + str(viewDB.get_display_name(mobile_number)) +"\n You last logged " +
                database.viewDB.get_last_login_day(mobile_number)+" at "+database.viewDB.get_last_login_time(mobile_number) +"!" +
                "   What would you like to do? \n1 : Check My Chats \n2 : Change Password \n3 : Logout \n" )
        choice = input("Enter your Choice\n")
        if choice.isdigit() :
            if choice =='1':
                    checkMyChats.check_my_chats(mobile_number)
            elif choice =='2':
                    changePassword.change_pwd(mobile_number)
            elif choice =='3':
                    print("You logged out successfully")
                    exit
    else:
        return False         
