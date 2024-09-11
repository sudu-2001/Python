# to find out the version of an array

import numpy as np

print(np.__version__)

# to find out the shape of an array

arr=np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

#reshape of 1d array to 2d array

arr=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


print(arr.reshape(3,4))

#reshape array 1d to 3d array

arr=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(arr.reshape(2,3,2))