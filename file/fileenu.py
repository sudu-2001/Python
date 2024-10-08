word="get"

with open("sud.txt","r") as file:

	for line_number,line in enumerate(file,start=1):

		if word in line:

			print(f"The {word} fornd in file:{file} in the line_number{line_number}")
