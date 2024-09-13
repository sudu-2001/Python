# to connect for the database import the the module name connector where it will take the parameters such as host,username,password

import mysql.connector

myd=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Sudu@2001"

)

print(myd)