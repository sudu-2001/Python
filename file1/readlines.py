def readfile(filepath):

    with open(filepath,'r') as file:

        x=file.readlines()

        y=file.readline()

        print(x)

readfile("name.txt") 

# to count the number of lines in the file

with open("name.txt",'r') as file:

    linecount=0

    file=file.read()

    for line in file:

        linecount+=1

    print(linecount)


