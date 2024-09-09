# *args: it will take many number of arguments **kwargs:It will take many numbers of keword arguments

def print_info(*args,**kwargs):

    print("argument:",args)

    print("key word argument:",kwargs)


print_info(1,2,3,4,name="alice",id=1)