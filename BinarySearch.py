# Start with a sorted array of numbers and a target value to find.
# Set two pointers: one at the start of the array and one at the end.
# Repeat while the start pointer is less than or equal to the end pointer:
#     Find the middle element of the array.
#     Compare the middle element with the target value.
#     If the middle element matches the target, return the index of the middle element.
#     If the middle element is greater than the target, move the end pointer to one element before the middle.
#     If the middle element is smaller than the target, move the start pointer to one element after the middle.
# If the target value is not found, return -1 (indicating the target is not present).

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
