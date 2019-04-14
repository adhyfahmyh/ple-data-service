import mysql.connector
from mysql.connector import Error

mySQLconnection = mysql.connector.connect(host='103.28.53.243',
                                          database='plewebid_wp389',
                                          user='plewebid_wp389',
                                          password='plewebid_wp389')


def get_content_id(shortlink):
    try:
        mySQLconnection = mysql.connector.connect(host='103.28.53.243',
                                                  database='plewebid_wp389',
                                                  user='plewebid_wp389',
                                                  password='plewebid_wp389')
        sql_select_Query = "SELECT ID FROM `wpky_posts` WHERE `guid` = '"+shortlink+"'"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        return cursor.fetchone()[0]
    except Error as e:
        print("Error while connecting to MySQL", e)


def is_activity_log_available(username, post_id):
    try:
        mySQLconnection = mysql.connector.connect(host='103.28.53.243',
                                                  database='plewebid_wp389',
                                                  user='plewebid_wp389',
                                                  password='plewebid_wp389')
        sql_select_Query = "SELECT * FROM `selection` WHERE `Username` = '" + \
            username+"' AND `ContentId` = '"+str(post_id)+"'"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        return cursor.fetchone() != None
    except Error as e:
        print("Error while connecting to MySQL", e)


def save_activity_log(username, shortlink, datetime):
    post_id = get_content_id(shortlink)
    save_open_date_activity(username, post_id, datetime)
    if is_activity_log_available(username, post_id):
        try:
            mySQLconnection = mysql.connector.connect(host='103.28.53.243',
                                                      database='plewebid_wp389',
                                                      user='plewebid_wp389',
                                                      password='plewebid_wp389')
            sql_select_Query = "UPDATE selection SET Frequency = Frequency + 1 WHERE `Username` = '" + \
                username+"' AND `ContentId` = '"+str(post_id)+"'"
            cursor = mySQLconnection.cursor()
            cursor.execute(sql_select_Query)
        except Error as e:
            print("Error while connecting to MySQL", e)
    else:
        try:
            mySQLconnection = mysql.connector.connect(host='103.28.53.243',
                                                      database='plewebid_wp389',
                                                      user='plewebid_wp389',
                                                      password='plewebid_wp389')
            sql_select_Query = "INSERT INTO selection (Username, ContentId, Frequency) VALUES ('" + \
                username+"', '"+str(post_id)+"', '1')"
            cursor = mySQLconnection.cursor()
            cursor.execute(sql_select_Query)
        except Error as e:
            print("Error while connecting to MySQL", e)


def save_open_date_activity(username, content_id, datetime):
    try:
        mySQLconnection = mysql.connector.connect(host='103.28.53.243',
                                                  database='plewebid_wp389',
                                                  user='plewebid_wp389',
                                                  password='plewebid_wp389')
        sql_select_Query = "INSERT INTO `active_time`(`Username`, `ContentId`, `Time_In`) VALUES ('" + \
            str(username)+"', '"+str(content_id)+"', '"+str(datetime)+"')"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
    except Error as e:
        print("Error while connecting to MySQL", e)


def is_activity_date_available(username, post_id):
    try:
        mySQLconnection = mysql.connector.connect(host='103.28.53.243',
                                                  database='plewebid_wp389',
                                                  user='plewebid_wp389',
                                                  password='plewebid_wp389')
        sql_select_Query = "SELECT * FROM `active_time` WHERE `Username` = '" + \
            username+"' AND `ContentId` = '"+str(post_id)+"'"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        return cursor.fetchone() != None
    except Error as e:
        print("Error while connecting to MySQL", e)


def save_close_date_activity(username, shortlink, datetime):
    print("Closed")
    post_id = get_content_id(shortlink)
    try:
        mySQLconnection = mysql.connector.connect(host='103.28.53.243',
                                                  database='plewebid_wp389',
                                                  user='plewebid_wp389',
                                                  password='plewebid_wp389')
        sql_select_Query = "UPDATE `active_time` SET `Time_Out`=NOW() WHERE `Username`='" + \
            str(username)+"' AND `ContentId`='"+str(post_id) + \
            "' AND `Time_In`='"+str(datetime)+"'"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
    except Error as e:
        print("Error while connecting to MySQL", e)
