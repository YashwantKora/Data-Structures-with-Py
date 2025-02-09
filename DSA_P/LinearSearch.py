import time
import matplotlib.pyplot as plt
import numpy as np

def LinearSearch(data, n, key):
    for i in range(0, n):
        if data[i] == key:
            return i
    return -1

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
key = 10
n = len(array)
start = time.perf_counter()
result = LinearSearch(array, n, key)
end = time.perf_counter() 

if result == -1:
    print("Element not present in the array")
else:
    print("Element present at index", result)  

print("The time is:", end-start)

x = [5,10,15,20]
y = [1.40, 2.60, 3.89, 3.30]

plt.plot(x, y)
plt.xlabel("X axis no of inputs")
plt.ylabel("Y axis time")
plt.title("Linear Complexity")
plt.show()