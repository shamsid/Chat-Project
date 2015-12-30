'''
Created on Oct 16, 2015

@author: shamsher.ahmed
'''
from utility import DBConnectivity
from exceptions import CustomExceptions

def validate_mobile_number(self,mobile_number1):
        mobile_number = str(mobile_number1)
        if len(mobile_number) == 10:
            for i in mobile_number:
                if i  not in '1234567890':
                    return False
            return True
        else:
            return False
    
def validate_password(self,password): 
    pass 

## This function takes mobile_number as a parameter and returns the TRUE is user is present 
## if user is not present than it raises "MobileNumberNotPresent" Exception 
def is_user_present(mobile_number):
    con = DBConnectivity.create_connection()
    db_cursor =  DBConnectivity.create_cursor(con)
    
    sql_statement = "select count(*) from login where MOB_NO =" + str(mobile_number)
    db_cursor.execute(sql_statement)
    for count in db_cursor:
        if count[0] ==  0:
            db_cursor.close()
            raise CustomExceptions.MobileNumberNotPresent
    db_cursor.close()
    return True
