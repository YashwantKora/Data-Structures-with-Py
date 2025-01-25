def BubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j+i]
                data[j+i] = temp

array = [1,5,2,8,9,3]
BubbleSort(array)
print(array)
