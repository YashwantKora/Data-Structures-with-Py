#5 Implement Bubble Sort algorithm, compute space and time complexities, plot graph using asymptotic notations

import time

s = time.perf_counter()

def bubble_sort(data, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

data = [1,3,5,7,9,2,4,6,8,10,14,12,45,18,11]
n = len(data)
bubble_sort(data, n)
print(data)

e = time.perf_counter()
print('time:', e-s)

# Metric	     Value
# Time (Best)	 O(n)
# Time (Average) O(n²)
# Time (Worst)	 O(n²)
# Space          O(1)