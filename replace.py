with open('file.txt', 'r') as file:
    content = file.read()
modified_content = content.replace('world','hello')
with open('file.txt', 'w') as file:
        file.write(modified_content)