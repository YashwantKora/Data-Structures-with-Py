# Start with a sorted array and a target value.
# Set two pointers: one at the start and one at the end of the array.
# Repeat while the start pointer is not past the end pointer:
#     Find the middle element.
#     If the middle element is the target, return its index.
#     If the target is smaller, move the end pointer left.
#     If the target is larger, move the start pointer right.
# If the target is not found, return -1.

def BinarySearch(data, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if data[mid] == x:
            return mid
        elif data[mid] > x:
            return BinarySearch(data, x, low, mid-1)
        elif data[mid] < x:
            return BinarySearch(data, x ,mid+1, high)
        else:
            return -1


array = [1,2,3,4,5,6,7,8,9,10]
n = len(array)
x = 10 
result = BinarySearch(array, x, 0, n-1)

if result == -1:
    print("Not Found!")
else:
    print("Found at index:", result)
