num=list(range(1,10))

print(num[:3])

new=[]

count=0

for n in num:
    new.append(n)

    count+=1
    if n==3:
        break

print(new)