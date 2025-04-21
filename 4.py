#4 Implement Linear Search, compute space and time complexities, plot graph using asymptotic notations

import time

s = time.perf_counter()

def linear_search(data, n, x):
    for i in range(0, n):
        if data[i] == x:
            return i
    return -1

data = [1,3,5,7,9,2,4,6,8,10,14,12,45,18,11]
x = 11
n = len(data)

result = linear_search(data, n, x)
if result == -1:
    print("element not found! GETT OU-")
else:
    print("element present at index,", result)
e = time.perf_counter()
print('time:', e-s)

import matplotlib.pyplot as plt
import numpy as np

x = [5, 10, 15]
y = [0.00059, 0.00083, 0.00081]

plt.plot(x,y)
plt.xlabel('number of inputs')
plt.ylabel('time')
plt.title("LINEAR SEARCH TIME COMPLEXITY")
plt.show()

#      Time     Space 
# Best:  O(1)   O(1)
# Worst: O(n)	O(1)