with open('sud.txt','r') as file:

	longest=""

	line=file.read()

	lines=line.split()

	print(lines)

	for c in lines:

		if(len(c)>len(longest)):

			longest=c


	print("The length of longest word :",len(longest))

	print("The longest word in file is :",longest)
