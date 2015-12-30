'''
Created on Oct 17, 2015

@author: vikas.yadav09
'''
from database import viewDB;
from utility import DBConnectivity

def validate_change_pwd(mob_no):
    usr_data_list=viewDB.get_user_information(mob_no);
    if(len(usr_data_list)==0):
        print("Not Registered")
    return usr_data_list;
def new_pwd(user,mob_no):
    try:
        con=DBConnectivity.create_connection();
        cur3=DBConnectivity.create_cursor(con);
        list_of_passwords=[];
        cur3.execute("select * from pwd_check where mob_no="+str(mob_no));
        for row in cur3:
            pwd1=row[1];
            pwd2=row[2];
            pwd3=row[3]; 
            list_of_passwords.append(pwd1);
            list_of_passwords.append(pwd2);
            list_of_passwords.append(pwd3);
        #print(list_of_passwords)
        if(user.get_pwd() in list_of_passwords):
            print("your password can not be previous 3 passwords");
        else:
            update_pwd_check=viewDB.update_password_check(user,list_of_passwords,mob_no);
            update_pwd=viewDB.update_password(user,mob_no)
            if(update_pwd==True):
                return True
            else:
                return False
    finally:
        cur3.close();
        con.close();
def validate_answer(mob_no,answer):
    usr_data_list=viewDB.get_user_information(mob_no);
    if(usr_data_list[3]==answer):
        return True;
    else:
        return False;