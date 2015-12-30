'''
Created on Oct 20, 2015

@author: vikas.yadav09
'''
from utility import DBConnectivity

def checkchat_DB(obj):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select count(*) from chatlog where sender=:mob_sender or receiver=:mob_receiver",
                    {"mob_sender":obj.get_mobile_number(),"mob_receiver":obj.get_mobile_number()})
        for row in cur:
            count=row[0];
        contactlist=[];
        if(count!=0):
            cur.execute("select sender from chatlog where receiver=:mob_receiver union select receiver from chatlog where sender=:mob_sender",
                        {"mob_sender":obj.get_mobile_number(),"mob_receiver":obj.get_mobile_number()})
            for row in cur:
                contactlist.append(row[0])
    finally:
        cur.close()
        con.close()
        return contactlist
    
def fetch_dispname(obj,contactlist):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        contactname=[]
        for val in contactlist:
            cur.execute("select nvl(disp_name,mob_no) from usr where mob_no=:mob",{"mob":val})
            for row in cur:
                contactname.append(row[0])
    finally:
        cur.close()
        con.close()
        return contactname
def get_UnreadCount(obj,contactlist):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        countlist=[0]*len(contactlist)
        for i in range(0,len(contactlist)):
            
            cur.execute("select count(message) from chatlog where status='U' group by sender,receiver having receiver="+contactlist[i])
            for row in cur:
                countlist[i]=row[0]
    finally:
        cur.close()
        con.close()
        return countlist
def check_receiver(receiver):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        flag=0;
        cur.execute("select count(*) from usr where mob_no="+receiver)
        for row in cur:
            count=row[0]
    except:
        print("Enter a Valid number")
        flag=1;
    finally:
        cur.close()
        con.close()
        if(flag!=1):
            if(count==1):
                return True;
            else:
                return False;
        else:
            return 
def update_status(obj):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        print(obj.get_receiver(),"-----",obj.get_mobile_number())
        cur.execute("update chatlog set status='R' where receiver="+str(obj.get_receiver())+ " and sender="+str(obj.get_mobile_number()));
    finally:
        cur.close()
        con.commit()
        con.close();
def get_conversation(obj):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select sender,message,to_char(messagetime,'Dy'),to_char(messagetime,'HH:mi'),to_char(messagetime,'dd-mon'),to_date(to_char(sysdate,'dd-mon-yyyy'))-to_date(to_char(messagetime,'dd-mon-yyyy')) from chatlog where (sender=:sender and receiver=:receiver) or (sender=:receiver and receiver=:sender) order by messagetime",{"sender":obj.get_mobile_number(),"receiver":obj.get_receiver()})
        converlist=[]
        daylist=[];
        timelist=[];
        no_dayslist=[];
        senderlist=[]
        datelist=[]
        for sender,message,day,time,date,no_days in cur:
            senderlist.append(sender)
            converlist.append(message)
            daylist.append(day)
            timelist.append(time)
            datelist.append(date)
            no_dayslist.append(no_days)
    finally:
        cur.close()
        con.close()
        
        for index in range(len(senderlist)):
            string=""
            print("...................................................................................................")
            if(str(senderlist[index])==str(obj.get_mobile_number())):
                string+="Me -> ";
            else:
                string+=str(senderlist[index])
                
            if(int(no_dayslist[index])==1):
                string+="Yesterday, at ";
            elif(int(no_dayslist[index])==0):
                string+="Today, at ";
            else:
                string+=" "+str(daylist[index])+","+str(datelist[index])+", at" 
            string+=str(timelist[index])
            print(string)
            print()
            print(converlist[index])
        return
def insert_userchat(obj):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("insert into chatlog(sender,receiver,message,status) values(:sender,:receiver,:message,:status)",
                    {"sender":obj.get_mobile_number(),"receiver":obj.get_receiver(),"message":obj.get_message(),"status":"U"})
    finally:
        con.commit()
        print("Message Sent")
        cur.close()
        con.close();              
        