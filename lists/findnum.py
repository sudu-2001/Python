#method:1 with using in operator

number=list(range(1,10))

if 3 in number:
    print("number is present in the list")

else:
    print("number is not present in the list")


#method2:2 with using a for loop

found='false'

for num in number:
    if num==3:
        found=True
        break

if found:
    print("number is present")

else:
    print("number is not present")