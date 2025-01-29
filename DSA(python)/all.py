array1 = [1,3,5,7,9,2,4,6,8,10]
def BubbleSort(data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    
BubbleSort(array1)
print(array1)


def SelectionSort(data):
    n = len(data)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if data[j] < data[min]:
                min = j
        data[i], data[min] = data[min], data[i]

array2 = [1,3,5,7,9,2,4,6,8,10]
SelectionSort(array2)
print(array2)

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
                data[k] =left[i]
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

array3 = [1,3,5,7,9,2,4,6,8,10]
MergeSort(array3)
print(array3)



def pivot(data, start, end):
    pivot = data[start]
    low = start + 1
    high = end
    while True:
        while low <= high and data[low] <= pivot:
            low += 1
        while low <= high and data[high] >= pivot:
            high -= 1   
        if low <= high:
            data[low], data[high] = data[high], data[low]
        else:
            break
    data[start], data[high] = data[high], data[start]
    return high
    

def QuickSort(data, start, end):
    if start >= end:
        return
    p = pivot(data, start , end)
    QuickSort(data, start, p - 1)
    QuickSort(data, p + 1, end)

array4 = [1,3,5,7,9,2,4,6,8,10]
QuickSort(array4, 0, len(array4) - 1)
print("quickie",array4)

def BinarySearch(data, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if data[mid] == x:
            return mid
        elif data[mid] > x:
            return BinarySearch(data, x, low, mid - 1)
        elif data[mid] < x:
            return BinarySearch(data, x, mid + 1, high)
        else:
            return -1   

array4 = [1,2,3,4,5,6,7,8,9,10]
result = BinarySearch(array4, 10, 0, len(array4) - 1)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print(f"Element is not present in array")

def LinearSearch(data, n, key):
    for i in range(n):
        if data[i] == key:
            return i
    return -1

LinearSearch(array4, len(array4), 10)
if result != -1:
    print(f"Element is present at index {result}")
else:   
    print(f"Element is not present in array")

def fibonacci(n):
    a = 0
    b = 1
    if n >= 0:
        print(a)
    if n >= 1:
        print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)

fibonacci(10)

"""
Bubble sort
bubblesort(array)
for i <- 1 to index of last element - 1
if left element < right element
swap left element and right element 
end
time complexity: O(n^2)
"""

"""
Selection sort
selectionsort(array)
for i <- 1 to index of last element - 1
set the first element as minimum
for each of the elements
if the element < minimum
set element as minimum
swap minimum with the first element
end
"""