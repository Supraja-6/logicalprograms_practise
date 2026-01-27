#COUNT THE NUMBER OF DIGITS
def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count
def main():
    n = int(input("Enter the digits: "))
    print(count_digits(n))
if __name__ == '__main__':
    main()

#FACTORIAL OF A NUMBER
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
def main():
    n = int(input("Enter the number: "))
    print(factorial(n))
if __name__ == '__main__':
    main()

#Trailing zeroes for the factorial of the number
def trailing_zeroes(n):
    res = 0
    powOf5 = 5
    while n >= powOf5:
        res += (n//powOf5)
        powOf5 *= 5
    return res
def main():
    n = int(input("Enter the number: "))
    print(trailing_zeroes(n))
if __name__ == '__main__':
    main()