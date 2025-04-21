#10 mplement Quick Sort algorithm, compute space and time complexities, plot graph using asymptotic notations and compare all solutions

import time

s = time.perf_counter()

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
print(array)

e = time.perf_counter()
print('time:', e-s)