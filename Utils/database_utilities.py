import mysql.connector as connector

from Utils.common_utilities import parseConfigurationFile


def connect_database(sql_query):
    try:
        con = connector.connect(host=parseConfigurationFile()['DB_HOST'],
                                user=parseConfigurationFile()['DB_USER'],
                                password=parseConfigurationFile()['DB_PASSWORD'],
                                port=parseConfigurationFile()['DB_PORT'],
                                database=parseConfigurationFile()['DB_NAME'])
        con.autocommit(False)
        temp_Query = str(sql_query).split(" ")[0]
        if temp_Query.lower() is "insert" or temp_Query.lower() is "update" or temp_Query.lower() is "delete":
            con_cursor = con.cursor()
            con_cursor.execute(sql_query)
            con.commit()
            return True
        elif temp_Query.lower() is "select":
            con_cursor = con.cursor()
            con_cursor.execute(sql_query)
            return con_cursor.fetchall()
        else:
            print("Failed Connecting database")
            exit(1)
    except connector.Error as err:
        print("Failed creating database: {err}")
        exit(1)
