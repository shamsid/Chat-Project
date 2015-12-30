'''
Created on Oct 17, 2015

@author: shamsher.ahmed
'''
class CheckMyChats_Class:
    def __init__(self):
        self.__mobile_number=None;
        self.__receiver=None;
        self.__message=None;

    def get_mobile_number(self):
        return self.__mobile_number

    def get_receiver(self):
        return self.__receiver

    def get_message(self):
        return self.__message

    def set_mobile_number(self, value):
        self.__mobile_number = value

    def set_receiver(self, value):
        self.__receiver = value

    def set_message(self, value):
        self.__message = value


        