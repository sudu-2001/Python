class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display_info(self):
        print(f"name:{self.name},id:{self.id}")

class job:
    def __init__(self,salary,designation):
        self.salary=salary
        self.designation=designation

    def display_job(self):
        print(f"salary:{self.salary},designation:{self.designation}")

class employee(job,person):
    def __init__(self, name,id,salary, designation):
        person.__init__(self,name,id)
        job.__init__(self,salary, designation)


    def display(self):
        self.display_info()
        self.display_job()

em=employee("sudarshan",1,1200000,"Q&A")

em.display_info()