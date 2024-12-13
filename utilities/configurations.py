"""
import configparser
import mysql.connector
from mysql.connector import Error
from dbDemo import cursor


def getConfig():
    config = configparser.ConfigParser()
    config.read('C:/Users/slobodanka.mihajlov/pytestProjects/BackEndAutomation/utilities/properties.ini')
    return config
# from poperties.ini
connect_config = {
    'user' : getConfig()['SQL']['user'],
    'password' : getConfig()['SQL']['password'],
    'host' : getConfig()['SQL']['host'],
    'database' :getConfig()['SQL']['database'],
}

def getPassword():
    return 'Bfsgsfgsgsg'


def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row
"""
import configparser

import mysql.connector
from mysql.connector import Error
#from dbDemo import cursor



def getConfig():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\slobodanka.mihajlov\\pytestProjects\\BackEndAutomation\\utilities\\properties.ini')
    return config
connect_config = {
    'user' : getConfig()['SQL']['user'],
    'password' : getConfig()['SQL']['password'],
    'host' : getConfig()['SQL']['host'],
    'database' :getConfig()['SQL']['database'],
}


def getPassword():
    return "gdgfdgfdgf"


def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row


