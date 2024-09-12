#open file in read mode

#with open("dam.txt",'x') as file:

#    x=file.read

#    print(x)

with open("dam.txt",'w') as file:

    y=file.writelines("hello \nmy name is xyz\nworking in xyz company")

    print(y)

#append mode will create a file if the file doesnt exist and it will be created 

with open("sud.txt",'a') as file:

    file.write("hello")

#write the data into the file with write and read mode

with open("name.txt","r+") as file:

    file.read()

    data="my name"

    file.write(data)

#read the file in binary format

with open("1.png",'rb') as file:

    content=file.read()

    print(content)