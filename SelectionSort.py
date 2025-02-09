# def SelectionSort(data):
#     n = len(data)
#     for i in range(n):
#         min = i
#         for j in range(i + 1, n):
#             if data[j] < data[min]:
#                 min = j
#         data[i], data[min] = data[min], data[i]

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