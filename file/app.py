with open('three.txt','a') as file:

	n=int(input("Enter the array range: "))

	arr=[]

	for i in range(0,n):

		i=input("The array elements are: ")

		arr.append(i)

	for name in arr:

		file.write(name)
