with open("three.txt","r") as file:

	word_count=0

	content=file.read()

	line=content.split()

	for lines in line:

		word_count+=1

	print(word_count)
