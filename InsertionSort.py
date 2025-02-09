# Start with an array of numbers.
# Repeat for each element from the second to the last:
#     Take the current element and compare it with the previous elements.
#     Shift larger elements one position to the right.
#     Insert the current element into its correct position.
# End when the array is sorted.

def InsertionSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j = j - 1
        data[j+1] = key

array = [2,4,6,8,1,3,5,7,9]
InsertionSort(array)
print(array)