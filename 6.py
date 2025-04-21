#6 Implement Selection Sort algorithm, compute space and time complexities, plot graph using asymptotic notations

import time

s = time.perf_counter()

def SelectionSort(data, n):
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if data[j] < data[min]:
                min = j
        data[i], data[min] = data[min], data[i]

data = [1,3,5,7,9,2,4,6,8,10,14,12,45,18,11]
n = len(data)
SelectionSort(data, n)
print(data)

e = time.perf_counter()
print('time:', e-s)

# Metric	      Value
# Time (Best)	  O(n²)
# Time (Average)  O(n²)
# Time (Worst)	  O(n²)
# Space	          O(1)