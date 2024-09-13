# to create table called student in the database

import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",

    user="root",

    password="Sudu@2001",

    database="student"
)

cursor=mydb.cursor()

cursor.execute("create table student (id int primary key,name varchar(50),marks float,address varchar(50))")

