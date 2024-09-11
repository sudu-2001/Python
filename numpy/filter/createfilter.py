import numpy as np

arr=np.array([41, 42, 43, 44])

filter_arr=[]

for x in arr:

    if x>42:

        filter_arr.append(True)

    else:

        filter_arr.append(False)

new_arr=arr[filter_arr]

print(filter_arr)

print(new_arr)

#with out using for loop

filter = arr>42

newarr=arr[filter]

print(filter)

print(newarr)