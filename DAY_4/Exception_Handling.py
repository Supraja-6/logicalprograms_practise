"""print("Secure connection has been established to bank server")
try:
    p = int(input("Enter your principal amount: "))
    t = int(input("Enter the duration: "))
    r = 10
except:
    print("Please provide a numerical value")
else:
    si = (p*t*r)/100
    print("Simple Interest =", si)
print("Secure connection has been closed to the bank server")

#EXAMPLE CODES WITH DIFFERENT EXCEPTIONS AND GENERIC EXCEPTION
print("Execution startes normally")
lst = [10, 20, 0, 40, 50]
d = {1 : 'c', 2 : 'Java', 3 : 'Python', 4 : 'c++'}
try:
    r = int(input("Enter the rank of the language: "))
    print(d[r])
    num = int(input("Enter the index of numerator: "))
    den = int(input("Enter the index of denominator: "))
    print(lst[num]/lst[den])
except KeyError:
    print("Key does not exist")
except IndexError as e:
    print(e)
except ZeroDivisionError:
    print("Division by zero")
except:
    print("Hey some issue occured")
print("Execution terminated normally")

#MULTIPLE METHODS AND THE FLOW OF EXCEPTION HANDLING
def fun2():
    print("fun2() started execution")
    num = int(input("Enter the numerator: "))
    den = int(input("Enter the denominator: "))
    res = num/den
    print(res)
    print("fun2() finished execution normally")

def fun1():
    print("fun1() started execution")
    fun2()
    print("fun1() finished execution normally")

def main():
    print("main() started execution")

    try:
        fun1()
    except ZeroDivisionError:
        print("Exception handled in main()")
    print("main() finished execution normally")
main()

#Simple programs
def validate(mob):
    if len(mob) == 10:
        print("Valid mobile number")
    else:
        raise ValueError
def main():
    mob = input()
    validate(mob)
main()"""

"""
def menu(item):
    if item == "pizza":
        print("Enjoy")
    elif item == "idly":
        print("Enjoy Idly")
    elif item == "burger":
        print("Enjoy burger")
    else:
        raise NameError
def main():
    item = input()
    menu(item)
main()


#Finally
def fun():
    print('fun() started execution')

    try:
        num = int(input("Enter the numerator: "))
        den = int(input("Enter the denominator: "))
        res = num/den
        print(res)
    except ZeroDivisionError:
        print("Exception handled in fun()")
    print("fun() finished execution")
def main():
    print('main() started execution')
    fun()
    print('main() finished execution.')"""


#CUSTOM EXCEPPTIONS
#Steps: Create a class with suitable custom name
"""class InvalidMobileNumberError(Exception):
    pass
def validate(mob):
    if len(mob) == 10:
        print("Valid mobile number")
    else:
        raise InvalidMobileNumberError("Enter 10 digit mobile number")
def main():
    mob = input()
    validate(mob)

main()"""

class ItemNotFoundError(Exception):
    pass
def menu(item):
    if item == "pizza":
        print("Enjoy")
    elif item == "idly":
        print("Enjoy Idly")
    elif item == "burger":
        print("Enjoy burger")
    else:
        raise ItemNotFoundError("Ch0ose from the mention food items.")
def main():
    item = input()
    try:
        menu(item)
    except ItemNotFoundError as e:
        print(e)
main()


