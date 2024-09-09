class person:
    def __init__(self,name,age):
        self.age=age
        self.name=name

    def __eq__(self,other):
        return self.name==other.name and self.age==other.age

    def __str__(self):
        return f"person(name={self.name},age={self.age})"

person1=person("alice",20)
person2=person("bob",23)
person3=person("tan",24)

print(person1==person2)
print(person1==person3)