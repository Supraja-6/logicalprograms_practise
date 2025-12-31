#DUNDER METHOD FOR BUILTIN
def main():
    s = 'pyt'
    s += 'hon'
    print(s)
    #s = s + 5
    #s = 5 + s
    #s = 5.__add__(s) o/p --> cant add int with string
    #print(s)
if __name__ == '__main__':
    main()

#DUNDER METHODS FOR CUSTOM CLASSES FOR ADDITION
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x , self.y  + other.y)
    def display(self):
        print(self.__dict__)
def main():
    p1 = Point(2, 3)
    p2 = Point(1, 1)
    p3 = p1 + p2
    #p3 = p1.__add__(p2)
    p3.display()
if __name__ == '__main__':
    main()

#DUNDER METHODS FOR CUSTOM CLASSES FOR MULTIPLICATION
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __mul__(self, other):
        return Point(self.x * other.x , self.y * other.y)
    def display(self):
        print(self.__dict__)
def main():
    p1 = Point(2, 3)
    p2 = Point(1, 1)
    p3 = p1 * p2
    #p3 = p1.__mul__(p2)
    p3.display()
if __name__ == '__main__':
    main()

#DUNDER METHODS FOR CUSTOM CLASSES FOR SUBTRACTION
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return Point(self.x - other.x , self.y - other.y)
    def display(self):
        print(self.__dict__)
def main():
    p1 = Point(2, 3)
    p2 = Point(1, 1)
    p3 = p1 - p2
    #p3 = p1.__sub__(p2)
    p3.display()
if __name__ == '__main__':
    main()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return Point(self.x - other.x , self.y - other.y)
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __repr__(self):
        return f'{type(self)} {id(self)}'
def main():
    p1 = Point(2, 3)
    p2 = Point(1, 1)
    #p3 = p1 + p2
    print(p1)    #It will print the meemory address because by default it is string
    print(p2)
    #print(p3)
    print(p1.__repr__())
    print(p2.__repr__())
if __name__ == '__main__':
    main()

