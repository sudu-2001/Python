# syntax of labda lambda arguments : expression

x=lambda a: a*2

print(x(3))

# sending with two parameters

x=lambda x,y:x*y

print(x(5,6))

# lambda inside function

def add(x,y):

    return lambda x,y:x+y

y=add(5,4)

print(y)

