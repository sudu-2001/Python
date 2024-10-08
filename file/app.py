with open("three.txt","a") as file:

	n=int(input("Enter the range of an array: "))

	arr=[]

	for i in range(0,n):

		name=input("Enter the name: ")

		arr.append(name)

	print(arr)

	for name in arr:

		file.write(name)
