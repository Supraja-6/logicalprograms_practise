#PATTERN MATCHING 
#WHEN TO USE PM --> 
import re
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