class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        pass

class dog(Animal):
    def speak(self):
        return "bhow"

class cat(Animal):
    def speak(self):
        return "mew"

dog=dog("kitten")
cat=cat("hardy")

print(cat.speak())

print(dog.speak())
