numbers = [1, 2, 3, 4, 5]

def multiply(x):
    
    return x*2

result=map(multiply,numbers)

print(list(result))

#addition

list1=[1,2,3]

list2=[4,5,6]

def add(x,y):

    return x+y

result=map(add,list1,list2)

print(list(result))

def divisible(x):

    return x%3==0

result= filter(divisible,numbers)

print(list(result))
    