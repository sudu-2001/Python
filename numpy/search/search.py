# by using where method it will return the index of the array

import numpy as np

arr=np.array([1, 2, 3, 4, 5, 4, 4])

x=np.where(arr==4)

print(x)

#divide by 2 

y=np.where(arr%2)

print(y)

# searched sort will perform binary search

arr=np.array([6, 7, 8, 9])

x=np.searchsorted(arr,7)

print(x)

# search an element from the right side

arr=np.array([6, 7, 8, 9])

x=np.searchsorted(arr,7,side='right')

print(x)

#insert multiple values into an array where it will return the index

arr=np.array([1, 3, 5])

x=np.searchsorted(arr,[2,4,6])

print(x)
