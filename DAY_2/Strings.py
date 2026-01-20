#STRINGS
"""s1 = 'Supraja'
print(s1)
s2 = "Supraja"
print(s2)
#s3 = 'Practice makes 'Perfect''#BY escape character \'Perfect\''
#print(s3)

s1 = "Hello"
print(s1)
s1 + "world"
print(s1)
s1 = s1 + "world"
print(s1)
s2 = s1 + "world"
print(s2)

s = input("Enter a string: ")
for i in range(0, len(s) - 2):
    print(s[i : i + 3])         #3 char strings

s = input("Enter a String: ")
print(s[1 : len(s) - 1])         #Last and first except
print(s[len(s) - 2 : 0 : -1])

#PALINDROMIC STRING
s = input("Enter a String: ")
if s == s[::-1]:
    print(s, "is Palindrome")
else:
    print(s, "is not a Palindrome")

#String --> UpperCase()
s = input("Enter a String: ")
s_upper = ""
for i in s:
    if ord(i) >= 97 and ord(i) <= 122:
        s_upper += chr(ord(i) - 32)
    else:
        s_upper += i
print(s)
print(s_upper)

#Program to reverse the second half of the string
s = input("Enter a String: ")
print(s[:len(s)//2:] + s[len(s) - 1 : len(s)//2 - 1 : -1])

#Built-in upper() and lower()
s = input("Enter a String: ")
s_upper = s.upper()
s_lower = s.lower()
print(s_lower)
print(s_upper)

#join()
lst = ["Python", "Java", "Django", "Spring"]
s = "".join(lst)
print(s)

#STRING REPLICATION
s = "Python"
s_rep = s * 3
print(s_rep)

#SWAPCASE()
s = "STAY HOME stay safe"
s1 = s.swapcase()
print(s)
print(s1)

#title and capitalize
s = "STAY HOME stay safe"
s1 = s.swapcase()
print(s)
print(s1)
s2 = s.title()
print(s2)
s3 = s.capitalize()
print(s3)
print("python".capitalize())"""

#STRING FORMATTING CONVERSION

s = "{0 : *>10}".format(999)
print(s)
s = "{0 : *<10}".format(999)
print(s)
s = "{0 : *^10}".format(999)
print(s)

import math
print(math.pi)
s = "{0 :.4f}".format(math.pi)    #fixed point notation
print(s)
s = "{0 : 10.4f}".format(math.pi)
print(s)


#DECIMAL TO BINARY
a = 70
print(a)
print("{0:b}".format(a))

#DECIMAL TO OCTAL
a = 70
print(a)
print("{0:o}".format(a))

#DECIMAL TO HEXADECIMAL
a = 70
print(a)
print("{0:x}".format(a))

#STRING USING FORMAT()
import math
name = "supraja"
place = "Kurnool"
print("{} {}". format(name, place))
print("{1} {0}".format(name, place))
print("{0:.4f}".format(math.pi))

#STRING USING F-STRING
import math
name = "supraja"
place = "Kurnool"
print(f"{name} {place}")
print(f"{place} {name}")
print(f"{math.pi:.4f}")

#raw string
name = r"Ro\nhit"
print(name)         #Ro\nhit as it is raw, in regex will be used 