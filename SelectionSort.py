# Start with an array of numbers.
# Repeat for each element in the array (except the last one):
#     Set the current element as the minimum.
#     For each subsequent element in the array:
#         Compare it with the current minimum.
#         If a smaller element is found, update the minimum.
#     After checking all remaining elements, swap the current element with the minimum element.

# End when the array is sorted.

def SelectionSort(data):
    n = len(data)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if data[j] < data[min]:
                min = j
        data[i], data[min] = data[min], data[i]
                
array = [3,5,1,2,6,4,7,9,8]
SelectionSort(array)
print(array) 