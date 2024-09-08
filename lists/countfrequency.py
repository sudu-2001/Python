#using for loop
lst = [1, 2, 2, 3, 4, 4, 4, 5]

dict={}

for item in lst:

    if item in dict:

        dict[item]+=1

    else:

        dict[item]=1

print(dict)