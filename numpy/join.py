#joining the two arrays 

import numpy as np

arr1=np.array([1, 2, 3])

arr2=np.array([4, 5, 6])

arr=np.concatenate((arr1,arr2))

print(arr)

#concatenate the two arrays of 2 dimensional arrays

arr1=np.array([[1, 2], [3, 4]])

arr2=np.array([[5, 6], [7, 8]])

arr=np.concatenate((arr1,arr2))

print(arr)

#concatenate 2 1d array by using stack method

arr1=np.array([1, 2, 3])

arr2=np.array([4, 5, 6])

arr=np.stack((arr1,arr2),axis=1)

print(arr)

# concatenate 2 arrays along with the 2 arrays stacked over columns

arr1=np.array([1, 2, 3])

arr2=np.array([4, 5, 6])

arr=np.hstack((arr1,arr2))

print(arr)

#concatenate 2 arrays staked over columns

arr1=np.array([1, 2, 3])

arr2=np.array([4, 5, 6])

arr=np.vstack((arr1,arr2))

print(arr)

