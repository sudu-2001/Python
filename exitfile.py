with open('example.txt','w') as file:
    while True:
        user_input=input(print("enter the text"))
        if user_input.lower() == 'exit':
            break
        file.write(user_input)