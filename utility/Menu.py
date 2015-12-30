'''
Created on Oct 16, 2015

@author: shamsher.ahmed
'''
'''
This module displays a menu to the user.
'''
from functionality import registration;
from functionality import forgotPassword
from functionality import Login
print("+-------------------+")
print("| Welcome to PyChat |")
print("+-------------------+")

print("Choose an option from below:\n")
end=False

while(end==False):
    print("1. Login")
    print("2. Register")
    print("3. Forgot Password?")
    
    
    print("4. Quit")
    option=input()
    if(option.isdigit() and (int(option)>=1 or int(option)<=4)):
        if(int(option)==1):
            print("PyChat Login:")
            Login.pychat_login();
        if(int(option)==2):
            print("PyChat Registration:")
            registration.user_registering();
        if(int(option)==3):
            print("PyChat Forgot Password:")
            forgotPassword.forget_password()
        if(int(option)==4):
            print("Thank you!")
            end=True
    else:
        print("Please enter a valid option ( 1,2,3,4)")