# Generator : is a function used to create the iterators

def count_up(max):

    count=0

    while count<=max:

        yield count

        count+=1


for x in count_up(5):

    print(x)

# Using tuple comprehensio

x=(x*x for x in range(10))

for y in x:

    print(y)