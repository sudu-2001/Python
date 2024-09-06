class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print(f"name:{self.name},id:{self.id}")

class fulltimeemployee(employee):
    def __init__(self, name, id,salary):
        super().__init__(name, id)
        self.salary=salary

    def display(self):
        super().display()
        print(f"salary:{self.salary}")

class manager(fulltimeemployee):
    def __init__(self, name, id, salary,department):
        super().__init__(name, id, salary)
        self.department=department

    def display(self):
        super().display()
        print(f"department:{self.department}")


man=manager("sudarshan",1,1200000,"Q&A")

man.display()
