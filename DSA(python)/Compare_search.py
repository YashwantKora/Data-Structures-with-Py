import time

#Linear Search

def LinearSearch(data, n, key):
    for i in range(n):
        if data[i] == key:
            return i 
    return -1
array = [1,2,3,4,5,6,7,8,9]
key = 6
n = len(array)
startLinear = time.perf_counter()

print("~LINEAR SEARCH~")
startLinear = time.perf_counter()
print("Element found at index:", LinearSearch(array, n, key))
endLinear = time.perf_counter()
print(f"Time taken: {endLinear - startLinear:.8f} seconds")
print()

#Binary Search

def BinarySearch(data, x, low, high):
    if high >= low:
        mid = low + (high-low) // 2
        if mid == x:
            return mid
        elif mid > x:
            return BinarySearch(data, x, low, mid - 1)
        elif mid < x:
            return BinarySearch(data, x, mid + 1, high)
    else: 
        return -1


array = [1,2,3,4,5,6,7,8,9,10]
x = 1


print("~BINARY SEARCH~")
startBinary = time.perf_counter()
if BinarySearch == -1:
    print("Element not found!")
else:
    print("Element found at index:", BinarySearch(array, x, 0, n-1))
endBinary = time.perf_counter()
print(f"Time taken: {endBinary - startBinary:.8f} seconds")
print("")