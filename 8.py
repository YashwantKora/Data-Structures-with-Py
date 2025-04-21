#8 Implement Binary Search using recursion, compute space and time complexities, plot graph using asymptotic notations and compare two

# Start with two markers:
#     One at the beginning of the list (low)
#     One at the end of the list (high)
# While low is less than or equal to high:
#     Find the middle element (use (low + high) // 2)
#     If the middle element is the one you're looking for — boom! Found it.
#     If your target is greater than the middle element:
#         Search in the right half (low = mid + 1)
#     If your target is less than the middle element:
#         Search in the left half (high = mid - 1)
# Keep repeating until you either:
#     Find the element
#     Or the search range gets invalid (low > high), which means it’s not in the list

import time

s = time.perf_counter()

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


e = time.perf_counter()
print('time:', e-s)

# Time Complexity:
#     Best: O(1) (if element is at mid)
#     Average/Worst: O(log n)

# Space Complexity:
#     O(1) for iterative
#     O(log n) for recursive (due to call stack)