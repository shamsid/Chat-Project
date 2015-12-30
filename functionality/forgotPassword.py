'''
Created on Oct 16, 2015

@author: shamsher.ahmed
'''
from validations import validateForgetpwd
from functionality import changePassword
from database import viewDB
from validations import Validations
import random
from exceptions import CustomExceptions
def forget_password():
    mob_no=input("Mobile Number : ");
    try:
        if mob_no =='':
            raise CustomExceptions.MobileNumberEmptyException()
        elif len(mob_no)<10:
            raise CustomExceptions.InvalidMobileNumberException
        elif not Validations.is_user_present(mob_no):
            raise CustomExceptions.MobileNumberNotPresent
        
    except CustomExceptions.MobileNumberEmptyException as e:
        print(e)
        return
    except CustomExceptions.MobileNumberNotPresent as e:
        print(e)
        return
    except CustomExceptions.InvalidMobileNumberException as e:
        print(e)
        return
        
        
    usr_data_list=validateForgetpwd.validate_forget_pwd(mob_no);
    dob=usr_data_list[1];
    
    dob=str(dob);
    
    sec_ques=usr_data_list[2];
    ch=random.choice(["YYYY","MM","DD"]);
    if(ch=="YYYY"):
        year=input("Enter Year of DOB (YYYY):");
        dob_list=dob.split("-");
        if(year==dob_list[0]):
            print("Answer the Below Question \n"+sec_ques);
            answer=input("Answer:");
            if(answer==usr_data_list[3]):
                changePassword.change_pwd(mob_no,'main_menu');
                viewDB.change_blocked_status(mob_no, 'False')
                #print("Password Changed")
            else:
                print("Invalid")
        else:
            print("Invalid Dob")
    elif(ch=="MM"):
        month=input("Enter Month of DOB (MM):");
        dob_list=dob.split("-");
        if(month==dob_list[1]):
            print("Answer the Below Question \n"+sec_ques);
            answer=input("Answer:");
            if(answer==usr_data_list[3]):
                changePassword.change_pwd(mob_no,'main_menu');
                viewDB.change_blocked_status(mob_no, 'False')
                #print("Password Changed")
            else:
                print("Invalid")
        else:
            print("Invalid Dob")
    elif(ch=="DD"):
        day=input("Enter Day of DOB (DD):");
        dob_list=dob.split("-");
        daydb=dob_list[2];
        daydb=daydb[0:2];
        if(day==daydb):
            print("Answer the Below Question \n"+sec_ques);
            answer=input("Answer:");
            if(answer==usr_data_list[3]):
                changePassword.change_pwd(mob_no,'main_menu');
                viewDB.change_blocked_status(mob_no, 'False')
                #print("Password Changed")
            else:
                print("Invalid")
        else:
            print("Invalid Dob")
    
    
            