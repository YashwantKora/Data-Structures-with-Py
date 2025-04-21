#7 Implement Insertion Sort algorithm, compute space and time complexities, plot graph using asymptotic notations. 

import time

s = time.perf_counter()

def InsertionSort(data, n):
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j = j - 1
        data[j+1] = key

data = [1,3,5,7,9,2,4,6,8,10,14,12,45,18,11]
n = len(data)
InsertionSort(data, n)
print(data)

e = time.perf_counter()
print('time:', e-s)