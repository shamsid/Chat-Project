'''
Created on Oct 16, 2015

@author: shamsher.ahmed
'''
from utility import DBConnectivity
from exceptions import CustomExceptions
from database import CheckMyChatDB

def check_receiver(obj,receiver):
    if(receiver==str(obj.get_mobile_number())):
        raise CustomExceptions.SenderSameAsReceiver
    elif(not CheckMyChatDB.check_receiver(receiver)):
        raise CustomExceptions.InvalidReceiver
def check_message_length(message):
    if(len(message)>50):
        return False;
    else:
        return True;