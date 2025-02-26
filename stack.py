class stack:
    def __init__(self, maxsize, top):
        self.maxsize = maxsize
        self.top = top
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def push(self, values):
        if self.top == self.maxsize -1:
            print("Stack OVERFLOWWWW")
        else:
            self.list.append(values)
            self.top += 1
            print(values, "has been inserted!")
    
    def pop(self):
        if self.top == -1:
            print("The stack is empty")
        else:
            print("popped item = ", self.list.pop())
            self.top -= 1

    def display(self):
        if self.top == -1:
            print("NO STACK EXISTS")

        else:
            print("CONTENTS OF THE STACK:")
            print(self)

S = stack(4, -1)
S.push(10)
S.push(20)
S.display()
S.pop()
S.display()