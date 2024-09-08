words = ["apple", "banana", "apple", "orange", "banana", "apple"]

dict={}

for item in words:

    if item in dict:

        dict[item]+=1

    else:

        dict[item]=1

print(dict)