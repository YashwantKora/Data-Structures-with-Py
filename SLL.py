# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def insert_at_beginning(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     def delete_beginning(self):
#         if self.head is None:
#             print("LL is Empty!")
#         else:
#             self.head = self.head.next
        
#     def search(self, key):
#         current = self.head
#         while current is not None:
#             if current.data == key:
#                 return True
#             current = current.next
#         return False
    
#     def printList(self):
#         temp = self.head
#         while temp:
#             print(str(temp.data) + " ", end="")
#             temp = temp.next

# if __name__ == '__main__':
#     LL = LinkedList()
#     n = Node(1)
#     LL.head = n
#     n1 = Node(2)
#     n.next = n1

#     LL.insert_at_beginning(10)
#     LL.insert_at_beginning(20)
#     print("LL")
#     LL.printList()
#     print("|")
#     LL.delete_beginning()
#     LL.printList()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinknkedList:
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

    def insert_after_node(self, prev_node, new_data):
        if prev_node is None:
            print("previous node must be present in the LL")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("LL IS EMPTY")
        else:
            self.head = self.head.next

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def print(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end="")
            temp = temp.next

if __name__ == '__main__':
    LL = LinknkedList()
    n = Node(1)
    LL.head = n
    n1 = Node(2)
    n.next = n1

    LL.insert_at_beginning(10)
    LL.insert_at_beginning(20)
    LL.insert_at_end(30)
    LL.insert_after_node(n1, 100)
    print("LL")
    LL.print()
    print("|")
    LL.delete_at_beginning()
    LL.print()
