# Start with an array of numbers.
# If the array has more than one element:
#     Choose a pivot element from the array.
#     Partition the array into two sub-arrays:
#         Elements less than the pivot go to the left, and elements greater go to the right.
#     Recursively apply quick sort to the left and right sub-arrays.
# End when the array is sorted.

import time

def partition(data, start, end):
    pivot = data[start]
    low = start + 1
    high = end

    while True:
        while low <= high and data[high] >= pivot:
            high -= 1
        while low <= high and data[low] <= pivot:
            low += 1
        if low <= high:
            data[low], data[high] = data[high], data[low]
        else:
            break
    data[start], data[high] = data[high], data[start]
    return high

def QuickSort(data, start, end):
    if start >= end:
        return
    p = partition(data, start, end)
    QuickSort(data,start, p - 1)
    QuickSort(data,p + 1, end)

array = [1,3,5,7,9,2,4,6,8,]
s = time.perf_counter()
QuickSort(array, 0, len(array) - 1)
e = time.perf_counter()
print(array)
print("Time:", e-s)