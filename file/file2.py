with open("sud.txt","r") as file:

	line_count=0

	char_count=0

	for lines in file:

		line_count+=1

		char_count+=len(lines)

print(f"The total number of lines in {file} file is:{line_count}")

print(f"The total number of charecters in {file} file is:{char_count}")
