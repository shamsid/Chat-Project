'''
Created on Oct 16, 2015

@author: shamsher.ahmed
'''
from database import viewDB;

def validate_forget_pwd(mob_no):
    usr_data_list=viewDB.get_user_information(mob_no);
    if(len(usr_data_list)==0):
        print("Not Registered")
    return usr_data_list;