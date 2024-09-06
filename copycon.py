with open('cat.txt','r') as file:
    content=file.read()
with open('reverse.txt','w') as file:
    file.write(content)