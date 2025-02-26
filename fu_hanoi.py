def tower_of_hanoi(disks, source, auxiliary, target):
    if disks == 1:
        print("move disk 1 from rod{} to rod{}".format(source, target))
        return
    
    tower_of_hanoi(disks -1, source, target, auxiliary)
    print("move disk{} from rod{} to rod{}".format(disks, source, target))

    tower_of_hanoi(disks -1, source, auxiliary, target)

disks = int(input("Enter the number of disk: "))
tower_of_hanoi(disks, 'A', 'B', 'C')