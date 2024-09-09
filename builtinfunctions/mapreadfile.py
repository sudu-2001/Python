# map function can be used by opening a file called cat.txt

def readline(line):

    return line.strip().upper()

file=open('cat.txt','r')

line=file.readlines()

y=map(readline,line)

print(list(y))
