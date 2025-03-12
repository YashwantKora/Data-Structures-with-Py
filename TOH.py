def TOH(disks, src, auxiliary, tar):
    if disks == 1:
        print("MOVE DISK 1 FROM ROD {} TO ROD {}".format(src, tar))
        return
    TOH(disks -1, src, tar, auxiliary)
    print("MOVE DISK {} FROM ROD {} to ROD {}".format(disks, src, tar))
    TOH(disks -1, auxiliary, src, tar)

disks = int(input("Enter the numbers of disk"))
TOH(disks, "A", "B", "C")