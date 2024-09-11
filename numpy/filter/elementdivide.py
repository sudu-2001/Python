import numpy as np

arr=np.array([1, 2, 3, 4, 5, 6, 7])

filter=[]

for x in arr:

    if x%2==0:

        filter.append(True)

    else:

        filter.append(False)

newarr=arr[filter]

print(filter)

print(newarr)

#with out using for loop

filter=arr%2==0

newarr=arr[filter]

print(filter)

print(newarr)

