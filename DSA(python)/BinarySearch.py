# def BinarySearch(data, x, low, high):
#     if high >= low:
#         mid = low + (high - low) // 2
#         if data[mid] == x:
#             return mid
#         elif data[mid] > x:
#             return BinarySearch(data, x, low, mid-1)
#         else:
#             return -1

# array = [1,2,3,4,5,6,7,8,9]
# n = len(array)
# x = 1
# result = BinarySearch(array, x, 0, n-1)

# if result == -1:
#     print("Element not found in the given array!")
# else:
#     print("Element found at index:", result)

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
