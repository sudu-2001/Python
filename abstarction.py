from abc import ABC,abstractmethod

class shape(ABC):
    def area(self):
        pass

class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width
    
rect=rectangle(10,5)
print(rect.area())