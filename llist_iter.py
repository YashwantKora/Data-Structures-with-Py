class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def print_iter(self):
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val


LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert("Welcome")
LL.insert("Python")
for i in LL.print_iter():
    print(i) 