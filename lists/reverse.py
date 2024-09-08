#using slicing method
num=list(range(1,11))

n=num[::-1]

print(n)

#using for loop
reverse=[]

for i in range(len(num)-1,-1,-1):

    reverse.append(num[i])

print(reverse)

