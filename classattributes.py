class instancecounter:
    count=0

    name="sudarshan"

    def __init__(self):
        instancecounter.count+=1

obj1=instancecounter()

obj2=instancecounter()

obj3=instancecounter()

print(instancecounter.count)

print(obj1.count)

print(obj1.name)

obj1.name="kosudarshan"

print(obj1.name)