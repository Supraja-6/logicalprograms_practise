class Stack:
    def __init__(self):
        self.res = []

    def push(self, element):
        self.res.append(element)

    def pop(self):
        t  = self.res[-1]
        self.res.pop()
        return t
    
    def main(self):
        self.push(10)
        self.push(30)
        print(self.pop())
        print(self.pop())
        #print(self.pop())

if __name__ == '__main__':
    stack_obj = Stack()
    stack_obj.main()


#STACK IMPLEMENTATION USING LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    def push(self, element):
        temp = Node(element)
        temp.next = self.top
        self.top = temp
    def pop(self):
        ele = self.top.data
        self.top = self.top.next
        return ele
    def is_Empty(self):
        return self.top == None
    def main(self):
        print(s.is_Empty())
        self.push(10)
        self.push(20)
        self.push(30)
        print(s.is_Empty())
        print(self.pop())
        print(self.pop())
        print(self.pop())
if __name__ == '__main__':
    s = Stack()
    s.main()


         