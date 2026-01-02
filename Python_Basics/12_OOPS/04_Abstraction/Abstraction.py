from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Payment via UPI")

class Card(Payment):
    def pay(self):
        print("Payment via Card")

payments = [UPI(), Card()]
for p in payments:
    p.pay()