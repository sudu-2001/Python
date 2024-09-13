# to fetch all the records from the table we will be using a method called fetchall

import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",

    user="root",

    password="Sudu@2001",

    database="student"
)

cursor=mydb.cursor()

cursor.execute("select * from student")

myresult=cursor.fetchall()

for x in myresult:

    print(x)