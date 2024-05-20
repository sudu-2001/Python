class car:
    def __init__(self,name,model):
        self.__name=name
        self.__model=model

    def grtinfo(self):
        return f"{self.__name} {self.__model}"
    

car1 = car("toyota","xuv")

print(car1.grtinfo())