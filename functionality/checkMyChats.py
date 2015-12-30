'''
Created on Oct 16, 2015

@author: shamsher.ahmed
'''
from database import viewDB;
from classes import User;
from validations import CheckMyChatValidations
from exceptions import CustomExceptions
from classes.CheckMyChats_Class import CheckMyChats_Class
from database import CheckMyChatDB

def check_my_chats(mobile_num):
    loop=True;
    while(loop):
        obj=CheckMyChats_Class();
        obj.set_mobile_number(mobile_num);
        contactlist=CheckMyChatDB.checkchat_DB(obj);
        length=len(contactlist)+2;
        contactname=CheckMyChatDB.fetch_dispname(obj,contactlist);
        countlist=CheckMyChatDB.get_UnreadCount(obj,contactlist);
        if(len(contactname)==0):
            print("1. New Chat")
            print("2. Exit")
        else:
            for index in range(0,len(contactname)):
                if(countlist[index]==0):
                    print(str(index+1)+"."+str(contactname[index]))
                else:
                    print(str(index+1)+"."+str(contactname[index])+" ["+str(countlist[index])+"]")
            print(str(len(contactname)+1)+". New Chat")
            print(str(len(contactname)+2)+". Exit")
                
        option=input("Enter your Choice : ");
        
        receiver=""
        if(option.isdigit() and int(option)>=1 and int(option)<=length):
            if(int(option)==length):
                loop=False;
            elif(int(option)==length-1):
                receiver=input("Enter the mobile No :")
                
                flag1=False;
            else:
                receiver=contactlist[int(option)-1]
                
                flag1=True;
        if(loop):
            flag=True;
            if(flag1==False):
                try:
                    CheckMyChatValidations.check_receiver(obj,receiver);
                except CustomExceptions.SenderSameAsReceiver as e:
                    print(e)
                    flag=False;
                except CustomExceptions.InvalidReceiver as e:
                    print(e)
                    flag=False;
            if(flag):
                
                obj.set_receiver(receiver);
                if(flag1==True):
                    print("Chat With "+obj.get_receiver())
                    print("******************************************************************************************")
                    CheckMyChatDB.get_conversation(obj);
                    CheckMyChatDB.update_status(obj);
                message=""
                while(message!="#EXIT"):
                    mess_loop=True;
                    while(mess_loop==True):
                        message=input("Message (#EXIT to quit chat):");
                        if(CheckMyChatValidations.check_message_length(message)):
                            mess_loop=False;
                        else:
                            print("Message should not exceed more than 50 characters")
                    if(message!="#EXIT"):
                        obj.set_message(message)
                        CheckMyChatDB.insert_userchat(obj);
                        
                        if(flag1==False):
                            print("Chat With"+obj.get_receiver());
                            print("************************************************************************************")
                            CheckMyChatDB.get_conversation(obj)
                            print(obj.get_mobile_number())
                            CheckMyChatDB.update_status(obj)  
    return
        