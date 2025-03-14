# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LL:
#     def __init__(self):
#         self.head = None

#     def insert_at_beginning(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     def delete_at_beginning(self):
#         if self.head is None:
#             print("Linked List is empty!")
#         else:
#             self.head = self.head.next

#     def search(self, key):
#         temp = self.head
#         while temp is not None:
#             if temp.data == key:
#                 return True
#             temp = temp.next
#         return False
    
#     def print(self):
#         temp = self.head
#         while temp:
#             print(temp.data)
#             temp = temp.next

# 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("SLL IS EMPTY")
        else:
            self.head = self.head.next

    def search(self, key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

LL = LL()
n = Node(5)
LL.head = n
n1 = Node(8)
n.next = n1

LL.insert_at_beginning(10)
LL.insert_at_beginning(20)
LL.insert_at_end(30)
print("LL")
LL.print()
print("|")
LL.delete_at_beginning()
LL.print()