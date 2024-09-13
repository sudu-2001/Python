# to create a database in the mysql we will use cursor object where it will call execute method

import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",

    user="root",
    
    password="Sudu@2001"
)

print(mydb)

cursor=mydb.cursor()

cursor.execute("create database student")
