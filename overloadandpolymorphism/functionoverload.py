class shapes:

    def area(self,length=None,width=None,height=None):

        if length !=None and width!=None and height!=None:

            x=0.5*width*height

            print(f"the area of triangle: ",x)

        elif length!=None and width!=None:

            y=length*width

            print(f"the area of rectangle is: ",y)

        else:

            z=length*length

            print(f"the area of square: ",z)



shape=shapes()

print(shape.area(2,3,4))

print(shape.area(2,4))

print(shape.area(2))
