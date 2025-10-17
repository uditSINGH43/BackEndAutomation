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
    return os.getenv("GITHUB_TOKEN")

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
