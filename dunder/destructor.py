class person:
    
    def __init__(self,name):
        self.name=name

    def __del__(self):
        print(f"the name:{self.name} has to be destroyed")

p=person("alice")

del person