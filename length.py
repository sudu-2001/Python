with open('file.txt','r') as file:
    for line in file:
        print(f"length of each line{len(line.split())}")