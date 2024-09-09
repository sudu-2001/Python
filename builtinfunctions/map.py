def square(x):

    return x*x

numbers=[1,2,3,4,5,6]

result=map(square,numbers)

print(list(result))

# add two lists

def add(x,y):

    return list1+list2

list1=[1,2,3,4]

list2=[4,5,6,7]

result=map(add,list1,list2)

print(list(result))

# lambda inside map

list1=[1,2,3,4]

y=map(lambda x: x*x,list1)

print(list(y))

# string to integer

list1=['1','2','3','4']

result=map(int,list1)

print(list(result))

#normalize the values

list1=[5,10,15.20,25]

def normalize(x,mini,maxi):

    return (x-mini)/(maxi-mini)

mini=min(list1)

maxi=max(list1)

result=map(lambda x:normalize(x,mini,maxi),list1)

print(list(result))