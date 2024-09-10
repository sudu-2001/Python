class ticket:

    def __init__(self,id):
        self.id=id

    def display(self):
        print(f"bugid={self.id}")


class bugticket(ticket):

    def __init__(self, id,bugtype):
        super().__init__(id)
        self.bugtype=bugtype

    def display(self):
        super().display()
        print(f"bugtype={self.bugtype}")

class securitybugticket(bugticket):

    def __init__(self, id, bugtype,securitylevel):
        super().__init__(id, bugtype)
        self.securitylevel=securitylevel

    def display(self):
        super().display()
        print(f"securitylevel={self.securitylevel}")



tick=ticket(1)
tick.display()
bug=bugticket(1,'Ui bug')
bug.display()
sec=securitybugticket(1,'process bug',"high")
sec.display()
