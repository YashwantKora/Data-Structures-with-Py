class Stack:
    def __init__(self, maxSize, top):
        self.maxSize = maxSize
        self.top = -1
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def push(self, values):
        if self.top == self.maxSize -1:
            print("STACK OVERFLOW!")
        else:
            self.list.append(values)
            self.top += 1
            print(values, "HAS BEEN INSERED INTO THE STACK")

    def pop(self):
        if self.top == -1:
            print("EMPTY STACK")
        else:
            print("Popped item: ", self.list.pop())
    
    def display(self):
        if self.top == -1:
            print("NO STACK EXISTS")
        else:
            print("CONTENTS OF THE STACK:")
            print(self)

S = Stack(4, -1)
S.push(10)
S.push(20)
S.display()
S.pop()
S.display()