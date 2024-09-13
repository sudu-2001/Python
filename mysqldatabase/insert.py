import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",

    user="root",

    password="Sudu@2001",

    database="student"
)

print(mydb)

cursor=mydb.cursor()

sql="insert into student (id,name,marks,address) values(%s,%s,%s,%s)"

val=[
    (1, 'Peter', 85, 'Lowstreet 4'),
    (2, 'Amy', 90, 'Apple st 652'),
    (3, 'Hannah', 75, 'Mountain 21'),
    (4, 'Michael', 88, 'Valley 345'),
    (5, 'Sandy', 80, 'Ocean blvd 2'),
    (6, 'Betty', 92, 'Green Grass 1'),
    (7, 'Richard', 76, 'Sky st 331'),
    (8, 'Susan', 89, 'One way 98'),
    (9, 'Vicky', 77, 'Yellow Garden 2'),
    (10, 'Ben', 84, 'Park Lane 38'),
    (11, 'William', 91, 'Central st 954'),
    (12, 'Chuck', 73, 'Main Road 989'),
    (13, 'Viola', 86, 'Sideway 1633')
]

cursor.executemany(sql,val)

mydb.commit()