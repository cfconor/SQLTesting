import pymysql


# Get username
username = 'root'


# Connect to DB
connection = pymysql.connect(host='localhost', user=username, db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        rows = [("Bob", 21, "1990-03-25 13:23:54"),
                ("Jim", 331, "1990-03-22 13:23:54"),
                ("Fred", 31, "1990-03-21 13:23:54")]
        cursor.executemany("""INSERT INTO Friends VALUES (%s, %s, %s);""",
                           rows)
        connection.commit()
finally:
    # close the connection
    connection.close()
