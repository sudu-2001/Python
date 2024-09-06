class employee:
    #class attributes
    id=1
    #instanse attributes
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def display(self):
        print(self.name,self.email)

e1=employee("sudarshan","xyz@gmail.com")
e1.name="xyz"
print(e1.id)

print(e1.name)
e1.display()

delattr(e1,'name')
print(e1.name)