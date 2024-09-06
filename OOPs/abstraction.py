from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def process_payment(self,amount:float):
        pass

class creditpayment(payment):
    def process_payment(self, amount: float):
        print(f"the amount paid is ${amount:.2f}")



class paypal(payment):
    def process_payment(self, amount: float):
        print(f"the amount paid is ${amount:.2f}")


payment2=paypal()
payment2.process_payment(1000000000000)
payment1=creditpayment()
payment1.process_payment(20000000)