#using sorted funciton
fruits = ['apple', 'orange', 'banana']

sort=sorted(fruits)

print(sort)

#using sort method

fruits.sort()

print(fruits)

#using bubble sort
n=len(fruits)

for i in range(n):

    for j in range(0,n-1-i):

        if fruits[j]>fruits[j+1]:

            fruits[j],fruits[j+1]=fruits[j],fruits[j+1]

print(fruits)