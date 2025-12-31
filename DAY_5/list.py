lst = [1,2,3,4]
print(lst)

lst = [10, 20, 30, 40, 50, 20]
print(len(lst))
print(min(lst))
print(max(lst))
print(sum(lst))

for i, j in enumerate(lst):
    print(i, j)

print(lst.count(20))
print(lst.index(40))
print(lst.index(20, 2, 6))


lst = [25, 17, 36, 7, 55, 13]
print(lst)
lst = sorted(lst) #by default ascending order
print(lst)
lst = sorted(lst, reverse=True)
print(lst)
lst.reverse()
print(lst)

#PROGRAM TO FIND SUM OF SUBLIST
lst = input("Enter a list between []\n")
lst = eval(lst)
start = int(input("Enter the start index"))
stop = int(input("Enter the stop index"))
print("sum =", sum(lst[start:stop+1:]))

#PROGRAM TO APPEND THE ELEMENTS WHICH IS NOT PRESENT IN THE PRIMARY LIST
lst1 = [10, 20, 30, 40]
lst2 = [35, 20, 10, 15]
for i in lst2:
    if i not in lst1:
        lst1.append(i)
print(lst1)

#Program to insert an element at right position within a sorted list
lst = eval(input("Enter a sorted list between []\n"))
n = int(input("Enter the value to be inserted\n"))
print(lst)
for i in range(len(lst)):
    if n < lst[i]:
        lst.insert(i, n)
        break
print(lst)

#Program to find the sum of minimum number and maximum numberof a list without using any built-in functions.
lst = [50, 80, 40, 20, 10, 30]
min = lst[0]
max = lst[0]
for i in range(len(lst)):
    if lst[i] < min:
        min = lst[i]
    elif lst[i] > max:
        max = lst[i]
print("Min + Max =",min+max)

#TO CALCULATE THE LENGTH OF A LIST WITHOUT USING BUILT-IN FUNCTIONS
lst = [50, 80, 40, 20, 10, 30, 100]
count = 0
for i in lst:
    count += 1
print(f"Length = {count}")

#PROGRAM TO CALCULATE THE SUM OF VALUES OF ENTIRE LIST WITHOUT USING BUILT-IN METHOD.
lst = [50, 80, 40, 20, 10, 30, 100]
sum = 0
for i in lst:
    sum += i 
print(f"Sum = {sum}")

#PROGRAM TO CALCULATE PRODUCT OF ALL ELEMENTS
lst = [50, 80, 40, 20, 10, 30, 100]
p = 1
for i in lst:
    p = p * i
print(f"Product = {p}")

#PROGRAM TO CHECK IF THE EXPRESSION CONTAINS BALANCED PARENTHESIS
s = input("Enter the an expression within brackets\n")
lst = []
for i in s:
    if i == '[' or i == '(' or i == '{':
        lst.append(i)
    elif i == ']' and lst[-1] == '[':
        lst.pop()
    elif i == ')' and lst[-1] == '(':
        lst.pop()
    elif i == '}' and lst[-1] == '{':
        lst.pop()
    else:
        break
if len(lst) == 0:
    print(s, "Expression is balanced")
else:
    print(s, "Expression is not balanced")

#COMPARISON OF LISTS
lst1 = [7, 3, 5]
lst2 = [7, 3, 5, 1]
print(lst1 == lst2)
print(lst1 != lst2)
print(lst2 > lst1)


#LIST COMPREHENSION
lst = [2, 5, 7, 8, 10, 12]
sq_lst = []
for i in lst:
    sq_lst.append(i ** 2)
print(lst)
print(sq_lst)

lst = [2, 5, 7, 8, 10, 12]
sq_lst = [i ** 2 for i in lst if i % 2 == 0]
print(lst)
print(sq_lst)