#iteration through thenumpy array
import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10])

for x in arr:

    print(x)

#iteration through the 2d array

arr=np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:

    print(x)

#iteration each dimension of the numpy array

arr=np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:

    for y in x:

        print(y)

#iterate over 3 dimensional array

arr=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:

    for y in x:

        for z in y:

            print(z)

#iterate over scalars

for x in np.nditer(arr):

    print(x)

# iterate over the numpy array containing different data type 

for x in np.nditer(arr,flags=['buffered'],op_dtypes='S'):

    print(x)

# using ndenumerator method the numpy aarray is traversed

for idx,x in np.ndenumerate(arr):

    print(idx,x)