s = {95, 45, 160, 80, 20, 66, 88, 15, 15, 65, 22}
print(s)

s = {10, 3.14, True, 1 + 3j, (40, 50, 60), 'Python'}
print(s)

#s = {[10, 20, 30], {66, 77, 88}, {1:'A', 2:'B'}} #All are mutable types 
#print(s)   #unhashable type: list

#Directly call the hash function using inbuilt function - hash
print(hash(99))
print(hash(99.9))

s = {5,78, 92, 77, 105, 3, 67}
print(s)
s.add(999)
print(s)
s.remove(999)
print(s)
#s.remove(111)  
#print(s)    #remove the element whih is not present in set --> KeyError
s.discard(111)
print(s)     #it will not give u an error
s.pop()
print(s)

s = {55, 77, 84, 95, 12}
print(s)
s.update({33, 44, 56})
print(s)

#Join sets - union() or |
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
s2 = {7, 9, 10, 77 ,15, 14, 16, 22, 86}
s3 = s1 | s2
print(s3)

#Intersection - only similar elements from both by using intersection() or &
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
s2 = {7, 9, 10, 77 ,15, 14, 16, 22, 86}
s3 = s1 & s2
print(s3)

#intersection_update  - 
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
s2 = {7, 9, 10, 77 ,15, 14, 16, 22, 86}
s3 = s1.intersection_update(s2)
print(s3)


#Difference - will return a new set that wil contain only items from the firsst set using difference() or -
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
s2 = {7, 9, 10, 77 ,15, 14, 16, 22, 86}
s3 = s1 - s2
print(s3)

#difference_update
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
s2 = {7, 9, 10, 77 ,15, 14, 16, 22, 86}
s3 = s1.difference_update(s2)
print(s3)

#symmetric difference - method will keep only the elements that are not present in both sets.
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
s2 = {7, 9, 10, 77 ,15, 14, 16, 22, 86}
s3 = s1 ^ s2
print(s3)

#symmetric_difference_update
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
s2 = {7, 9, 10, 77 ,15, 14, 16, 22, 86}
s3 = s1.symmetric_difference_update(s2)
print(s3)

#Program to pring no of duplicate elements in the list
lst = list(map(int, input(). split()))
s = set()
print(len(lst) - len(s))

#set comprehension - concise way of creating set 
s = {5, 4, 9, 8, 7, 2}
res = {i ** 2 for i in s}
print(s)
print(res)

#set comprehension - find the square of only even numbers
s = {5, 4, 9, 8, 7, 2}
res = set()
for i in s:
    if i % 2 == 0:
        res.add(i ** 2)
print(s)
print(res)

#Check if a string is pangram
s = "The Quick Brown Fox Jumps Over a Lazy Dog"
s = s.upper()
c = set()
for i in s:
    if ord(i) >= 65 and ord(i) <= 90:
        c.add(i)
if len(c) == 26:
    print(s, "is a pangram")
else:
    print(s, "is not pangram")

#Heterogram - a word, phrase or sentence where no letter of the alphabet is repeated
s = "The Big Dwarf Only Jumps!".upper()
l = []
for i in s:
    if ord(i) >= 65 and ord(i) <= 90:
        l.append(i)
c = set(l)
if len(l) == len(c):
    print(s, "is heterogram")
else:
    print(s,"is not heterogram")