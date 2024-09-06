with open('reverse.txt','r') as file:
    content=file.read()
    print(content.lower().split().count('hi'.lower()))