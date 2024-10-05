import mysql.connector

def conn_db():

	return mysql.connector.connect(

	host="localhost",

	user="root",

	password="Sudu@2001",

	database="school"

	)

def create_tb(conn):

	cursor=conn.cursor()

	table_query="create table if not exists teacher(id int AUTO_INCREMENT primary key,name varchar(50),age varchar(50));"

	cursor.execute(table_query)

	conn.commit()

	print("Table has been created successfully!")

	cursor.close()

def insert_tb(conn):

	cursor=conn.cursor()

	print("Enter the details for the Teacher: ")

	name=input("Enter your name:")

	age=input("Enter your age:")

	insert_query="insert into teacher (name,age) values(%s,%s);"

	cursor.execute(insert_query,(name,age))

	conn.commit()

	print("record entered into table successfully!")

def update_tb(conn):

	cursor=conn.cursor()

	id=int(input("Enter the id to update the table: "))

	name=input("Enter the name to update: ")

	update_query="update teacher set name=%s where id=%s;"

	cursor.execute(update_query,(id,name))

	conn.commit()

	print("Successfully updates table!")

def delete_tb(conn):

	cursor=conn.cursor()

	id=int(input("Enter the id to delete record from table"))

	delete_query="delete from teacher where id=%s"

	cursor.execute(delete_query,(id,))

	conn.commit()

	print("Record is successfully deleted from the table!")

def search_tb(conn):

	cursor=conn.cursor()

	name=input("Enter the name to search: ")

	search_query="Select * from teacher where name Like %s;"

	cursor.execute(search_query,('%' +name+ '%',))

	results=cursor.fetchall()

	if results:

		for row in results:

			print(f"name:{row[0]}\nage:{row[1]}\nid:{row[2]}")

	cursor.close()

def main():

	conn=conn_db()

	while True:

		print("1. create table.\n2.Insert table.\n3.update table.\n4.delete record\n5.serach.")

		try:

			ch=int(input("Enter choice:"))

		except ValueError:

			print("Invalid choice,Try again")

			continue

		if ch==1:

			create_tb(conn)

		elif ch==2:

			insert_tb(conn)


		elif ch==3:

			update_tb(conn)

		elif ch==4:

			delete_tb(conn)

		elif ch==5:

			search_tb(conn)

		elif ch==6:

			conn.close()

			print("Disconnecting")

			break

if __name__=="__main__":

	main()
