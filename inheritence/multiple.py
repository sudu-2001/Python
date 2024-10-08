class job:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def jobdisplay(self):
        print(f"name={self.name}\nid={self.id}")

class role:
    def __init__(self,type,language):
        self.type=type
        self.language=language

    def roledisplay(self):
        print(f"type={self.type}\nlanguage={self.language}")

class company(job,role):
    def __init__(self, name, id,type,language):
        job.__init__(self,name, id) 
        role.__init__(self,type,language)

    def display(self):
        self.jobdisplay()
        self.roledisplay()

com=company("developer",1,"fulltime","java python")

com.display()
