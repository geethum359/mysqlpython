import mysql.connector
conn=mysql.connector.connect(host='localhost',password='root',user='root')
mycursor=conn.cursor()
mycursor.execute("CREATE DATABASE db1")

conn.commit()
conn.close()