import mysql.connector
from mysql.connector import Error

def save_activity_log():
    try:
        mySQLconnection = mysql.connector.connect(host='103.28.53.243',
                                    database='plewebid_wp389',
                                    user='plewebid_wp389',
                                    password='plewebid_wp389')
        sql_select_Query = "INSERT INTO selection (UserId, ContentId, Frequency) VALUES ('2', '2', '3')"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            print("MySQL connection is closed")
