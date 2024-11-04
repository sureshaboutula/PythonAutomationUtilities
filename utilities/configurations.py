import configparser
import mysql.connector
from mysql.connector import Error

def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

connectdb_config = {
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password'],
    'host' : getConfig()['SQL']['host'],
    'database' : getConfig()['SQL']['database']
}

def getPassword():
    return "Suresh@2789"

def getdbConnection():
    try:
        conn = mysql.connector.connect(**connectdb_config)
        if conn.is_connected():
            print("connection successful")
            return conn
    except Error as e:
        print(e)

def getQuery(query):
    conn = getdbConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()

