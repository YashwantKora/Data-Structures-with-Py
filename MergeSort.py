# Start with an array of numbers.
# If the array has more than one element:
#     Split the array into two halves.
#     Recursively sort each half.
#     Merge the two sorted halves:
#         Compare elements from both halves and add the smaller one to the result.
# End when the array is sorted.

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
