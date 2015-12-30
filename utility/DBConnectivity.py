'''
Created on Oct 16, 2015

@author: shamsher.ahmed
'''
import cx_Oracle
def create_connection():
    return cx_Oracle.Connection('Database Connection Path')

def create_cursor(con):
    return cx_Oracle.Cursor(con)
