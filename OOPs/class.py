#what is class?
#A class is a blue print of object it will containing Object attributes,methods ect

class car:
    def __init__(self,model,year):
        self.year=year
        self.model=model

    def display(self):
        print(self.model,self.year) 

c=car("ford",1987)
c.display()   