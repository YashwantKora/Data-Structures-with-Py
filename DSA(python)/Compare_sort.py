import time 

#Bubble Sort

def BubbleSort(data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

array = [1,3,5,7,9,2,4,6,8]
startBubble = time.perf_counter()
BubbleSort(array)
endBubble = time.perf_counter()

print("~BUBBLE SORT~")
print("Sorted Array:", array)
print(f"Time taken: {endBubble - startBubble:.8f} seconds")
print()

#Selection Sort

def SelectionSort(data):
    n = len(data)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if data[j] < data[min]:
                min = j
        data[i], data[j] = data[j], data[i]

array = [1,3,5,7,9,2,4,6,8]
startSelection = time.perf_counter()
BubbleSort(array)
endSelection = time.perf_counter()

print("~SELECTION SORT~")
print("Sorted Array:", array)
print(f"Time taken: {endSelection - startSelection:.8f} seconds")
print()

#Merge Sort
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

array = [1,3,5,7,9,2,4,6,8]
startMerge = time.perf_counter()
MergeSort(array)
endMerge = time.perf_counter()

print("~MERGE SORT~")
print("Sorted Array:", array)
print(f"Time taken: {endMerge - startMerge:.8f} seconds")
print()