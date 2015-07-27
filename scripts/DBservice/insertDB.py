import mysql.connector

cnx = mysql.connector.connect(user='root', password='123',
                              host='127.0.0.1',
                              database='myDB')
cur = cnx.cursor()
cur.execute("SELECT * FROM user")
for response in cur:
    print(response)
cur.close()
cnx.close()
