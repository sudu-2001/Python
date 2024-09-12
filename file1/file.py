def readfile(filepath):

    with open(filepath,'r') as file:

        file.read()

def writefile(filepath,content):

    with open(filepath,'w') as file:

        file.write(content)

readfile('name.txt')

writefile('name.txt',"hello \nEmployee \nyou have benn created a satarday file")

    