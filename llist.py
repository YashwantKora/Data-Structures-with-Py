class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head =new_node

    def delete_beginning(self):
        if self.head is None:
            print("LL is empty, cannot be deleted")
        self.head = self.head.next

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
            return False

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data ," " , end=' ')
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist = LinkedList()
    n = Node(1)
    llist.head = n
    n1 = Node(2)
    n.next = n1

    llist.insertAtBeginning(10)
    llist.insertAtBeginning(20)
    llist.insertAtBeginning(30)
    llist.insertAtBeginning(40)
    llist.insertAtBeginning(50)
    print("Linked List")
    llist.printList()
    print("After Deleting an element")
    llist.delete_beginning()
    llist.printList()
    print()
    item_to_find = 10
    if llist.search(item_to_find):
        print(str(item_to_find) + "Is found")
    else:
        print(str(item_to_find) + "Is not found")
    print("Linked List is")
    llist.printList()
