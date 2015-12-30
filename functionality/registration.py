'''
Created on Oct 16, 2015

@author: shamsher.ahmed
'''
from validations import validate_methods
from classes.Captcha import Captcha;
from classes.User import User;
from database import viewDB
from exceptions import CustomExceptions;
from functionality import Login
def prompt():
    ch=input("Do You Wish to Continue Registration (Y/N)?");
    if(ch=='Y'):
        user_registering();
    else:
        exit;
def user_registering():
    a=User();
    mob_no = input("Mobile Number :");
    a.set_mob_no(mob_no);
    pwd = input("Password :");
    a.set_pwd(pwd);
    confirm_pwd = input("Confirm Password : ");
    a.set_confirm_pwd(confirm_pwd);
    dob = input("Date (DD-Mon-YYYY) : ");
    a.set_dob(dob);
    disp_name = input("Display Name (Optional) : ")
    a.set_disp_name(disp_name);
    sec_ques = input("Security Question : ")
    a.set_sec_ques(sec_ques);
    sec_ans = input("Security Answer : ");
    a.set_sec_ans(sec_ans)
    temp=Captcha().get_captcha();
    print("Enter the CAPTCHA shown below : ")
    print(temp)
    cptcha=input();
    #is_data_valid=validate_methods.register_validations(a);
    try:
        if(validate_methods.validate_mobile_number(a)):
            if(validate_methods.validate_password(a)):
                if(validate_methods.validate_confirm_password(a)):
                    if(validate_methods.validate_dob(a)):
                        if(validate_methods.validate_security_question(a)):
                            if(validate_methods.valdiate_security_answer(a)):
                                if(validate_methods.validate_captcha(temp, cptcha)):
                                    updatedb=viewDB.update_table_usr(a)
                                    if(updatedb==True):
                                        ch=input("Registration Successful !\n Do you Want to login (Y/N)?");
                                        if(ch in ('Y','y')):
                                            Login.pychat_login(a.get_mob_no())
                                        else:
                                            exit
                                        
    except CustomExceptions.InvalidCaptchaException as e:
        print(e)
        prompt()
    except CustomExceptions.InvalidConfirmPasswordException as e:
        print(e)
        prompt()
    except CustomExceptions.InvalidMobileNumberException as e:
        print(e)
        prompt()
    except CustomExceptions.InvalidPasswordException as e:
        print(e)
        prompt()
    except CustomExceptions.InvalidSecurityQuestionException as e:
        print(e)
        prompt()
    except CustomExceptions.InvalidSecurityAnswerException as e:
        print(e)
        prompt()
    except CustomExceptions.InvalidDateFormatException as e:
        print(e)
        prompt()
            
            
        
