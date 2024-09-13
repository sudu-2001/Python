# to know the databases in mysql

import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",

    user="root",

    password="Sudu@2001"

)

mucursor=mydb.cursor()

mucursor.execute("show databases")

for x in mucursor:

    print(x)