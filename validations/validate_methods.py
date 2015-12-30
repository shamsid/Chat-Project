'''
Created on Oct 16, 2015

@author: shamsher.ahmed
'''
from classes.User import User 
from exceptions import CustomExceptions
import re
def validate_mobile_number(user):
    if(len(str(user.get_mob_no()))!=10):
        raise CustomExceptions.InvalidMobileNumberException();
    elif(len(str(user.get_mob_no()))==10):
        mob_no=str(user.get_mob_no());
        if(not mob_no.isnumeric()):
            raise CustomExceptions.InvalidMobileNumberException();
    return True;
def validate_password(user):
    if(len(user.get_pwd())<6 or len(user.get_pwd())>10):
        raise CustomExceptions.InvalidPasswordException();
    elif(len(user.get_pwd())>=6 and len(user.get_pwd())<=10):
        flag=0;
        if((re.search(r'\@',user.get_pwd()) or re.search(r"\.",user.get_pwd()) or re.search(r"\#",user.get_pwd())) and (re.search(r"\d*",user.get_pwd()))):
            pwd=user.get_pwd();
            for i in pwd:
                if(str(i).islower()):
                    count=1;
            if(count==1):
                for j in pwd:
                    if(str(j).isupper()):
                        count=2;
            if(count==2):
                flag=0;
        else:
            flag=flag+1;
        if(flag!=0):
            raise CustomExceptions.InvalidPasswordException();
    return True;
        
def validate_confirm_password(user):
    if(user.get_pwd() != user.get_confirm_pwd()):
        raise CustomExceptions.InvalidConfirmPasswordException();
    return True;
def validate_security_question(user):
    if(len(user.get_sec_ques())<5 or len(user.get_sec_ques())>30):
        raise CustomExceptions.InvalidSecurityQuestionException();
    return True;
def valdiate_security_answer(user):
    if(len(user.get_sec_ans())<5 or len(user.get_sec_ans())>30):
        raise CustomExceptions.InvalidSecurityAnswerException();
    return True
def validate_captcha(old_captcha,new_captcha):
    if(old_captcha!=new_captcha):
        raise CustomExceptions.InvalidCaptchaException();
    return True
    
def validate_dob(user):
    if(not re.search(r"[0,1,2,3][0-9]-[Jan,Feb,Mar,Apr,May,June,July,Aug,Sep,Oct,Nov,Dec][a-z][a-z]-\d\d\d\d", user.get_dob())):
        raise CustomExceptions.InvalidDateFormatException(); 
    return True
