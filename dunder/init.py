class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print(f"name:{self.name},id:{self.id}")

p=person("alice",1)

print(p.display())