class employee:
    def __init__(self,name,id):

        self.name=name

        self.id=id

    def display(self):

        print(f"name={self.name},id={self.id}")

class fulltime(employee):

    def __init__(self, name, id,salary):
        super().__init__(name, id)
        self.salary=salary

    def display(self):
        super().display()
        print(f"{self.salary}")

emp=fulltime("alice",1,200000)

emp.display()