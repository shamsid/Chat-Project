'''
Created on Oct 16, 2015

@author: vikas.yadav09
'''
from utility import DBConnectivity;
from exceptions import CustomExceptions
from validations import Validations
import cx_Oracle
def update_table_usr(user):
    try:
        con=DBConnectivity.create_connection();
        cur=DBConnectivity.create_cursor(con);
        cur.execute("Insert into usr values("+user.get_mob_no()+",'"+user.get_pwd()+"','"+user.get_dob()+"','"+user.get_disp_name()+"','"+user.get_sec_ques()+"','"+user.get_sec_ans()+"')");
        cur.execute("Insert into pwd_check values("+user.get_mob_no()+",'"+user.get_pwd()+"','""','""')")
        cur.execute("Insert into login (mob_no,disp_name) values("+user.get_mob_no()+",'"+user.get_disp_name()+"')")
        con.commit()
        return True;
    except cx_Oracle.IntegrityError as e:
        print("Mobile Number Already Registered");
    finally:
        cur.close()
        con.close()
def get_user_information(mob_no):
    try:
        con=DBConnectivity.create_connection();
        cur=DBConnectivity.create_cursor(con);
        usr_data_list=[];
        cur.execute("select mob_no,dob,sec_ques,sec_ans,pwd from usr where mob_no="+str(mob_no));
        for row in cur:
            mobile_number=row[0];
            dob=row[1];
            sec_ques=row[2];
            sec_ans=row[3];
            pwd=row[4];
            usr_data_list.append(mobile_number)
            usr_data_list.append(dob)
            usr_data_list.append(sec_ques)
            usr_data_list.append(sec_ans)
            usr_data_list.append(pwd)
        return usr_data_list;
    finally:
        cur.close()
        con.close()
def update_password(user,mob_no):
    new_pwd=user.get_pwd()
    try:
        con=DBConnectivity.create_connection();
        cur2=DBConnectivity.create_cursor(con);
        cur2.execute("Update usr set pwd='"+new_pwd+"' where mob_no="+str(mob_no));
        return True
    finally:
        cur2.close()
        con.commit()
        con.close()
        
def update_password_check(user,password_list,mob_no):
    new_pwd=user.get_pwd();
    try:
        con=DBConnectivity.create_connection();
        cur5=DBConnectivity.create_cursor(con);
        cur5.execute("update pwd_check set old_pwd1=:p1,old_pwd2=:p2,old_pwd3=:p3 where mob_no=:no",
                     {"p1":password_list[1],"p2":password_list[2],"p3":new_pwd,"no":str(mob_no)})
        return True;
    finally:
        cur5.close()
        con.commit()
        con.close();
def get_password(mobile_number):
    con = DBConnectivity.create_connection()
    db_cursor =  DBConnectivity.create_cursor(con)
    try:
        if Validations.is_user_present(mobile_number):
            sql_statement = "select pwd   from usr where MOB_NO=" + str(mobile_number)
            db_cursor.execute(sql_statement)
            for row in db_cursor:
                return row[0]
    except CustomExceptions.MobileNumberNotPresent as e:
        print(e)
        return None
    finally:
        db_cursor.close()
        con.close()
def get_display_name(mobile_number):
    con = DBConnectivity.create_connection()
    db_cursor =  DBConnectivity.create_cursor(con)
    try:
        if Validations.is_user_present(mobile_number):
            sql_statement = "select disp_name,mob_no    from login where mob_no=" + str(mobile_number)
            db_cursor.execute(sql_statement)
        for row in db_cursor:
            if row[0] !=None:
                return row[0]
            else:
                return row[1]
    except CustomExceptions.MobileNumberNotPresent as e:
        print(e)
        return None
    finally:
        db_cursor.close()
        con.close()
def get_last_login_day(mobile_number):
    con = DBConnectivity.create_connection()
    db_cursor =  DBConnectivity.create_cursor(con)
    try:
        if Validations.is_user_present(mobile_number):
            sql_statement="select case when to_char(last_login ,'yyyy-mm-dd')=to_char(systimestamp,'yyyy-mm-dd') then 'today' when to_char(last_login ,'yyyy-mm-dd')=to_char(systimestamp-1,'yyyy-mm-dd') then 'yesterday' else to_char(last_login,'Dy, dd Mon') end from login where mob_no="+str(mobile_number)
            db_cursor.execute(sql_statement)
        for row in db_cursor:
                return row[0]
    except CustomExceptions.MobileNumberNotPresent as e:
        print(e)
    finally:
        db_cursor.close()
        con.close()
def insert_login_timestamp_into_database(mobile_number):
    sql_statment = "update login set last_login = systimestamp where mob_no = " +str(mobile_number)
    con = DBConnectivity.create_connection()
    db_cursor =  DBConnectivity.create_cursor(con)
    try:
        db_cursor.execute(sql_statment)
    except CustomExceptions.MobileNumberNotPresent as e:
        print(e)
    finally:
        con.commit()
        db_cursor.close()
        con.close()
def get_last_login_time(mobile_number):
    sql_statement = "select to_char(last_login,'hh:mi:ss')from login where mob_no=" + str(mobile_number)
    con = DBConnectivity.create_connection()
    db_cursor =  DBConnectivity.create_cursor(con)
    try:
        db_cursor.execute(sql_statement)
        for row in db_cursor:
                return row[0]
    except CustomExceptions.MobileNumberNotPresent as e:
        print(e)
    finally:
        db_cursor.close()
        con.close()
        
def validate_forget_pwd(mob_no):
    usr_data_list=get_user_information(mob_no);
    if(len(usr_data_list)==0):
        pass
    return usr_data_list; 

        
def get_blocked_status(mobile_number):
    sql_statements = "select blocked_status from login where mob_no =" + str(mobile_number)
    con = DBConnectivity.create_connection()
    db_cursor =  DBConnectivity.create_cursor(con)
    try:
        if Validations.is_user_present(mobile_number):
            
            db_cursor.execute(sql_statements)
            for row in db_cursor:
                return row[0]
    except CustomExceptions.MobileNumberNotPresent as e:
            print(e)
    finally:
            db_cursor.close()
            con.close()

def change_blocked_status(mobile_number, status):
    sql_statements = "Update login set blocked_status='"+status+"'where mob_no="+str(mobile_number)
    try:
        con = DBConnectivity.create_connection()
        db_cursor =  DBConnectivity.create_cursor(con)
        db_cursor.execute(sql_statements)
    except CustomExceptions.MobileNumberNotPresent as e:
        print(e)
    finally:
        con.commit()
        db_cursor.close()
        con.close()
        