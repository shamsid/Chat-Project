'''
Created on Oct 17, 2015

@author: vikas.yadav09
'''
from database import viewDB;

def validate_forget_pwd(mob_no):
    usr_data_list=viewDB.get_user_information(mob_no);
    if(len(usr_data_list)==0):
        print("Not Registered")
    return usr_data_list;