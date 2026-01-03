"""lst = [20, 40, 10, 90, 60, 39]
print(lst)
lst.sort()
print(lst)
lst.sort(reverse = True)
print(lst)"""

#SELECTION SORT
lst = [18, 12, 2, 16, 10, 14]
print(lst)
for i in range(0, len(lst) - 1):
    for j in range(i + 1, len(lst)):
       if lst[j] < lst[i]:
           lst[i], lst[j] = lst[j], lst[i]
print(lst)

#USER-DEFINED CLASS WITH DUNDER METHOD
class Footballer:
    def __init__(self, name, goals, asist):
        self.name = name
        self.goals = goals
        self.asist = asist

    def display(self):
        print(self.__dict__)

    def __lt__(self, other):
        return self.goals < other.goals
        
    def __gt__(self, other):
        return self.goals > other.goals
             
    def __str__(self):
        return f'{self.name} {self.goals} {self.asist}'
        
"""def sort_footballer(lst):
    for i in range(0, len(lst) - 1):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]"""
        
def main():
    f1 = Footballer('Messi', 650, 359)
    f2 = Footballer('Cristiano', 750, 250)
    f3 = Footballer('Neymar', 450, 125)
    f4 = Footballer('Luis', 300, 600) 

    lst = [f1, f2, f3, f4]
    lst.sort()
    #sort_footballer(lst)

    for i in lst:
        print(i)
    #f1.display()
    #f2.display()
    #print(f1 < f2)
    #f1.__lt__(f2)
main()

