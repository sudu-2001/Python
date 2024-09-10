class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def caluclate_salary(self):
        return f"this function is overridden"
    
class fulltimeemployee(employee):
    def __init__(self, name, id,salary):
        super().__init__(name, id)
        self.salary=salary*12

    def caluclate_salary(self):
        print(f"salary:{self.salary},name:{self.name}")

class contractemployee(employee):
    def __init__(self, name, id,salary,workhour):
        super().__init__(name, id)
        self.salary=salary *workhour
        self.workhour=workhour

    def caluclate_salary(self):
        print(f"salary:{self.salary}")

emp=employee("bob",1)
print(emp.caluclate_salary())

ful=fulltimeemployee("sudarshan",1,12000)
con=contractemployee("sudarshan",1,12000,4)
print(con.caluclate_salary())
print(ful.caluclate_salary())