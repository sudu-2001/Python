counter=0

def increment():

    global counter

    counter+=1

    print("counter:",counter)

increment()
increment()

def outer():

    outer_var="modified"

    def inner():

        nonlocal outer_var

        print("inner:",outer_var)

    print("outer:",outer_var)

outer()