with open("sud.txt",'r') as file:

	longestword=""

	line=file.read()

	lines=line.split()

	print(line)

	for c in lines:

		if len(c)>len(longestword):

			longestword=c

	print(longestword)
