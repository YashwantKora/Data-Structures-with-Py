class Stack:
    def __init__(self, max_size, top):
        self.max_size = max_size
        self.top = top
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
    
    def push(self, value):
        if self.top == self.max_size:
            print("STACK OVERFLOW!")
        else:
            self.list.append(value)
            self.top += 1
            print(value, "has been added to stack")

    def pop(self):
        if self.top == -1:
            print("The stack is empty")
        else:
            print("Popped item:", self.list.pop())
            self.top -= 1

    def display(self):
        if self.top == -1:
            print("The stack is empty")
        else:
            print(self)

S = Stack(4, -1)
S.push(10)
S.push(20)
S.display()
S.pop()
S.display()