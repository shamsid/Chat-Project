
from classes.User import User
from validations import validateChangepwd
from exceptions import CustomExceptions;
from database import viewDB
from validations import validate_methods
def change_pwd(mob_no,from_choice ='login'):
    try:
        a=User();
        if from_choice == 'login':
            old_pwd=input("Old Password : ");
            validate_pwd=validateChangepwd.validate_change_pwd(mob_no);
            
            if(validate_pwd[4]!=old_pwd):
                raise CustomExceptions.InvalidPassword;
        
        new_pwd=input("New Password : ")
        confirm_new_pwd=input("Confirm New password : ");
        if(confirm_new_pwd!=new_pwd):
            raise CustomExceptions.InvalidConfirmPasswordException();
        else:
            #===================================================================
            # if len(new_pwd) >10 or len(new_pwd)<6:
            #     raise CustomExceptions.InvalidPassword
            #===================================================================
            
            a.set_pwd(new_pwd)
            if validate_methods.validate_password(a):
                new_pwd=validateChangepwd.new_pwd(a,mob_no);
                if(new_pwd==True):
                    print("Password changed Successfully")
    except CustomExceptions.InvalidConfirmPasswordException as e:
        print(e)
    except CustomExceptions.InvalidPassword as e:
        print(e)
    except CustomExceptions.InvalidPasswordException as e:
        print(e)
        
def forget_change_pwd(mob_no):
    try:
        a=User();
        question=[];
        print("Answer the Below Question : ");
        question=viewDB.get_user_information(mob_no);
        print(question[2]);
        answer=input("Answer :");
        is_ans_valid=validateChangepwd.validate_answer(mob_no, answer)
        if(is_ans_valid==False):
            raise CustomExceptions.InvalidAnswerException();
        new_pwd=input("New Password : ")
        confirm_new_pwd=input("Confirm New password : ");
        if(confirm_new_pwd!=new_pwd):
            raise CustomExceptions.InvalidConfirmPasswordException();
        else:
            a.set_pwd(new_pwd)
            new_pwd=validateChangepwd.new_pwd(a,mob_no);
            if(new_pwd==True):
                print("Password changed Successfully")
    except CustomExceptions.InvalidConfirmPasswordException as e:
        print(e)
    except CustomExceptions.InvalidAnswerException as e:
        print(e)
        