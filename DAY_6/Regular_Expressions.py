#PATTERN MATCHING 
#WHEN TO USE PM --> 
"""import re
text = "Python is very easy"
regex = r"Python"
match = re.match(regex, text)
print(match)
#print(match.span())  #(0,6) tuple
#unpacking a tuple
#start, end = match.span()
#print(text[start:end:match.end()])

#Match is a function which will start searching from the beginneing , if in beginning it is not there it return none
#Search --> will search the entire string
import re
text = "Python is very easy"
regex = r"super"
print(re.match(regex, text))   #None
print(re.search(regex, text))  #search will only return none if that string is not present

#META CHARACTERS --> .
import re
text = "Python is super easy"
regex = r"."    #First match single character
match = re.search(regex, text)
print(match)

#findall - a list of all matching characters
import re
text = "Python is super easy"
regex = r"."
l = re.findall(regex, text)
print(l)

#META CHARACTER - \ -->escape character
import re
text = "Python is super easy."
regex = r"\."
l = re.findall(regex, text)
print(l)

#META CHARACTER - | --> A|B
import re
text = "Python is super easy."
regex = r"Python | super"
l = re.findall(regex, text)
print(l)

#META CHARACTER - * --> o or many
import re
text = "a whole hole is not a wwhole"
regex = r"w*hole"
l = re.findall(regex, text)
print(l)

#META CHARACTER - ? --> 0 or 1
import re
text = "a whole hole is not a wwhole"
regex = r"w?hole"
l = re.findall(regex, text)
print(l)

#META CHARACTER - + --> 1 or many
import re
text = "a whole hole is not a wwhole"
regex = r"w+hole"
l = re.findall(regex, text)
print(l)

import re
text = "I know that no one is there in the school now"
regex = r"k?now?"
l = re.findall(regex, text)
print(l)
print("Number of occurences = ", len(l))

import re
text = "python has nothing to do with the snake python"
regex = r"python$"            #match ending python
match = re.search(regex, text)
print(match)

import re
text = "python has nothing to do with the snake python"
regex = r"^python"            #match beginning python
match = re.search(regex, text)
print(match)

import re
text = "python java ai data science"
regex = r"[aeiou]"
l = re.findall(regex, text)
print(l)
print("Number of occurences = ", len(l))

#To match all alpha numeric
import re
text = "My name is supraja and this is my number: 829762735"
regex = r"[a-zA-Z0-9]"       #\w
l = re.findall(regex, text)
print(l)
print("Number of Occurences =", len(l))

#To find the matches of vowels occuring twice
import re
text = "If foot becomes feet tooth becomes teeth"
regex = r"[aeiou]{2}"
l = re.findall(regex, text)
print(l)
print("Number of occurences", len(l))

#To find the matches week and weak
import re
text = "Only the weak wait for the weak to end"
regex = r"we[ae]k"
l = re.findall(regex, text)
print(l)
print("Number of occurences", len(l))
"""

#Program for email validation
import re
text = '''rohit@gmail.com
rohit@@gmail.com
rohit_xyz@gmail.com
roh?>@gmail.com
rohit-123@gmail.com
'''
regex = r"[a-zA-Z0-9_$-]+@[a-zA-Z] + gmail.com"
l = re.findall(regex, text)
print(l)

import re
p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

"""\w matches a single word character.
\w+ matches a group of word characters.
\W matches non-word characters.
"""
import re
p = re.compile('\w')
print(p.findall("He said * in some_lang."))

p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he \
said *** in some_language."))

p = re.compile('\W')
print(p.findall("he said *** in some_language."))