#filtering array by using the boolean list

import numpy as np

arr=np.array([42,32,54,2])

x=[True,False,True,True]

newarr=arr[x]

print(newarr)



