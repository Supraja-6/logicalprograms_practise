#OOPs
class Car:
    def __init__(self):
        self.brand = "BMW"
        self.color = "Pink"
    def start_engine(self):
        print("Starting Engine")
    def accelerate(self):
        print("Car is accelerating")
def main():
    c1 = Car()
    print(c1.brand)
    print(c1.color)
    c1.start_engine()
    c1.accelerate()
if __name__ == '__main__':
    main()


#ENCAPSULATION --> Process of wrapping all variables and methods into a single unit.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name          # Public variable
        self.__balance = balance  # Private variable (data hidden)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
# Main program
name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))

account = BankAccount(name, balance)

print("\nAccount Holder:", account.name)
print("Current Balance:", account.get_balance())

deposit_amount = int(input("\nEnter amount to deposit: "))
account.deposit(deposit_amount)
print("Balance after deposit:", account.get_balance())

withdraw_amount = int(input("\nEnter amount to withdraw: "))
account.withdraw(withdraw_amount)
print("Final Balance:", account.get_balance())


#Using Property
"""class AccountHolder:
    def __init__(self):
        self.__bal = 10000
    def get_bal(self):
        print('get_bal() is called')
        return self.__bal
    def set_bal(self, amt):
        print('set_bal() is called')
        if amt > 0:
            self.__bal = amt
        else:
            print("Invalid amount")
    bal = property(get_bal, set_bal)
    ah = AccountHolder()
    print(ah.bal)
    ah.bal = 20000
    print(ah.bal)"""

#INHERITANCE - Process of one class acquiring the properties and behaviour from another class
class Animal:
    def bark(self):
        print("Dog is sleeping")
class Cat(Animal):
    def eat(self):
        print("Cat is eating")
c1 = Cat()
c1.bark()
c1.eat()

#TYPES - SINGLE, MULTI-LEVEL, 
#SINGLE INHERITANCE 
class Alpha:
    def fun1(self):
        print("Alpha is inheriting from object class")
print(dir(Alpha))

#MULTI-LEVEL INHERITANCE
class Alpha:
    def fun1(Self):
        print("Inside alpha fun1()")
class Beta(Alpha):
    def fun2(self):
        print("Inside beta fun2()")
class Gamma(Beta):
    pass  #inherited methods will be there
g = Gamma()
#g.fun1()
#g.fun2()
print(dir(Gamma))

#MULTIPLE INHERITANCE
class Alpha:
    def fun1(self):
        print('Alpha class fun1()')
class Beta:
    def fun2(self):
        print('Beta class fun2()')
class Gamma(Alpha, Beta):
    pass
g = Gamma()
g.fun1()
g.fun2()

#MULTIPLE INHERITANCE - METHOD RESOLUTION ORDER USING help() or classname.dunder mro or class method mro
class Alpha:
    def fun1(self):
        print('Alpha class fun1()')
class Beta:
    def fun1(self):
        print('Beta class fun2()')
class Gamma(Alpha, Beta):
    pass
g = Gamma()
g.fun1()
help(Gamma)
#print(Gamma.__mro__)
#print(Gamma.mro)

#METHODS IN INHERITANCE - INHERITED, OVERRIDEN AND SPECIALISED METHODS
class Messanger:
    def send_message(self):
        print('Text message is sent')
    def receive_message(self):
        print('Text message is received')
class InternalMessanger(Messanger):
    pass
class WhatsAppMessanger(Messanger):
    def send_message(self):
        print('Text, Photos, Videos are sent')
    def receive_message(self):
        print('Text, Photos, Videos are received')
    def set_dp(Self):
        print('DP is set')
    def set_status(self):
        print('Status is set')
im = InternalMessanger()
im.send_message()
im.receive_message()
wam = WhatsAppMessanger()
wam.send_message()
wam.receive_message()
wam.set_dp()
wam.set_status

#Super
class Customer:
    def __init__(self, name, ph, email):
        self.name = name
        self.ph = ph
        self.email = email
class PlainiumCustomer(Customer):
    def __init__(self, name, ph, email, plat_id):
        super().__init__(name, ph, email)
        self.plat_id = plat_id

    def display(self):
        print(self.__dict__)
def main():
    p = PlainiumCustomer('Rohit', 8796734567, 'rohit123@gmail.com', 6)
    p.display()
if __name__ == '__main__':
    main()

#super in multi-level Inheritance
class A:
    def fun(self):
        print('A')
class B(A):
    def fun(self):
        print('B')
class C(B):
    def fun(self):
        super(B, self).fun()
        print('C')
c = C()
c.fun()

#super in multiple Inheritance
class A:
    def fun(self):
        print('A')
class B:
    def fun(self):
        print('B')
class C(A, B):
    def test(self):
        super().fun()
        print('C')
c = C()
#help(c)
c.test()

#POLYMORPHISM : ONE:MANY which means the code gives different output or performing different task
class Messanger:
    def use_keyboard(self):
        print("Using Keyword")
    def send_message(self):
        print("Message sent")
    def receive_message(self):
        print("Message receive")
class WhatsApp(Messanger):
    def send_message(self):
        print("Text, Photos, Videos sent using wa")
    def receive_message(self):
        print("Text, Photos, Videos are received using wa")
    def send_live_location(self):
        print("Live location sent")
class Facebook(Messanger):
    def send_message(self):
        print("Text, Photos, Videos sent using fb")
    def receive_message(self):
        print("Text, Photos, Videos are received using fb")
    def use_builtin_apps(self):
        print("using built-in apps using  fb")
def use_messanger(ref):
    ref.use_keyboard()
    ref.send_message()
    ref.receive_message()
    if type(ref) == WhatsApp:
        ref.send_live_location()
    if type(ref) == Facebook:
        ref.use_builtin_apps()
wa = WhatsApp()
fa = Facebook()
use_messanger(wa)
use_messanger(fa)

#ABSTRACTION
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike started with kick")
    def stop(self):
        print("Bike stopped using brakes")

class Car(Vehicle):
    def start(self):
        print("Car started with key")
    def stop(self):
        print("Car stopped using brakes")
b = Bike()
b.start()
b.stop()
c = Car()
c.start()
c.stop()
