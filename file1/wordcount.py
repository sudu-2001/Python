#to count the number of words in a file

with open("name.txt",'r') as file:

    wordcount=0

    for line in file:

        words=line.split()

        for x in words:

            wordcount+=1

print(wordcount)

# to count the number of word in a file

with open("name.txt",'r') as file:

    x=file.read()

    print(len(x))

# to count the unique charecters in the file

with open("name.txt",'r') as file:

    unique=set()

    for line in file:

        a=line.split()

        for word in a:

            unique.add(word)

print(len(unique))

#count the specific word in a file

word=0

with open("name.txt",'r') as file:

    target="hello"

    for line in file:

        if target in line:

            word+=1

print(word)


