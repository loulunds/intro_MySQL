import os
import pymysql

#Get username from workspace
username = os.getenv('GITPOD_USER')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    with connection.cursor() as cursor:
        sql = 'select * from Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()