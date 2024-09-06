with open('file.txt','r') as file:
    content=file.read()
reverse=content[::-1]
with open('reverse.txt','w') as file:
    file.write(reverse)
    
