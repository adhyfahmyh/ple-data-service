import mysql.connector
from mysql.connector import Error
try:
   mySQLconnection = mysql.connector.connect(host='103.28.53.243',
                             database='plewebid_wp389',
                             user='plewebid_wp389',
                             password='plewebid_wp389')
   sql_select_Query = "INSERT INTO selection (UserId, ContentId, Frequency) VALUES ('2', '2', '3')"
   cursor = mySQLconnection .cursor()
   cursor.execute(sql_select_Query)
   records = cursor.fetchall()
   print("Total number of rows in python_developers is - ", cursor.rowcount)
   print ("Printing each row's column values i.e.  developer record")
   for row in records:
       print("Id = ", row[0], )
       print("Name = ", row[1])
       print("Freq  = ", row[2])
   cursor.close()
   
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(mySQLconnection.is_connected()):
        mySQLconnection.close()
        print("MySQL connection is closed")