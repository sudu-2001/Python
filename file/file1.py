import os

with open('sud.txt','w') as file:

	file.writelines("Hello world\nI am there to live and conquer and do some adventeourous things\nso get out of my way")

with open ('sud.txt','r') as file:

	lines=file.readlines()

	wordcount=0

	for line in lines:

		words=line.split()

		print(words)

		for x in words:

			wordcount +=1

	print(wordcount)

#to read the content of files in reverse order

with open('sud.txt','r') as file:

	lines=file.readlines()

	lines.reverse()

	for line in lines:

		print(line)

#size of the file

	filesize=os.path.getsize("/home/sudarshan/practice/file/sud.txt")

	print(f"The size of file path is: {filesize}")
