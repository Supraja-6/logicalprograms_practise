def power_of(a, b):
    c = a ** b
    print(c)
def get_quotient(num, den):
    quotient = num / den
    print(quotient)

if __name__ == '__main__':
    print(__name__)
    power_of(2, 5)
    get_quotient(100, 6)

#BREAK, CONTINUE, PASS
n = int(input("Enter a number: "))
for i in range(2, n + 1):
    if n % i == 0:
        pass
if i == n:
    print(n, "is Prime number")
else:
    print(n, "is not prime")


n = int(input("Enter a number: "))
for i in range(2, n + 1):
    if n % i == 0:
        break
if i == n:
    print(n, "is Prime number")
else:
    print(n, "is not prime")


"""n = int(input("Enter a number: "))
for i in range(2, n + 1):
    if n % i == 0:
        continue
if i == n:
    print(n, "is Prime number")
else:
    print(n, "is not prime")"""

#LAMBDA FUNCTIONS
l = [10, 13, 15, 20, 28]
res = list(filter(lambda x : (x % 2 == 0), l))
print(res)




#TYPES OF VARIABLES - GLOBAL VARIABLES
x = 99
def fun():
    y = 999
    print(y)
fun()

#LOCAL AND GLOBAL
x = 99
print(x)
def fun():
    y = 999
    print(y)
    print(x)
fun()
print(x)

#LOCAL VARIABLE
x = 99
def fun():
    y = 999
    print(y)
fun()
#print(y)

#RECURSIVE FUNCTION
n = int(input("Enter a number: "))
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
print(fact(n))