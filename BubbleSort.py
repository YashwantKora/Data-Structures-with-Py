# Start with an array of numbers.
# Repeat for the length of the array:

#     For each element in the array (except the last sorted elements):
#         Compare the current element with the next one.
#         If the current element is greater than the next one, swap them.

# If no swaps were made, the array is sorted.
# End when the array is sorted.

def BubbleSort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n -i -1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

array = [3,5,1,2,6,4,7,9,8]
BubbleSort(array)
print(array)
