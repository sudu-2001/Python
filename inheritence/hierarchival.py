class employee:

    def __init__(self,name,id):

        self.name=name

        self.id=id

    def display(self):

        print(f"name={self.name}\nid={self.id}")


class parttime(employee):

    def __init__(self, name, id,salary,hour):
        super().__init__(name, id)
        self.salary=salary
        self.hour=hour*salary

    def display(self):
        
        super().display()
        print(f"salary={self.salary}\n hour={self.hour}")

class fulltime(employee):

    def __init__(self, name, id,salary):
        super().__init__(name, id)
        self.salary=salary

    def display(self):
        super().display()
        print(f"salary={self.salary}")

full=fulltime("alice",1,200000000)

part=parttime("bob",1,2000000,4)

full.display()

part.display()
