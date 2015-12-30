'''
Created on Oct 16, 2015

@author: vikas.yadav09
'''
from utility import DBConnectivity
from validations import Validations
from exceptions import CustomExceptions


def get_password(mobile_number):
    con = DBConnectivity.create_connection()
    db_cursor =  DBConnectivity.create_cursor(con)
    try:
        if Validations.is_user_present(mobile_number):
            sql_statement = "select pwd   from usr where MOB_NO=" + str(mobile_number)
            db_cursor.execute(sql_statement)
            for row in db_cursor:
                db_cursor.close()
                con.close()
                return row[0]
    except CustomExceptions.MobileNumberNotPresent as e:
        print(e)
        db_cursor.close()
        con.close()
        return None

def get_display_name(mobile_number):
    con = DBConnectivity.create_connection()
    db_cursor =  DBConnectivity.create_cursor(con)
    try:
        if Validations.is_user_present(mobile_number):
            sql_statement = "select disp_name    from login where mob_no=" + str(mobile_number)
            db_cursor.execute(sql_statement)
        for row in db_cursor:
                db_cursor.close()
                con.close()
                return row[0]
    except CustomExceptions.MobileNumberNotPresent as e:
        print(e)
        db_cursor.close()
        con.close()
        return None
 
def get_last_login_time(mobile_number):
    con = DBConnectivity.create_connection()
    db_cursor =  DBConnectivity.create_cursor(con)
    try:
        if Validations.is_user_present(mobile_number):
            sql_statement = "select last_login     from login where mob_no=" + str(mobile_number)
            db_cursor.execute(sql_statement)
        for row in db_cursor:
                db_cursor.close()
                con.close()
                return row[0]
    except CustomExceptions.MobileNumberNotPresent as e:
        print(e)
        db_cursor.close()
        con.close()
        return None

        