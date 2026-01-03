#Tuple is ordered, allow duplicates, immutable collection of items which can be of different data types(heterogeneos)
#Tuple operations and methods : concatenation(+), repetition(*), in, len(), .count(), .index()

t = (10, 20, 30, 40)
print(t)
print(t[-2])
#t.append(50) --> attributeError
#print(t)
#t.insert(2, 99)
#print(t)          --> attributeerror
#t.extend(60, 70, 80)
#print(t)          --> attributeerror

tup = ()
print(tup)

#USING BUILT-IN
tup= tuple()
print(tup)

#STORE HETEROGENEOUS DATA
tup = (10, 20, 5, True, 1+3j, 'Python')
print(tup)
#tup.remove(1+3j)
#print(tup)                 #AttributeError: tuple dont habe remove 

#There is no remove so we have to convert tup to list then remove it
tup = ("apple", "banana", "orange")
y = list(tup)
y.remove("orange")
tup = tuple(y)

#del --> used to delete the tuple completely
tup = ("apple", "banana")
del tup
#print(tup)   --> tup no longer exists

#TUPLE CAN STORE A TUPLE, LIST, DICTIONARY IN IT AS WELL
tup = (10, [20, 30, 40], (50, 60, 70), {9, 10, 11}, {1:'x', 2:'y'})
print(tup)

#SLICING ON TUPLE
tup = (10, 20.5, True, 1+3j, 'Python')
print(tup[2])
print(tup[1:4])
#tup(10)
#print(tup)
print(type(tup))        #Type is int , whenever we try to store a single element or singleton tuple there's a certain way to do it
tup = (10,)             #Creating atuple with single element
print(tup)
print(type(tup))

#packing  - Even without () the elements are treated as tuple because they are packed inside a tuple.
#When we create a tuple, we normally assign values to it --> packing
#But in python, we ar also allowed to extract values back into variables --> unpacking
tup = 10, 20, 30
print(tup)
print(type(tup))  

#check if item exists using in
tup = ("Apple", "Banana")
if "apple" in tup:
    print("Yes")


#When we want to add items do not have built-in append(),
#1.Convert into a list
tup = ("apple", "banana")
y = list(tup)
y.append("orange")
tup = tuple(y)



#If the number of variables is less than the number of values, then we can use "*" to the variable name and the values will be assigned to the variable as a list.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#If the * is added to another variable name than the last, Python will assign values to the variables until the number of values left matches the number of variables left
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#Join the tuples using +
tup1 = ("a", "b", "c")
tup2 = (1, 2, 3)
tup3 = tup1 + tup2
print(tup3)

#Multiply tuples
tup1 = ("a", "b", "c")
tup2 = tup1 * 2
print(tup2)

#Tuple methods: count()(Returns the no of times a specified value occurs in a tuple)
#             : index()(Searches the tuple for a specified value and returns the position of where it was found)
tup = (1, 2, 3, 4, 5, 6)
print(tup.count(2))
print(tup.index(2))