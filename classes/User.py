'''
Created on Oct 16, 2015

@author: vikas.yadav09
'''
class User:
    def __init__(self):
        self.__mob_no = None;
        self.__pwd = None;
        self.__confirmPwd=None;
        self.__dob = None;
        self.__disp_name = None;
        self.__sec_ques = None;
        self.__sec_ans = None;

    def get_confirm_pwd(self):
        return self.__confirmPwd

    def set_confirm_pwd(self, value):
        self.__confirmPwd = value

    def get_mob_no(self):
        return self.__mob_no

    def get_pwd(self):
        return self.__pwd

    def get_dob(self):
        return self.__dob

    def get_disp_name(self):
        return self.__disp_name

    def get_sec_ques(self):
        return self.__sec_ques

    def get_sec_ans(self):
        return self.__sec_ans

    def set_mob_no(self, value):
        self.__mob_no = value

    def set_pwd(self, value):
        self.__pwd = value

    def set_dob(self, value):
        self.__dob = value

    def set_disp_name(self, value):
        self.__disp_name = value

    def set_sec_ques(self, value):
        self.__sec_ques = value

    def set_sec_ans(self, value):
        self.__sec_ans = value
    
