import configparser
import os

import mysql.connector
from mysql.connector import Error

def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config
connect_config = {
    'user' : getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password'],
    'database': getConfig()['SQL']['database'],
    'host': getConfig()['SQL']['host'],


}


def getPassword():
    return "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"

def getConnection():
    try:
        mydb = mysql.connector.connect(**connect_config)
        if mydb.is_connected():
            print("Connection established")
            return mydb
    except Error as e:
        print(e)



def getQuery(query):
    mydb = getConnection()
    cursor = mydb.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    mydb.close()
    return row
