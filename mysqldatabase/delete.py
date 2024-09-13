import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",

    user="root",

    password="Sudu@2001",

    database="student"
)

cursor=mydb.cursor()

cursor.execute("delete from student where id=13")

mydb.commit()

print(cursor.rowcount)

cursor.execute("select * from student")

result=cursor.fetchall()

for x in result:

    print(x)