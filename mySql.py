import pymysql


# Get username
username = 'root'


# Connect to DB
connection = pymysql.connect(host='localhost', user=username, db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close the connection
    connection.close()
