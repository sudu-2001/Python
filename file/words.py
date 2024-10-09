with open("sud.txt",'r') as file:

	word_count=0

	for i in file:

		lines=i.split()

		word_count+=len(lines)

	print("The total words in file: ",word_count)
