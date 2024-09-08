#using set method will remove the duplicate values from the list

dat1=[1,2,2,3,3,4,4,5,6,6]

# list is converted into set and again converted into list

unique=list(set(dat1))

print(unique)

#using for loop

duplicate=[]

seen=set()

for item in dat1:

    if item in seen:

        duplicate.append(item)

    else:

        seen.add(item)

print(duplicate)