#1.ATM TRANSACTION VALIDATOR

balance = int(input())
n = int(input())
amounts = list(map(int, input().split()))
for amt in amounts:
    if amt % 100 == 0 and balance >= amt:
        print("SUCCESS")
        balance -= amt
    else:
        print("FAILED")
print(balance)


#2.SMART ELECTRICITY BILL 
units = int(input("Enter units: "))
bill = 0
if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = 100 * 3 + (units - 100) * 5
else:
    bill = 100 * 3 + 100 * 5 + (units - 200) * 8
if units > 300:
    bill += bill * 0.10
print("Total Bill:", int(bill))


#3.PASSWORD STRENGTH EVALUATION
password = input()
digit_count = 0
upper_count = 0
for ch in password:
    if ch.isdigit():
        digit_count += 1
    elif ch.isupper():
        upper_count += 1
if len(password) >= 8 and digit_count >= 1 and upper_count >= 1:
    print("STRONG")
else:
    print("WEAK")


#4.TRAFFIC SIGNAL SIMULATION
T = int(input())
time = T % 90
if time == 0:
    time = 90
if 1 <= time <= 30:
    print("RED")
elif 31 <= time <= 45:
    print("YELLOW")
else:
    print("GREEN")


#5.SALARY DEDUCTION SYSTEM
salary = float(input)
late_days = int(input())
absent_days = int(input())
deduction_percent = 0
if late_days > 10:
    deduction_percent += 10
elif late_days > 5:
    deduction_percent += 5
if absent_days > 2:
    deduction_percent += 5
final_salary = salary - (salary * deduction_percent/100)
print(int(final_salary))

#6.PRIME RANGE ANALYZER
a = int(input())
b = int(input())
count = 0
for num in range(a, b + 1):
    if num <= 1:
        continue
    prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            prime = False
            break
        i += 1
    if prime:
        count += 1
print(count)


#7.ONLINE ORDER DISCOUNT ENGINE
amount = int(input())
if amount >= 5000:
    discount = amount * 20 / 100
elif amount >= 3000:
    discount = amount * 10 / 100
elif amount >= 1000:
    discount = amount * 5 / 100
else:
    discount = 0
payable_amount = amount - discount
print(int(payable_amount))


#8.BINARY TO DECIMAL CONVERTER
binary = input()
decimal = 0
power = 0
i = len(binary) - 1
while i >= 0:
    digit = int(binary[i])
    decimal = decimal + digit * (2 ** power)
    power = power + 1
    i = i - 1
print(decimal)

#MOBILE BATTERY DRAIN SIMULATOR
drain = int(input())
battery = 100
minutes = 0
while battery > 0:
    battery = battery - drain
    minutes = minutes + 1
print(minutes)


#10.EXAM RESULT PROCESSOR
m1, m2, m3, m4, m5 = map(int, input().split())
if m1 < 35 or m2 < 35 or m3 < 35 or m4 < 35 or m5 < 35:
    print("FAIL")
else:
    avg = (m1 + m2 + m3 + m4 + m5) / 5
    if avg >= 75:
        print("DISTINCTION")
    else:
        print("PASS")


