#without using built in function

number=list(range(1,10))

new_number=[]

for num in number:
    if num != 5:
        new_number.append(num)

print (new_number) 

#with using built in function

number.remove(5)
print(number)