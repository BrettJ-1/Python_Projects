from abc import ABC, abstractmethod
class suit (ABC) :
    def paySlip (self, amount):
        print ("Your credit amount: ", amount) #Used string followed by "amount" variable
        
    @abstractmethod
    def payment (self, amount): #imported @abstractmethod
        pass

class CreditCardPayment(suit):
    def payment (self, amount) :
        print ('Your purchase amount of {} exceeded your credit limit '.format(amount)) #Created string calling obj.payment
        
obj = CreditCardPayment() #Created variable amounts
obj.paySlip ("$1500.00")
obj.payment ("$1778.99")
