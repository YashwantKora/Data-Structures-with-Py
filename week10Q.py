class queue:
    def __init__(self):
        self.queue_ds = []
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        self.queue_ds.append(value)

        if self.front == -1:
            self.front += 1
            self.rear += 1
            print(value, "is sucessfully inserted!")
        else:
            self.rear += 1
            print(value, "is sucessfully inserted!")

    def dequeue(self):
        if len(self.queue_ds) == 0:
            print("Queue is empty")
            return
        else:
            temp = self.queue_ds.pop(self.front)
            self.rear -= 1
            print("Deleted item:", temp)

            if len(self.queue_ds) == 0:
                self.front = -1
                self.rear = -1
                return temp

    def display(self):
        if len(self.queue_ds) == 0:
            print("Queue is empty")
            return
        
        print("The Queue")
        if self.front == self.rear:
            print(self.queue_ds[self.front], "<-FRONT,<-REAR")
            return
        print(self.queue_ds[self.front], "<-FRONT")
        i = self.front + 1
        while i < self.rear:

            print(self.queue_ds[i])
            i += 1
        print(self.queue_ds[self.rear], "<-REAR")   
        print("The Queue ends")

a = queue()
while True:
    option = int(input("1 for insert\n 2 for delete\n 3 for display\n 4 to exit"))
    if option == 1:
        value = int(input("enter the value: "))
        a.enqueue(value)
        continue
    elif option == 2:
        a.dequeue()
        continue
    elif option == 3:
        a.display()
        continue
    elif option == 4:
        print("EXITING...")
        break
    else:
        print("INVALID BRO")