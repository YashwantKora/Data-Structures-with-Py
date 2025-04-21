#7 Implement Insertion Sort algorithm, compute space and time complexities, plot graph using asymptotic notations. 


# 🔸 Algorithm for Insertion Sort
# Input:
#     A list of n elements
# Steps:
#     Start from the second element (index 1). Assume the first element is already sorted.
#     For each element i from 1 to n - 1, do the following:
#         Take the current element (arr[i]) and call it the key.
#         Compare the key with the elements before it (from i-1 down to 0).
#         Shift each element that is greater than the key to the right by one position.
#         Once you find the right spot (where the element is smaller than or equal to the key), insert the key there.
#     Repeat the process until the entire list is sorted.

import time

s = time.perf_counter()

def InsertionSort(data, n):

    for i in range(1, n):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j+1] = key

data = [1,3,5,7,9,2,4,6,8,10,14,12,45,18,11]
n = len(data)
InsertionSort(data, n)
print(data)

e = time.perf_counter()
print('time:', e-s)

# Time Complexity:
#     Best: O(n) (already sorted)
#     Average: O(n²)
#     Worst: O(n²)

# Space Complexity:
#     O(1) (in-place sort)