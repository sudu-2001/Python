with open('one.txt','r') as file:

	content1=file.read()

with open('two.txt','r') as file:

	content2=file.read()

with open('three.txt','w') as file:

	file.write(content1)

	file.write(content2)
