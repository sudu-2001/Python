import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",

    user="root",

    password="Sudu@2001",

    database="student"
)

cursor=mydb.cursor()

cursor.execute("drop table courses")

cursor.execute("show tables")

for x in cursor:

    print(x)