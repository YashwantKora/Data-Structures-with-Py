# def TOH(disks, src, auxiliary, tar):
#     if disks == 1:
#         print("MOVE DISK 1 FROM ROD {} TO ROD {}".format(src, tar))
#         return
#     TOH(disks -1, src, tar, auxiliary)
#     print("MOVE DISK {} FROM ROD {} to ROD {}".format(disks, src, tar))
#     TOH(disks -1, auxiliary, src, tar)

# disks = int(input("Enter the numbers of disk"))
# TOH(disks, "A", "B", "C")

def tower_of_hanoi(disk, source, auxiliary, target):
    if disk == 1:
        print("Move disk 1 from rod {} to rod {}".format(source, target))
        return
    tower_of_hanoi(disk - 1, source, target, auxiliary)
    print("Move disk {} from rod {} to rod {}".format(disk, source, target))
    tower_of_hanoi(disk - 1, auxiliary, source, target)

disk = int(input("Enter the number of disks: "))
tower_of_hanoi(disk, "A", "B", 'C')