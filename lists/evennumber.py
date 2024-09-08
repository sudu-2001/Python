list=list(range(1,10))

even=[]

for num in list:
    if num%2==0:
        even.append(num)

print(even)

# method 2

eve=[num for num in list if num%2==0]

print(eve)
