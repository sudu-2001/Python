def rotated(lst,k):

    n=len(lst)

    k=k%n

    rotate=lst[k:]+lst[:k]

    print(rotate)

lst=[1,2,3,4,5] 

k=2

rotated(lst,k)