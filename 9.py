# Implement Merge Sort algorithm, compute space and time complexities, plot graph using asymptotic notations and compare all solutions

import time

s = time.perf_counter()

def MergeSort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        MergeSort(left)
        MergeSort(right)
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
array = [2,4,6,8,1,3,5,7,9]
MergeSort(array)
print(array)

e = time.perf_counter()
print('time:', e-s)

# Metric	       Value
# Time (Best)	   O(n log n)
# Time (Average)   O(n log n)
# Time (Worst)	   O(n log n)
# Space	           O(n)