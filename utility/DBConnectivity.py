'''
Created on Oct 16, 2015

@author: shamsher.ahmed
'''
import cx_Oracle
def create_connection():
    return cx_Oracle.Connection('T709988/T709988@10.123.79.56/GEORLI01')

def create_cursor(con):
    return cx_Oracle.Cursor(con)