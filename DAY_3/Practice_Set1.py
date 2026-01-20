#1.ATM TRANSACTION VALIDATOR
"""balance = int(input())
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
units = int(input())
bill = 0
if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = 100 * 3 + (units - 100) * 5
else:
    bill = 100 * 3 + 100 * 5 + (units - 200) * 8
if units > 300:
    extra_units = units - 300
    surcharge = extra_units * 8 * 0.10
    bill += surcharge
print(int(bill))"""



#3.PASSWORD STRENGTH EVALUATION
"""password = input()
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
print(int(final_salary))"""

#6.PRIME RANGE ANALYZER
"""a = int(input())
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

#9.MOBILE BATTERY DRAIN SIMULATOR
drain = int(input())
battery = 100
minutes = 0
while battery > 0:
    battery = battery - drain
    minutes = minutes + 1
print(minutes)"""


#10.EXAM RESULT PROCESSOR
"""m1, m2, m3, m4, m5 = map(int, input().split())
if m1 < 35 or m2 < 35 or m3 < 35 or m4 < 35 or m5 < 35:
    print("FAIL")
else:
    avg = (m1 + m2 + m3 + m4 + m5) / 5
    if avg >= 75:
        print("DISTINCTION")
    else:
        print("PASS")

#11.NUMBER COMPRESSION COUNTER
num = int(input())
count = 0
number = int(input())
while number % 2 == 0:
    number //= 2
    count += 1
print(count)


#12.VOWEL FREQUENCY ANALYZER
sentence = input()
vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0
for ch in sentence.lower():
    if ch in vowels:
        count += 1
print(count)
"""

#13.TRAIN TICKET FARE CALCULATOR
distance = int(input())
age = int(input())
base_fare = distance * 2
if age >= 60:
    fare = base_fare * 0.7   # 30% discount
elif age < 12:
    fare = base_fare * 0.5   # 50% discount
else:
    fare = base_fare
print(int(fare))
distance = int(input())
age = int(input())
base_fare = distance * 2
if age >= 60:
    fare = base_fare * 0.7   # 30% discount
elif age < 12:
    fare = base_fare * 0.5   # 50% discount
else:
    fare = base_fare
print(int(fare))


#14.NUMBER PATTERN VALIDATOR
num = input().strip()
is_increasing = True
for i in range(1, len(num)):
    if num[i] <= num[i - 1]:
        is_increasing = False
        break
if is_increasing:
    print("YES")
else:
    print("NO")


#15.SMART DOOR LOCK SYSTEM
correct_pin = input().strip()
access = False
for _ in range(3):
    attempt = input().strip()
    if attempt == correct_pin:
        access = True
        break
if access:
    print("ACCESS GRANTED")
else:
    print("LOCKED")


#16.WATER TANK OVERFLOW DETECTOR
n = int(input())
inflows = list(map(int, input().split()))
capacity = 1000
current_volume = 0
for i in range(n):
    current_volume += inflows[i]
    if current_volume > capacity:
        print(i + 1) 
        break


#17.ARMSTRONG NUMBER CHECKER
num = int(input())
temp = num
sum_of_cubes = 0
while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10
if sum_of_cubes == num:
    print("YES")
else:
    print("NO")


#18.BUS SEAT ALLOCATION
n = int(input())
remaining_seats = 40
for _ in range(n):
    request = int(input())
    if request <= remaining_seats:
        print("CONFIRMED")
        remaining_seats -= request
    else:
        print("WAITLISTED")


#19.NUMBER MIRROR VALIDATOR
num = int(input())
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if num == reverse:
    print("PALINDROME")
else:
    print("NOT PALINDROME")


#20.DIGITAL LOCK COUNTDOWN
num = int(input())
while num >= 10:
    digit_sum = 0
    while num > 0:
        digit = num % 10
        digit_sum += digit
        num //= 10
    num = digit_sum
print(num)



