#split the array into 3 arrays

import numpy as np

arr=np.array([1, 2, 3, 4, 5, 6])

x=np.array_split(arr,3)

print(x)

print(x[0])

print(x[1])

print(x[2])

#if the elements are not satisified in the array the it will incorporate only one element into the sub arrays

arr=np.array([1, 2, 3, 4, 5, 6])

x=np.array_split(arr,4)

print(x)

# split the 2d arrays into 2d arrays

arr=np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

x=np.array_split(arr,3)

print(x)

# split the array into single column stack

arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

x=np.hsplit(arr,3)

print(x)

