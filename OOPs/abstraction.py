from abc import ABC,abstractmethod

class payment:
    @abstractmethod
    def transaction(self,amount:float):
        pass

class paypal(payment):
    def transaction(self, amount: float):
        print(f"amount paid:{amount}")

class upi(payment):
    def transaction(self, amount: float):
        print(f"amount paid:{amount}")

pay=paypal()
up=upi()

pay.transaction(200)
up.transaction(300)