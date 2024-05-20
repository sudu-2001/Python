class person:
    name="sudarshan"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        return f"{self.name} {self.age}"
    
per=person("sudarshan",23)

print(per.display())

per.name="ko"
per.age=22

print(per.name)

print(per.age)