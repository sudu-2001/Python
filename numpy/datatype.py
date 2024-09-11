#converting the array into string data type

import numpy as np

arr=np.array([1, 2, 3, 4],dtype='S')

print(arr)

#string datatype

arr=np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

# convert the array from one data type to another by using as type method

arr=np.array([1, 2, 3, 4])

arr_float=arr.astype(float)

print(arr_float.dtype)

print(arr.dtype)

# convert the array into boolean type

arr=np.array([1, 2, 0, 0])

bool=arr.astype(bool)

print(bool)

#copy any changes done to copy array and original array it eill not affect the both of the array

arr=np.array([1, 2, 0, 0])

x=arr.copy()

arr[0]=42

print(x)

print(arr)

#view any changes done to copy and original array will affect both the array

arr=np.array([1, 2, 0, 0])

y=arr.view()

arr[0]=32

print(y)

# to check weather it owns the data

arr=np.array([1, 2, 0, 0])

y=arr.view()

x=arr.copy()

print(x.base)

print(y.base)

