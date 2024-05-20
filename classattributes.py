class instancecounter:
    count=0

    def __init__(self):
        instancecounter.count+=1

obj1=instancecounter()

obj2=instancecounter()

obj3=instancecounter()

print(instancecounter.count)

print(obj1.count)