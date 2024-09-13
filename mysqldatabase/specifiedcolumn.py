import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",

    user="root",

    password="Sudu@2001",

    database="student"
)

cursor=mydb.cursor()

cursor.execute("select name,id from student")

result=cursor.fetchone()

print(result)

