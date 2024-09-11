#array creation

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,9,10,11,12,1,3,14,15,16])

print(arr)

# n dimension array

arr=np.array([1,2,3,4],ndmin=5)

print(arr)

print("the dimension of the array",arr.ndim)

#accessing the element from the numpy array

arr=np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('the 2and last element is:',arr[1][4])

#accessing the element from 2 dimensional array 

arr=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0,1,2])

#accessing element from the last 

arr=np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(arr[1,-1])

#access element from the both of the array

arr=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1,1:4])

#data type of an array

print(arr.dtype)
