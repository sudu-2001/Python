import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",

    user="root",

    password="Sudu@2001",

    database="student"

)

cursor=mydb.cursor()

cursor.execute("update student set marks=97 where id=7")

mydb.commit()

cursor.execute("select * from student")

result=cursor.fetchall()

print(result)