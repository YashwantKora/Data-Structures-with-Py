# def BubbleSort(data):
#     for i in range(len(data)):
#         for j in range(len(data) - i - 1):
#             if data[j] > data[j + 1]:
#                 temp = data[j]
#                 data[j], data[j + 1] = data[j + 1], data[j]

def BubbleSort(data):
    n = len(data)
    for i in range(n):
        for j in range(n -i -1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]



array = [3,5,1,2,6,4,7,9,8]
BubbleSort(array)
print(array)
