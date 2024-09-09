class person:
    
    def __init__(self,x,y):

        self.x=x
        self.y=y

    def __add__(self,other):

        return person(self.x+other.x,self.y+other.y)
    
    def __str__(self):

        return f"person({self.x},{self.y})"
    
p=person(1,2)

p1=person(3,4)

p2=p+p1

print(p2)