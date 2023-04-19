import mysql.connector
conn=mysql.connector.connect(host='localhost',password='root',user='root',database='db1')
mycursor=conn.cursor()
# mycursor.execute("CREATE TABLE custumer(id VARCHAR(10),name VARCHAR(15))")
tabs="INSERT INTO custumer(id,name) VALUES (1,'achu'),(2,'achuz'),(3,'ammu'),(4,'annu')"
mycursor.execute(tabs)
conn.commit()
mycursor.execute("SELECT * FROM custumer")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
conn.close()