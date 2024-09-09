class person:

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def __str__(self):
        return f"name={self.name}, age={self.id}"

    def __repr__(self):
        return f"name='{self.name}', age={self.id}"

per=person("bob",21)

print(str(per))

print(repr(per))