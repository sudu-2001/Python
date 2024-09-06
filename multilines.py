with open('cat.txt','w') as file:
    lines=["hi greeting","good afternoon"]
    for line in lines:
        file.write(line + "\n")